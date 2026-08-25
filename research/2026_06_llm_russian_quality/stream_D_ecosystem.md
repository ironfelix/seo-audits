# Stream D: Russian LLM Ecosystem — Systems Analysis
**Research date:** 2026-06-01
**Framework:** CREAM with systems-thinking lens
**Researcher:** SCOUT D (holist / systems)

---

## Key Findings (15 items, confidence rated)

1. **The tokenization penalty is structural, not incidental.** Russian Cyrillic in cl100k_base (GPT-4 tokenizer) costs approximately 2x more tokens per character than English. GPT-4o's o200k_base tokenizer (200k vocabulary vs 100k) partially addresses this, but the fundamental asymmetry remains. This is not merely a cost issue — it is an inference-time disadvantage: a 4096-token context in Russian carries less information than the same context in English. **Confidence: HIGH (multiple independent sources confirm ~2x ratio for Cyrillic).**

2. **YandexGPT 5 was trained on 15 trillion tokens, primarily Russian and English, with a proprietary corpus drawn from Yandex's search index.** The Powerup phase used 320B tokens of high-quality data. This is the single largest known Russian-language pretraining dataset available to any organization outside OpenAI/Anthropic. **Confidence: HIGH (Yandex public disclosures, Hugging Face model card).**

3. **GigaChat's new MoE architecture (June 2025) represents the first publicly documented MoE model natively designed for Russian.** 20B total parameters, 3.3B active per pass, trained on ~10 trillion tokens (63.76% English, 26.49% Russian). The training corpus is notably English-dominated — Russian is a quarter, not a majority. **Confidence: HIGH (ACL 2025 paper arXiv:2506.09440).**

4. **Multilingual models make semantic decisions in English-centric representation space, independent of input/output language.** Research on Llama-3.1-70B, Gemma-2-27b, Mixtral-8x22B confirms this. Russian was not directly tested in the cited study, but the pattern is structurally predicted to apply equally. This "thinks in English, translates to Russian" effect is the deepest systemic weakness of globally trained models on Russian output. **Confidence: MEDIUM-HIGH (arXiv:2502.15603, Russian not directly tested).**

5. **Vikhr's tokenizer adaptation is a proven mechanism.** By rebuilding the vocabulary to 40k tokens optimized for Russian (SentencePiece), Vikhr reduces token count for a typical Russian phrase from 13 to 7 — a 46% reduction. This directly improves context utilization and inference speed without changing model size. The technique is replicable and has been applied to Mistral and YandexGPT 5 Lite bases. **Confidence: HIGH (Vikhr arXiv:2405.13929, reproducible benchmark data).**

6. **Saiga (IlyaGusev) remains the community reference for Russian open-source alignment, but relies on LoRA without full pretraining.** The approach produces good instruction-following in Russian but does not address the tokenizer inefficiency problem. Saiga-Llama3-8b achieved competitive MERA scores largely due to Llama-3's strong base multilingual capabilities rather than the Russian adaptation itself. **Confidence: HIGH (Habr testing, benchmark data).**

7. **YandexGPT holds a structural advantage through proprietary data: the full Yandex Search index (~100TB, filtered to ~1TB), comprising Russian web, news, and domain content unavailable to external researchers.** GigaChat has equivalent access to Sber ecosystem data (banking, legal, customer service). These moats are not replicable by open-source practitioners. **Confidence: HIGH (Yandex/Sber public statements, YaLM-100B GitHub).**

8. **On the MERA benchmark (21 tasks, Russian LLM evaluation), GigaChat 2 MAX scores 0.67, with +7% to +33% advantage over international models on USE (unified state exam) reasoning tasks.** However, on coreference resolution (RWSD), GigaChat trails frontier models by 7–18%. This reveals a domain-specific pattern: Russian-trained models outperform on culturally grounded tasks, underperform on structural linguistic tasks requiring world-knowledge generalization. **Confidence: HIGH (ACL 2025 GigaChat Family paper).**

9. **The "model collapse" feedback loop is already forming in the Russian internet.** Russian networks (documented "Pravda" disinformation operation) deliberately flood web crawlers with AI-generated Russian content, compounding the natural problem of AI content proliferating on Runet. Future training runs scraping Common Crawl will encounter increasingly synthetic Russian text. This degrades quality specifically in the long tail of Russian language use — regional dialects, specialized professional discourse, authentic cultural references. **Confidence: MEDIUM-HIGH (Nature 2024 model collapse research + multiple reports on Pravda network).**

10. **Qwen3 (Alibaba) is emerging as a competitive multilingual base for Russian without Russia-specific training.** Qwen3-235B-A22B supports 100+ languages and is rated among the top open-source models for Russian in 2026 practitioner assessments. This represents a systemic challenge: a Chinese lab may be providing better Russian-language OSS infrastructure than Russian labs, through sheer scale. **Confidence: MEDIUM (practitioner assessments, limited formal benchmarks).**

11. **The open-source Russian ecosystem has a dependency chain problem.** Vikhr adapts Mistral. Saiga adapts LLaMA. Both depend on continued compute and research investment from Western organizations. If Mistral or Meta changes licensing (as Meta did in 2024 with LLaMA 3 commercial restrictions), the entire Russian OSS stack is affected. YandexGPT 5 Lite's open release partially mitigates this by providing a native Russian base for the community. **Confidence: HIGH (observed ecosystem structure, YandexGPT 5 Lite HuggingFace release).**

12. **Global models' Russian quality gap is narrowing fast but is qualitative, not quantitative.** GPT-4o and Claude 3.7 Sonnet approach YandexGPT on grammatical correctness benchmarks. The remaining gap is in cultural-pragmatic competence: idiomatic expressions, Russian business communication conventions, regulatory context (GOST, Russian civil code), and contemporary slang. These are impossible to learn from translated English content. **Confidence: MEDIUM-HIGH (comparative user studies, MERA results patterns).**

13. **Russian is the 4th largest language on the global internet by content volume (approximately 6% of Common Crawl), but receives proportionally less representation in frontier model training compared to its internet footprint.** English at ~45–55% dominates by orders of magnitude. The result: for every unit of Russian reasoning capability in a multilingual model, there was approximately 7–9x less training signal. **Confidence: MEDIUM (Common Crawl distribution estimates are approximate).**

14. **Learned Embedding Propagation (LEP, arXiv:2412.21140, December 2024) represents a new technique for Russian adaptation that bypasses full continued pretraining.** By propagating new vocabulary embeddings into existing instruct-tuned models, it allows Russian vocabulary extension without the instruction-tuning step. This reduces adaptation cost by an estimated 60–80% while achieving competitive performance with traditional continued-pretraining approaches on LLaMA-3-8B and Mistral-7B. **Confidence: MEDIUM (single paper, not yet widely replicated).**

15. **LLM Arena (llmarena.ru), Russia's crowdsourced ELO-based evaluation platform, provides a demand-side view of Russian quality that formal benchmarks miss.** Users vote on blind comparisons of real-world tasks in Russian, making it structurally resistant to benchmark gaming. The platform became significant in 2024–2025 specifically because MERA and other academic benchmarks poorly capture practical Russian-language use. This gap between benchmark performance and user preference is itself a systemic signal — formal evaluation infrastructure for Russian lags behind model development. **Confidence: HIGH (platform design and purpose are well-documented).**

---

## Model Comparison Table

| Model | Developer | Architecture | Russian Training Data | Known Russian Strengths | Known Russian Weaknesses | MERA Score |
|---|---|---|---|---|---|---|
| YandexGPT 5.1 Pro | Yandex | Transformer (LLaMA-like), proprietary | 15T tokens (Yandex search index, ~49% Russian in base), Phase 2: 320B HQ | Idiomatic Russian, business docs, regulatory context, cultural references | Limited context (128K vs 1M Claude), less powerful on global reasoning | Outperforms GPT-4.1 in 56% cases (Yandex claim) |
| YandexGPT 5 Lite | Yandex | 8B LLaMA-like, open-source | Same base, bilingual Russian/English | Open base for community fine-tuning, 32K context | Smaller model, limited capabilities vs Pro | Not published |
| GigaChat 2 MAX | SberDevices | Dense transformer, proprietary | ~10T tokens: 63.76% English, 26.49% Russian, custom Cyrillic tokenizer | Legal/banking domain, follows complex Russian instructions, USE reasoning | Coreference resolution (RWSD) -7% to -18% vs frontier | 0.670 |
| GigaChat 2 PRO | SberDevices | Dense transformer, proprietary | Same | Business writing, structured data extraction | — | 0.649 |
| GigaChat-A3B | SberDevices | MoE 20B total / 3.3B active, open | Same, MoE architecture | 2x training speed, 40% less inference latency | Smaller effective size | 0.512 |
| Vikhr-Mistral-7B | Vikhrmodels | Adapted Mistral 7B, full weight tuning | 11B Russian tokens (Wikipedia 4B, science 2.5B, news 1B, Habr 1B), vocab adaptation | Tokenizer efficiency (13 → 7 tokens/phrase), open-source SOTA at launch | 7B scale limits complex reasoning | MERA 0.485, Ru-MMLU 0.80 |
| Vikhr-Nemo-12B | Vikhrmodels | Adapted Mistral Nemo | Expanded corpus vs 7B | Better RAG performance | — | Higher than 7B variant |
| QVikhr-3-4B | Vikhrmodels | Adapted Qwen3-4B | Qwen base + Russian tuning | +20.7% on Russian benchmarks vs base Qwen3-4B | Small model | Not published |
| Saiga-Mistral-7B | IlyaGusev | Mistral + LoRA adapter | LoRA on Russian instruction pairs (ru_turbo_saiga, ru_sharegpt) | Accessible, good instruction-following in Russian | No tokenizer adaptation, full pretraining skipped | Competitive with open-source peers |
| Saiga-Llama3-8B | IlyaGusev | LLaMA-3-8B + SFT + SimPO | ru_turbo_saiga + oasst1_ru + ru_sharegpt | Strong base from LLaMA-3, competitive MERA | Dependent on Meta base model licensing | 2nd place open-source in tested period |
| ruGPT-3.5-13B | SberAI / ai-forever | GPT-3 style decoder | Russian web + domain data | Foundation for GigaChat training | Outdated architecture, superseded | — |
| FRED-T5 | SberAI / RussianNLP | T5 encoder-decoder | Russian summarization corpus | Russian summarization tasks | Not a generative chat model | — |
| GPT-4o | OpenAI | Dense transformer, proprietary | ~13T tokens, English-dominant, improved o200k_base tokenizer | Strong global reasoning, improved non-Latin tokenizer vs GPT-4 | "Thinks in English," cultural-pragmatic gap in Russian | Near parity with Russian models on MERA structural tasks |
| Claude 3.7/4.5 Sonnet | Anthropic | Transformer, proprietary | Unknown composition, English-heavy | Strong structured writing, follows complex instructions | Weakest Russian cultural-pragmatic competence among frontier models | Not published for Russian |
| Qwen3-235B-A22B | Alibaba | MoE, open-source | 36T tokens, 100+ languages | Consistently rated top open-source for Russian 2026, strong multilingual | No Russian-specific cultural specialization | Practitioner-rated top open-source |
| Qwen3-14B | Alibaba | Dense, open-source | Same corpus | Cost-efficient Russian performance | — | Practitioner-rated |

---

## Systemic Factors Determining Russian Quality

### Factor 1: Tokenizer Design — The Infrastructure of Representation

The tokenizer is the deepest architectural determinant of Russian quality, yet it is the least discussed in product comparisons. A model's tokenizer determines:

- **Context efficiency:** How many Russian words fit in a 4096-token window. With cl100k_base (GPT-4), a Russian paragraph may consume 2x the tokens of the equivalent English paragraph. This means a Russian speaker using GPT-4 was effectively operating with half the effective context.
- **Semantic granularity:** Poor tokenization fragments Russian morphology. Russian is a highly inflected language — the same root takes dozens of endings. If the tokenizer doesn't encode common suffixes efficiently, the model must learn morphological patterns through statistical inference from poor representations rather than through native tokens.
- **Training signal density:** During pretraining, a poorly tokenized Russian corpus produces fewer gradient updates per byte of Russian content than an equivalent English corpus. The model is literally learning less from the same amount of Russian text.

Vikhr's empirical demonstration — reducing a 13-token sequence to 7 tokens through vocabulary adaptation — translates directly to inference quality, not just cost. It is a 46% improvement in information density per context window for Russian.

GigaChat and YandexGPT both built custom tokenizers from scratch, optimized for Cyrillic. This is the single most important architectural decision a Russian LLM developer can make. Models that skip this step (Saiga's LoRA approach) carry the tokenizer penalty permanently.

### Factor 2: Proprietary Data Moats — Non-Replicable Training Signals

The two leading Russian models have access to data that no open-source practitioner can replicate:

- **Yandex:** The full search index of the Russian web, representing years of crawled, deduplicated, and quality-filtered Russian text. The heuristic filtering pipeline (LSH deduplication, length filtration, entropy filtration, domain filtration) applied to ~100TB of raw data to produce ~1TB of high-quality Russian content represents years of engineering investment.
- **Sber:** The GigaChat training corpus included web data from Common Crawl 2017–2023, but also access to Sber's internal ecosystem: banking documentation, customer service transcripts, legal templates, and regulatory filings — specialized Russian text that does not appear on the public internet.

These data moats create a structural two-tier market: proprietary Russian models with domain-specific corpora, and open-source models scraping public Common Crawl derivatives.

### Factor 3: The English-Centric Reasoning Problem — A Systemic Cognitive Architecture Issue

Research demonstrates that LLMs trained primarily on English develop English-centric internal representations. When processing Russian input, these models:

1. Map Russian tokens to semantic concepts via English-proximate representations
2. Perform reasoning in English conceptual space
3. Generate Russian output by translating back through the same representation

This is not a stylistic preference — it is an architectural consequence of gradient descent on English-dominated data. The evidence comes from logit lens analysis (English concepts appear in intermediate layers before target-language tokens) and steering vector experiments (English steering vectors are more effective than native-language vectors even for non-English outputs).

For Russian specifically, this manifests as:
- Calques from English idioms in Russian text ("принять вызов" for "accept the challenge" instead of native equivalents)
- Logic structures that follow English argument patterns (SVO, linear exposition) rather than Russian rhetorical conventions (topic-comment, digressive elaboration)
- Missing pragmatic markers: Russian uses a different set of discourse-structuring particles and hedges than English

Models trained with Russian as a primary language (YandexGPT, early GigaChat) avoid this problem by learning Russian as a first-class representation rather than a translation target.

### Factor 4: Scale Asymmetry — Russian Cannot Compete With English on Tokens

English internet content is 7–10x larger than Russian by token count. The training data composition reflects this:
- GigaChat's corpus: 63.76% English, 26.49% Russian
- GPT-3's training: Russian estimated at 1.5–3% of the original WebText corpus
- YandexGPT: The only organization where Russian is genuinely dominant in training

Scale matters because LLMs learn language patterns statistically. A model trained on 1 trillion Russian tokens learns better Russian than one trained on 100 billion Russian tokens, even if total training volume is equal. Russian-specialist organizations (Yandex, Sber) can allocate their full compute budget to Russian optimization. OpenAI and Anthropic cannot — their business model requires maximizing English performance first.

### Factor 5: Cultural-Pragmatic Knowledge — The Unverifiable Gap

Formal benchmarks measure structural Russian (grammar, morphology, factual recall). They do not measure:
- Russian business communication conventions (circular argumentation, status-inflected communication styles)
- Contemporary Russian slang evolution (rapidly changing, not in Wikipedia)
- Soviet and post-Soviet cultural reference density
- Russian-specific regulatory knowledge (ГОСТы, КоАП, 44-ФЗ)

This is where the gap between Russian-trained models and global models is largest, and where it is least measurable. Users in professional contexts consistently rate Russian-specialized models higher on practical tasks even when benchmarks show near-parity — this is the mechanism.

---

## Training Data Quality Issues

### Issue 1: Common Crawl Russian Quality

Common Crawl's Russian subset is large (Russian is 4th globally by web content volume) but quality-stratified:
- **High quality:** RuNet news sites, Wikipedia, academic publications (Cyberleninka), professional forums (Habr, professional communities)
- **Medium quality:** Social networks, commentary sections, e-commerce product descriptions
- **Low quality:** SEO-optimized content, clickbait farms, low-content aggregators, spam

The distribution is heavily skewed toward low-quality content. Without aggressive filtering, a model trained on raw Russian Common Crawl will learn the statistical patterns of Russian SEO spam, not literary or professional Russian.

### Issue 2: Domain Coverage Gaps

Certain high-value Russian domains are underrepresented even in large corpora:
- **Oral Russian:** Speech-to-text-converted phone conversations, podcasts, interviews — the register where Russian slang, regional variation, and pragmatic markers are densest
- **Professional domain text:** Legal filings, medical records, engineering standards — often not publicly accessible
- **Post-2022 content:** The Russian internet has been increasingly isolated from Western infrastructure since 2022; crawling coverage may have degraded

### Issue 3: Synthetic Content Contamination

The "Pravda" disinformation network (documented by multiple researchers in 2024–2025) has systematically seeded Russian-language content across thousands of websites designed to appear authentic to web crawlers. These sites publish AI-generated propaganda text in Russian, which is then harvested by web scrapers for training data.

This creates a dual contamination problem:
1. **Factual contamination:** False historical and political claims embedded in training data
2. **Stylistic contamination:** AI-generated Russian text patterns (formulaic, repetitive, poor idiomatic range) become over-represented in training corpora

Future models trained on 2024–2025 web crawls will have learned from a partially corrupted Russian internet. Models trained before 2022–2023 may ironically have encountered higher-quality authentic Russian text.

### Issue 4: Annotation and Instruction-Tuning Data Scarcity

High-quality Russian instruction-tuning data (human-authored question-answer pairs, preference data for RLHF) is 10–20x scarcer than English equivalents. This creates an alignment bottleneck: a model can have excellent Russian pretraining but weak Russian alignment, producing grammatically correct but contextually inappropriate responses. Sber and Yandex have invested heavily in Russian RLHF (Yandex employed 300+ AI trainers for alignment), but this investment is unavailable to the open-source community.

---

## Second-Order Effects and Feedback Loops

### Loop 1: AI-Generated Russian Degrades Future Training Data

The most dangerous long-term feedback loop:
1. Russian LLMs generate large volumes of AI-text for websites, articles, SEO content
2. This AI-generated Russian floods Common Crawl snapshots
3. Next-generation models training on those snapshots learn from AI-generated Russian
4. The result: "model collapse" — progressive loss of linguistic diversity, long-tail language patterns, and authentic cultural references

This loop is accelerating. Russian businesses adopted AI content generation faster in 2023–2025 than Western equivalents, partly due to lower cost sensitivity to AI writing quality. The Russian internet is becoming AI-saturated. Research published in Nature (2024, Shumailov et al.) confirms that recursive training on model outputs causes irreversible distribution collapse — tails of authentic linguistic variety disappear.

Human-generated text from pre-2022 Russian internet may become a valued, scarce resource for training future models.

### Loop 2: Market Isolation Amplifies Data Advantage

Geopolitical isolation of the Russian internet (2022+) creates a feedback loop:
- Western models face increasing difficulty accessing Russian web data (technical and legal barriers)
- Russian-produced models retain access to RuNet, widening their data advantage over time
- Russian users' inability to access frontier Western models (API restrictions, payment barriers) increases demand for domestic alternatives
- Increased domestic usage generates more Russian-language interaction data (feedback and preference data) for Yandex/Sber
- This preference data further improves Russian alignment

Isolation is paradoxically strengthening Russian-specialist models relative to global ones in their home market.

### Loop 3: Open-Source Dependency and Infrastructure Risk

The Russian open-source ecosystem depends on:
- Mistral (French) → Vikhr base
- Meta (American) → Saiga base
- Qwen (Chinese) → QVikhr base

If Meta restricts LLaMA licensing further, or if Mistral pivots strategy, the entire open-source Russian LLM community must adapt. YandexGPT 5 Lite's open release (2025) is a partial hedge against this risk — providing a native Russian base model that the community can build on without foreign dependency. This is a strategically important step, even if YandexGPT 5 Lite underperforms frontier models.

### Loop 4: Benchmark Overfitting Degrades Russian Evaluation

MERA (21-task benchmark, 2024) has become the standard Russian LLM evaluation. As models are increasingly optimized against MERA, the benchmark's signal quality degrades. Russian LLM Arena (llmarena.ru, ELO-based crowdsourced evaluation) was created specifically because MERA fails to capture practical Russian-language utility. But LLM Arena has its own feedback loop: as model developers discover which task categories generate favorable Arena ratings, they fine-tune specifically for those distributions.

There is currently no benchmark-resistant evaluation infrastructure for Russian that has scale. This means Russian LLM quality is harder to assess objectively than English LLM quality — the measurement problem compounds the training problem.

### Loop 5: Cost Penalty Reduces Russian User Base for Premium Models

Russian Cyrillic requires ~2x tokens per character vs English in standard tokenizers. At identical API pricing, Russian users pay approximately 2x more per word than English users. This creates a cost pressure that:
- Pushes Russian users toward models with Russian-optimized tokenizers (YandexGPT, GigaChat), even if those models have lower ceiling quality
- Reduces the volume of Russian interactions with frontier global models (GPT-4o, Claude)
- Which reduces the amount of Russian preference feedback available to OpenAI/Anthropic
- Which perpetuates their relative weakness on Russian cultural-pragmatic tasks

This is a self-reinforcing market segmentation: cost disadvantage pushes Russian users to local models, which reduces data feedback to global models, which maintains local models' relative advantage on Russian tasks.

---

## CREAM Analysis Summary

### Claims
Russian-specialist model developers (Yandex, Sber) claim their models outperform global models on Russian-language tasks. These claims are partially supported by benchmarks (MERA) and practitioner assessments but are framed in ways that minimize the global models' progress. The claims are most defensible for domain-specific Russian tasks (legal, regulatory) and least defensible for global reasoning tasks conducted in Russian.

### Results
- MERA 2024–2025: GigaChat 2 MAX 0.67, competitive with frontier models on Russian tasks; +7–33% on USE reasoning
- Vikhr MERA 0.485, Ru-MMLU 0.80 — open-source best at time of publication
- YandexGPT 5.1 Pro claims to outperform GPT-4.1 in 56% of comparative evaluations (Yandex-run, not independently verified)
- Practical user tests: YandexGPT and GigaChat lead for Russian business text; Saiga-Mistral leads for local/private deployment
- LLM Arena (crowdsourced): Most recent data suggests frontier global models are competitive with Russian specialists on general tasks; Russian specialists lead on culturally-grounded tasks

### Evidence
- Training data composition: GigaChat 10T tokens (64% English, 26% Russian); YandexGPT 5 15T tokens (Russian + English, search index); Vikhr 11B Russian tokens
- Tokenizer improvement: Vikhr reduces Russian token count by 46% via vocabulary adaptation
- English-centric reasoning: confirmed in LLaMA, Gemma, Mixtral (Russian not directly tested but structurally predicted)
- Model collapse: Nature 2024 confirms recursive AI data training causes collapse; Pravda network documented contaminating Russian training data
- Data moats: Yandex search index, Sber internal data — not publicly replicable

### Alternatives
- **Full pretraining on Russian** (GigaChat, YandexGPT): maximum Russian quality, maximum cost
- **Continued pretraining on Russian base** (Vikhr): good balance, open-source
- **LoRA instruction tuning only** (Saiga): lowest cost, carries tokenizer penalty
- **Learned Embedding Propagation** (LEP, 2024): fast adaptation without full finetuning, competitive results
- **Rely on multilingual general models** (Qwen3, LLaMA-3): increasingly viable as global models improve, no Russian cultural-pragmatic specialization

### Mechanisms
See "Systemic Factors" section above. The five mechanisms in order of impact:
1. Tokenizer design (structural, irreversible in deployed models)
2. Proprietary data moats (Yandex search index, Sber ecosystem)
3. English-centric reasoning architecture (affects all globally-trained models)
4. Scale asymmetry (Russian gets 5–10x less training signal per parameter than English)
5. Cultural-pragmatic gap (unmeasurable by benchmarks, felt in real use)

---

## Sources Used

- [GigaChat Family: Efficient Russian Language Modeling Through Mixture of Experts Architecture (arXiv:2506.09440, ACL 2025)](https://arxiv.org/html/2506.09440v1)
- [Vikhr: The Family of Open-Source Instruction-Tuned Large Language Models for Russian (arXiv:2405.13929)](https://arxiv.org/html/2405.13929v1)
- [Do Multilingual LLMs Think In English? (arXiv:2502.15603)](https://arxiv.org/html/2502.15603v1)
- [Facilitating Large Language Model Russian Adaptation with Learned Embedding Propagation (arXiv:2412.21140)](https://arxiv.org/abs/2412.21140)
- [MERA: A Comprehensive LLM Evaluation in Russian (arXiv:2401.04531)](https://arxiv.org/abs/2401.04531)
- [AI Models Collapse When Trained on Recursively Generated Data (Nature, 2024)](https://www.nature.com/articles/s41586-024-07566-y)
- [YandexGPT 5 Lite model card, Hugging Face](https://huggingface.co/yandex/YandexGPT-5-Lite-8B-pretrain)
- [YandexGPT: A Russian Developer's Perspective on the LLM Landscape (Geminy.ai, 2025)](https://geminy.ai/2025/02/24/yandexgpt-a-russian-developers-perspective-on-the-llm-landscape/)
- [Yandex B2B Tech: YandexGPT 5.1 Pro (TAdviser)](https://tadviser.com/index.php/Product:YandexGPT)
- [Impact of Tokenization on LLaMa Russian Adaptation (arXiv:2312.02598)](https://arxiv.org/html/2312.02598v1)
- [GPT-4's Hidden Cost: Is Your Language Pricing You Out of AI Innovation?](https://tomaszurbanski.substack.com/p/the-hidden-price-tag-on-gpt-4-for)
- [GigaChat 2.0 in API (Habr, SberDevices)](https://habr.com/ru/companies/sberdevices/articles/890552/)
- [Testing LLMs for Russian Language (Habr)](https://habr.com/ru/articles/856436/)
- [LLM Arena: Crowdsourced Russian LLM Evaluation](https://llmarena.ru/)
- [Russian Propaganda Network Poisoning AI Training Data (Bulletin of Atomic Scientists, 2025)](https://thebulletin.org/2025/03/russian-networks-flood-the-internet-with-propaganda-aiming-to-corrupt-ai-chatbots/)
- [Vikhr: Digest of models based on YandexGPT 5 Lite (Hugging Face Blog)](https://huggingface.co/blog/WaveCut/yandexgpt5-models-family-digest)
- [GigaChat vs ChatGPT: сравнение на русском (Zerocoder)](https://ya.zerocoder.ru/tgp-gigachat-vs-chatgpt-chi-otvety-tochnee-i-kreativnee-na-russkom-yazyke/)
- [Best Open Source LLM for Russian in 2026 (SiliconFlow)](https://www.siliconflow.com/articles/en/best-open-source-LLM-for-Russian)
- [IlyaGusev/rulm: Language modeling and instruction tuning for Russian (GitHub)](https://github.com/IlyaGusev/rulm)
- [YaLM-100B: Pretrained language model 100B parameters (Yandex GitHub)](https://github.com/yandex/YaLM-100B)
