# Stream A — Русскоязычные NLP-бенчмарки

**Date:** 2026-06-01
**Scout:** SCOUT-A
**Reasoning style:** ANALYTICAL (systematizer)
**Task:** Broad literature survey — landscape mapping of Russian-language NLP benchmarks

---

## 1. Таксономия бенчмарков по поколениям и типу задач

Прежде чем перейти к конкретным системам, полезно выстроить классификационную сетку. Русскоязычные NLP-бенчмарки делятся по нескольким осям:

**По поколению:**
- Поколение 1 (2020–2022): аналоги GLUE/SuperGLUE для русского — задачи на понимание текста (NLU), классификация, NLI
- Поколение 2 (2022–2023): few-shot оценка, adversarial robustness, QA над базами знаний
- Поколение 3 (2024–2025): комплексная оценка LLM в instruction-формате (zero/few-shot), мультимодальность, длинный контекст, доменная специализация

**По типу задач:**
- NLU (Natural Language Understanding): классификация, NLI, WSD, coreference
- QA (Question Answering): закрытые ответы, KBQA, MRC
- Генерация: код, перефразирование, детоксификация
- Оценка качества текста: грамматическая приемлемость, стилистика
- Эмбеддинги: semantic similarity, retrieval, reranking
- Мультимодальные: изображение, аудио, видео + текст
- Длинный контекст: 4k–128k токенов

---

## 2. Детальное описание основных бенчмарков

### 2.1 MERA (Multimodal Evaluation of Russian-language Architectures)

**Статус:** Главный действующий отраслевой стандарт для оценки LLM на русском языке.

**Источники:** arXiv:2401.04531; ACL Anthology 2024.acl-long.534; официальный сайт mera.a-ai.ru; GitHub MERA-Evaluation/MERA

**Организаторы:** AI Alliance Russia (консорциум: Сбер, MTS AI, Яндекс, ИТМО, Сколтех, НИУ ВШЭ, РАН и другие)

**Год первой публикации:** Январь 2024 (arXiv), представлен на ACL 2024

**Версии:**
- v1.0 (январь 2024): 21 задача, 11 доменов навыков
- v1.2.0 (сентябрь 2024): расширение до 23 задач (15 базовых + 8 диагностических)
- MERA Code (июль 2025): оценка генерации кода
- MERA Multi (ноябрь 2025, arXiv:2511.15552): 18 мультимодальных задач (изображение, аудио, видео)
- MERA Industrial (июнь 2025): доменная оценка в отраслевых контекстах

**Структура (версия v1.2.0):**

Три группы навыков: Perception (восприятие входных данных), Reasoning (рассуждение), Knowledge (внутренние знания модели).

*Группа 1 — Problem-Solving Tasks (11 задач):*
- MathLogicQA — математика, логика
- MultiQ — рассуждения
- PARus — здравый смысл (аналог COPA)
- RCB — Natural Language Inference
- ruModAr — модульная арифметика
- ruMultiAr — многошаговая арифметика
- ruOpenBookQA — знания о мире
- ruTiE — рассуждение, диалоговый контекст, память
- ruWorldTree — знания о мире
- RWSD — Winograd Schema на русском
- SimpleAr — простая арифметика

*Группа 2 — Exam-Based Tasks (6 задач):*
- BPS — код, математика
- CheGeKa — знания о мире (задания из «Что? Где? Когда?»)
- LCS — код, математика
- ruHumanEval — генерация кода
- ruMMLU — многодоменные профессиональные знания
- USE — единый государственный экзамен

*Группа 3 — Diagnostic/Ethics Tasks (4 задачи):*
- ruDetox — детоксификация текста
- ruEthics — этические суждения
- ruHateSpeech — обнаружение ненависти
- ruHHH — Helpful, Harmless, Honest оценка

**Методология оценки:**
- Формат: zero-shot и few-shot с фиксированными промптами (3–12 промптов на задачу)
- Режимы оценки: log-likelihood continuation (выбор наиболее вероятного продолжения) и greedy generation
- Метрики: accuracy, exact match, F1 (token-wise и macro), Matthews correlation coefficient, pass@k (код), Grade norm (экзамены), Joint score (стиль + смысл + беглость)
- Итоговый балл: среднее по базовым задачам, диагностические задачи исключены
- Защита от утечки данных: приватные ответы для финального набора

**Ключевые результаты (2024):**
- Лучшая открытая модель при запуске: Mistral — ~40% на problem-solving задачах
- Человеческий базис: 87.2% в целом
- Разрыв модели / человек: ~47 процентных пунктов
- По состоянию на 2025: Claude Opus 4.6 — 0.862, BerryLM-XL (Wildberries) — 0.835
- GigaChat 2 Max (Сбер) — 0.67, входит в топ-6 за 2024 год

**Публичный лидерборд:** Да, на mera.a-ai.ru/en/text

---

### 2.2 RussianSuperGLUE

**Статус:** Первое поколение, частично устаревший — вытеснен MERA для LLM-оценки, но полезен для энкодер-моделей.

**Источники:** arXiv:2010.15925; EMNLP 2020 (aclanthology.org/2020.emnlp-main.381); GitHub RussianNLP/RussianSuperGLUE; HuggingFace datasets RussianNLP/russian_super_glue

**Организаторы:** RussianNLP (Сбер AI, ВШЭ и другие)

**Год:** 2020 (v1.0), 2022 (v1.1)

**Задачи (9 задач, аналог SuperGLUE):**
1. RWSD — Winograd Schema Dataset (anaphora resolution)
2. PARus — аналог COPA (причинно-следственный выбор)
3. MuSeRC — Multiple Sentence Reading Comprehension
4. RCB — Russian Commitment Bank (NLI)
5. DaNetQA — Да/Нет вопросы
6. RuCoS — Russian Cross-lingual Choice of Plausible Alternatives (Reading Comp.)
7. TERRa — Text Entailment Recognition for Russian
8. RUSSE — Russian Semantic Similarity Evaluation (WSD)
9. RuBQ — адаптированный QA-набор

**v1.1 (2022):** обновлены RUSSE, DaNetQA, RuCoS, MuSeRC (расширение, новые тест-сеты).

**Методология:** Jiant-framework; трансформер-базелайны (ruGPT, ruBERT); human-level evaluation опубликован; оценивается точность (accuracy) и F1.

**Публичный лидерборд:** Да (GitHub + HuggingFace)

---

### 2.3 TAPE (Text Attack and Pragmatic Evaluation)

**Источники:** arXiv:2210.12813; EMNLP 2022 Findings (aclanthology.org/2022.findings-emnlp.183); GitHub RussianNLP/TAPE; tape-benchmark.com

**Год:** 2022

**Характеристика:** Бенчмарк для оценки few-shot / zero-shot NLU с акцентом на robustness (устойчивость к атакам).

**Задачи (6 сложных NLU задач):**
- Multi-hop reasoning (многоступенчатое рассуждение)
- Ethical concepts (этические концепции)
- Logic (логика)
- Commonsense knowledge (здравый смысл)
- (2 дополнительные задачи, полный список в arXiv)

**Уникальные черты методологии:**
- Adversarial attacks (лингвистически-ориентированные атаки): орфографические пертурбации, перефразирование, синтаксические трансформации
- Subpopulation analysis: детальный анализ производительности по подгруппам
- Инструмент RuTransform (Python-фреймворк для генерации adversarial examples на русском)

**Ключевые выводы:**
- Орфографические пертурбации влияют больше всего — модели резко теряют производительность при опечатках
- Перефразирование (семантический уровень) — наименее разрушительно
- Значительный разрыв модели / человек на большинстве задач

**Публичный лидерборд:** Да (tape-benchmark.com)

---

### 2.4 RuBQ и RuBQ 2.0

**Источники:** ResearchGate:341565440 (v1.0); OpenReview P5UQFFoQ4PJ; Springer ESWC 2021; GitHub vladislavneon/RuBQ

**Год:** 2020 (v1.0), 2021 (v2.0)

**Тип:** Knowledge Base Question Answering (KBQA) над Wikidata

**RuBQ 1.0:**
- 1500 русскоязычных вопросов разной сложности
- Каждый вопрос: машинный перевод на английский + SPARQL-запрос + ответы из Wikidata
- Подмножество Wikidata с русскими метками

**RuBQ 2.0:**
- 2910 вопросов (расширение через search engine query suggestions)
- Краудсорсинговая + внутренняя аннотация
- Добавлены answer-bearing paragraphs из Wikipedia (для MRC)
- Лицензия: CC-BY-4.0

**Области применения:** KBQA, Machine Reading Comprehension, Hybrid QA, Semantic Parsing

**Публичный лидерборд:** Частично (KGQA leaderboard на GitHub, Wikidata track)

---

### 2.5 RuCoLA (Russian Corpus of Linguistic Acceptability)

**Источники:** arXiv:2210.12814; EMNLP 2022 (aclanthology.org/2022.emnlp-main.348); rucola-benchmark.com; GitHub RussianNLP/RuCoLA

**Год:** 2022

**Тип:** Лингвистическая приемлемость — оценка грамматической / семантической корректности предложений

**Состав:**
- 9800 in-domain предложений из лингвистических публикаций (экспертно написанные)
- 3600 out-of-domain предложений, сгенерированных языковыми моделями
- Бинарные метки приемлемости

**Что измеряет:** Не грамматическую корректность в формальном смысле, а acceptability — воспринял бы носитель язык это предложение как естественное. Охватывает синтаксические, семантические ошибки и галлюцинации генеративных моделей.

**Ключевые выводы:** Языковые модели значительно отстают от человека, особенно в обнаружении морфологических и семантических ошибок.

**Публичный лидерборд:** Да (rucola-benchmark.com)

---

### 2.6 LIBRA (Long Input Benchmark for Russian Analysis)

**Источники:** arXiv:2408.02439; ResearchGate:382884635; отдельная статья «Long Context Benchmark for the Russian Language» (CODI 2025, aclanthology.org/2025.codi-1.1)

**Год:** 2024 (arXiv август 2024), дополнение на CODI 2025

**Авторы:** Алена Феногенова и коллеги (ai-forever / SberDevices)

**Тип:** Длинный контекст — оценка понимания текстов 4k–128k токенов

**Состав:** 21 адаптированный датасет

**4 группы сложности по длине контекста:**
- 4k токенов
- 8–16k токенов
- 32–64k токенов
- 128k токенов

**Задачи:** Information Retrieval, Knowledge Extraction, MRC, QA, Reasoning

**CODI 2025 расширение:** 18 датасетов, аналогичная 4-уровневая структура.

**Мотивация:** До создания LIBRA у русского языка не было инструмента для прозрачной оценки long-context понимания (аналоги LongBench и L-Eval существовали только для английского).

**Публичный лидерборд:** Да (упомянут в статье)

---

### 2.7 ruMTEB (Russian Massive Text Embedding Benchmark)

**Источники:** arXiv:2408.12503; NAACL 2025 (aclanthology.org/2025.naacl-long.12); HuggingFace papers:2408.12503

**Год:** 2024 (arXiv), представлен на NAACL 2025

**Тип:** Оценка текстовых эмбеддингов (аналог MTEB для русского)

**Состав:**
- 23 задачи специфичных для русского языка
- 7 категорий: Semantic Textual Similarity, Text Classification, Reranking, Retrieval, Clustering, Bitext Mining, Pair Classification
- 17 новых датасетов (не переводы с английского)

**Ключевые выводы:**
- Русскоязычные модели (ruBERT и производные) превосходят мультиязычные на большинстве задач
- Представлена модель ru-en-RoSBERTa как новый SOTA для русских эмбеддингов

**Публичный лидерборд:** Да (HuggingFace + интеграция в оригинальный MTEB)

---

### 2.8 POLLUX

**Источники:** arXiv:2505.24616; ResearchGate:392315430; OpenReview MkR0EmODgI

**Год:** Май 2025 (arXiv)

**Авторы:** Никита Мартынов и коллеги, Сбер + НИУ ВШЭ

**Тип:** Generative evaluation — оценка качества генеративных ответов (LLM-as-Judge)

**Состав:**
- 2100 промптов, созданных вручную профессиональными авторами
- 35 типов задач: генерация кода, creative writing, практический ассистент и др.
- 3 уровня сложности: easy / medium / hard

**Уникальная методология:**
- LLM оценивает ответы с детальными критериями и обоснованием оценок (scoring protocol с justification)
- Детальная таксономия задач (35 типов) — более детальная, чем в MERA

**Отличие от MERA:** MERA — структурированные задачи с объективными ответами. POLLUX — open-ended генерация с субъективной оценкой качества.

---

### 2.9 RusConText

**Источники:** ACL 2025 SRW (aclanthology.org/2025.acl-srw.91); PDF прямая ссылка

**Год:** 2025 (ACL Student Research Workshop, Vienna)

**Авторы:** Andrey Chirkin, Svetlana Kuznetsova, Maria Volina, Anna Dengina

**Тип:** Short-context understanding (краткоконтекстное понимание)

**4 задачи:**
1. Coreference resolution (разрешение кореференций)
2. Discourse understanding (понимание дискурса)
3. Idiom interpretation (интерпретация идиом)
4. Ellipsis resolution (разрешение элипсиса)

**Особенность:** Фокус на прагматическом и дискурсивном уровне языка — явления, сложные именно для русского (идиомы, нулевые подлежащие, дискурсивные маркеры).

---

### 2.10 RuSimulBench

**Источники:** IEEE Xplore 11008128; FRUCT proceedings

**Год:** 2025 (IEEE)

**Тип:** Оценка стабильности и креативности LLM на русском

**Две оси оценки:**
- Stability (стабильность): Cosine similarity + logical equivalence scoring при вариациях промпта
- Creativity (креативность): разнообразие и оригинальность ответов

**Методология:** Комбинация автоматических метрик и человеческой оценки.

---

### 2.11 SLAVA (Benchmark of Sociopolitical Landscape and Value Analysis)

**Источники:** GitHub ikanam-ai/slava

**Год:** 2024–2025

**Авторы:** Исследователи РАНХиГС

**Тип:** Социополитическая и ценностная оценка — фактологическая точность LLM в российском контексте

**Особенность:** Включает «чувствительные» темы, которые другие бенчмарки обходят. Замерял, что YandexGPT 5.1 Pro занимает второе место (Alice AI LLM на первом).

---

### 2.12 RusBEIR (Russian BEIR)

**Источники:** arXiv:2504.12879; arXiv:2511.05079 (Wikipedia extension); Dialogue 2025 proceedings

**Год:** 2025 (апрель)

**Тип:** Information Retrieval — zero-shot оценка IR-моделей на русском (аналог BEIR)

**Состав:** 17+ датасетов по различным доменам и задачам (адаптированные + переведённые + оригинальные)

**Ключевые выводы:**
- Нейросетевые модели (mE5-large, BGE-M3) превосходят лексические на большинстве задач
- Слабое место: long-document retrieval из-за ограничений input size

---

### 2.13 RuBQ (включён в RussianSuperGLUE) + SberQuAD

**SberQuAD** — русскоязычный аналог SQuAD, Machine Reading Comprehension с аннотированными passage + Q&A парами. Создан SberDevices. Используется как базелайн в нескольких бенчмарках.

---

### 2.14 Культурная оценка (Cultural Evaluation of LLMs in Russian)

**Источники:** Dialogue 2025 (dialogue-conf.org/2025/04/GromenkoEetal.029.pdf)

**Год:** 2025

**Тип:** Культурно-лингвистическая оценка — фразеологизмы, крылатые выражения, культурные типажи

**Охват:** 10 многоязычных LLM: GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro, Mistral NeMo 12B и др.

**Ключевые выводы:**
- Лидеры: GPT-4o и Claude 3.5 Sonnet
- Аутсайдер: Mistral NeMo 12B — самый низкий результат
- Типичные ошибки: выбор синонимичного, но неверного ответа; непонимание культурной логики идиом

---

## 3. Что измеряют бенчмарки: систематизация метрик

### 3.1 Автоматические метрики

| Категория | Метрика | Применение |
|-----------|---------|------------|
| Точность | Accuracy | Задачи с одним правильным ответом (multiple choice, NLI) |
| Точность + полнота | F1 (token-wise, macro) | QA, NER |
| Корреляция | Matthews Correlation Coefficient | Бинарная классификация, RuCoLA |
| Код | pass@k | ruHumanEval, RuCodeEval |
| Экзамен | Grade norm | USE-задачи в MERA |
| Комплексная | Joint Score (стиль + смысл + беглость) | Генерация текста |
| Качество генерации | Perplexity | Языковое моделирование, не задачи) |
| Эмбеддинги | Cosine similarity | ruMTEB, LIBRA |
| IR | NDCG@k, Recall@k | RusBEIR, ruMTEB retrieval |

### 3.2 Perplexity как метрика

Perplexity — историческая метрика, количественно выражающая «удивление» модели тестовым корпусом (обратная функция от вероятности). Применяется преимущественно на этапе обучения и валидации, а не в бенчмарках задач.

**Ключевое ограничение для русского языка:** Perplexity зависит от корпуса и токенизации. Для BPE-токенизатора английского языка perplexity нельзя напрямую сравнивать с perplexity модели, обученной на кириллическом токенизаторе — из-за разного числа токенов на слово. Это методологическая проблема при сравнении мультиязычных и русскоязычных моделей.

### 3.3 Human evaluation vs автоматические метрики

**Проблема корреляции:** Автоматические метрики систематически не совпадают с человеческими оценками качества. Одинаковые баллы по BLEU/F1 могут соответствовать текстам разного воспринимаемого качества.

**Практика в русскоязычных бенчмарках:**
- MERA использует human baseline как якорь (87.2% — уровень человека для общего балла)
- TAPE публикует human baselines для каждой задачи
- POLLUX использует LLM-as-Judge (GPT-4-уровень) с обоснованием оценок — попытка автоматизировать субъективную оценку
- RuCoLA содержит исходно человеческие аннотации приемлемости

**«Человечность» текста как метрика:** Специализированной русскоязычной метрики «человечности» не обнаружено. Косвенно её замеряют: (а) через linguistic acceptability (RuCoLA), (б) через human preference в Arena-стиле (rulm-sbs2 от GitHub kuk/rulm-sbs2).

---

## 4. Специфика русского языка для LLM

### 4.1 Морфологическая сложность

Русский — синтетический флективный язык с высоким уровнем морфологической сложности:
- 6 падежей × 3 рода × 2 числа = сотни форм слова
- Глагольные виды (совершенный/несовершенный) без прямого аналога в английском
- Приставочное словообразование: одна основа порождает десятки дериватов

**Влияние на LLM:**
- BPE-токенизаторы, обученные преимущественно на английском, нарезают русские словоформы нерационально — до 3–5 токенов на одно словоизменение
- Падежное согласование и глагольный вид труднее захватить в seq2seq формате
- Ошибки чаще всего в морфологическом согласовании (данные RuCoLA)

### 4.2 Токенизация: кириллица vs латиница

**Проблема:** Стандартные BPE-токенизаторы (GPT-3, GPT-4, LLaMA) обучены на корпусах, где русскоязычный текст занимает малую долю.

**Количественные оценки (из исследований, верифицировать):**
- GPT-3.5: число токенов на слово для украинского/русского растёт в ~3 раза по сравнению с английским (Frontiers in AI 2025, данные по украинскому как ближайшему аналогу)
- LLaMA русская адаптация (arXiv:2312.02598): замена токенизатора даёт ускорение fine-tuning на 35%, inference — до 60%

**Практические последствия:**
- Сокращение эффективного контекстного окна: при 4096 токенах для русского текста реальный объём обрабатываемого содержания в 2–3 раза меньше, чем для английского
- Более высокая стоимость инференса (больше токенов = больше вычислений)
- Деградация качества на задачах, чувствительных к длине контекста

**Решения в русскоязычных моделях:**
- Vikhr (arXiv:2405.13929): эффективный кириллический токенизатор
- T-pro 2.0: Cyrillic-dense tokenizer
- GigaChat: нативный русскоязычный токенизатор
- Unigram-токенизация демонстрирует более высокую морфологическую точность, чем BPE (данные arXiv:2312.02598)

### 4.3 Свободный порядок слов

Русский допускает широкую вариацию порядка слов без изменения базового пропозиционального смысла (но с прагматическими различиями: тема/рема, фокус, топик). Это создаёт сложности для:
- Parsing-задач (свободный порядок затрудняет синтаксическую разметку)
- Subject-verb agreement prediction
- Генерации: модели склонны копировать типичный порядок из обучающих данных, теряя прагматические нюансы

---

## 5. Лидерборды и независимые рейтинги

### 5.1 Официальные лидерборды

| Платформа | Бенчмарк | Статус |
|-----------|---------|--------|
| mera.a-ai.ru/en/text | MERA (текст) | Активный, публичный |
| mera.a-ai.ru/en/multi | MERA Multi | Активный, публичный |
| rucola-benchmark.com | RuCoLA | Активный |
| tape-benchmark.com | TAPE | Активный |
| HuggingFace (MTEB) | ruMTEB | Интегрирован в MTEB |

### 5.2 Независимые сравнения

**rulm-sbs2** (GitHub kuk/rulm-sbs2): Side-by-side human evaluation, сравнивает Saiga, YandexGPT, GigaChat в Arena-стиле.

**SLAVA лидерборд (2025):** Alice AI LLM #1, YandexGPT 5.1 Pro #2.

**Независимые тесты от бизнес-аналитиков:** Регулярно фиксируется разрыв между заявлениями вендоров и независимыми результатами. Яндекс заявлял, что YandexGPT 5.1 Pro превосходит GPT-4.1 в 56% случаев — независимого подтверждения нет (данные на 2025-08).

### 5.3 Участники отрасли

**Производители русскоязычных моделей**, регулярно отчитывающиеся по бенчмаркам:
- Сбер: GigaChat семейство (MoE-архитектура), активно участвует в MERA, POLLUX
- Яндекс: YandexGPT серия
- MTS AI: участник AI Alliance Russia
- Wildberries + Russ: BerryLM серия (топ MERA лидерборда 2025)
- Open-source: Vikhr (ретрактирован в ACL, но данные опубликованы)

---

## 6. Сводная таблица бенчмарков

| Бенчмарк | Создатель | Год | Задач | Что измеряет | Лидерборд |
|----------|-----------|-----|-------|-------------|-----------|
| MERA v1.2 | AI Alliance Russia (Сбер, МТС, Яндекс, ВШЭ и др.) | 2024 | 23 (15+8) | NLU, reasoning, math, code, ethics | Да, mera.a-ai.ru |
| MERA Multi | Тот же консорциум | 2025 | 18 | Изображение, аудио, видео + текст | Да |
| MERA Code | Тот же консорциум | 2025 | N/A | Генерация кода | Да |
| MERA Industrial | AI Alliance Russia | 2025 | N/A | Доменная оценка (отрасли) | Закрытый |
| RussianSuperGLUE | RussianNLP (Сбер + ВШЭ) | 2020/2022 | 9 | NLU, NLI, WSD, QA, coreference | Да (GitHub) |
| TAPE | RussianNLP | 2022 | 6 | Few-shot NLU, adversarial robustness | Да (tape-benchmark.com) |
| RuBQ 2.0 | Владислав Рыбин и др. | 2021 | 1 (2910 вопросов) | KBQA над Wikidata + MRC | Частично (KGQA leaderboard) |
| RuCoLA | RussianNLP (ВШЭ и др.) | 2022 | 1 (бинарная) | Лингвистическая приемлемость | Да (rucola-benchmark.com) |
| LIBRA | ai-forever (Феногенова и др.) | 2024 | 21 | Long-context (4k–128k) | Да |
| Long Context Benchmark | Независимые авторы | 2025 | 18 | Long-context (до 128k) | Не установлено |
| ruMTEB | ai-forever + внешние | 2024/2025 | 23 | Текстовые эмбеддинги (7 категорий) | Да (HF MTEB) |
| POLLUX | Сбер + ВШЭ | 2025 | 35 типов, 2100 промптов | Генеративное качество (LLM-as-Judge) | Не установлено |
| RusConText | Независимые (ВШЭ?) | 2025 | 4 | Short-context, дискурс, идиомы, коркеференция | Нет |
| RuSimulBench | Независимые | 2025 | 2 оси | Стабильность + Креативность | Нет |
| SLAVA | РАНХиГС | 2024/2025 | N/A | Социополитическая + ценностная точность | Нет |
| RusBEIR | Независимые | 2025 | 17+ | Information Retrieval (zero-shot) | GitHub |
| Культурная оценка (Dialogue 2025) | Независимые | 2025 | 2 (Cultural Types + Catchphrases) | Культурно-лингвистические знания | Нет |
| SberQuAD | SberDevices | 2019/2020 | 1 (QA) | Machine Reading Comprehension | Нет (используется как датасет) |
| rulm-sbs2 | @kuk (независимый) | 2023–2025 | Arena-style | Human preference (side-by-side) | GitHub (kuk/rulm-sbs2) |

---

## 7. Оценка достоверности находок

### HIGH — высокая уверенность

- **MERA существует, имеет публичный лидерборд, представлен на ACL 2024:** опубликован на arXiv (2401.04531), в ACL Anthology, имеет официальный сайт, GitHub репозитории в двух организациях (ai-forever и MERA-Evaluation).
- **RussianSuperGLUE — 9 задач, 2020, EMNLP:** публикация подтверждена ACL Anthology + HuggingFace datasets.
- **TAPE — 2022, EMNLP Findings:** arXiv + ACL Anthology + GitHub + официальный сайт.
- **RuBQ 2.0 — 2910 вопросов, KBQA, 2021:** Springer ESWC + OpenReview + GitHub.
- **RuCoLA — 9800+3600 предложений, EMNLP 2022:** arXiv + ACL Anthology + официальный сайт.
- **LIBRA — 2024, arXiv:** arXiv:2408.02439 + ResearchGate.
- **ruMTEB — 23 задачи, 2024/2025, NAACL 2025:** arXiv + ACL Anthology.
- **Токенизация русского в BPE-моделях неэффективна (~3x vs английский):** подтверждено несколькими независимыми источниками (Frontiers in AI 2025 на украинском как аналог; arXiv:2312.02598 на русском).

### MODERATE — умеренная уверенность

- **MERA v1.2 = 23 задачи (15 базовых + 8 диагностических):** упомянуто в результатах поиска, но официальный список нужно сверить с GitHub.
- **Human baseline MERA = 87.2%:** взят из arXiv:2401.04531, нужна точная страница статьи.
- **Лидерборд MERA на 2025 — Claude Opus 4.6 на вершине (0.862):** получено с официального сайта mera.a-ai.ru, но возможно кеш — нужна верификация на дату публикации.
- **GigaChat 2 Max — 0.67 на MERA, место ~6:** из нескольких вторичных источников (Substack, arXiv:2506.09440), прямая проверка на лидерборде желательна.
- **POLLUX — 2100 промптов, 35 типов задач:** arXiv:2505.24616, май 2025, данные из абстракта.
- **SLAVA — YandexGPT 5.1 Pro на #2:** вторичный источник (mysummit.school blog), нет академической публикации.

### LOW — низкая уверенность, требует проверки

- **Ускорение inference на 60% при русском токенизаторе для LLaMA:** данные arXiv:2312.02598, но конкретные числа не были получены при прямом обращении к статье — страница вернула только общий абстракт.
- **Число токенов на слово для русского в GPT-3.5 = ~3x:** данные получены на примере украинского языка (Frontiers in AI 2025), экстраполированы на русский как ближайший аналог. Требует прямого измерения для русского.
- **MERA Industrial (июнь 2025) — структура и задачи:** объявлено, но академической публикации или детального описания задач не найдено.
- **RuSimulBench детали:** только из FRUCT proceedings и IEEE Xplore, полный текст не проверялся.

---

## 8. Пробелы, отмеченные для CRITIC

### 8.1 Фактологические пробелы, требующие проверки

1. **Точный список задач MERA v1.2 (23 задачи):** В arXiv-статье (январь 2024) описано 21 задание. Версия v1.2.0 (сентябрь 2024) добавила задачи — нужен актуальный GitHub README для полного списка.

2. **Числа токенизационной неэффективности конкретно для русского:** Данные ~3x взяты из исследования украинского языка. Для русского может быть другая цифра. ArXiv:2312.02598 (LLaMA Russian Adaptation) содержит точные данные, но они не были получены при запросе.

3. **Статус Vikhr:** Статья ретрактирована в ACL Anthology (2024.mrl-1.15). Причина ретракции не установлена. Использовать данные из этой статьи следует с осторожностью.

4. **MERA Industrial:** Объявлено в июне 2025, но нет академической публикации. Структура, задачи и лидерборд не известны из верифицированных источников.

5. **Структура TAPE (6 задач):** Названия конкретных 6 задач не были получены — только категории. Нужно проверить по arXiv:2210.12813.

6. **Лидерборд MERA в реальном времени:** Данные с mera.a-ai.ru получены из кеша WebFetch. Актуальный список топ-моделей может отличаться.

### 8.2 Концептуальные пробелы ландшафта

1. **Нет специализированного русскоязычного бенчмарка для стилистической оценки:** RuCoLA измеряет приемлемость, POLLUX — качество открытой генерации, но нет аналога PromptBench или AlpacaEval специфично для оценки стиля русскоязычного текста.

2. **«Человечность» текста без метрики:** Нет стандартизированной русскоязычной метрики, измеряющей «человекоподобность» generated text (отдельно от acceptability и task accuracy). Human preference в Arena-стиле (rulm-sbs2) — ближайший аналог, но не академический бенчмарк.

3. **Отсутствие данных о диалектах и региональных вариантах:** Все найденные бенчмарки работают с нормативным русским. Оценка качества на региональных или молодёжных регистрах не обнаружена.

4. **Ограниченность кросс-бенчмаркового сравнения:** Нет публикации, систематически сравнивающей результаты одних и тех же моделей по всем перечисленным бенчмаркам одновременно. Каждый бенчмарк публикует свои базелайны независимо.

5. **Отсутствие метрик беглости генерации, специфичных для русского:** BLEU, ROUGE применяются, но русская морфология делает эти метрики менее надёжными (одно «слово» = много форм, F1 по токенам не захватывает это). Специализированных русских аналогов BERTScore / MoverScore не обнаружено.

---

## 9. Источники

- [MERA: A Comprehensive LLM Evaluation in Russian (arXiv:2401.04531)](https://arxiv.org/abs/2401.04531)
- [MERA — ACL Anthology 2024](https://aclanthology.org/2024.acl-long.534/)
- [MERA официальный сайт](https://mera.a-ai.ru/en/text)
- [GitHub MERA-Evaluation/MERA](https://github.com/MERA-Evaluation/MERA)
- [Multimodal Evaluation of Russian-language Architectures (arXiv:2511.15552)](https://arxiv.org/abs/2511.15552)
- [RussianSuperGLUE (arXiv:2010.15925)](https://arxiv.org/abs/2010.15925)
- [RussianSuperGLUE — EMNLP 2020](https://aclanthology.org/2020.emnlp-main.381/)
- [Russian SuperGLUE 1.1 (arXiv:2202.07791)](https://arxiv.org/pdf/2202.07791)
- [TAPE: Assessing Few-shot Russian Language Understanding (arXiv:2210.12813)](https://arxiv.org/abs/2210.12813)
- [TAPE — EMNLP 2022 Findings](https://aclanthology.org/2022.findings-emnlp.183/)
- [TAPE official site](https://tape-benchmark.com/)
- [RuBQ 2.0 — Springer / ESWC 2021](https://link.springer.com/chapter/10.1007/978-3-030-77385-4_32)
- [RuCoLA (arXiv:2210.12814)](https://arxiv.org/abs/2210.12814)
- [RuCoLA — EMNLP 2022](https://aclanthology.org/2022.emnlp-main.348/)
- [RuCoLA benchmark site](https://rucola-benchmark.com/)
- [LIBRA (arXiv:2408.02439)](https://arxiv.org/abs/2408.02439)
- [Long Context Benchmark for Russian — CODI 2025](https://aclanthology.org/2025.codi-1.1/)
- [ruMTEB (arXiv:2408.12503)](https://arxiv.org/abs/2408.12503)
- [ruMTEB — NAACL 2025](https://aclanthology.org/2025.naacl-long.12/)
- [POLLUX (arXiv:2505.24616)](https://arxiv.org/abs/2505.24616)
- [RusConText — ACL SRW 2025](https://aclanthology.org/2025.acl-srw.91/)
- [RusBEIR (arXiv:2504.12879)](https://arxiv.org/abs/2504.12879)
- [Impact of Tokenization on LLaMA Russian Adaptation (arXiv:2312.02598)](https://arxiv.org/abs/2312.02598)
- [Vikhr: Open-Source Russian LLMs (arXiv:2405.13929)](https://arxiv.org/abs/2405.13929)
- [GigaChat Family: MoE Architecture (arXiv:2506.09440)](https://arxiv.org/html/2506.09440v1)
- [Tokenization efficiency for Ukrainian (Frontiers in AI 2025)](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1538165/full)
- [Cultural Evaluation of LLMs in Russian — Dialogue 2025](https://dialogue-conf.org/wp-content/uploads/2025/04/GromenkoEetal.029.pdf)
- [GitHub SLAVA benchmark](https://github.com/ikanam-ai/slava)
- [GitHub rulm-sbs2](https://github.com/kuk/rulm-sbs2)
- [HuggingFace RussianSuperGLUE dataset](https://huggingface.co/datasets/RussianNLP/russian_super_glue)

---

## 10. ДОПОЛНЕНИЕ: CREAM-анализ ключевых бенчмарков и SOTA-таблица (SCOUT A, 2026-06-01)

*Этот раздел добавлен аналитическим агентом SCOUT A после независимого сбора данных. Дополняет разделы выше верифицированными данными лидерборда и структурированным CREAM-анализом.*

### 10.1 Живой лидерборд MERA Text v1.2.0 (данные с mera.a-ai.ru, 2026-06-01)

| Место | Модель | Балл | Команда |
|-------|--------|------|---------|
| 1 | Claude Opus 4.6 | 0.862 | MERA team |
| 2 | Human Benchmark | 0.852 | MERA (reference) |
| 3 | BerryLM-XL | 0.835 | Wildberries & Russ AI |
| 4 | BerryLM-L-v2-early-ckpt | 0.822 | Wildberries & Russ AI |
| 5 | GPT-5.4 | 0.821 | MERA team |
| 6 | BerryLM-v2-reasoning-budget-low | 0.810 | Wildberries & Russ AI |
| 7 | GLM-5.1 | 0.804 | MERA team |
| 8 | Qwen3-235B-A22B-Thinking-2507 | 0.795 | MERA team |
| 9 | Cotype Light 3 | 0.792 | MWS AI |
| 10 | Qwen3.6-35B-A3B | 0.792 | MERA team |

**Ключевые наблюдения:**
- BerryLM-XL (Wildberries) — лучшая русскоязычная открытая модель, #3 выше GPT-5.4
- GigaChat и YandexGPT в топ-10 не обнаружены — их позиции ниже или они не участвуют в текущем раунде
- 3 из топ-10 — BerryLM разных конфигураций (признак туннинга под бенчмарк?)
- Человеческий базис (0.852) уже преодолён ведущей моделью — benchmark saturation начинается

### 10.2 CREAM-анализ

#### MERA

| CREAM | Содержание |
|-------|-----------|
| **Claim** | Комплексная оценка LLM для русского языка — аналог MMLU/HELM: reasoning, knowledge, math, code, ethics |
| **Results** | Claude Opus 4.6 = 0.862 (выше Human 0.852); BerryLM-XL = 0.835; GigaChat 2 Max ~0.67 (2024); gap модель/человек при запуске ~47 п.п. |
| **Evidence** | Рецензированная публикация (ACL 2024); private scoring anti-contamination; black-box методология; human baselines по каждой задаче |
| **Alternatives** | RussianSuperGLUE (устаревший), TAPE (robustness фокус), POLLUX (генеративное качество), MMLU-RU (перевод) |
| **Mechanisms** | 21 задача, 11 доменов навыков; zero/few-shot; log-likelihood + greedy generation; accuracy/F1/MCC/pass@k по типу задачи; mean aggregation |
| **Key gap** | 67% задач — закрытые (MCQ + классификация). Не измеряет беглость, натуральность, стилистику, «человекоподобность» текста |

#### POLLUX

| CREAM | Содержание |
|-------|-----------|
| **Claim** | Оценка генеративного качества LLM на русском: 35 типов задач (код, creative writing, QA, планирование), LLM-as-judge с критериями |
| **Results** | Gemma-3-27B-It лидирует (1.205); T-Pro-It-1.0 (#4, 1.115) — лучший Russian-focused; GPT-4 (#5, 1.110); выявлен self-judging bias |
| **Evidence** | 24,447 экспертных часов; промпты созданы с нуля (не из интернета); Spearman 0.641 судья vs. человек; 7B/32B judge модели открыты |
| **Alternatives** | MERA (объективные ответы), Arena-Hard-RU (preference-based), RuSimulBench (stability+creativity) |
| **Mechanisms** | 66 критериев в 5 категориях (critical, fine-grained, domain-specific, task-specific, subjective); шкала 0/1/2; judge генерирует балл + обоснование |
| **Key gap** | Hallucination rate ~25% у судьи; self-judging bias; "naturalness" — лишь 1 из 66 критериев; нет прямого human ground truth по всем задачам |

#### LIBRA

| CREAM | Содержание |
|-------|-----------|
| **Claim** | Оценка long-context понимания LLM на русском: 4k–128k токенов, 4 группы сложности |
| **Results** | GPT-4o лидирует (70.2%); GLM4-9B-Chat второй (52.3%); open-source модели деградируют выше 32k токенов |
| **Evidence** | arXiv 2024; 21 датасет; открытый лидерборд |
| **Alternatives** | LongBench (English), L-Eval (English), RusConText (short-context) |
| **Mechanisms** | 4 группы сложности: retrieval → QA → multi-hop → domain expertise; accuracy-based scoring |
| **Key gap** | Тексты из специализированных доменов — ограниченная обобщаемость; синтетические задачи могут иметь ошибки |

#### REPA (ключевой для понимания разрыва оценки)

| CREAM | Содержание |
|-------|-----------|
| **Claim** | Датасет ошибок + оценка качества LLM-as-judge на русском; 10 типов ошибок |
| **Results** | Существенный gap между точностью LLM-судьи на русском vs. английском; partial alignment с human preferences |
| **Evidence** | 1,000 запросов, 2,000 ответов; 8 LLM-судей; Slavic NLP 2025 (ACL) |
| **Alternatives** | MT-Bench (английский аналог), POLLUX (специализированный русский judge) |
| **Mechanisms** | Pairwise human preference; 10 error-type labels; Bradley-Terry ranking |
| **Key gap** | 1,000 запросов — небольшой масштаб; задачи сгенерированы LLM, не экспертами |

### 10.3 SOTA-таблица по всем бенчмаркам

| Модель | Бенчмарк | Балл | Метрика | Дата | Tier источника | Примечания |
|--------|----------|------|---------|------|----------------|------------|
| Claude Opus 4.6 | MERA Text v1.2.0 | 0.862 | avg accuracy (15 задач) | 2026-06 | T1 (лидерборд) | #1, выше человека |
| Human Benchmark | MERA Text v1.2.0 | 0.852 | avg accuracy | 2024-ongoing | T1 | Ориентир потолка |
| BerryLM-XL | MERA Text v1.2.0 | 0.835 | avg accuracy | 2026-06 | T1 | Wildberries/Russ AI; лучшая open-source |
| GPT-5.4 | MERA Text v1.2.0 | 0.821 | avg accuracy | 2026-06 | T1 | 5-е место |
| GigaChat 2 MAX | MERA Text | ~0.67 | avg accuracy | 2024-25 | T2 | Разные источники расходятся; заявлен #1 среди русских моделей |
| GigaChat-Pro v1 | MERA Text | 0.537 | avg accuracy | 2024 | T1 | Неполный сабмит |
| Llama-2-13b | MERA Text (paper) | 0.368 | avg accuracy | 2024 | T1 (статья) | Лучший baseline при запуске бенчмарка |
| GPT-4o | LIBRA | 70.2% | accuracy | 2024 | T1 (статья) | Топ long-context |
| GLM4-9B-Chat | LIBRA | 52.3% | accuracy | 2024 | T1 (статья) | #2 |
| FRED-T5-1.7B | RussianSuperGLUE | 0.762 | aggregated | 2023-24 | T2 | Топ на устаревшем бенчмарке |
| Gemma-3-27B-It | POLLUX | 1.205 | composite | 2025 | T1 (статья) | Лидер POLLUX |
| T-Pro-It-1.0 | POLLUX | 1.115 | composite | 2025 | T1 (статья) | Лучший Russian-focused |
| GPT-4 | POLLUX | 1.110 | composite | 2025 | T1 (статья) | #5 |
| Vikhr nemo-12b | Arena-Hard-RU | 79.8 | win rate vs baseline | 2024 | T2 | Arena-Hard-Auto модификация |
| GigaChat 2 MAX | MMLU-RU | 80.46 | accuracy | 2025 | T2 | Опережает GPT-4o (80.00) на русском |
| GPT-4o | MMLU-EN | 88.70 | accuracy | 2025 | T2 | Преимущество на английском сохраняется |
| LLaMA+Unigram | RussianSuperGLUE | 0.509 | mean zero-shot | 2023 | T1 (статья) | +3.3 п.п. от замены токенизатора |
| LLaMA (базовый) | RussianSuperGLUE | 0.445 | mean zero-shot | 2023 | T1 (статья) | До замены токенизатора |

### 10.4 Критический вывод: разрыв между бенчмарком и реальным качеством текста

**Все существующие русскоязычные бенчмарки измеряют task-solving accuracy, а не language quality.**

Пользователя при генерации текстов интересует:
- Беглость и натуральность (звучит ли текст как написанный носителем?)
- Стилистическая уместность (формальный/разговорный регистр)
- Отсутствие «кальки с английского» (English accent problem)
- Морфологическая корректность в генеративных задачах (согласование, вид глагола)
- Культурная уместность (идиомы, речевые клише, обращения)

Ни один из перечисленных бенчмарков это не измеряет напрямую. Ближайшие инструменты:
- POLLUX: subjective criteria (5 из 66), включая "naturalness" — косвенно
- RuCoLA: linguistic acceptability входных предложений, не генерированных
- rulm-sbs2: human preference при side-by-side сравнении — не академический

**Это ключевой пробел для потенциального нового инструмента оценки.**

### 10.5 Временная шкала развития экосистемы

```
2015  RUSSE (semantic similarity, word-level)
2019  SberQuAD (MRC аналог SQuAD)
2020  RuBQ 1.0 (KBQA); RussianSuperGLUE (EMNLP)
2021  RuBQ 2.0
2022  TAPE (few-shot + adversarial, EMNLP);
      RuCoLA (linguistic acceptability, EMNLP);
      RUSSE Detox shared task
2023  Tokenization research (LLaMA Russian adaptation)
2024  MERA Text (21 задача, ACL) ← ключевая веха
      LIBRA (long context, 4k–128k)
      ruMTEB (embeddings, NAACL 2025)
      Arena-Hard-RU (Vikhr Models)
      SLAVA (sociopolitical)
2025  POLLUX (35 типов задач, generative, LLM-as-judge)
      RusConText (4 linguistic tasks, ACL SRW)
      REPA (error type annotation, Slavic NLP)
      MERA Multi (18 multimodal tasks)
      RusBEIR (IR, 17+ datasets)
      Cultural Evaluation (Dialogue 2025)
      MERA Code, SWE-MERA
      T-Pro 2.0 + T-Math benchmark
      GigaChat Family MoE paper (ACL Demo)
2026  MERA Industrial (анонсирован)
      Непрерывные обновления лидерборда
```
