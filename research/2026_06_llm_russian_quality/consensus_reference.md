---
type: consensus_reference
domain: science
title: "Качество русского текста LLM-моделей — Consensus Reference"
created: 2026-06-02
confidence: 0.35
tags: [russian NLP, LLM, benchmarks, MERA, humanness, text quality]
field_maturity: CONTESTED
hypothesis_verdicts:
  H1_scale_wins: SUPPORTED
  H2_english_accent_structural: MODERATE
  H3_task_determines_winner: SUPPORTED
  H4_benchmarks_irrelevant: PARTIAL
---

# Качество русского текста LLM-моделей: Consensus Reference

**Синтез:** 5 Scout-потоков + CRITIC + METHODOLOGIST + 2 Deep Dive + Reflection 2
**Дата синтеза:** 2026-06-02
**Глобальная уверенность:** 0.35 / 1.00
**Статус поля:** CONTESTED

---

## TL;DR

- **Нет ни одного бенчмарка, который измеряет "человечность" русского текста.** MERA, POLLUX и все другие русскоязычные оценочные системы измеряют task-accuracy (правильность ответа на задачи), а не стилистическое качество, натуральность или идиоматичность. Это консенсус всех потоков. [HIGH confidence]

- **MERA структурно скомпрометирован.** 67% задач — закрытые форматы (MCQ/классификация), управляется консорциумом с прямым конфликтом интересов (Сбер разрабатывает GigaChat и администрирует бенчмарк), нет независимой репликации. Лидерборд-позиции не следует цитировать как доказательство качества текста. [HIGH confidence, Grade A sources]

- **Claude Opus 4.6 лидирует MERA (0.862), превысив человеческий базис (0.852).** Это является сигналом начинающейся сатурации бенчмарка, а не доказательством превосходства над носителями русского. MERA потеряет дифференцирующую силу в течение 12–18 месяцев. [MODERATE confidence — MERA leaderboard, Grade C/D source; benchmark design critique, Grade A/B]

- **Масштаб побеждает специализацию на frontier-уровне (H1 ПОДДЕРЖАНА).** Claude без кириллического токенизатора занимает #1 MERA, что опровергает простую гипотезу "русский токенизатор = русское качество". Однако это верно для benchmark-задач, не обязательно для написания живого текста. [MODERATE confidence]

- **Задача определяет победителя (H3 ПОДДЕРЖАНА).** Ни одна модель не доминирует во всех видах русскоязычного контента. Практический консенсус: Claude для длинных статей и редактуры, YandexGPT для заголовков и digital-copy, GigaChat для юридических документов, Qwen3-235B/DeepSeek для массового SEO-контента. [HIGH confidence, multiple Grade D sources, directionally consistent]

- **BerryLM-XL — экстремальный случай разрыва бенчмарк/практика.** Занимает #3 MERA при нулевом упоминании в practitioner-источниках, закрытый API, три варианта одного обучающего прогона в TOP-10. Circumstantial evidence гейминга через GRPO с reward-функцией на task accuracy. [MODERATE confidence — mechanism plausible, direct proof absent]

- **«Думает по-английски» — структурный механизм, не реплицированный для русского (H2 УМЕРЕННАЯ).** Llama/Gemma/Mixtral обрабатывают семантику через English-центричное пространство. Для YandexGPT и GigaChat этот механизм не протестирован напрямую. [MODERATE-LOW confidence — Grade C preprint, Russian not directly tested]

- **R-HLS (Russian Human-likeness Score) частично реализуем сегодня.** 5 из 6 критериев автоматизируются: burstiness, deverbal noun ratio, participial stacking, em-dash count, lemma-MTLD. Регистровая консистентность и коллокационный чекер требуют 2–4 месяцев разработки. Воплощённое знание принципиально не автоматизируется. [HIGH confidence for mechanism; LOW confidence for specific Russian thresholds]

- **Токенизационный штраф для русского (~2x больше токенов в BPE-токенизаторах) — структурная проблема.** Влияет на стоимость, эффективное контекстное окно и качество обучающего сигнала. Конкретный множитель варьируется: 2x (Cyrillic в cl100k_base) до 7–8x (отдельные тексты по данным практиков). [MODERATE-HIGH confidence — multiple sources, exact ratio varies by tokenizer version]

- **Люди-аннотаторы определяют AI-русский на уровне 66.6%** — около случайного угадывания. Лучшие автоматические детекторы (GigaCheck) достигают 86% на научных абстрактах, деградируя на новых моделях. Детекторы ловят RLHF-артефакты, а не фундаментальную AI-природу текста. [MODERATE-HIGH confidence — RuATD 2022, AINL-Eval 2025]

---

## Field Consensus Map

### Established consensus — с чем согласны все потоки

**Измерительная инфраструктура для вопроса «кто пишет лучший русский текст» отсутствует.** Это единственный вопрос, по которому достигнут подлинный консенсус. SCOUT A, B, C, D, E, CRITIC и METHODOLOGIST — все независимо пришли к выводу: ни MERA, ни POLLUX, ни любой другой существующий инструмент не измеряет стилистическое качество русского текста, его натуральность, идиоматичность или «человечность». RuCoLA (linguistic acceptability) близко, но измеряет дискриминацию, не генерацию. POLLUX включает naturalness среди 66 критериев, но не публикует формулу. Отсутствие метрики — это не временная техническая проблема, а принципиальный концептуальный пробел.

**MERA не предназначен для оценки writing quality.** Бенчмарк проектировался для оценки «фундаментальных способностей LLM» (reasoning, knowledge, math, code). Из 15 core tasks: 0 измеряют стилистическую связность, регистровое разнообразие, натуральность, аргументационную структуру или editorial coherence. Это не критика MERA как такового — это описание области его применимости. Проблема возникает, когда MERA-рейтинги интерпретируются как ответ на вопрос «кто лучше пишет по-русски».

**Задача определяет оптимальную модель.** Ни в одном из 5 потоков, ни в одном practitioner-источнике нет утверждения, что одна модель доминирует во всех видах русскоязычного контента. Это фактический консенсус независимо от его методологического качества.

### Active debates — реальные продолжающиеся разногласия

**Степень сатурации MERA.** Stream A констатирует: Claude Opus 4.6 уже превысил human baseline. METHODOLOGIST предупреждает: MERA потеряет дифференцирующую силу в 12–18 месяцев. CRITIC замечает: GigaChat и YandexGPT исчезли из TOP-10, хотя A и D продолжают трактовать их как ведущих игроков. Точный временной горизонт не установлен.

**Масштаб vs специализация.** H1 (scale beats specialization) поддержана на MERA. Но Stream D документирует системные причины, почему Russian-specific training должна давать advantages в культурно-прагматических задачах — которые MERA не измеряет. Два утверждения могут быть одновременно верными: масштаб выигрывает на benchmark, специализация выигрывает на реальном письме.

**Природа BerryLM-gap.** DD-B устанавливает circumstantial evidence гейминга (GRPO reward на MCQ, три submission варианта, нет API). Но DD-B также честно признаёт: закрытость, а не слабость, может объяснять отсутствие practitioner-упоминаний. Вердикт окончательно не установлен.

**Токенизационный множитель.** Данные варьируются: 2x (Cyrillic в cl100k_base, множество источников), 3x (по данным нескольких исследований), 7–8x (practitioner данные по отдельным текстам). Контролируемое измерение на одном тексте с несколькими токенизаторами не опубликовано.

### Strongest evidence — наиболее robustly поддержанные утверждения

1. Russian SuperGLUE был геймингован rule-based эвристиками до эпохи LLM (arXiv:2105.01192, Grade B, replicated by benchmark authors' own revision)
2. MCQ-формат уязвим к positional bias, изменение порядка вариантов сдвигает рейтинг на до 8 позиций (arXiv:2309.03882, multiple replications)
3. Cross-lingual contamination не детектируется text-overlap методами (arXiv:2406.13236, demonstrated on Llama3 + Qwen1.5)
4. Model collapse от рекурсивного AI-контента в данных обучения (Nature 2024, Grade A, multiple replications)
5. Люди-аннотаторы определяют AI-русский на 66.6% (RuATD 2022, Grade B)
6. RLHF instruction-tuning артефакты — основной сигнал для детекторов (arXiv:2605.19516)

### The key open question — главный неотвеченный вопрос

**Существует ли измеримая, воспроизводимая разница между моделями по качеству написания русского текста — и если да, какова она количественно?**

Это вопрос, ради которого затевалось исследование. Ответ: **измерить нельзя, потому что инструмента нет.** Можно получить Grade D practitioner evidence (Habr/vc.ru), указывающий на Claude как лидера для formal Russian. Можно получить blind evaluation с единственной точкой (8.6/10 vs 7.8/10). Но нет ни одного peer-reviewed, independently replicated, protocol-documented исследования, которое бы отвечало на этот вопрос с измеримой уверенностью.

---

## Knowledge Map

### Central claims (два конкурирующих центра)

**Центр A — технический:** "Масштаб и quality training data определяют качество русского текста. Claude #1 на MERA; YandexGPT имеет наибольший Russian pretraining corpus; GigaChat — нативный токенизатор и доменные данные. Эти факторы объясняют разрыв."

**Центр B — прагматический:** "Задача определяет оптимальную модель. Нет универсального победителя. Practitioner consensus важнее benchmark-позиций, потому что benchmarks не измеряют то, что нужно."

Оба центра совместимы — они отвечают на разные аспекты вопроса. Противоречие между ними мнимое.

### Supporting pillars — хорошо обоснованные суб-утверждения

1. **Токенизация = фундаментальный инфраструктурный фактор.** BPE-токенизаторы, обученные на English-dominant corpora, фрагментируют кириллицу inefficiently, создавая 2x+ tokenization overhead. Vikhr продемонстрировал 46% сокращение токенов через vocabulary adaptation.

2. **Морфология русского создаёт специфические AI-failure modes.** 6 падежей, видо-временная система, свободный порядок слов — всё это создаёт конкретные, измеримые паттерны ошибок (RuBLiMP, EMNLP 2024): LLM систематически хуже людей в структурных зависимостях, отрицании, переходности.

3. **RLHF создаёт детектируемые артефакты в русском тексте.** Девербальные существительные (×2 относительно человека), причастные стеки (×2-5), em-dash overuse (×3.28 по данным arXiv:2603.27006), RLHF-фразы-маркеры. Механизм: reward за "деловой/профессиональный" стиль усиливает паттерны формального регистра.

4. **Model collapse от AI-generated Russian content — реальный риск.** Сеть "Pravda" (задокументировано) систематически засевает AI-generated Russian content в Common Crawl. Nature 2024 подтверждает: рекурсивное обучение на AI-output ведёт к потере linguistic diversity. Это структурная угроза качеству будущих моделей.

5. **Proprietary data moats дают YandexGPT и GigaChat structural advantages.** Яндекс имеет доступ к полному поисковому индексу (~100TB filtered to ~1TB high-quality Russian). Сбер — к банковским документам, юридическим шаблонам, customer service данным. Эти данные не реплицируются open-source практиками.

### Contested zones — реальные разногласия

**Зона 1: Что важнее — токенизатор или масштаб обучения?** Claude без кириллического токенизатора = #1 MERA. Vikhr с кириллическим токенизатором = значительно ниже. Но Claude обучен на данных несопоставимо большего масштаба. Изолировать вклад токенизатора от вклада масштаба в существующих данных невозможно.

**Зона 2: Думает ли multilingual LLM «по-английски» при генерации на русском?** Механизм документирован для Llama/Gemma/Mixtral (arXiv:2502.15603, Grade C). Для YandexGPT и GigaChat — не тестировалось. Russian-primary training может (или не может) изменить это. Уверенность: LOW для экстраполяции на русскоязычные модели.

**Зона 3: Где граница MERA как useful signal?** Даже CRITIC признаёт: понимание контекста и знание фактов (что MERA измеряет) являются необходимыми, хотя и недостаточными условиями writing quality. Корреляция между MERA TOP и practitioner ranking не нулевая — Claude #1 и там, и там. Вопрос: насколько полезен MERA как прокси, если не как прямой измеритель?

### Frontier questions — неотвечаемые сегодня

**Q1:** Каковы верифицированные пороги burstiness для русского текста по жанрам? (Требует: 500+ текстов каждого жанра × human/AI, 6–8 недель разметки.)

**Q2:** Ведёт ли Russian-dominant pretraining к Russian-centric intermediate representations, или "думает по-английски" неизбежно для любой мультиязычной модели? (Требует: logit lens analysis на YandexGPT/GigaChat.)

### Newcomer reading list — 3 фундаментальных источника

1. **MERA (arXiv:2401.04531 + ACL 2024)** — базовый стандарт русскоязычной оценки, Grade A. Читать вместе с критикой из arXiv:2105.01192 (RSG heuristics gaming).

2. **RuBLiMP (arXiv:2406.19232, EMNLP 2024)** — 45k минимальных пар, Grade B. Единственный peer-reviewed инструмент для конкретных лингвистических failure modes LLM на русском.

3. **REPA (arXiv:2503.13102, Slavic NLP 2025)** — первый human-labeled бенчмарк для оценки качества генерации на русском, Grade B. Наиболее независимый из существующих инструментов.

---

## 1. Foundations & Key Concepts

### Что такое «качество русского текста» и «человечность»?

«Качество русского текста» — понятие, для которого в поле нет единого операционального определения. Существующие попытки операционализации распадаются на три несводимых класса:

**Класс 1: Task accuracy** (что измеряют бенчмарки). Правильность ответа на закрытые задачи: MCQ, NLI, арифметика, код. Это легко измерить, но имеет низкую экологическую валидность для writing tasks.

**Класс 2: Linguistic acceptability** (что измеряет RuCoLA). Воспринял бы носитель данное предложение как грамматически и семантически корректное? Это peer-reviewed, но измеряет discrimination (что корректно?), а не generation (что написать?).

**Класс 3: Humanness / naturalness** (что пытается измерить DD-A). Звучит ли текст как написанный носителем русского языка? Включает: burstiness, deverbal noun ratio, participial stacking density, register consistency, morphosyntactic accuracy, lemma-MTLD. Нет peer-reviewed валидации русских порогов — только extrapolation из английских данных.

Конкурирующие теории «человечности» текста (из Stream C) — ни одна не является консенсусной:

- **Теория A (perplexity):** текст человеческий в той мере, в которой он непредсказуем для языковой модели. Слабость: экспертный академический текст может иметь низкую perplexity, потому что следует жёстким конвенциям.
- **Теория B (стилометрия):** текст человеческий, если несёт последовательный индивидуальный fingerprint. LLM усредняют по миллионам авторов.
- **Теория C (воплощённое знание):** текст человеческий, если содержит конкретный первично-пережитый опыт. Это принципиально не автоматизируется.
- **Теория D (паттерн ошибок):** текст человеческий, если содержит human-specific imperfections. Слабость: образованный носитель пишет без ошибок.
- **Теория E (прагматическая вовлечённость):** текст человеческий, если автор имеет ставку в коммуникативном исходе. AI нейтрален по дизайну.

Эти теории делают разные предсказания и имеют разные measurement implications. «Точность humanness detection» разных систем не сопоставима — они измеряют разные конструкты.

### Историческое развитие оценки Russian LLM

**Поколение 1 (2020–2022):** Аналоги GLUE/SuperGLUE. RussianSuperGLUE (2020, EMNLP, Grade A), TAPE (2022, EMNLP, Grade A), RuCoLA (2022, EMNLP, Grade A). Задачи: NLU, классификация, NLI. Проблема: RSG геймингован rule-based heuristics ещё в 2021 (arXiv:2105.01192, Grade B) — single lexical feature «был» matched BERT performance on TERRA task.

**Поколение 2 (2022–2023):** Few-shot оценка, adversarial robustness, KBQA. RuBLiMP (2024, EMNLP), RuATD shared task (2022), research on Russian LLaMA adaptation.

**Поколение 3 (2024–2025):** Комплексная оценка LLM в instruction-формате. MERA (2024, ACL, Grade A) — ключевая веха. POLLUX (2025, arXiv), REPA (2025, Slavic NLP), MERA Multi/Code/Industrial.

**Генерация 0 (параллельная): Practitioner evaluation.** llmarena.ru (ELO-based crowdsourcing), Habr/vc.ru тесты. Методологически Grade D, но единственный источник данных о реальном writing quality.

### Доминирующая теоретическая рамка

**MERA + task-accuracy парадигма.** Исходящее предположение: если модель правильно отвечает на разнообразные задачи в instruction-формате на русском языке, это является proxy для общего качества русского language understanding. Это предположение **не верифицировано** и прямо оспаривается:

- Stream B: корреляция между MERA-позицией и practitioner-признанием слабая (GigaChat — высокий MERA, низкий practitioner rating; BerryLM — #3 MERA, 0 practitioner-упоминаний)
- Stream E: «не использовать MERA как прокси для качества письма. Тестировать на реальных задачах»
- METHODOLOGIST: «GigaChat's training has been optimized for MERA-type tasks, not for natural language quality that practitioners evaluate» — прямое применение Goodhart's Law

### Benchmark-practice gap как центральное напряжение поля

Разрыв между benchmark performance и реальным writing quality — не баг, а фича существующей системы. MERA создавался не для измерения writing quality. Когда его результаты используются для ответа на вопрос «кто лучше пишет по-русски?», это category error.

Этот разрыв **задокументирован** (не просто теоретически предсказан):
- GigaChat имеет высокий MERA-балл + доступный API + реальных пользователей → устойчивая практическая критика «ЕГЭ-шного стиля»
- BerryLM #3 MERA → 0 practitioner-упоминаний
- YandexGPT scored 1/5 on logical reasoning tasks in practitioner tests → rated #1 for Russian headline generation

---

## 2. Current State of the Art (June 2026)

### MERA Leaderboard (mera.a-ai.ru, данные June 2026)

**ДИСКЛЕЙМЕР:** Данные с официального лидерборда. Лидерборд управляется консорциумом с прямым COI (Сбер). Нет независимой репликации. MCQ-dominated format (67%). Трактовать как task-solving benchmark, не как writing quality ranking.

| Место | Модель | Балл MERA | Команда / Организация |
|-------|--------|-----------|----------------------|
| 1 | Claude Opus 4.6 | 0.862 | MERA team / Anthropic |
| 2 | Human Benchmark | 0.852 | MERA reference |
| 3 | BerryLM-XL | 0.835 | Wildberries & Russ AI |
| 4 | BerryLM-L-v2-early-ckpt | 0.822 | Wildberries & Russ AI |
| 5 | GPT-5.4 | 0.821 | MERA team / OpenAI |
| 6 | BerryLM-v2-reasoning-budget-low | 0.810 | Wildberries & Russ AI |
| 7 | GLM-5.1 | 0.804 | MERA team |
| 8 | Qwen3-235B-A22B-Thinking-2507 | 0.795 | MERA team |
| 9 | Cotype Light 3 | 0.792 | MWS AI |
| 10 | Qwen3.6-35B-A3B | 0.792 | MERA team |

**Ключевые наблюдения:**
- GigaChat и YandexGPT отсутствуют в TOP-10 (их оценки устарели: GigaChat 2 Max ~0.67 для 2024-2025, GigaChat 3 Ultra Preview 0.683 — по данным Stream E на других snapshot'ах)
- 3 варианта BerryLM (одна организация) в TOP-10 = gaming signal
- Human baseline (0.852) уже превышен → начало сатурации

**Предупреждение о GigaChat scores:** В потоках зафиксированы противоречия: Stream A/D — GigaChat 2 Max ~0.67; Stream E — GigaChat 3 Ultra Preview 0.683. Это разные версии модели на разных snapshot'ах лидерборда. Прямое сравнение некорректно.

### POLLUX (arXiv:2505.24616, 2025)

Gemma-3-27B-It лидирует (1.205); T-Pro-It-1.0 #4 (1.115) — лучший Russian-focused; GPT-4 #5 (1.110). Hallucination rate судьи ~25%; self-judging bias не исключён; Сбер в числе со-авторов — COI.

### MERA Saturation

Human baseline (0.852) уже превышен Claude Opus 4.6 (0.862). RSG был насыщен за ~2 года; MERA на той же траектории. Прогноз: бенчмарк потеряет дифференцирующую силу на frontier-уровне в течение 12–18 месяцев. Это НЕ означает, что модели «умнее людей» — означает, что бенчмарк перестаёт измерять то, для чего создавался.

### Practitioner Consensus (Grade D, directionally robust)

| Задача | Первичная | Вторичная | Обоснование |
|--------|-----------|-----------|-------------|
| Длинные статьи / бизнес-текст | Claude Opus/Sonnet 4.x | ChatGPT | Blind eval 8.6/10; наименьшее редактирование для натуральности |
| SEO titles / заголовки | YandexGPT 5 | ChatGPT | Обучен на русском вебе, digital-native стиль |
| Массовый SEO-контент | Qwen3-235B | DeepSeek V3 | 130× дешевле при 91% качества |
| Юридические / официальные | GigaChat 2 Max | ChatGPT | Russian legal training data, работает без VPN |
| Редактура | Claude | ChatGPT | Best instruction following в русском |
| Классификация/структурирование | YandexGPT 5 | GigaChat | YandexGPT: 70% vs 51% GPT-4o на Russian classification |
| Неформальный / разговорный | ChatGPT | YandexGPT | Более гибкий register |
| Конфиденциальные корп. данные | GigaChat (on-premise) | Vikhr (локально) | Российская юрисдикция |

---

## 3. Mechanisms & Theory

### Почему русский труден для LLM: системные причины

**Причина 1: Токенизация (Grade A-MODERATE)**

BPE-токенизаторы, обученные на English-dominant corpora, фрагментируют кириллицу неэффективно. Данные по множителю варьируются:
- cl100k_base (GPT-4): ~2x больше токенов на символ vs English
- Практические данные (practitioner): 7-8x больше токенов на эквивалентный русский текст vs English
- Vikhr demonstration: 13→7 токенов для типичной русской фразы (46% сокращение через vocabulary adaptation)
- LLaMA Russian adaptation (arXiv:2312.02598, Grade C): замена токенизатора → ускорение inference до 60%

Следствия: (1) сокращение эффективного контекстного окна, (2) более высокая стоимость inference, (3) более слабый training signal на единицу Russian text.

**Причина 2: Морфологическая сложность (Grade A-HIGH)**

6 падежей × 3 рода × 2 числа × глагольные виды = сотни форм слова. AI failure modes (RuBLiMP, EMNLP 2024):
- Слабость в структурных зависимостях, отрицании, переходности
- Хорошее локальное согласование (число, род) — но деградация в длинных падежных цепочках
- Несовершенный вид вместо совершенного при обозначении завершённого события

**Причина 3: «Думает по-английски» (Grade C — MODERATE, экстраполяция)**

Llama-3.1-70B, Gemma-2-27b, Mixtral-8x22B обрабатывают семантику через English-proximate representation space (arXiv:2502.15603). Применительно к этим моделям: промежуточные слои содержат English-centric концепты даже при Russian input/output. Для YandexGPT и GigaChat — не тестировалось. Степень применимости к Russian-primary моделям: UNKNOWN.

Проявления в тексте (если механизм работает): кальки с английских идиом, SVO-порядок там где уместен topic-comment, отсутствие русских дискурсивных частиц и маркеров.

**Причина 4: Scale asymmetry (Grade MODERATE)**

English internet content — 7–10x больше Russian по объёму токенов. GigaChat training: 63.76% English, 26.49% Russian. GPT-3 original: Russian ~1.5–3% WebText. Следствие: для каждой единицы Russian reasoning capability было ~7–9x меньше training signal.

**Причина 5: Cultural-pragmatic gap (Grade MODERATE — documented но не измеряемо)**

Формальные бенчмарки не измеряют: современный Russian slang, советские/постсоветские культурные референции, Russian business communication conventions, regulatory knowledge (ГОСТы, КоАП, 44-ФЗ). Именно здесь разрыв между Russian-trained и global моделями наибольший — и именно здесь он наименее измерим.

### AI-маркеры в русском тексте (механизмы)

**Burstiness — низкая вариативность длин предложений**

Цепочка: авторегрессивное сэмплирование → заострённое распределение при T<1.0 → модальные длины предложений → низкая σ → flagged as AI.

Данные (английский, 200 samples, Grade D practitioner):
- Человек: σ=8.2 слова, B≈0.72
- GPT-4o: σ=4.1 слова, B≈0.35
- Claude: σ=5.3 слова, B≈0.41

Для русского: пороги не верифицированы академически. Extrapolation: B<0.35 = AI signal, B>0.55 = human-like. Требует валидации на русском корпусе.

**Девербальные существительные (×2)**

Цепочка: формальный регистр доминирует в обучающих данных → RLHF вознаграждает «деловой» стиль → осуществление/проведение/обеспечение вместо глаголов → детектируется через NN/VBX POS ratio.

**Причастные стеки (×2–5)**

Та же причина: причастные обороты нормативны в письменном русском → overrepresented в обучающих данных → AI стекирует несколько подряд (2-5× чаще человека).

**Em-dash overuse (×3.28)**

Данные: GPT-4.1 — 10.62 em-dash на 1000 слов; человеческий baseline — ~3.23 (arXiv:2603.27006, Grade C, единственный preprint, не реплицирован). Механизм: markdown leakage — огромный training corpus содержит markdown с em-dash как clause separator.

**RLHF-opener phrases**

«Следует отметить», «важно понимать», «в данном контексте», «таким образом» — прямые продукты RLHF reward за «engaged, thorough, helpful» стиль. Детекторы ловят именно эти artifacts, а не фундаментальную AI-природу текста. Доказательство: base (pre-RLHF) модели GPTZero считает «человеческими» в 96–98% случаев.

---

## 4. Key Results & Evidence

### F1: Ни один бенчмарк не измеряет русскую натуральность/человечность

**Finding:** Ни MERA, ни POLLUX, ни любой другой существующий русскоязычный NLP-бенчмарк не содержит задач, измеряющих стилистическое качество, натуральность или «человечность» генерируемого текста.

**Evidence:** Структурный анализ MERA (15 core tasks: математика, логика, код, knowledge recall, диалог — ни одной writing quality задачи). POLLUX включает naturalness как 1 из 66 критериев, не публикует формулу. Консенсус SCOUTs A, B, C, D, E + CRITIC + DD-A.

**Confidence:** HIGH
**Caveats:** RuCoLA (EMNLP 2022) измеряет linguistic acceptability — близко, но для discrimination, не generation. POLLUX/REPA — шаги в правильном направлении, но не peer-reviewed решения.

---

### F2: MERA структурно скомпрометирован

**Finding:** MERA имеет три системных проблемы, делающих его leaderboard ненадёжным для сравнения writing quality: (1) MCQ-доминирование (67% задач — gameable формат), (2) конфликт интересов (Сбер = GigaChat developer + MERA consortium member), (3) structural contamination risk (CC-BY-4.0 datasets в pre-training corpora).

**Evidence:** arXiv:2105.01192 (Grade B): RSG геймингован rule-based эвристиками. arXiv:2309.03882 (Grade C, multiple replications): MCQ уязвим к positional bias. arXiv:2406.13236 (Grade C): cross-lingual contamination не детектируется text-overlap методами. METHODOLOGIST: структурный conflict of interest — «highest risk assessment».

**Confidence:** HIGH
**Caveats:** MERA полезен для оценки reasoning и knowledge-recall способностей. Проблема — не в бенчмарке как таковом, а в неправомерной экстраполяции его результатов на writing quality.

---

### F3: Масштаб побеждает специализацию на frontier-уровне

**Finding:** Claude Opus 4.6 (без нативного кириллического токенизатора, English-heavy training) занимает #1 MERA (0.862). Это опровергает простую гипотезу «Russian tokenizer = Russian quality».

**Evidence:** Официальный MERA leaderboard (Grade C/D — website, no peer review). Поддерживается practitioner consensus: Claude также #1 для editorial Russian writing.

**Confidence:** MODERATE — MERA score; MODERATE для writing quality practitioner claim
**Caveats:** MERA измеряет task-solving, не writing. Обе позиции (#1 MERA и #1 practitioner для editorial) могут объясняться масштабом обучения и RLHF quality, без impacting русскоязычную nativeness. «Масштаб побеждает» верно на benchmark и в formal writing, может быть неверно в idioms/cultural tasks где не измерялось peer-reviewed способом.

---

### F4: Токенизационный штраф для русского (~2–3x в BPE)

**Finding:** Standard BPE-токенизаторы требуют ~2–3x больше токенов для русского текста vs English-эквивалента. Vikhr демонстрирует 46% сокращение через vocabulary adaptation.

**Evidence:** Vikhr arXiv:2405.13929 (Grade C, RETRACTED from ACL — данные с осторожностью); Frontiers AI 2025 (Ukrainian as proxy, Grade C); practitioner данные (7–8x для отдельных текстов, Grade D); cl100k_base tokenizer characterization (multiple sources).

**Confidence:** MODERATE-HIGH для факта штрафа; LOW для точного множителя
**Caveats:** Vikhr retracted from ACL — причина ретракции не установлена, данные из этой статьи требуют осторожности. Точный множитель варьируется от 2x до 7-8x в зависимости от метода измерения и типа текста.

---

### F5: Человеческая детекция AI-русского ~66%

**Finding:** Люди-аннотаторы определяют AI-сгенерированный русский текст на уровне ~66.6% — около случайного угадывания (RuATD 2022, binary classification task).

**Evidence:** arXiv:2206.01583, Grade B. 30 команд участвовало в shared task. Binary accuracy лучшей системы: 83%. Human annotator baseline: 66.6%.

**Confidence:** MODERATE-HIGH
**Caveats:** Датасет создан до эпохи GPT-4/ChatGPT — использовались более слабые генераторы. Реальная challenge с современными моделями, вероятно, выше. Claim «90% detection for AI-familiar humans» (Habr, Grade D) — не подтверждён источником и несопоставим с RuATD (другая популяция, другой период, другие генераторы). **[FACT-CHECK: FAIL — не цитировать 90% как установленный факт]**

---

### F6: BerryLM-MERA gap — circumstantial evidence gaming

**Finding:** BerryLM-XL (#3 MERA, 0.835) имеет закрытый API, 0 practitioner-упоминаний, три варианта одного обучающего прогона в TOP-10, GRPO training с reward-функцией на task accuracy. Это circumstantial evidence целенаправленной оптимизации под MERA-формат.

**Evidence:** DD-B (2026-06-02): live verification через HuggingFace model card и MERA leaderboard. Механизм: GRPO с 11 reward-функциями включая «точность на целевых задачах» + MCQ positional bias calibration.

**Confidence:** MODERATE для gaming mechanism (plausible, not proven); HIGH для факта разрыва (0 practitioner mentions = empirical)
**Caveats:** Закрытость, а не слабость модели, также объясняет отсутствие practitioner-упоминаний. BerryLM может быть реально сильной моделью для e-commerce NLP tasks. Без независимого теста на writing quality вердикт неокончателен.

---

### F7: R-HLS частично реализуем сегодня

**Finding:** Russian Human-likeness Score (R-HLS) — 6-критериальный фреймворк — частично автоматизируем уже сегодня. 5 критериев (burstiness, deverbal ratio, participial stacking, em-dash count, lemma-MTLD) требуют 1 дня разработки на Python. Регистровая консистентность — 2–4 месяца. Воплощённое знание принципиально не автоматизируется.

**Evidence:** DD-A (2026-06-02): systematic review существующих фреймворков (POLLUX, RuBLiMP, REPA, StyloMetrix, RuCoLA). Python pseudocode с razdel, pymorphy2, natasha.

**Confidence:** HIGH для факта реализуемости; LOW для верифицированных русских порогов
**Caveats:** Пороговые значения (B<0.35 = AI, B>0.55 = human) экстраполированы из английского. Нет peer-reviewed валидации на русском корпусе. Регистровый классификатор и collocation checker требуют значительной разработки.

---

### F8: Task-specific model selection — практический ответ

**Finding:** Оптимальная модель зависит от задачи. Нет универсального победителя для всех видов русскоязычного контента. Practitioner consensus из 6+ независимых источников: Claude для длинных статей, YandexGPT для заголовков, GigaChat для юридических документов, Qwen3-235B для массового дешёвого контента.

**Evidence:** Stream E (Grade D, 6+ sources, consistent directional signal). S4 (Habr 2026): Qwen3-235B = 9% ниже лидеров по качеству, в 130× дешевле. S5: YandexGPT 5 Pro 70% vs GPT-4o 51% на Russian text classification.

**Confidence:** HIGH для направленного консенсуса; LOW для точных количественных разниц
**Caveats:** Все practitioner-источники — Grade D. Sample bias: IT-грамотные Habr-читатели и vc.ru предприниматели. Нет controlled experimental design, нет blinding.

---

### F9: MERA сатурация начинается

**Finding:** Human baseline MERA (0.852) уже превышен Claude Opus 4.6 (0.862). Бенчмарк теряет дифференцирующую силу на frontier-уровне. RSG был насыщен за ~2 года — MERA на той же траектории.

**Evidence:** Stream A (10.1): live leaderboard данные. RSG saturation: arXiv:2202.07791 (Grade A). METHODOLOGIST: «12–18 month window before benchmark obsolescence».

**Confidence:** HIGH для факта превышения human baseline; MODERATE для 12–18 month прогноза
**Caveats:** Не каждая задача в MERA насыщена — агрегатный score скрывает вариацию по задачам. Benchmark может быть redesigned (MERA уже добавил Code, Multi, Industrial variants).

---

### F10: GigaChat/YandexGPT COI в evaluation ecosystem

**Finding:** Сбер одновременно: (1) член консорциума AI Alliance Russia, администрирующего MERA, (2) разработчик GigaChat, конкурирующего на MERA, (3) со-автор POLLUX, (4) разработчик GigaCheck (главный Russian AI detector). Это структурный conflict of interest, отсутствующий в Western evaluation ecosystem в такой концентрации.

**Evidence:** Структурный анализ (METHODOLOGIST, CRITIC). Публичная документация MERA консорциума. arXiv:2506.09440 (GigaChat MoE paper = ACL 2025 demo, Sber authorship). «Pharmaceutical company running own drug trials» — аналогия точна и принята несколькими потоками.

**Confidence:** HIGH — observable from public documentation
**Caveats:** COI не доказывает намеренных манипуляций. MERA может быть methodologically sound несмотря на COI. Но без independent replication COI требует epistemic discount на любые GigaChat/MERA-related claims.

---

## 5. Open Problems & Frontiers

**Пробел 1 — Нет Russian humanness benchmark.** Это ключевой gap поля. Правильный дизайн: blind human preference study с аннотаторами, стратифицированными по региону, возрасту, профессиональному background; задачи из собственных профессиональных доменов аннотаторов; разделение «правильный ответ» vs «предпочтительная формулировка». Аналог: LMSYS Chatbot Arena с адекватным Russian coverage (сейчас <2% от global арены).

**Пробел 2 — Токенизационный ratio требует контролируемого измерения.** 30 минут Python-кода: один текст, несколько токенизаторов, прямое сравнение. Это не сделано ни в одной peer-reviewed публикации для прямого русского измерения.

**Пробел 3 — «Думает по-английски» для Russian-primary моделей — не тестировалось.** Logit lens analysis на YandexGPT и GigaChat напрямую подтвердил или опроверг бы, формируют ли они Russian-centric intermediate representations.

**Пробел 4 — Независимая репликация MERA.** Ни один evaluation результат из MERA leaderboard не реплицирован независимой стороной без commercial interest. Retro-holdout study (методология arXiv:2410.09247) применительно к MERA предсказуемо показало бы 10–20 pp inflation для top models.

**Пробел 5 — Верифицированные пороги burstiness для русского.** Все числовые пороги экстраполированы из английского. Корпусное исследование: 500+ текстов каждого жанра × human/AI × 6–8 недель.

**Пробел 6 — Причина ретракции Vikhr из ACL.** arXiv:2405.13929 ретрактирован. До установления причины все Vikhr-derived claims (tokenizer efficiency, MERA scores) требуют осторожности.

**Пробел 7 — Что происходит когда MERA полностью насыщается?** Если человеческий baseline будет превышён на 5–10 pp к 2027, бенчмарк потеряет практическую ценность. Какой инструмент придёт на замену? Ответа нет.

---

## 6. Cross-Domain Connections

**Goodhart's Law прямо применим.** «Когда мера становится целью, она перестаёт быть хорошей мерой.» GigaChat и BerryLM — задокументированные случаи оптимизации под MERA вместо оптимизации под Russian text quality. Это не уникально для России — HuggingFace Open LLM Leaderboard был вынужден выпустить v2 по той же причине — но в России отягощается COI в governance.

**RLHF reward hacking.** Тот же механизм, что и в sycophancy и verbosity bias: модель оптимизируется под reward signal (одобрение RLHF-аннотаторов, предпочитающих «professionalism»), что создаёт predictable artifacts (deverbal nouns, hedge phrases, participial stacking). Это documentee в западном контексте (arXiv:2310.10076, Grade C) и применим к русским RLHF-моделям через тот же механизм.

**Readability research и его limits.** Flesch-Kincaid была адаптирована для русского (формула Оберневой, 2006), но признана недостаточно валидным инструментом из-за структурных различий русского и английского. Это демонстрирует более широкую проблему: английские NLP-инструменты не переносятся напрямую в русский контекст без переделки.

**Model collapse и информационная экология.** Nature 2024 (Grade A): рекурсивное обучение на AI-output ведёт к «irreversible distribution collapse» — потере linguistic diversity, исчезновению long-tail паттернов. Это прямо применимо к Runet: документированная «Pravda» disinformation сеть систематически засевает AI-generated Russian content в Common Crawl. Русский интернет становится AI-saturated быстрее, чем Western equivalents.

**Information hazard в evaluation ecosystem.** Когда benchmark scores становятся marketing targets (Сбер публикует GigaChat MERA ranks как PR), возникает information hazard: пользователи принимают решения на основе metrics, оптимизированных организациями с commercial interest.

---

## 7. Practical Implications

### Decision Matrix для практиков

| Задача | Первичная | Вторичная | Обоснование | Confidence |
|--------|-----------|-----------|-------------|------------|
| Длинные статьи / бизнес-текст | Claude Sonnet 4.6 | ChatGPT | Blind eval 8.6/10; min editing for naturalness | MODERATE |
| SEO titles / headlines | YandexGPT 5 Pro | ChatGPT | Digital-native Russian UX patterns | MODERATE |
| Bulk SEO content (100+ статей) | Qwen3-235B | DeepSeek V3 | 130× дешевле при 91% качества | MODERATE |
| Юридические / официальные документы | GigaChat 2 Max | ChatGPT | Russian legal training data | MODERATE |
| Редактура / style editing | Claude | ChatGPT | Best instruction following in Russian | MODERATE |
| Классификация/извлечение из текстов | YandexGPT 5 | GigaChat | 70% vs 51% GPT-4o | MODERATE |
| Неформальный / разговорный стиль | ChatGPT | YandexGPT | Flexible register | MODERATE |
| Конфиденциальные данные (on-premise) | GigaChat | Vikhr | Russian jurisdiction / local deploy | LOW-MODERATE |
| Код + текст | DeepSeek R1 | ChatGPT | Reasoning + writing | LOW |

**Все рекомендации основаны на Grade D practitioner consensus, не на peer-reviewed experimental evidence.** Для конкретного use case: воспроизвести методологию Habr-теста (5 реальных тем × несколько моделей × LLM-judge или blind human evaluation).

### Рекомендованный workflow для качественного русского контента

**Стадия 1 (Research/Structure):** DeepSeek V3 или ChatGPT. Стоимость: ~$0.05–0.10 на 3000-word статью.

**Стадия 2 (Draft Writing):** Claude Sonnet 4.6. Системный промпт: определение голоса, запрет AI-маркеров («следует отметить», «важно понимать», «данный», «комплексный»), лимит тире ≤8 на статью. Стоимость: ~$0.30–0.60.

**Стадия 3 (Style Editing):** Claude или human editor. Проверка: em-dash count, AI-фразы, burstiness, конкретные детали.

**Стадия 4 (Headlines/SEO):** YandexGPT 5 Pro. Генерация H1-вариантов, meta descriptions.

**Суммарная стоимость:** ~$0.45–0.90 на статью 3000 слов (vs ~$1.50–3.00 при Opus only).

### Практическая оценка качества СЕГОДНЯ (до появления R-HLS)

```python
import statistics
import razdel
import pymorphy2

def quick_humanness_check(text):
    """Базовая R-HLS оценка — реализуется сегодня"""

    # 1. Burstiness (вариативность длин предложений)
    sentences = list(razdel.sentenize(text))
    lengths = [len(s.text.split()) for s in sentences]
    B = statistics.stdev(lengths) / statistics.mean(lengths) if len(lengths) > 1 else 0

    # 2. Deverbal noun ratio
    morph = pymorphy2.MorphAnalyzer()
    words = [w for s in sentences for w in s.text.split()]
    nouns = [w for w in words if 'NOUN' in morph.parse(w)[0].tag]
    deverbal_suffixes = ('ение', 'ание', 'ация', 'ство', 'тие')
    deverbals = [w for w in nouns if any(w.lower().endswith(s) for s in deverbal_suffixes)]
    DN = len(deverbals) / max(len(nouns), 1)

    # 3. Em-dash density
    em_dash_count = text.count('—')
    em_per_1000 = em_dash_count / (len(words) / 1000) if words else 0

    # 4. RLHF-artifacts
    ai_phrases = [
        'следует отметить', 'важно понимать', 'таким образом',
        'необходимо учитывать', 'стоит отметить', 'в данном контексте',
        'является ключевым', 'комплексный подход', 'эффективный инструмент'
    ]
    phrase_hits = sum(1 for p in ai_phrases if p in text.lower())

    return {
        'burstiness': round(B, 3),        # цель: > 0.55
        'deverbal_ratio': round(DN, 3),    # цель: < 0.20
        'em_dash_per_1000': round(em_per_1000, 2),  # цель: < 4.0
        'ai_phrase_hits': phrase_hits,     # цель: 0–1
    }
```

**Пороговые ориентиры (extrapolated из English, не валидированы для русского):**

| Метрика | AI-сигнал | Человекоподобный |
|---------|-----------|-----------------|
| burstiness | < 0.35 | > 0.55 |
| deverbal_ratio | > 0.40 | < 0.20 |
| em_dash_per_1000 | > 6.0 | < 4.0 |
| ai_phrase_hits | ≥ 3 | 0–1 |

---

## 8. Methodological Notes

### MERA Evaluation Protocol и его ограничения

**Что MERA измеряет:** Zero-shot и few-shot performance на 15 core tasks (MCQ, classification, QA с открытым ответом, код, математика, диалог). Оценивается через log-likelihood (для MCQ) и greedy generation (для открытых задач). Итоговый score — среднее по базовым задачам.

**Ключевые ограничения:**
- 67% задач — gameable MCQ/classification format (arXiv:2309.03882)
- CC-BY-4.0 источники = structural contamination risk (arXiv:2406.13236)
- Self-reporting: модели сабмитят через MERA API управляемый AI Alliance Russia (Сбер-affiliated)
- Нет confidence intervals — aggregate score без error bars
- Human baseline (0.852) установлен один раз при запуске, не обновляется
- YandexGPT стратегически не участвует в public leaderboard — вероятно, неблагоприятные scores

**Как тестировать модели для Russian writing quality (практическая процедура):**

1. Выбрать 5 реальных задач из своего domain (не generic prompts)
2. Запустить каждую модель на каждую задачу (min 2 seeds)
3. Blind evaluation: человек без знания источника оценивает по 5-point шкале (natуральность, стилистическая уместность, отсутствие AI-markers, фактическая точность, структура)
4. Если нет человека: LLM-judge с explicit rubric (GPT-4 или Claude как судья — REPA: 0.641 Spearman с human для Russian)
5. R-HLS_basic: автоматическая часть (burstiness, DN ratio, em-dash, AI-фразы)
6. Сравнить стоимость × качество для конкретного use case

**Common pitfalls:**

- Доверять MERA-рейтингу для writing tasks → category error
- Использовать English-калиброванные детекторы для Russian → high FP rate
- Применять пороги burstiness из English без адаптации → не валидировано
- Принимать vendor benchmark claims без independent verification (YandexGPT «56% > GPT-4.1» — single-party, no replication)
- Игнорировать COI при цитировании MERA scores для GigaChat

### Source Grading (по METHODOLOGIST)

Grade A (11%): MERA (ACL 2024), RussianSuperGLUE (EMNLP 2020), TAPE (EMNLP 2022), Model Collapse (Nature 2024)
Grade B (26%): RuCoLA (EMNLP 2022), RSG Heuristics (2021), REPA (Slavic NLP 2025), GigaChat MoE (ACL 2025), RuATD 2022, RuBLiMP (EMNLP 2024)
Grade C (51%): Большинство preprints (Vikhr, POLLUX, LIBRA, cross-lingual contamination, em-dash, Think in English, AINL-Eval, LEP, LLaMA tokenization)
Grade D (11%): Habr articles, vc.ru blogs, GigaCheck vendor materials, SLAVA GitHub, MERA leaderboard snapshot

**Предупреждение:** 51% cited sources — Grade C preprints. Только 11% достигли стандарта Grade A. Поле делает сильные количественные claims на слабой доказательной базе.

---

## 9. Key Researchers & Groups

**MERA / AI Alliance Russia:** arXiv:2401.04531 + ACL 2024.acl-long.534. Консорциум: Сбер, МТС AI, Яндекс, ИТМО, Сколтех, НИУ ВШЭ, РАН. Конфликт интересов: Сбер разрабатывает GigaChat и является ключевым членом консорциума.

**POLLUX:** arXiv:2505.24616, MIPT + Сбер. Никита Мартынов и коллеги. COI: Сбер co-authorship.

**RuBLiMP (EMNLP 2024):** arXiv:2406.19232. Независимая команда. 45k минимальных пар, 12 лингвистических явлений. Наиболее независимый peer-reviewed инструмент для Russian linguistic competence.

**REPA (Slavic NLP / ACL 2025):** arXiv:2503.13102. Наиболее независимый инструмент для оценки качества генерации на русском. 10 типов ошибок, human-labeled.

**GigaChat / Сбер:** arXiv:2506.09440 (ACL 2025 Demo). MoE архитектура, 20B параметров, 3.3B активных. Открытые веса для GigaChat-A3B.

**"Think in English" / Wendler et al. 2025:** arXiv:2502.15603. Llama-3.1-70B, Gemma-2-27b, Mixtral-8x22B. Русский не тестировался напрямую.

**RuATD 2022 / Dialogue shared task:** arXiv:2206.01583. Базовый shared task по детекции AI-русского. Human baseline: 66.6%.

**Vikhr / Vikhrmodels:** arXiv:2405.13929 (RETRACTED from ACL — причина не установлена). llmarena.ru и Vikhrmodels HuggingFace leaderboard — наиболее независимые Russian ELO-платформы.

**Russian practitioner community:** Habr.com, vc.ru, Telegram. Grade D, но единственный источник данных о реальном writing quality. Bias: IT-грамотные Московские профессионалы.

---

## 10. Confidence & Limitations

### Global Confidence: 0.35 / 1.00

Это поле, где измерительная инфраструктура структурно скомпрометирована. Доминирующий бенчмарк управляется организациями с прямыми коммерческими интересами в его результатах, доминирован gameable MCQ-форматами, лишён независимой репликации. Единственный альтернативный quality signal (practitioner experience) — методологически Grade D. Академическая литература по Russian-specific humanness detection — nascent.

### Confidence By Section

| Раздел | Confidence | Основание |
|--------|------------|-----------|
| Нет humanness benchmark | HIGH | Консенсус всех потоков, структурный анализ |
| MERA structurally compromised | HIGH | Grade A/B sources, replicated gaming (RSG) |
| Claude #1 MERA | MODERATE | Leaderboard (Grade C/D), not peer-reviewed |
| Tokenization penalty | MODERATE-HIGH | Multiple sources, exact multiplier varies |
| Human detection 66% | MODERATE-HIGH | Grade B (RuATD 2022) |
| BerryLM gaming | MODERATE | Circumstantial evidence, not proven |
| Practitioner model rankings | LOW-MODERATE | Grade D only, biased sample |
| R-HLS thresholds (русские) | LOW | Extrapolated from English, not validated |
| "Think in English" for Russian | LOW | Non-Russian models only, Grade C |
| Em-dash 3.28x ratio | LOW | Single preprint, Grade C, not replicated |

### Field Maturity: CONTESTED

Не EMERGING (инфраструктура существует), но и не ACTIVE в здоровом смысле. CONTESTED потому что:
- Primary evaluation infrastructure — у commercially interested parties
- Independent replication структурно отсутствует
- Gap between benchmark claims и practitioner experience — задокументирован, но не разрешён
- Поле эволюционирует быстро: MERA за 18 месяцев добавил Multi/Code/Industrial variants — любой claim устаревает за 6 месяцев

### 5 RED FLAGS от METHODOLOGIST

1. **RED FLAG — Conflict of Interest в MERA Governance.** Сбер разрабатывает GigaChat и является founding member MERA консорциума. GigaChat MERA scores функционально self-reported. Любое сравнение через MERA с участием GigaChat требует epistemic discount.

2. **RED FLAG — Benchmark Gaming Signal (BerryLM).** Три BerryLM варианта в MERA TOP-10 (#3, #4, #6) от одной организации = canonical gaming signal. Stream A сам это флагирует: «признак туннинга под бенчмарк?»

3. **RED FLAG — Vikhr Retraction.** arXiv:2405.13929 ретрактирован из ACL. Причина ретракции не установлена. Все Vikhr-derived claims (tokenizer efficiency, MERA scores, Ru-MMLU 0.80) требуют осторожности.

4. **RED FLAG — MERA Saturation.** Human baseline (0.852) уже превышен. 12–18 month window до benchmark obsolescence на frontier-уровне.

5. **RED FLAG — «Pravda» Network Contamination.** Задокументированная disinformation network систематически засевает AI-generated Russian content в Common Crawl. Будущие модели, обученные на post-2024 данных, столкнутся с деградированным Russian internet.

### Key Unknowns (Known Unknowns из _reflection_2.md)

- Токенизация 2x vs 3x vs 7–8x — требует контролируемого измерения
- Человеческая детекция 66% vs 90% — разные популяции, нужно разграничить
- BerryLM task-level breakdown — закрытые данные
- «Think in English» применительно к YandexGPT/GigaChat — не протестировано
- R-HLS пороги для русского — нужен верифицированный human corpus

### Что изменило бы этот consensus

1. **Independent MERA replication** европейским university consortium без COI → калибровало бы confidence в leaderboard scores
2. **Retro-holdout study для MERA** (по методологии arXiv:2410.09247) → показало бы реальный inflation magnitude
3. **Russian-specific burstiness/DN ratio corpus study** (6–8 недель, verified human corpus) → заменило бы extrapolated пороги на empirically grounded Russian norms
4. **Logit lens analysis на YandexGPT/GigaChat** → подтвердило или опровергло «Think in English» для Russian-primary models

---

## Прямой ответ на исходный вопрос

**Вопрос:** Какие LLM-модели в 2026 году пишут на русском языке наиболее качественно и «по-человечески» — и какие бенчмарки это измеряют объективно?

**Ответ (калиброванный):**

Ни один из существующих бенчмарков не измеряет это объективно. MERA — ближайший к стандарту, но измеряет task-solving accuracy, а не writing humanness, структурно скомпрометирован COI, и начинает сатурировать. Это не временная проблема — это принципиальный пробел измерительной инфраструктуры.

Лучшая практическая оценка доступна из Grade D practitioner sources (Habr, vc.ru), которые при всей методологической слабости являются единственным источником данных о реальном writing quality:

**Claude Opus/Sonnet 4.x** — наиболее естественный formal и semi-formal Russian, наименьшее количество редактирования для натуральности, #1 MERA (но с asterisk: MCQ-dominated, COI governance, no independent replication).

**YandexGPT 5 Pro** — лучший digital-native Russian для заголовков и short-form content. Structural advantages: обучен на русском поисковом индексе, нативный токенизатор. Structural weakness: слабый на сложной аналитике и reasoning-heavy tasks.

**GigaChat 2 Max** — лучший для юридических и регуляторных документов. Nemesis: «ЕГЭ-шный стиль» в editorial writing. Высокий MERA-балл не транслируется в натуральность текста.

**DeepSeek V3 / Qwen3-235B** — оптимальные по цене/качеству для bulk content. 91% качества при 130× меньшей стоимости vs GPT-5.

Уверенность в этих рекомендациях: **LOW-MODERATE**. Они основаны на Grade D practitioner consensus, могут устаревать за 3–6 месяцев по мере выпуска новых версий, и зависят от конкретного use case.

**Наиболее честный ответ:** Мы не знаем ответ с достаточной уверенностью, потому что инструмента для его измерения не существует. Создание peer-reviewed Russian Human-likeness Benchmark является главным незаполненным gap в области.

---

*Synthesizer: CYCLE 3 Integration | Sources: stream_A, stream_B, stream_C, stream_D, stream_E, _critic_review, _methods_review, deep_dive_A_humanness_criteria, deep_dive_B_berrylm_gap, _reflection_2 | 2026-06-02*
