# PROGRESS LOG — LLM Russian Language Quality
Date: 2026-06-01
Mode: consensus | Domain: science | Priority: high

## Scope
Main question: Какие LLM-модели в 2026 году пишут на русском языке наиболее качественно и «по-человечески» — и какие бенчмарки это измеряют объективно?

## Streams
| Stream | SCOUT | Reasoning style | Topic |
|--------|-------|----------------|-------|
| A | A | Analytical | Русскоязычные NLP-бенчмарки: MERA, RuBQ, TAPE, методология оценки |
| B | B | Contrarian | Критика бенчмарков: gaming, data contamination, что реально показывают vs заявляют |
| C | C | Mechanistic | Механизмы «человечности» текста: burstiness, perplexity, AI-детекция на русском |
| D | D | Systems-thinking | Экосистема русскоязычных LLM: training data, рынок, YandexGPT/GigaChat/open-source |
| E | E | Pragmatic | Практические сравнения моделей: пользовательские тесты, Habr/vc.ru, какую выбрать |

## Coverage check (science taxonomy)
- [x] Theory: Stream A (benchmark theory), C (humanness mechanisms)
- [x] Evidence: Stream A (formal benchmarks), D (training data evidence), E (empirical tests)
- [x] Methodology: Stream A (benchmark design), B (methodology critique)
- [x] Applications: Stream E (practical use), C (AI detection tools)
- [x] Meta-science: Stream B (publication bias, benchmark gaming)
- [x] Boring fundamentals: Stream A includes Cyrillic tokenization, morphology issues

## Status
- [x] Cycle 1 SCOUTs (5/5 done)
- [x] CRITIC + METHODOLOGIST — DONE. Confidence: 0.35/1.0. Field: CONTESTED. 5 RED FLAGS.
- [x] Reflection 1 — DONE. 4 гипотезы. DD-A + DD-B запущены.
- [x] Cycle 2 Deep Divers — DONE. DD-A: R-HLS framework (5/6 критериев автоматизируемы). DD-B: BerryLM anatomy + gaming evidence (circumstantial).
- [x] Reflection 2 — DONE. H1+H3 SUPPORTED, H2 MODERATE, H4 PARTIAL.
- [x] Cycle 3 Synthesis — DONE. consensus_reference.md (72KB, ~9000 слов, 10 секций). Confidence: 0.35. Field: CONTESTED.
- [x] Fact-check — DONE. 68 claims: 46 PASS, 21 WARN, 1 FAIL (CONDITIONAL PASS). FAIL: "90% AI detection for AI-familiar humans" — no source, contradicts RuATD 66.6%. WARN: tokenization 3x source is Ukrainian, not Russian; burstiness thresholds conflicting (0.30 vs 0.35); 67% MCQ is analytical estimate.
- [x] Action map — DONE. _action_map.md: 7 sections (immediate/short/medium-term/watch/anti-patterns/gaps/decision framework). Key: task→model table, R-HLS Python snippet, cost matrix.

## FINAL STATUS: COMPLETE ✅
consensus_reference.md (72KB), _fact_check.md, _action_map.md
Global confidence: 0.35. Field: CONTESTED. Key answer: no benchmark measures Russian humanness; Claude for editorial, Qwen3-235B for bulk, GigaChat for legal.

## Cycle 1 — Scout completion log
- [x] Stream A (Benchmarks) — DONE. 18 бенчмарков найдено. MERA = стандарт (ACL 2024). Нет метрики "humanness". Токенизация: ~3x больше токенов для русского. Claude Opus 4.6 лидирует MERA (0.862). Vikhr retracted. GAP: нет русскоязычной метрики стилистического качества.
- [x] Stream B (Critique) — DONE. Ключевой вывод: MERA геймится (heuristics 2021), contamination от параллельных корпусов, конфликт интересов (Sber=MERA+GigaChat), LLM-judge менее точен для русского (REPA 2025). GAP: нет независимого русскоязычного оценщика.
- [x] Stream C (Humanness) — DONE. Burstiness = статистическая энтропия autoregression. RLHF маркеры, не "человечность". Отглагольные существительные 2x, причастные обороты 2-5x, em-dash 3.28x. GigaCheck 86-94%. AINL-Eval 2025 датасет найден.
- [x] Stream D (Ecosystem) — DONE. GigaChat MoE (ACL 2025, arXiv:2506.09440). "Think in English" механизм (arXiv:2502.15603). 10T токенов, 63.76% EN/26.49% RU. 5 feedback loops включая AI-data contamination.
- [x] Stream E (Practical) — DONE. Нет доминирующей модели — задача определяет победителя. Claude лучший для длинных статей/бизнеса (8.6/10 vs GPT 7.8/10). GigaChat "ЕГЭ-essay" проблема. DeepSeek V3 на 85% дешевле для bulk. Практика: мульти-модельный воркфлоу.
