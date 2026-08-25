# Stream B: Benchmark Critique and Gaming
**SCOUT B — Contrarian / Skeptic lens**
*Research date: 2026-06-01*

---

## Key Findings (bullet list, confidence-rated)

1. **Russian SuperGLUE was gamed by rule-based heuristics before LLMs even arrived.** A 2021 paper ("Unreasonable Effectiveness of Rule-Based Heuristics in Solving Russian SuperGLUE Tasks", arXiv:2105.01192) demonstrated that simple classifiers exploiting lexical artifacts (e.g., labeling all instances as "entailment" when the word "был" appears) outperformed or matched pre-trained language models on multiple tasks. Conclusion: the benchmark was measuring artifact exploitation, not language understanding. **Confidence: HIGH — peer-reviewed, replicated finding.**

2. **MERA's claim to be "black-box" and "contamination-free" is structurally weak.** MERA (arXiv:2401.04531) uses datasets from public sources under CC-BY-4.0 licenses — the same sources that appear in Common Crawl and other large pre-training corpora. The "black-box" design prevents models from fine-tuning on the test set directly, but does nothing about pre-training contamination. This distinction is cosmetic. **Confidence: HIGH — structural argument, no counter-evidence found.**

3. **Cross-lingual contamination is an undetected contamination vector specific to Russian.** Research ("Data Contamination Can Cross Language Barriers", arXiv:2406.13236) shows that training on translated benchmark data in other languages inflates scores on Russian tasks while evading detection methods based on text overlap. A model contaminated on English MMLU or translated Russian equivalents will score higher on MERA tasks derived from similar knowledge domains without having learned Russian. **Confidence: HIGH — experimentally demonstrated on Llama3 and Qwen1.5.**

4. **Benchmark inflation of 16+ percentage points documented on real models.** "Benchmark Inflation: Revealing LLM Performance Gaps Using Retro-Holdouts" (arXiv:2410.09247) found inflation of up to 16 pp on TruthfulQA across models including GPT, Claude, Mistral, and Gemma. No analogous Russian study exists, but there is no reason to expect the Russian ecosystem — where even fewer independent evaluators operate — to be immune. The inflation is likely larger. **Confidence: HIGH for general claim; MEDIUM for Russia-specific extrapolation.**

5. **MERA is largely translated or adapted from English benchmarks, importing Anglo-centric cultural biases.** Several MERA tasks (RuWorldTree, RuMMLU-style components) derive from English originals. Research on Global MMLU (arXiv:2412.03304) found that ~28% of MMLU questions require culturally sensitive knowledge, with 84.9% of geography items biased toward North American/Western contexts. Translation also introduces artifacts that distort meaning. A model that memorized English benchmark answers needs only superficial translation awareness to score well in Russian. **Confidence: HIGH — documented in Global MMLU paper; MERA origin of individual tasks confirmed in paper.**

6. **Multiple-choice format — the dominant format in MERA — is the most gameable format.** Research ("Artifacts or Abduction: How Do LLMs Answer Multiple-Choice Questions Without the Question?", arXiv:2402.12483) shows LLMs can achieve above-chance accuracy on MCQA using only the answer choices, without seeing the question. Additionally, minor perturbations like reordering choices shift MMLU rankings by up to 8 positions. MERA's 14 out of 21 tasks are classification or multiple-choice. **Confidence: HIGH — multiple independent papers converge on this finding.**

7. **LLM-as-judge evaluation in Russian has a documented performance gap versus English.** REPA (arXiv:2503.13102), a 2025 benchmark of 1,000 Russian queries and 2,000 LLM responses, found "a notable gap between LLM judge performance in Russian and English." Rankings based on LLM preferences only partially align with human preferences. This means automated evaluation for Russian text quality — increasingly used as a proxy for human judgment — is less reliable than claimed. **Confidence: HIGH — peer-reviewed, 2025 publication.**

8. **POLLUX (2025) acknowledges that existing Russian benchmarks are opaque and non-reproducible.** The POLLUX paper (arXiv:2505.24616) explicitly states its motivation as filling a gap left by existing Russian benchmarks that lack transparent, criteria-driven evaluation. The benchmark's authors include Sber contributors — which raises the next finding. **Confidence: HIGH — self-disclosure in paper abstract.**

9. **Structural conflict of interest: benchmark authors and model developers overlap in Russia.** MERA is administered by AI Alliance Russia and developed with participation of Sber (GigaChat), Yandex, and SberDevices. The same organizations that run the benchmark compete on it. GigaChat has topped MERA rankings and Sber publishes GigaChat's MERA scores as marketing claims. POLLUX is also co-authored by Sber researchers. Western leaderboards face similar problems, but independent third-party Russian-language benchmarks are nearly absent. **Confidence: HIGH — observable from benchmark documentation; no independent auditor identified.**

10. **BLEU and ROUGE — still used in some Russian NLP sub-tasks — have poor correlation with human judgment.** Multiple studies document that these metrics reward lexical overlap rather than semantic quality. For Russian, with its rich morphology, the penalty for morphological variation (same word, different inflection) is structurally higher than for English, making BLEU particularly unreliable. **Confidence: HIGH — general finding well-documented; Russian morphology argument is logical inference, not measured.**

11. **Russian SuperGLUE was revised (version 1.1, arXiv:2202.07791) precisely because the original version contained unresolved vulnerabilities.** The revision paper is titled "Revising the Lessons not Learned" — an admission from the creators that the prior version was measuring artifacts, not capabilities. Key tasks (RUSSE, DaNetQA, RuCoS, MuSeRC) were fixed. The successor MERA was launched partly because even 1.1 became saturated. **Confidence: HIGH — documented in revision paper.**

12. **Benchmark saturation is observable: RSG was saturated faster than GLUE.** English GLUE was saturated in roughly one year; Russian SuperGLUE showed similar trajectory. When frontier models approach human performance on a benchmark, the benchmark stops differentiating. MERA is already showing ceiling effects on some tasks for top-tier models. **Confidence: MEDIUM — saturation claim for RSG is documented; MERA ceiling effects are partial/inferred from leaderboard trends.**

13. **The gap between benchmark scores and real-world writing quality is unquantified for Russian.** No published study directly compares Russian LLM benchmark rankings to practitioner preference for text quality tasks (copywriting, summarization, business writing). The REPA benchmark covers 10 error types but not stylistic register, tonal appropriateness, or domain-specific quality. This gap is the core blind spot of the entire Russian evaluation ecosystem. **Confidence: HIGH that the gap exists; MEDIUM on its magnitude.**

14. **Verbosity bias corrupts LLM-as-judge evaluations, and Russian models may be systematically rewarded for it.** Research establishes that LLM judges prefer longer answers even without quality improvement. GigaChat and YandexGPT are anecdotally noted for producing verbose, formatted output. If LLM-based evaluations are used to rank Russian models, verbosity bias could explain high human-preference scores independent of actual quality. **Confidence: MEDIUM — verbosity bias documented; Russian-specific extension is reasonable inference.**

15. **Goodhart's Law is in full effect: Russian benchmark scores are now marketing targets, not quality indicators.** Sber announces GigaChat rankings on MERA as proof of superiority. Yandex claims YandexGPT leads the "ru-LLM Arena" Elo rating. When organizations optimize model training and RLHF pipelines specifically toward benchmark performance, benchmark performance stops measuring what it was designed to measure. **Confidence: HIGH — this is Goodhart's Law applied to the observable Russian AI market situation.**

---

## Evidence for Benchmark Gaming (Specific Cases and Models)

### Russian SuperGLUE — The Definitive Documented Case

The clearest documented case of gaming a Russian benchmark predates the LLM era. In 2021, Iazykova et al. (arXiv:2105.01192) showed that:

- Simple rule-based classifiers without any neural components achieved competitive or superior results to BERT and GPT-3 fine-tuned models on multiple RSG tasks.
- The heuristic for the TERRA (textual entailment) task was a single lexical feature: presence of the word "был." This single binary feature matched the performance of substantially more complex models.
- The RCB task (commonsense NLI) was similarly vulnerable to frequency-based heuristics derived from annotation artifacts introduced by crowdworkers.

The mechanism: crowdworkers who created the Russian NLI datasets used predictable linguistic patterns when writing non-entailing pairs. Models learned these patterns rather than semantic inference.

This is not speculation — it is an empirically confirmed failure mode of a mainstream Russian NLP benchmark. The RSG 1.1 revision attempted fixes, but the underlying vulnerability — annotation artifacts from crowdsourced data — was not fully eliminated.

### Multiple-Choice Format Exploitation

MERA uses multiple-choice format for 14 of its 21 tasks. Research ("Large Language Models Are Not Robust Multiple Choice Selectors", arXiv:2309.03882) demonstrates:

- LLMs exhibit strong positional biases in MCQ (e.g., systematic preference for option "A" or "C" across tasks).
- Models can be ranked differently simply by reordering answer choices with no change to underlying knowledge.
- "Leaving the barn door open for Clever Hans" (arXiv:2410.11672) shows LLMs can learn to identify correct answers from surface features of the benchmark format itself.

A model fine-tuned on Russian MCQ-style data from Common Crawl (abundant in Russian educational and test-prep content, including ЕГЭ preparation materials) has seen the pattern of these formats extensively — regardless of whether it "understood" the questions.

### GigaChat on MERA — The Conflict-of-Interest Problem

Sber developed GigaChat and participates in MERA's governance structure. When GigaChat tops the MERA leaderboard, this should be treated with the same skepticism applied to pharmaceutical companies running their own drug trials. The paper trail shows:

- MERA Industrial (2025) includes domains (agronomy, aquaculture, medicine) where GigaChat and other Russian models compete.
- Tests are "developed by the best experts from Russia's leading universities" — but the selection of those universities and the validation of test quality is not independently audited.
- Sber press releases describe GigaChat Ultra as "outperforming DeepSeek V3.1 and Qwen3-235B in Russian-language tasks" — a claim sourced from evaluations that Sber has a structural interest in winning.

---

## Evidence for Data Contamination

### The Public Dataset Problem

MERA explicitly states its datasets are from "open sources maintaining their original licenses (primarily CC-BY-4.0)." This is also a description of what ends up in pre-training corpora. Common Crawl, which underlies most LLM pre-training pipelines, crawls the same open Russian internet. The datasets used in MERA tasks include:

- RuBQ (Russian questions from Wikidata) — published openly, widely cited, indexed by Google.
- RuWorldTree (adapted from the English WorldTree dataset) — publicly available on HuggingFace as `ai-forever/MERA`.
- MathLogicQA — original dataset, but published with the MERA repository on HuggingFace.

The MERA HuggingFace dataset (`ai-forever/MERA`, `MERA-evaluation/MERA`) is publicly downloadable. Any model trained after January 2024 using HuggingFace datasets in its pre-training pipeline — including models from Meta, Alibaba, or Google that compete on the leaderboard — has structural opportunity for contamination.

### Cross-Lingual Contamination Is Undetectable

The paper "Data Contamination Can Cross Language Barriers" (arXiv:2406.13236) is particularly damaging for Russian benchmarks. The authors performed the following experiment:

1. Fine-tuned LLaMA3-8B and Qwen1.5-7b on translated versions of MMLU, ARC Challenge, and MathQA in seven languages.
2. Evaluated on English test sets.
3. Showed that performance inflated substantially and existing detection methods (based on text overlap) failed to detect the contamination.

Applied to Russia: a model pre-trained on a Russian translation of MMLU (abundant on Russian educational sites) will score higher on MERA tasks that share conceptual overlap with MMLU domains (science, history, geography) without this being detectable as "contamination" by standard methods.

The Contamination Report for Multilingual Benchmarks (arXiv:2410.16186) studied 7 popular multilingual benchmarks and found that "almost all models show signs of being contaminated with almost all the benchmarks tested." Russian is among the covered languages.

### Benchmark Inflation Magnitude

The "retro-holdout" methodology (arXiv:2410.09247) constructed held-out equivalents of TruthfulQA and measured the gap: up to 16 percentage points inflation per model. If this approach were applied to MERA tasks, the expected finding — based on the same structural conditions (public datasets, large training corpora, commercial competition) — would show meaningful score inflation. No one has run this experiment for MERA because no independent Russian evaluator has the resources or incentive to do so.

---

## Benchmark vs. Human Evaluation Gaps

### REPA: The First Systematic Russian Evidence

The REPA dataset (arXiv:2503.13102) is the most direct evidence available. Key finding: rankings based on human annotator preferences only partially align with LLM-judge rankings. The paper identifies 10 error types including factual accuracy, relevance, coherence, and fluency. The gap is described as "notable" — the paper does not quantify it precisely, but the finding confirms the gap exists and is non-trivial.

Critically, REPA found that LLM judges in Russian underperform LLM judges in English. This means that the dominant automated evaluation method — using a strong LLM (GPT-4, Claude) to judge Russian outputs — is less reliable than the same method for English. Any Russian benchmark using LLM-as-judge has an inherent accuracy penalty relative to its English counterparts.

### POLLUX's Implicit Acknowledgment

POLLUX (arXiv:2505.24616) was motivated by the observation that existing Russian benchmarks do not measure generative quality in a transparent, criteria-driven way. The benchmark's authors explicitly critique "traditional resource-consuming, side-by-side human comparisons" while acknowledging that automated metrics have failed to replace them adequately. The existence of POLLUX is itself evidence that the Russian evaluation community considers existing benchmarks inadequate for measuring text generation quality.

### The "Correct Answer" vs. "Natural Text" Chasm

MERA's 21 tasks are overwhelmingly structured around classification, multiple-choice, and factual question-answering. Zero tasks measure:

- Register appropriateness (formal vs. colloquial)
- Stylistic coherence across a long document
- Absence of calques from English syntax
- Natural use of Russian idiomatic expressions
- Tonal consistency

A model can score 85% on MERA while producing text that any Russian speaker would identify as non-native — hypercorrect formal register, absent of живой язык (living language), with English-influenced syntax ("Это является важным аспектом рассмотрения вопроса" rather than "Это важно"). MERA does not detect this failure mode at all.

### Practitioner Evidence (Weak but Directional)

Habr articles on testing Russian LLMs (2024) report that practitioners find GigaChat and YandexGPT produce text "with high grammatical accuracy" but note stylistic issues and reduced coherence in some models. The distinction practitioners make in practice — YandexGPT for tech content, GigaChat for legal/regulatory Russian — is not captured by any benchmark metric. Benchmark rankings do not differentiate by use case; practitioners evaluate by use case by definition.

---

## What Would a Better Evaluation Look Like?

### 1. Private, Dynamically Refreshed Test Sets

The core structural problem is static public datasets. A rigorous alternative:

- Test sets created and held entirely privately by an independent third party (no overlap with model developers).
- Questions generated from events post-dating training cutoffs, using the "ArxivRoll" approach (arXiv:2412.13670) — content from recent publications that could not plausibly be in pre-training data.
- Refreshed every 6 months to prevent gradual contamination.

For Russian specifically: use content from recent Russian-language publications (РИА Новости wires from last 30 days, recent Госдума documents, recent scientific publications in Russian journals) as source material for questions.

### 2. Production Task Evaluation

Replace MCQ with open-ended tasks drawn from actual practitioner use cases:

- Write a business letter declining a partnership offer (formal register, specific conventions).
- Summarize a 2,000-word legal contract in 150 words without paraphrase errors.
- Generate a sales script for a B2B call with objection handling (tests colloquial register, living language).
- Explain the difference between депозит and вклад to a person unfamiliar with banking (tests clarity without jargon).

These tasks cannot be gamed by MCQ positional bias or memorized answer patterns. They require actual Russian language competence.

### 3. Blind Human Preference Studies with Controlled Demographics

A Russian-language equivalent of Chatbot Arena with:

- Annotators stratified by region, age, and professional background (not just Moskovskie IT-shniki).
- Tasks drawn from the annotators' own professional domains.
- Blind comparison with no model identity disclosure.
- Separation of evaluators for "correct answer" vs. "preferred phrasing" tasks.

Currently, Russian representation on the main Chatbot Arena platform is under 2% of total conversations. There is no scaled Russian-language human preference dataset.

### 4. Adversarial Testing for Russian-Specific Failure Modes

A dedicated adversarial suite targeting known weaknesses:

- **Morphological stress tests**: unusual but grammatically correct inflection forms that models may produce incorrectly.
- **Register switches**: mid-document shifts between formal and colloquial that models should handle gracefully.
- **Calque detection**: prompts designed to elicit English syntactic calques ("является одним из важных факторов").
- **Idiom production**: prompts requiring colloquial expressions where a grammatically correct but unnatural paraphrase should score lower.

### 5. Independent Governance

A benchmark run by a body without commercial interests in any competing model. In Russia, given the current market structure (Sber/GigaChat, Yandex/YandexGPT dominate both model development and AI research infrastructure), this likely requires:

- University-led evaluation (НИУ ВШЭ, МФТИ, КФУ) with no corporate AI model involvement.
- International collaboration (FAIR, academic labs outside Russia) to prevent domestic market dynamics from corrupting evaluation.
- Public audit trails for how test questions were selected and validated.

### 6. Error Taxonomy-Based Evaluation

Following the REPA approach but expanding it: evaluate models against a taxonomy of Russian-specific errors including:

- Ложные друзья переводчика (false cognates used incorrectly)
- Тавтология (redundant repetition — a common LLM failure in Russian)
- Нарушение управления (incorrect case government after verbs/prepositions)
- Кальки с английского (syntactic and lexical calques)
- Неуместный официально-деловой стиль в неформальном контексте

This is measurable with trained human annotators and provides actionable diagnostic information that MCQ benchmarks structurally cannot.

---

## Sources Used

- [MERA: A Comprehensive LLM Evaluation in Russian (arXiv:2401.04531)](https://arxiv.org/abs/2401.04531)
- [MERA ACL 2024 paper](https://aclanthology.org/2024.acl-long.534/)
- [MERA official benchmark site](https://mera.a-ai.ru/en/text)
- [MERA GitHub (ai-forever)](https://github.com/ai-forever/MERA)
- [Unreasonable Effectiveness of Rule-Based Heuristics in Solving Russian SuperGLUE Tasks (arXiv:2105.01192)](https://arxiv.org/abs/2105.01192)
- [Russian SuperGLUE 1.1: Revising the Lessons not Learned (arXiv:2202.07791)](https://arxiv.org/abs/2202.07791)
- [Data Contamination Can Cross Language Barriers (arXiv:2406.13236)](https://arxiv.org/html/2406.13236v2)
- [Contamination Report for Multilingual Benchmarks (arXiv:2410.16186)](https://arxiv.org/pdf/2410.16186)
- [Benchmark Inflation: Revealing LLM Performance Gaps Using Retro-Holdouts (arXiv:2410.09247)](https://arxiv.org/abs/2410.09247)
- [Benchmark Data Contamination of Large Language Models: A Survey (arXiv:2406.04244)](https://arxiv.org/abs/2406.04244)
- [Benchmarking LLMs Under Data Contamination: Static to Dynamic (arXiv:2502.17521)](https://arxiv.org/html/2502.17521v2)
- [REPA: Russian Error Types Annotation (arXiv:2503.13102)](https://arxiv.org/abs/2503.13102)
- [Eye of Judgement: POLLUX Benchmark (arXiv:2505.24616)](https://arxiv.org/abs/2505.24616)
- [Global MMLU: Cultural and Linguistic Biases (arXiv:2412.03304)](https://arxiv.org/pdf/2412.03304)
- [Spanish and LLM Benchmarks: is MMLU Lost in Translation? (arXiv:2406.17789)](https://arxiv.org/html/2406.17789v1)
- [Artifacts or Abduction: How Do LLMs Answer MCQ Without the Question? (arXiv:2402.12483)](https://arxiv.org/html/2402.12483v1)
- [Large Language Models Are Not Robust Multiple Choice Selectors (arXiv:2309.03882)](https://arxiv.org/pdf/2309.03882)
- [Leaving the Barn Door Open for Clever Hans (arXiv:2410.11672)](https://arxiv.org/pdf/2410.11672)
- [When Benchmarks are Targets: Leaderboard Sensitivity (arXiv:2402.01781)](https://arxiv.org/html/2402.01781v1)
- [Line Goes Up? Inherent Limitations of Benchmarks (arXiv:2502.14318)](https://arxiv.org/abs/2502.14318)
- [Verbosity Bias in Preference Labeling by LLMs (arXiv:2310.10076)](https://arxiv.org/pdf/2310.10076)
- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena (arXiv:2306.05685)](https://arxiv.org/abs/2306.05685)
- [Gaming the System: Goodhart's Law Exemplified in AI Leaderboard Controversy](https://blog.collinear.ai/p/gaming-the-system-goodharts-law-exemplified-in-ai-leaderboard-controversy)
- [AntiLeakBench: Preventing Data Contamination with Updated Real-World Knowledge (arXiv:2412.13670)](https://arxiv.org/pdf/2412.13670)
- [LLM Benchmark Datasets Should Be Contamination-Resistant (arXiv:2605.19999)](https://arxiv.org/html/2605.19999v1)
- [The Vulnerability of Language Model Benchmarks (arXiv:2412.03597)](https://arxiv.org/abs/2412.03597)
- [Тестируем LLM для русского языка (Habr, 2024)](https://habr.com/ru/articles/856436/)
- [GigaChat Family: Efficient Russian Language Modeling (arXiv:2506.09440)](https://arxiv.org/html/2506.09440v1)
- [Vikhr: Open-Source Instruction-Tuned LLMs for Russian (arXiv:2405.13929)](https://arxiv.org/html/2405.13929v2)
- [GAOKAO-Eval: Does High Score Truly Reflect Strong Capabilities? (arXiv:2412.10056)](https://arxiv.org/pdf/2412.10056)
- [LLM Evaluation Is Broken: Why BLEU and ROUGE Don't Measure Real Understanding](https://towardsai.net/p/machine-learning/llm-evaluation-is-broken-why-bleu-and-rouge-dont-measure-real-understanding)
- [LLM Benchmarks vs Real-World Performance (TransPerfect/Dataforce)](https://www.dataforce.ai/blog/why-academic-llm-benchmarks-rarely-reflect-real-world-performance)
