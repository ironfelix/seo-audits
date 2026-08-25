# Stream E: Practical LLM Comparison for Russian Writing

**Researcher:** Scout E (Pragmatic)
**Date:** 2026-06-01
**Focus:** What practitioners, writers, and content creators actually experience — not benchmarks

---

## Key Findings (14 items with confidence)

### 1. No single model dominates Russian writing — task type determines the winner
**Confidence: HIGH** (confirmed by 6+ independent sources)

Every practitioner-facing review from 2025-2026 arrives at the same conclusion: no single model wins across all Russian writing tasks. The practical split:
- Claude: natural long-form prose, minimal bureaucratic tone, style consistency
- ChatGPT/GPT-5.x: structured content, emotional copy, mixed-language prompts
- DeepSeek V3: cost-effective SEO drafts, factual/technical material
- YandexGPT 5 Pro: headlines, digital-native style, content planning
- GigaChat: Russian business/legal context, no VPN friction

**Action:** Build a multi-model workflow, not a single-model dependency.

---

### 2. Claude produces the least "AI-sounding" Russian prose — but struggles with slang and informal registers
**Confidence: HIGH** (multiple practitioner sources, Habr user study)

Claude (Sonnet/Opus 4.x) consistently earns the highest marks for naturalness in formal and semi-formal Russian writing. One Habr author with two months of comparative use reported "significantly fewer stylistic and semantic edits" after Claude output vs ChatGPT. A blind evaluation study scored Claude Opus 4.6 at 8.6/10 for prose quality vs GPT-5.4's 7.8/10.

However, documented weakness: Claude knows "основные выражения" of slang but fails with current internet slang, meme language, and informal register. It defaults to educated-neutral Russian even when instructed otherwise.

**Action for ФП content:** Claude is the correct primary writer for expert articles, business case studies, analytical pieces. Do not rely on it for colloquial voice without heavy prompting.

---

### 3. ChatGPT is the safer default for mixed-language prompts and structured formats
**Confidence: HIGH**

When prompts contain English instructions alongside Russian output requirements, or when the task requires strict formatting (extraction, lists with exact counts, date formats), ChatGPT outperforms Claude. The critical finding from rephrase-it.com's 2026 comparison: both models exhibit "English gravity well" behavior — internally processing through English representations before generating Russian. ChatGPT recovers more reliably from this under "realistic, messy prompts."

Specific failure mode documented for Claude: under bilingual pressure or when the system prompt is in English but output must be in Russian, Claude drifts linguistically more than ChatGPT.

**Action:** Use ChatGPT when the pipeline involves English system prompts, when content requires precise structural compliance, or when dealing with bilingual documents.

---

### 4. GigaChat produces recognizably formulaic Russian — the "ЕГЭ essay" problem
**Confidence: HIGH** (direct Habr test with human evaluators)

In a documented Habr test where ChatGPT-4o, GigaChat, YandexGPT, and a human writer produced a ~1500-character journalistic piece, GigaChat's output was described by the author as exhibiting "шаблонность сочинения ЕГЭ по русскому" (the formulaic structure of a Russian school exam essay). The text was immediately recognizable as AI-generated and "режет глаз" (jarring to read).

GigaChat's advantage is Russian business/legal context knowledge, format instruction adherence (improved 2x in GigaChat 2 MAX per Sber's own claims), and frictionless access without VPN.

**Action:** GigaChat is viable for internal documents, regulatory text, documentation — not for public-facing editorial content where voice matters.

---

### 5. YandexGPT produces modern, digital-native Russian — but struggles with complex reasoning
**Confidence: HIGH**

YandexGPT 5 Pro earned perfect 5-star ratings for headlines and content planning in a BotHub comparison, with outputs described as "more contemporary and aligned with internet writing style." This is its genuine advantage: the model is trained on the Russian web, so it writes like the Russian web.

Critical weakness confirmed by test: YandexGPT scored 1 out of 5 on logic/programming tasks. The writing quality degrades on analytical and multi-step reasoning tasks. Also: free tier capped at 20 responses/day — unusable for production workflows without paid subscription.

**Action:** Use YandexGPT for headline generation, content plan creation, short-form social posts. Do not use for long analytical articles.

---

### 6. The core technical reason GPT models struggle with Russian: tokenizer fragmentation
**Confidence: HIGH** (documented technical analysis, Habr article with empirical data)

OpenAI's tokenizer treats Russian as character-level rather than word-level. The English pangram (43 chars) takes 9 tokens; the Russian equivalent (53 chars) takes 70 tokens. This creates documented failure modes:
- Case ending errors (probability distributions for individual letters become near-equal)
- "Frequency penalty" parameter actively harms Russian output — penalizes letter repetition rather than word repetition
- The model "answers in letters, not words" for Russian

This is a structural disadvantage for GPT models that cannot be fully overcome by prompting. Newer GPT versions have partially mitigated this via better multilingual training data, but the tokenizer architecture remains.

**Action:** When using GPT API for Russian, avoid frequency_penalty > 0. Expect slightly higher token costs due to fragmentation (roughly 7-8x more tokens per equivalent Russian text vs English).

---

### 7. Claude's specific Russian failure modes: idioms, hyper-formal punctuation, contemporary culture
**Confidence: MEDIUM-HIGH**

Documented specific Claude weaknesses:
- Phraseological precision: occasionally misuses idioms (e.g., "как горох об стену" instead of "как об стенку горох") — semantically equivalent but noticeable to native speakers
- Contemporary Russian internet culture and slang: knows the expressions but applies them mechanically
- Long creative works (2000+ words): stylistic averaging and voice inconsistency appear
- Cultural specificity: address formats, government documents, regional realities — defaults to "international" neutral

Documented Claude strength that mitigates: near-professional-level Russian punctuation (comma placement, em-dash usage between subject and predicate) — this is where GPT models visibly stumble.

**Action:** Always include a style reference/persona in Claude prompts. For any text over 2000 words, break into sections with style anchors.

---

### 8. AI-generated Russian text has 12 documented detection markers — some model-specific
**Confidence: HIGH** (Habr analytical article with empirical data)

Key detection markers for Russian AI text (from Habr's documented analysis):
- Em-dash overuse: AI average 10.62 per 1000 words vs human baseline of 3.23
- Participle chain overuse
- Exactly-three-item lists
- Promotional vocabulary: "уникальный," "потрясающий," "комплексный"
- English calques: "играет ключевую роль," "на сегодняшний день"
- Hedging phrases: "важно отметить," "следует подчеркнуть," "необходимо понимать"

Model-specific signatures:
- **ChatGPT**: most polished, maximum em-dash, promotional register
- **Claude**: more narrative, longer hedge-filled sentences, careful structure
- **DeepSeek**: driest, most personality-free — grammatically correct but forgettable

Human readers familiar with AI tools detect AI text at ~90% accuracy. Automated detectors drop to 67% F1 in cross-domain scenarios.

**Action for ФП content:** The CLAUDE.md anti-checklist targets exactly these markers. The 8-em-dash rule directly addresses the #1 detection signal (AI average is 10.62 per 1000 words). This is validated by independent research.

---

### 9. DeepSeek V3 is the cost-quality sweet spot for SEO bulk content in Russian
**Confidence: MEDIUM-HIGH**

Multiple practitioner reports confirm DeepSeek V3 as the economically rational choice for volume SEO content in Russian:
- API cost: $0.28/$0.42 per million tokens (input/output) — approximately 85% cheaper than GPT-5.2, 97% cheaper on output
- One content freelancer reported API costs under $10/month to produce 45-50 articles
- One Habr review notes "низкий perplexity на кириллице" and near-publication-ready text with proper grammar and idioms
- Writing style: grammatically correct but "dry, forgettable" — requires style layer

Practical workflow reported: DeepSeek gathers research and produces factual draft, Claude refines style.

**Action:** For high-volume, factual SEO content in Russian, DeepSeek V3 is the economically correct choice. Add a Claude editing pass for voice consistency.

---

### 10. The "hybrid pipeline" approach is now the practitioner consensus for quality Russian content
**Confidence: HIGH** (confirmed by 5+ independent practitioner sources)

The dominant recommendation across vc.ru, Habr, and practitioner blogs in 2025-2026 is not "which model" but "which model for which stage":

- **Research/structure**: DeepSeek V3 or ChatGPT
- **Writing/draft**: Claude (long-form) or ChatGPT (structured/promotional)
- **Style refinement**: Claude
- **Trend/SEO alignment**: Gemini (Google algorithm proximity)
- **Headlines/social**: YandexGPT

No single model wins. The consensus is multi-model workflow.

**Action:** The existing ФП pipeline (researcher → writer → editor) already aligns with this. The recommendation is to be explicit about *which* model runs which stage.

---

### 11. Gemini is underrated for Russian, overrated for voice
**Confidence: MEDIUM**

Gemini 3.1 Pro scored best for creative Russian writing in a Habr/BotHub multi-model comparison (humorous story with three chapters), edging out Claude on humor and situational comedy. However, multiple sources describe Gemini's Russian as "slightly impersonal" and lacking in voice for business contexts. Its core advantage: Google algorithm proximity for SEO content and multimodal capabilities.

Cost advantage: In the BotHub comparison, Gemini cost 20 rubles per task vs ChatGPT's 25 and Claude's 68 rubles.

**Action:** Consider Gemini for creative/narrative content and Google-indexed SEO where algorithm alignment matters. Not the default for B2B business writing.

---

### 12. YandexGPT results exceed ChatGPT on Russian-language benchmarks — but benchmark ≠ writing quality
**Confidence: MEDIUM**

Per MERA benchmark (Russian-language evaluation standard): GPT-5.2 scores 0.707, GigaChat 3 Ultra Preview 0.683. YandexGPT Pro 5.1 is absent from public benchmarks due to API limitations. GigaChat 2.0 MAX scores 80.46% on MMLU (Russian) vs GPT-4o at 80.00%.

The practical disconnect: GigaChat's MERA superiority does not translate to better writing quality — its formulaic tendencies override benchmark performance. YandexGPT's digital-native naturalness scores poorly on analytical benchmarks but better in user-facing writing tests.

**Action:** Do not use MERA or MMLU scores as proxies for writing quality. Test on actual use-case prompts.

---

### 13. Professional copywriters use multi-model workflows, with Claude and ChatGPT as the core pair
**Confidence: HIGH**

Survey-style findings from Russian practitioner sources: 60% of professional copywriters now work in AI collaboration. The typical setup reported: ChatGPT for quick queries, image generation, and first-pass structure; Claude for substantial writing projects, complex editing, and long-form drafts. DeepSeek for budget-constrained bulk production.

One specific pattern: "Claude для редактирования, ChatGPT для первичной структуры" (Claude for editing, ChatGPT for initial structure) appears across multiple independent sources.

**Action:** This validates the existing ФП pipeline structure — writer (Claude) + editor (Claude) is the correct core pair for quality content.

---

### 14. Editing time reduction is real but not zero — all models require editorial work for publication-quality Russian
**Confidence: HIGH**

No model produces publication-ready Russian without editing. What varies is the type of editing required:
- **Claude output**: style/voice adjustment, removing over-hedged phrases, tightening em-dashes
- **ChatGPT output**: removing English calques, structural list-breaking, adding voice
- **DeepSeek output**: adding personality, reducing dryness, fact-specific additions
- **YandexGPT output**: removing excess length, adding depth, coherence in longer texts
- **GigaChat output**: breaking formulaic structure, adding authentic voice

The practitioner estimate: AI reduces writing time by 50-70% but editorial time remains at 30-50% of original human writing time for quality content.

---

## Model Ranking Table by Use Case

| Use Case | Rank 1 | Rank 2 | Rank 3 | Rank 4 | Notes |
|----------|--------|--------|--------|--------|-------|
| Long-form article (1000+ words) | Claude | ChatGPT | DeepSeek | Gemini | Claude: least editing for naturalness |
| Business writing (деловой стиль) | Claude | ChatGPT | YandexGPT | GigaChat | Claude: best tone control |
| Colloquial/informal Russian | ChatGPT | YandexGPT | Claude | GigaChat | ChatGPT: more flexible register |
| Technical writing (Russian) | DeepSeek | ChatGPT | Claude | — | DeepSeek: best cost/quality ratio |
| SEO/marketing content | ChatGPT | Claude | DeepSeek | Gemini | Hybrid approach recommended |
| Headlines / short digital copy | YandexGPT | ChatGPT | Claude | — | YandexGPT: modern web Russian |
| Creative/narrative | Gemini | Claude | ChatGPT | — | Gemini: humor and narrative irony |
| Bulk content production | DeepSeek | ChatGPT | GigaChat | — | DeepSeek: 85% cheaper than GPT-5 |
| Legal/regulatory documents | GigaChat | ChatGPT | YandexGPT | — | GigaChat: Russian legal context |
| Editing existing text | Claude | ChatGPT | — | — | Claude: best instruction adherence |

---

## Specific Failure Modes Per Model

### GPT-4o / GPT-5.x
- English calques in Russian output ("играет ключевую роль," "на сегодняшний день")
- Tokenizer fragmentation causes subtle case-ending errors under frequency_penalty > 0
- Language drift under bilingual prompts — may mix languages mid-response
- Excessive em-dash usage in formal Russian (primary AI-detection signal)
- Verbose disclaimers on sensitive topics that interrupt text flow
- "Promotional register" default — outputs sound like ad copy when writing informational content

### Claude Sonnet/Opus 4.x
- Phraseological imprecision on rare/archaic Russian idioms
- Contemporary Russian internet slang: knows expressions but applies mechanically
- Stylistic averaging in texts over 2000 words
- Defaults to "educated-neutral" register even when informal style is requested
- Over-hedging: hedge-filled sentences that read as cautious rather than authoritative
- Cultural specifics: Russian address formats, government procedures, regional realities
- Higher cost: Claude Opus 4.6 at $5/$25 per M tokens vs DeepSeek at $0.28/$0.42

### YandexGPT 5 Pro
- Logical reasoning and multi-step analysis: scores 1/5 in structured tests
- Produces "too long" responses with unnecessary filler sections
- Free tier: 20 requests/day limit — unusable for production without paid plan
- Context retention issues in longer multi-turn conversations
- Analytical depth insufficient for expert-level business content

### GigaChat 2.x/3 Ultra
- "ЕГЭ essay" structure: formulaic, predictable paragraph patterns
- Immediately recognizable as AI-generated to native readers
- Weaker performance on complex analytical tasks
- Most expensive Russian model: GigaChat Max API ~234₽ per 1000 review tokens vs DeepSeek's ~8.43₽
- Better at instruction-following than naturalness

### DeepSeek V3/R1
- Style: grammatically correct but "dry and forgettable" — lowest personality score
- Requires additional style layer (Claude editing pass) for any public-facing content
- Data privacy concerns for Russian business content (Chinese jurisdiction)
- R1 thinking mode: adds significant latency for simple writing tasks (reasoning overhead)

### Gemini 2.5/3.x
- "Slightly impersonal" Russian — adequate but lacks distinctive voice
- Gmail/Docs integration failures reported in practice
- Code modification tasks produce errors
- Strong on analysis and trend alignment, weak on authentic voice in business writing

---

## Community Consensus

Where clear community consensus exists (2025-2026, Habr + vc.ru + practitioner blogs):

**Consensus 1:** Claude writes the most natural Russian for formal/semi-formal content, requires the least editorial work for voice and style.

**Consensus 2:** ChatGPT is the "safe default" — adequate at everything, excellent at structured content and emotional copy. Most practitioners maintain both Claude and ChatGPT subscriptions.

**Consensus 3:** DeepSeek V3 is the rational economic choice for bulk SEO content in Russian — quality is "good enough" at 85% lower cost than GPT-5.

**Consensus 4:** Russian-native models (YandexGPT, GigaChat) are not competitive for long-form editorial content. Their advantage is frictionless access, legal/regulatory context, and digital-native short-form content.

**Consensus 5:** No model is production-ready without editing. The practitioner consensus is 50-70% time savings on drafting, but editorial work remains necessary.

**Where consensus is absent:**
- Whether Claude or ChatGPT is "better overall" — depends entirely on task type and prompt quality
- Whether GigaChat's benchmark superiority (MERA) translates to practical writing quality (evidence suggests it does not)
- The exact editing time reduction across models (estimates range from "minimal" to "half the original time")

---

## Recommended Workflow for Russian Content Creation

Based on practitioner evidence, the following workflow minimizes editorial time while maximizing quality for business/expert Russian content:

### Stage 1: Research and Structure (DeepSeek V3 or ChatGPT)
Use DeepSeek V3 for factual research, data gathering, structural outline. Cost-effective at $0.28 input/M tokens. If budget is not a constraint, ChatGPT's structure and factual grounding is slightly superior.

### Stage 2: Draft Writing (Claude Sonnet 4.6)
Write the full draft in Claude. Use a detailed system prompt that includes:
- Voice/persona definition (prevents the "educated-neutral" default)
- Specific style constraints (em-dash limit, no hedging phrases, no promotional vocabulary)
- Audience definition
- Explicit instruction to avoid: "следует отметить," "важно понимать," "данный," "комплексный"

Claude Sonnet 4.6 is the cost-practical choice over Opus 4.6 for most content (3x cheaper, quality difference marginal for non-reasoning tasks).

### Stage 3: Style Editing (Claude or Human Editor)
Claude handles its own editing well — instruct it to: remove AI markers, reduce em-dashes to maximum 8 per article, eliminate hedging phrases, add specific details and examples. Human editor reviews for: factual accuracy, brand voice, genuinely colloquial passages.

### Stage 4: Headlines and SEO Elements (YandexGPT or ChatGPT)
YandexGPT 5 Pro excels at generating multiple headline variants with modern Russian web register. Use it for H1 alternatives, social media copy, meta descriptions.

### Stage 5: Trend/Algorithm Check (Gemini or Perplexity)
Optional: use Gemini for Google algorithm alignment check, or Perplexity for real-time SERP verification.

### Cost Estimate Per 3000-word Russian Article (API workflow):
- DeepSeek (research/outline): ~$0.05-0.10
- Claude Sonnet 4.6 (draft + edit): ~$0.30-0.60
- ChatGPT (structural elements): ~$0.10-0.20
- **Total: ~$0.45-0.90 per article**
- vs. Claude Opus 4.6 only: ~$1.50-3.00

---

## Sources Used

### Habr.com
- [Ультимативный гид: Топ-20 нейросетей для текстов 2025](https://habr.com/ru/articles/948672/) — model rankings, perplexity scores, cost comparisons
- [ChatGPT vs Claude: Мой опыт после двух месяцев использования](https://habr.com/ru/articles/915212/) — practitioner two-month comparison, Russian writing specifically
- [Новый ChatGPT-4о vs GigaChat vs YandexGPT vs Человек](https://habr.com/ru/companies/nfckey/articles/817417/) — direct Russian writing test with human baseline
- [LLM модели: зарубежные VS отечественные](https://habr.com/ru/articles/1000058/) — MERA benchmark data, cost comparison table
- [Тестируем YandexGPT-5-Pro](https://habr.com/ru/companies/bothub/articles/893128/) — specific YandexGPT writing quality tests
- [Сравнение нейросетей в генерациях: Claude vs ChatGPT vs Gemini](https://habr.com/ru/companies/bothub/articles/1011410/) — multi-task comparison including Russian creative writing
- [Ваш текст воняет GPT. 12 мест, откуда несёт](https://habr.com/ru/articles/1022906/) — AI detection markers in Russian text (empirical data)
- [Почему Chat GPT говорит по-русски с нейронным акцентом?](https://habr.com/ru/articles/716460/) — tokenizer fragmentation analysis
- [Великое переселение: Почему бизнес переходит с ChatGPT на Claude](https://habr.com/ru/articles/1014936/) — business switching data, prose quality scores
- [Топ нейросетей для SEO-обработки текста](https://habr.com/ru/companies/bothub/articles/1008974/) — SEO-specific Russian content comparison

### vc.ru
- [Claude AI нейросеть в России: преимущества работы с русским языком](https://vc.ru/ai/2839162-claude-ai-neiroset-v-rossii-preimushchestva-rabotyi-s-russkim-yazyikom) — Claude Russian capabilities analysis
- [Нейросеть для автоматизации контента 2026: ChatGPT, Claude или DeepSeek](https://mayai.ru/nejroset-dlya-avtomatizaczii-kontenta-2026-chatgpt-claude-ili-deepseek/) — content automation comparison
- [Я подписалась на GPT, Claude и Gemini одновременно](https://vc.ru/ai/2941891-sravnenie-chatgpt-claude-i-gemini) — one-month practical comparison

### Specialized blogs
- [Claude на русском: качество, нюансы и стиль (WebGPT)](https://gptweb.ru/blog/reviews/claude-in-russian-quality-nuances-style) — detailed Claude Russian strengths/weaknesses
- [Claude vs ChatGPT for Russian in 2026 (Rephrase)](https://rephrase-it.com/blog/claude-vs-chatgpt-for-russian-in-2026) — task-by-task comparison, English gravity well analysis
- [GigaChat или YandexGPT: какую российскую нейросеть выбрать](https://jaycopilot.com/blog/bitva-gigantov-yandexgpt-ili-gigachat) — Russian-native model comparison
- [Technologika: Тестируем LLM для русского языка](https://www.technologika.ru/blog/testing-llm-with-russian-language) — structured 8-task Russian language evaluation
- [ChatGPT vs Claude vs Gemini: какая нейросеть лучше для SEO ИИ копирайтинга](https://www.sostav.ru/blogs/288326/83041) — SEO copywriting specific comparison
- [Эксперимент с нейросетями: SEO-задачи (Илья Карбышев)](https://ilya-karbyshev.ru/eksperiment-s-ii-kak-ya-reshal-seo-zadachi-s-pomoshhju-nejronok-i-kakoj-rezultat-poluchil/) — practical SEO experiment with failure mode documentation

### Pricing sources
- [LLM API Pricing 2026 (BenchLM)](https://benchlm.ai/llm-pricing) — current API pricing for cost calculations

---

## Confidence Assessment

**High confidence findings** (multiple independent sources, consistent): items 1, 3, 4, 5, 6, 8, 10, 13, 14

**Medium-high confidence** (2-3 sources, generally consistent): items 2, 7, 9, 12

**Medium confidence** (1-2 sources, some contradictions): item 11 (Gemini)

**Low confidence / insufficient data:** Qwen for Russian, Mistral for Russian, local Russian fine-tuned models (insufficient practitioner evidence found)

---

*Stream E research completed 2026-06-01. Total sources consulted: 25+. Coverage: Habr, vc.ru, practitioner blogs, technical analyses. Notable gap: no Reddit r/LocalLLaMA data found (searches returned no relevant Russian-focused threads). Telegram channel data unavailable (not indexed).*

---

## SUPPLEMENTARY FINDINGS (Scout E — Second Pass, 2026-06-01)

Additional research via live WebSearch confirmed and extended the above findings with new data points.

---

### S1. MERA Benchmark — конкретные цифры рейтинга (верифицировано)

**Confidence: HIGH** (официальный источник mera.a-ai.ru)

Актуальный рейтинг MERA (Multimodal Evaluation for Russian-language Architectures, AI Alliance):
- GPT-5.2: 0,707 — 5-е место
- GigaChat 3 Ultra Preview: 0,683 — 6-е место
- DeepSeek-V3-0324: 0,674 — 9-е место

В июне 2025 запущен MERA Industrial (бизнес-задачи), в июле 2025 — MERA Code (программирование на русском).

**Практическое значение:** MERA — наиболее достоверный публичный бенчмарк для русского языка. GigaChat 3 Ultra Preview реально конкурентоспособен с GPT-5.2. Однако, как подтверждает Finding 12 выше, высокий MERA-балл не гарантирует качество написания живых текстов.

**Источник:** [mera.a-ai.ru](https://mera.a-ai.ru/ru/text)

---

### S2. Российская Arena для русского языка — двойная структура

**Confidence: HIGH**

Существует две отдельных платформы для ELO-оценки LLM на русском:

1. **llmarena.ru** — краудсорсинговая платформа с анонимными сравнениями, ELO по Bradley-Terry. Специализируется на русском. Есть Arena Hard Benchmark (500 промптов).
2. **Vikhrmodels/arenahardlb (HuggingFace)** — RuArenaGeneral, основан на Arena Hard Auto. Единственный полностью открытый современный бенчмарк на русском. GitHub: VikhrModels/ru_llm_arena. Поддерживает OpenAI-compatible API.

**Глобальный lmarena.ai:** нет отдельной Russian-категории. Доля русских промптов выросла с 1% (апр 2023) до 15,7% (дек 2024). Ни одна российская модель не попала в топ-100 lmarena.

**Практическое значение:** Для актуальных рейтингов качества на русском — использовать llmarena.ru и Vikhrmodels leaderboard, не глобальный lmarena.

**Источник:** [llmarena.ru](https://llmarena.ru/), [huggingface Vikhrmodels](https://huggingface.co/spaces/Vikhrmodels/arenahardlb), [github VikhrModels/ru_llm_arena](https://github.com/VikhrModels/ru_llm_arena)

---

### S3. Тест 34 AI-моделей на задачах менеджера — количественный разрыв

**Confidence: HIGH** (Habr, январь 2026)

В тесте 34 AI-моделей на задачах менеджера (планирование встреч, написание писем, анализ отчётов):
- Топ-3 международных модели: средний балл **4,78 / 5**
- Топ-2 российских модели: средний балл **4,36 / 5**
- Разрыв: **0,42 балла** = разница «отлично» vs «хорошо»

Вывод авторов: «Приемлемо для рутины, заметно при сложной аналитике или стратегических решениях». Grok (xAI) ошибочно фигурировал в первой версии как доступный в РФ — API заблокирован.

**Практическое значение:** Для операционных задач (переписка, короткие тексты) — российских моделей достаточно и доступны без VPN. Для сложного контента — нужен Claude/ChatGPT.

**Источник:** [habr.com 34 AI модели](https://habr.com/ru/articles/1010568/)

---

### S4. Тест 18 моделей для production-контента на русском — Qwen как победитель по цена/качество

**Confidence: HIGH** (Habr, 2026)

Тест 18 LLM для генерации образовательного контента на русском языке. Методология: реальные затраты ~$92 на итерации, финальный тест — $3. Оценка через LLM-судью.

Победитель по цена/качество: **Qwen3-235B** — на 9% ниже лидеров по качеству, но в **130 раз дешевле** ($0,0008/вызов). Ключевой инсайт статьи: «публичных бенчмарков для задачи "кто лучше пишет статью по B2B-продажам на русском" не существует».

**Практическое значение:** Методологию воспроизводимо применить к любому типу контента: взять 5 реальных тем → несколько моделей → оценить LLM-судьёй. Это единственный способ подобрать модель под конкретный тип контента, а не полагаться на общие рейтинги.

**Источник:** [habr.com 18 моделей production](https://habr.com/ru/articles/1021388/)

---

### S5. YandexGPT 5 Pro — количественные данные по бенчмаркам

**Confidence: HIGH** (Habr, BotHub)

Конкретные цифры YandexGPT-5-Pro:
- MMLU: 83%
- MMLU PRO: 68%
- DROP RU: 63% (лучше Qwen на 2%, хуже ChatGPT на 5%)
- IFEval RU: 77%
- Классификация информации (русский): **70% vs 51% у GPT-4o** — YandexGPT лидирует
- Извлечение данных: **71% vs 48% у GPT-4o**
- Переформулирование: 58% vs 51% у GPT-4o

Слабые стороны: нет мультимодальности, слабее в программировании и математике.

**Практическое значение:** YandexGPT — лучший выбор для задач **классификации и структурирования русскоязычных текстов**. Для написания нативного контента — конкурентоспособен, но «до лидеров рынка не дотягивается».

**Источник:** [habr.com YandexGPT-5-Pro](https://habr.com/ru/companies/bothub/articles/893128/)

---

### S6. GigaChat — снижение цен втрое и практические ограничения

**Confidence: HIGH** (официальные источники)

С 1 февраля 2026: Сбер снизил GigaChat API в 3 раза. Доступны GigaChat-2, GigaChat-2-Pro, GigaChat-2-Max. Модели первого поколения перенаправляются на второе. Работает без VPN, оплата по счёту для юрлиц.

GigaChat 3 (702B параметров, MoE архитектура, 36B активных): MIT-лицензия, открытые веса. 86,59% на HumanEval+.

Пользовательские тесты — слабые стороны: написание кода («функции просто не работали»), творческие тексты («значительно слабее Алисы»).

**Практическое значение:** GigaChat незаменим для российских нормативных документов, тендерной документации, юридических текстов. Для SEO-контента и маркетинговых статей — не первый выбор.

**Источник:** [developers.sber.ru тарифы](https://developers.sber.ru/docs/ru/gigachat/api/tariffs), [habr.com GigaChat снижение цен](https://habr.com/ru/companies/sberbank/news/991878/), [habr.com GigaChat и Alice AI](https://habr.com/ru/companies/bothub/articles/972292/)

---

### S7. Open-source модели сравнялись с проприетарными (ноябрь 2025)

**Confidence: MEDIUM-HIGH**

Habr-анализ: «ноябрь 2025 — месяц, когда open-source официально догнал проприетарные». Kimi-K2 (Moonshot AI) обошёл GPT-4o на 30+ п.п. на SWE-bench, 84,5% на GPQA Diamond (уровень Claude 3.5 Sonnet).

Для русских задач: Qwen3-235B и потенциально Kimi-K2 — конкурентоспособные альтернативы облаку. Для локального деплоя с конфиденциальными данными: Qwen3-235B или Vikhr.

**Практическое значение:** В 2026 году нет смысла жертвовать качеством ради локального деплоя при правильном выборе open-source модели.

**Источник:** [habr.com 18 LLM конец монополии](https://habr.com/ru/articles/971864/)

---

### S8. Vikhr и Saiga — open-source для русского, достигли уровня облачных российских моделей

**Confidence: MEDIUM**

Vikhr и Saiga (файн-тюнинги на Mistral/LLaMA) достигают качества GigaChat и YandexGPT на простых задачах. На специфических задачах Vikhr выигрывает у Saiga на 1–2%. Saiga обновляется быстрее с новыми базовыми моделями, Vikhr лучше для conversational Russian.

**Актуальность:** Оба семейства актуальны для локального деплоя без облака и без утечки данных. Единственный вменяемый open-source вариант на русском с приемлемым качеством.

**Источник:** [habr.com Vikhr](https://habr.com/ru/articles/787894/), [arxiv.org Vikhr v6](https://arxiv.org/html/2405.13929v6), [agmind.dev Saiga vs Vikhr](https://prem.agmind.dev/blog/fine-tune-llm-pod-russkij-saiga-vikhr/)

---

### Дополнительная матрица решений (русскоязычный контекст)

| Задача | Первый выбор | Второй выбор | Примечание |
|--------|-------------|-------------|-----------|
| SEO Title/Description для Яндекса | YandexGPT 5 | ChatGPT | YandexGPT лучше понимает паттерны Яндекса |
| Массовый SEO-контент (100+ статей) | Qwen3-235B | DeepSeek V3 | 130x дешевле при 91% качества |
| Работа с нормативными документами РФ | GigaChat 2 Max | YandexGPT 5 | Обучен на российской правовой базе |
| Классификация/извлечение из текстов | YandexGPT 5 | GigaChat | YandexGPT: 70% vs 51% GPT-4o |
| Деловые письма и коммерческие предложения | Claude Sonnet 4.6 | YandexGPT 5 | Claude точнее следует стилевым инструкциям |
| Конфиденциальные корпоративные данные | GigaChat (on-premise) | Vikhr (локально) | Российская юрисдикция или локальный деплой |

*Эта матрица дополняет, не заменяет основную таблицу выше.*

---

*Supplementary findings added 2026-06-01 via live WebSearch. Additional sources: mera.a-ai.ru, llmarena.ru, developers.sber.ru, habr.com (5 новых статей), vc.ru (3 новые статьи). Всего источников в файле: 35+.*
