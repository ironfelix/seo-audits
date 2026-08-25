# -*- coding: utf-8 -*-
"""Пересобирает блок «Сводка: инструментарий SEO-агентов» из самих карточек страницы.

Зачем: сводка, написанная руками, расходится с содержимым. Страница два месяца
утверждала «19 метрик», когда в скилле было 28. Здесь она ВЫВОДИТСЯ из карточек,
поэтому соврать не может.

Запуск из корня seo-audits:  python3 tools/build_ledger.py
"""
import re, html, collections, pathlib

P = pathlib.Path(__file__).resolve().parent.parent / 'pipeline-backlog.html'

TRACKS = [
    ('🤖 Автономность и оркестрация', 'агент ведёт работу сам, человек только апрувит', ['38', '26']),
    ('🔍 SEO-оптимизация', 'базовый слой: позиции, перелинковка, поведение', ['11', '19', '22', '28']),
    ('🌐 GEO-оптимизация', 'цитируемость в AI: разметка, промпты, замеры', ['2', '10', '18', '9', '42', '23', '32', '33', '34']),
    ('🛡 Гейты качества', 'чтобы не звать человека на проверку', ['И3', 'И5', 'И6', 'И10', '13']),
    ('📐 Форматы и дистрибуция', 'контент-стратегия, отложено до подтверждения гипотез', ['25', '27', '31', '35', '14', '41']),
]


def item_spans(h):
    out = []
    for m in re.finditer(r'<div class="(item(?: [^"]*)?)">', h):
        start, cls, depth, i = m.start(), m.group(1), 0, m.start()
        while True:
            nxt = re.search(r'<div\b|</div>', h[i:])
            pos = i + nxt.start()
            if h[pos:pos + 5] == '</div':
                depth -= 1; i = pos + 6
                if depth == 0:
                    end = i; break
            else:
                depth += 1; i = pos + 4
        num = re.search(r'<div class="item-num">([^<]+)</div>', h[start:end])
        out.append((num.group(1) if num else None, start, end, cls))
    return out


def rows_from(h):
    rows = []
    for num, s, e, cls in item_spans(h):
        blk = h[s:e]
        title_raw = re.search(r'<div class="item-title">(.*?)</div>', blk, re.S).group(1)
        tag = re.search(r'<span class="tag-(?:done|part|frozen|new)">(.*?)</span>', title_raw)
        tagtxt = re.sub('<[^>]+>', '', tag.group(1)).strip() if tag else ''
        title = re.sub(r'<span class="tag-(?:done|part|frozen|new)">.*?</span>', '', title_raw)
        title = html.unescape(re.sub('<[^>]+>', '', title)).strip()
        status = ('done' if 'done' in cls else 'part' if ' part' in cls
                  else 'frozen' if 'frozen' in cls else 'open')
        rows.append(dict(num=num, title=title, tag=tagtxt, status=status,
                         skills=re.findall(r'<span class="tag tag-skill">([^<]+)</span>', blk)))
    return rows


def build(rows):
    by = {r['num']: r for r in rows}
    esc = html.escape

    def li(n):
        r = by.get(n)
        if not r or r['status'] not in ('open', 'part'):
            return ''
        mark = '🟡' if r['status'] == 'part' else '○'
        note = f' <i>{esc(r["tag"])}</i>' if r['status'] == 'part' and r['tag'] else ''
        sk = ', '.join(r['skills'])
        sk = f' <span class="lg-skill">{esc(sk)}</span>' if sk else ''
        return f'<li class="{"lg-part" if r["status"]=="part" else ""}"><b>{esc(str(n))}</b> {mark} {esc(r["title"])}{sk}{note}</li>'

    left, counted = '', set()
    for title, sub, nums in TRACKS:
        items = [x for x in (li(n) for n in nums) if x]
        if not items:
            continue
        counted |= {n for n in nums if by.get(n, {}).get('status') in ('open', 'part')}
        left += f'<div class="lg-sub">{title} · {len(items)}<span class="lg-note">{sub}</span></div><ul>' + ''.join(items) + '</ul>'
    rest = [r['num'] for r in rows if r['status'] in ('open', 'part') and r['num'] not in counted]
    if rest:
        left += f'<div class="lg-sub">Прочее · {len(rest)}</div><ul>' + ''.join(li(n) for n in rest) + '</ul>'

    done_by = collections.OrderedDict()
    for r in rows:
        if r['status'] != 'done':
            continue
        m = re.search(r'(\d\d\.\d\d)', r['tag'])
        d = m.group(1) if m and m.group(1) in ('25.08', '19.08', '12.06') else 'ранее'
        done_by.setdefault(d, []).append(r['num'])
    labels = {'25.08': '25.08 — плотность в гейт', '19.08': '19.08 — ревизия доски',
              '12.06': '12.06 — спринт quick wins', 'ранее': 'ранее'}
    done_html = ''
    for d in ('25.08', '19.08', '12.06', 'ранее'):
        if d not in done_by:
            continue
        done_html += f'<div class="lg-sub">{labels[d]} · {len(done_by[d])}</div><ul>' + ''.join(
            f'<li class="lg-done"><b>{esc(str(n))}</b> ✅ {esc(by[n]["title"])}</li>' for n in done_by[d]) + '</ul>'

    moved = [r for r in rows if r['status'] == 'frozen' and 'вынесено' in r['tag']]
    frozen = [r for r in rows if r['status'] == 'frozen' and 'вынесено' not in r['tag']]
    n_done = sum(1 for r in rows if r['status'] == 'done')
    n_open = sum(1 for r in rows if r['status'] == 'open')
    n_part = sum(1 for r in rows if r['status'] == 'part')

    return f'''  <div class="ledger">
    <h3>Сводка: инструментарий SEO-агентов <span class="lg-stamp">сгенерировано из карточек ниже · tools/build_ledger.py</span></h3>
    <p class="lg-intro">Доска про <b>инструментарий</b>: что доделать, чтобы агенты работали автономно — сначала по SEO, потом по GEO. Исполнение контента и операционка сюда не входят и вынесены отдельно.</p>
    <div class="lg-cols">
      <div class="lg-col lg-col-done">
        <div class="lg-head">✅ Сделано — {n_done}</div>
        {done_html}
      </div>
      <div class="lg-col lg-col-left">
        <div class="lg-head">Осталось — {n_open} открытых + {n_part} частично</div>
        {left}
        <div class="lg-sub">Вынесено — не про пайплайн · {len(moved)}</div>
        <ul class="lg-frozen">{''.join(f'<li><b>{esc(str(r["num"]))}</b> {esc(r["title"])}</li>' for r in moved)}</ul>
        <div class="lg-sub">❄️ Заморожено · {len(frozen)}</div>
        <ul class="lg-frozen"><li>{", ".join(str(r["num"]) for r in frozen)} — Global-трек и продуктизация под клиента</li></ul>
      </div>
    </div>
  </div>

'''


if __name__ == '__main__':
    h = P.read_text(encoding='utf-8')
    block = build(rows_from(h))
    i, j = h.index('  <div class="ledger">'), h.index('  <div class="rev-banner">')
    P.write_text(h[:i] + block + h[j:], encoding='utf-8')
    r = rows_from(P.read_text(encoding='utf-8'))
    c = collections.Counter(x['status'] for x in r)
    print(f'сводка пересобрана: {len(r)} карточек — {dict(c)}')
