---
type: action_map
source_files: [consensus_reference.md, _reflection_2.md, deep_dive_A_humanness_criteria.md]
created: 2026-06-02
author: ACTION MAPPER
global_confidence: 0.35
field_status: CONTESTED
---

# Action Map — Russian LLM Writing Quality Research

**For:** Russian-language content creators, SEO professionals, editorial teams, researchers working with AI-generated Russian text.
**Based on:** Consensus Reference (Cycle 3 synthesis), Reflection 2, Deep Dive A (R-HLS framework).
**Field maturity warning:** 51% of cited sources are Grade C preprints. Only 11% are Grade A. Every quantitative claim should be treated as directional, not definitive. Global confidence of the underlying research: 0.35 / 1.00.

---

## 1. Immediate Actions (Today)

### 1.1 Select the right model for each task type

Use this task-to-model mapping, derived from practitioner consensus (Grade D — directionally robust but not peer-reviewed). Apply confidence tags per recommendation.

| Task | Primary model | Fallback | Confidence |
|------|--------------|----------|-----------|
| Long-form articles, business text | Claude Sonnet 4.6 | ChatGPT | MODERATE |
| SEO headlines, short digital copy | YandexGPT 5 Pro | ChatGPT | MODERATE |
| Bulk SEO content (100+ articles) | Qwen3-235B | DeepSeek V3 | MODERATE |
| Legal / regulatory / official documents | GigaChat 2 Max | ChatGPT | MODERATE |
| Copy editing, style revision | Claude | ChatGPT | MODERATE |
| Text classification, structured extraction | YandexGPT 5 | GigaChat | MODERATE |
| Informal / conversational register | ChatGPT | YandexGPT | MODERATE |
| On-premise / confidential data | GigaChat (local) | Vikhr | LOW-MODERATE |

Do not interpret these rankings as peer-reviewed findings — they reflect Grade D practitioner consensus from Habr and vc.ru, biased toward IT-literate Moscow professionals. Run your own A/B test on your domain before committing to a workflow (see Section 2).

### 1.2 Stop using MERA rankings as a writing quality proxy

Treat MERA scores as task-solving accuracy, not editorial quality. [HIGH confidence]

MERA measures MCQ, classification, math, code, and knowledge recall. It contains zero tasks measuring stylistic quality, register naturalness, or idiomatic fluency. Citing MERA position to justify a model choice for writing tasks is a category error. Additionally: 67% of MERA tasks are MCQ format (gameable), the benchmark is administered by a consortium that includes Sber (which also develops GigaChat — a direct conflict of interest), and the human baseline (0.852) has already been exceeded by Claude Opus 4.6 (0.862), signaling benchmark saturation.

Practical rule: Ignore MERA rankings entirely when choosing a model for Russian editorial or SEO content. Run domain-specific tests instead.

### 1.3 Purge RLHF-artifact phrases from all LLM output before publishing

Implement a mandatory phrase filter on all Russian LLM output. [HIGH confidence for mechanism; the specific list is empirically grounded but not exhaustively validated]

These phrases are products of RLHF reward for "engaged, thorough, helpful" style. They are the primary signal that automated AI detectors use — and the primary cue that signals AI-origin to trained human readers. Pre-RLHF base models are classified as "human" by GPTZero at a 96–98% rate; post-RLHF models drop significantly. Removing these phrases is the single highest-ROI editing step.

Minimum phrase blocklist (add to system prompt AND post-processing filter):

```
следует отметить
важно понимать
важно отметить
стоит отметить
необходимо учитывать
в данном контексте
таким образом
данный (в значении «этот»)
является ключевым
комплексный подход
эффективный инструмент
не просто X, а Y (шаблон)
с одной стороны... с другой стороны
```

### 1.4 Apply the em-dash rule to every article

Limit em-dash usage to fewer than 8 per article, and no more than 2 per paragraph. [MODERATE confidence — single preprint arXiv:2603.27006, Grade C, not replicated; but directional signal is robust]

GPT-4.1 produces 10.62 em-dashes per 1,000 words; the human baseline is approximately 3.23. This 3.28× overuse is the most easily detected surface-level AI marker in Russian text. Implement as a final check before publication: `text.count('—') / word_count * 1000` — target below 4.0.

### 1.5 Run the 5-minute basic humanness check on every LLM output

Implement this Python snippet in your editorial pipeline. It requires no new infrastructure — only `razdel` and `pymorphy2`, both installable via pip. [HIGH confidence for the mechanism; LOW confidence for the specific Russian-calibrated thresholds, which are extrapolated from English data]

```python
import statistics
import razdel
import pymorphy2

def quick_humanness_check(text):
    # 1. Burstiness — sentence length variability
    sentences = list(razdel.sentenize(text))
    lengths = [len(s.text.split()) for s in sentences]
    B = statistics.stdev(lengths) / statistics.mean(lengths) if len(lengths) > 1 else 0

    # 2. Deverbal noun ratio (канцеляризм signal)
    morph = pymorphy2.MorphAnalyzer()
    words = [w for s in sentences for w in s.text.split()]
    nouns = [w for w in words if 'NOUN' in morph.parse(w)[0].tag]
    deverbal_suffixes = ('ение', 'ание', 'ация', 'ство', 'тие', 'овка')
    deverbals = [w for w in nouns if any(w.lower().endswith(s) for s in deverbal_suffixes)]
    DN = len(deverbals) / max(len(nouns), 1)

    # 3. Em-dash density
    em_per_1000 = text.count('—') / (len(words) / 1000) if words else 0

    # 4. RLHF-artifact phrases
    ai_phrases = ['следует отметить', 'важно понимать', 'таким образом',
                  'необходимо учитывать', 'стоит отметить', 'в данном контексте',
                  'является ключевым', 'комплексный подход', 'эффективный инструмент']
    phrase_hits = sum(1 for p in ai_phrases if p in text.lower())

    return {
        'burstiness': round(B, 3),           # target: > 0.55
        'deverbal_ratio': round(DN, 3),      # target: < 0.20
        'em_dash_per_1000': round(em_per_1000, 2),  # target: < 4.0
        'ai_phrase_hits': phrase_hits,       # target: 0–1
    }
```

Threshold table (extrapolated from English, not validated on Russian corpus — use as directional signal only):

| Metric | AI-signal zone | Human-like zone |
|--------|---------------|----------------|
| burstiness | < 0.35 | > 0.55 |
| deverbal_ratio | > 0.40 | < 0.20 |
| em_dash_per_1000 | > 6.0 | < 4.0 |
| ai_phrase_hits | ≥ 3 | 0–1 |

### 1.6 Add the manual humanness checklist to your editorial SOP

Pair the automated check with a 10-minute human review step. [HIGH confidence — these are verified editorial judgment criteria]

For every LLM-generated article:
1. Read the first and last paragraph — check for RLHF openers and closers.
2. Find 3 sentences with participial or gerundive phrases (причастные/деепричастные обороты) — verify that the subject of the main clause matches the gerund subject.
3. Check 5 random verb-noun collocations — does it say «достигать результата» where a native speaker would say «добиваться результата»?
4. Verify at least one "dirty detail" exists: a concrete number, a named person, a specific failure, a specific date — something that cannot be generated without primary experience.

The last criterion — embodied knowledge (Теория C) — is the single strongest signal of genuine human authorship and is fundamentally non-automatable.

---

## 2. Short-Term Actions (1–4 Weeks)

### 2.1 Run a domain-specific A/B model comparison on your own content

Design and execute a controlled model comparison for your specific content type. [HIGH confidence that you should do this; MODERATE confidence that the results will generalize beyond your domain]

Method (adapted from Habr practitioner protocol):
1. Select 5 real topics from your actual editorial calendar — not generic test prompts.
2. Run each topic through: Claude Sonnet 4.6, YandexGPT 5 Pro, Qwen3-235B, and one additional model relevant to your domain.
3. Use identical system prompts for all models (include the RLHF-artifact blocklist from Section 1.3).
4. Blind evaluation: have a human evaluator (or an LLM-judge with explicit rubric) score each output without knowing the source model. Score on: naturalness, register appropriateness, absence of AI markers, factual accuracy, structural coherence (1–5 scale each).
5. Apply the quick_humanness_check script from Section 1.5 to all outputs.
6. Calculate cost per 1,000 words for each model at your actual usage volume.
7. Make a task-specific model selection decision based on quality × cost, not on MERA rankings.

Note: LLM-as-a-judge for Russian text has a Spearman correlation of 0.641 with human judgments (REPA benchmark) — adequate for screening, not for final quality certification.

### 2.2 Implement a multi-model workflow for content production

Design a pipeline where different models handle different stages, rather than using a single model end-to-end. [HIGH confidence — practitioner consensus is consistent across 6+ independent sources; H3 "task determines winner" is strongly supported]

Recommended pipeline (cost-optimized):

- Stage 1 — Research and structure: DeepSeek V3 or ChatGPT. Estimated cost: $0.05–0.10 per 3,000-word article.
- Stage 2 — Draft writing: Claude Sonnet 4.6. System prompt must include: voice definition, RLHF-artifact blocklist, em-dash limit (≤8 per article), instruction to use specific numbers instead of ranges wherever possible. Estimated cost: $0.30–0.60.
- Stage 3 — Style editing: Claude (or human editor). Check: em-dash count, AI-phrase grep, burstiness score, at least one concrete embodied detail.
- Stage 4 — Headlines and meta descriptions: YandexGPT 5 Pro. Generate 3–5 H1 variants; select the one that sounds most like a native digital-native Russian speaker.

Total estimated cost: $0.45–0.90 per article (vs. $1.50–3.00 with Opus-only pipeline).

### 2.3 Implement the R-HLS basic prototype

Build and deploy the minimal viable R-HLS (Russian Human-likeness Score) implementation in your editorial pipeline within one working week. [HIGH confidence for technical feasibility; LOW confidence for the specific threshold values]

Implementation steps:
1. Install dependencies: `pip install razdel pymorphy2 natasha lexical-diversity`
2. Implement the `quick_humanness_check()` function from Section 1.5 — this takes approximately 1 day.
3. Extend with participial stacking detection using natasha (adds approximately 1 additional hour):

```python
from natasha import Segmenter, MorphVocab, NewsEmbedding, NewsMorphTagger, Doc

def count_participial_stacking(text, emb, segmenter, morph_tagger, morph_vocab):
    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    for token in doc.tokens:
        token.lemmatize(morph_vocab)
    # Count sentences where 2+ participles/gerunds co-occur
    sentences = list(razdel.sentenize(text))
    stacked_count = 0
    for sent in sentences:
        sent_doc = Doc(sent.text)
        sent_doc.segment(segmenter)
        sent_doc.tag_morph(morph_tagger)
        parts = [t for t in sent_doc.tokens
                 if t.pos == 'VERB' and
                 ('Part' in (t.feats or {}).get('VerbForm', '') or
                  'Conv' in (t.feats or {}).get('VerbForm', ''))]
        if len(parts) >= 2:
            stacked_count += 1
    return stacked_count / max(len(sentences), 1)  # target: < 0.15
```

4. Add lemma-MTLD using lexical-diversity library:

```python
from lexical_diversity import lex_div as ld

def compute_lemma_mtld(text):
    morph = pymorphy2.MorphAnalyzer()
    words = text.split()
    lemmas = [morph.parse(w)[0].normal_form for w in words if w.isalpha()]
    return ld.mtld(lemmas)  # target: > 80 (human-like); < 60 (AI-signal)
```

5. Combine into a single scoring function that returns a dashboard of signals, not a single composite score. Do not collapse to one number yet — the weighting scheme has no empirical validation for Russian.
6. Log scores for every article published. Use this log to build your own baseline corpus (see Section 3.2).

---

## 3. Medium-Term Actions (1–3 Months)

### 3.1 Build a register consistency module for R-HLS

Develop the register consistency component (Criterion 4) of R-HLS using the lexical signal approach. [MODERATE confidence for the approach; the mechanism is well-documented, but no ready-made Russian tool exists]

Register consistency is the most perceptually salient humanness criterion for native Russian speakers but the hardest to automate. It requires detecting when a text switches registers mid-article — for example, a formal business paragraph followed by a sentence containing a ChatGPT-fingerprint opener.

Minimum viable approach (Approach B from DD-A):
1. Compile three register-marker dictionaries: formal-bureaucratic markers (настоящим, во избежание, в соответствии с), conversational markers (ну, вот, кстати, короче, же/ведь), RLHF-artifact markers (стоит отметить, важно понимать, не просто X а Y).
2. For each paragraph, compute the ratio of each marker type. Flag paragraphs where marker types from different registers co-occur.
3. Compute a register consistency score as the inverse of paragraph-level marker-type mixing rate.

Estimated development time: 2–3 weeks for the lexical approach. Budget 2–4 months for a fine-tuned classifier approach (requires ruBERT fine-tuning on НКРЯ register-annotated data).

### 3.2 Build a verified Russian human corpus for R-HLS threshold calibration

Collect 500+ human-written texts per genre to replace the extrapolated English thresholds with empirically grounded Russian norms. [HIGH confidence that this is needed; the current thresholds are explicitly not validated for Russian]

Execution plan:
1. Define 3–4 genres matching your content type (e.g., business blog, SEO article, journalistic feature, formal report).
2. Collect 500 texts per genre — clearly human-authored (bylined, pre-2020 to minimize AI contamination, from sources with high editorial standards).
3. For each text, run the R-HLS basic pipeline (burstiness, DN ratio, em-dash density, participial stacking, lemma-MTLD).
4. Establish genre-specific percentile distributions — your threshold for "human-like" should be the 25th percentile of your human corpus, not an English-derived constant.
5. Generate matched AI-authored texts using your primary production models (Claude, YandexGPT) and compute the same metrics.
6. Calculate the optimal classification threshold for each metric using the receiver operating characteristic (ROC) approach.
7. Update your R-HLS scoring function thresholds with the new Russian-calibrated values.

Estimated timeline: 6–8 weeks (corpus collection + annotation + analysis).

### 3.3 Use the AINL-Eval 2025 dataset as a testing resource

Obtain and integrate the AINL-Eval 2025 dataset (52,305 samples; best system accuracy: 86.35%) for testing your R-HLS implementation against a labeled benchmark. [MODERATE confidence — the dataset exists and is peer-reviewed; Grade C preprint arXiv:2508.09622]

Steps:
1. Locate and download the AINL-Eval 2025 dataset (Detection of AI-Generated Scientific Abstracts in Russian, arXiv:2508.09622).
2. Note that this dataset is domain-specific (scientific abstracts) — do not expect transfer to SEO or blog content without re-calibration.
3. Run your R-HLS basic implementation against the binary human/AI labels in this dataset to measure precision and recall of your scoring thresholds.
4. Use the results to identify which R-HLS criteria have the highest discriminative power for scientific Russian text. Treat the insights as directional for other genres.
5. Do not use the top-performing systems from AINL-Eval 2025 as drop-in quality gates for editorial content — they are fine-tuned transformers optimized for academic abstracts and will produce high false-positive rates on creative, conversational, or editorial Russian.

---

## 4. Watch List (Monitor, Do Not Act Yet)

### 4.1 MERA saturation timeline (12–18 months) [MODERATE confidence]

Monitor MERA leaderboard (mera.a-ai.ru) quarterly. Claude Opus 4.6 has already exceeded the human baseline (0.862 vs 0.852). When the top 5 models are clustered within 2–3 points of each other above the human baseline, MERA ceases to be a useful differentiator for any purpose. Watch for the MERA consortium to release a v2 redesign — this will signal that they acknowledge the saturation problem. Do not invest in MERA-based model selection logic; it will need to be rebuilt.

### 4.2 "Think in English" mechanism — wait for Russian-specific replication [LOW confidence for Russian models]

The "Think in English" paper (arXiv:2502.15603, Wendler et al. 2025) demonstrated that Llama-3.1-70B, Gemma-2-27b, and Mixtral-8x22B process semantics through English-proximate intermediate representations even when input and output are Russian. This mechanism, if confirmed for YandexGPT and GigaChat, would explain specific classes of failure (calques, missing discourse particles, SVO bias in topic-comment contexts). However, the mechanism was not tested on Russian-primary models. Do not act on this finding until a logit lens analysis is published specifically for YandexGPT and/or GigaChat. Check arXiv quarterly for "YandexGPT intermediate representations" or "GigaChat multilingual representations."

### 4.3 BerryLM public API (if/when released) [LOW confidence it will be released; MODERATE that it would be worth testing]

BerryLM-XL (#3 MERA, 0.835) is a closed-license model developed by Wildberries and Russ AI. It has zero practitioner mentions, which is explained by its closed API — not necessarily by poor quality. If Wildberries releases a public API or a commercial product, test it immediately on your editorial tasks. The circumstantial evidence of benchmark gaming (three BerryLM variants in TOP-10, GRPO training with MCQ-optimized reward functions) suggests its MERA position overstates its writing quality — but this is unverified. Reserve judgment until you can test it directly on real Russian editorial tasks.

### 4.4 Vikhr tokenization efficiency claims [LOW confidence — source retracted]

arXiv:2405.13929 (Vikhr) was retracted from ACL. The reason for retraction has not been publicly established. Vikhr's claims about 46% token reduction through vocabulary adaptation are directionally plausible (the mechanism is sound) but cannot be cited with confidence until the retraction is explained or a replacement paper is published. Monitor arXiv for a corrected submission.

### 4.5 Pravda network contamination of Russian training data [MODERATE confidence for the fact; LOW for the magnitude]

A documented AI-content disinformation network ("Pravda") systematically seeds AI-generated Russian content into Common Crawl. Models trained on post-2024 web data will increasingly train on AI-generated Russian rather than human-generated Russian, accelerating model collapse (Nature 2024 mechanism). Watch for publications measuring the fraction of AI-generated content in Russian Common Crawl snapshots. If this fraction crosses a significant threshold, it will affect the quality of all models trained on post-contamination data — including future versions of Claude, YandexGPT, and GigaChat.

---

## 5. What NOT to Do

### 5.1 Do not use MERA rankings as writing quality evidence [HIGH confidence]

Never cite a model's MERA score as evidence that it writes better Russian than a competitor. MERA measures task-solving accuracy on MCQ, classification, math, and code tasks. It contains no tasks measuring stylistic quality, register naturalness, idiomatic fluency, or editorial coherence. Stating "Model X ranks #3 on MERA, therefore its Russian is better" is a category error that this research establishes with high confidence.

### 5.2 Do not run a single-model workflow for Russian content production [HIGH confidence]

No single model dominates all Russian content tasks. Using Claude for everything ignores YandexGPT's structural advantages for headlines (trained on the Russian search index, digital-native patterns). Using YandexGPT for everything ignores Claude's advantages for long-form editing. Using GigaChat for everything ignores its documented "ЕГЭ-шный стиль" failure mode in editorial writing. The practitioner consensus for multi-model workflows is consistent across 6+ independent sources.

### 5.3 Do not rely on automated AI detectors as quality gates [HIGH confidence for the mechanism; MODERATE for the operational conclusion]

Automated Russian AI detectors (including GigaCheck) have three structural problems for editorial QA use:
1. They detect RLHF-artifact fingerprints, not fundamental AI-ness — pre-RLHF base models pass at 96–98%.
2. They degrade on new models — a detector trained on GPT-4 outputs may perform worse on Claude 4.6 outputs.
3. Human annotators in the RuATD 2022 benchmark classified AI-Russian text correctly only 66.6% of the time — barely above chance. The best automated system reached 86.35% on scientific abstracts specifically.

Use automated detectors as one signal in a dashboard, not as a binary pass/fail gate. Pair them with the R-HLS criteria from Section 1.5.

### 5.4 Do not use GigaChat for editorial Russian copy without heavy human editing [MODERATE confidence]

GigaChat has a documented practitioner failure mode called "ЕГЭ-шный стиль" — a formal, bureaucratic, exam-essay-like register that is appropriate for regulatory documents but reads as unnatural in editorial, marketing, or SEO content. Its high MERA score reflects optimization for task-accuracy on MCQ-dominated benchmarks, which does not translate to naturalness in editorial writing. If you need GigaChat for data sovereignty reasons (Russian jurisdiction, on-premise deployment), budget for a full human edit of every output — do not rely on automated post-processing alone.

### 5.5 Do not apply English NLP thresholds to Russian text without re-calibration [HIGH confidence for the principle; LOW confidence for knowing exactly how much they differ]

The Flesch-Kincaid readability formula adapted for Russian (Oborneva 2006) is documented as producing lower correlation with perceived difficulty than the English original — because Russian averages 3.29 syllables per word vs. 2.97 in English, and compensates with morphologically shorter sentences. The burstiness thresholds (B < 0.35 = AI signal, B > 0.55 = human-like) were derived from English academic text samples. Apply them only as directional signals until you have calibrated them on a verified Russian corpus (see Section 3.2).

### 5.6 Do not cite vendor benchmark claims without independent verification [HIGH confidence]

YandexGPT's claim of "56% better than GPT-4.1 on Russian tasks" is a single-party, non-replicated benchmark result. GigaChat MERA scores are functionally self-reported through a consortium where Sber is both a member and a developer of the evaluated model. These are not independent validations. Apply an epistemic discount to any benchmark claim made by a commercially interested party without independent replication.

---

## 6. Knowledge Gaps That Block Decision-Making

### 6.1 Tokenization ratio — exact measurement not available [blocks: infrastructure cost planning, model selection for long-context tasks]

The tokenization penalty for Russian in BPE tokenizers ranges from 2× (cl100k_base, multiple sources) to 7–8× (practitioner data for specific texts). This range is too wide to make reliable decisions about: context window planning for long documents, cost estimation for Russian vs. English content at scale, whether tokenizer adaptation (as in Vikhr) is worth the engineering investment. Resolution: write 30 lines of Python to tokenize the same text with 4–5 different tokenizers and report the ratio directly. This measurement does not exist in any peer-reviewed publication for Russian specifically. Any team that runs this measurement will have a more grounded basis for model selection than the current literature provides.

### 6.2 R-HLS thresholds — need a verified Russian human corpus [blocks: automated quality gates, reliable AI-marker detection]

All quantitative thresholds in the R-HLS framework (burstiness > 0.55 = human-like, deverbal_ratio < 0.20 = human-like, etc.) are extrapolated from English data. There is no peer-reviewed Russian corpus study that establishes these thresholds for Russian text by genre. Until a verified corpus is built (see Section 3.2), do not use these thresholds as hard pass/fail criteria — use them as qualitative signals and flag borderline cases for human review.

### 6.3 "Think in English" for YandexGPT and GigaChat — untested [blocks: understanding failure modes for Russian-primary models]

The "Think in English" mechanism (arXiv:2502.15603) was demonstrated only for Llama, Gemma, and Mixtral — models with English-dominant pretraining. For YandexGPT (trained primarily on the Russian Yandex search index) and GigaChat (26.49% Russian in training data), it is unknown whether intermediate representations are English-centric or Russian-centric. This blocks the ability to predict specific failure patterns: if YandexGPT genuinely thinks in Russian, its failure modes in long-form text will differ qualitatively from Claude's — but we cannot characterize them without a logit lens analysis.

### 6.4 Independent MERA replication — does not exist [blocks: trusting any MERA-based claim]

No evaluation result from the MERA leaderboard has been independently replicated by a party without commercial interest in the outcome. The absence of independent replication means every leaderboard position carries an unknown inflation magnitude. Retro-holdout analysis (methodology from arXiv:2410.09247) applied to MERA would likely show 10–20 percentage point inflation for top models, but this has not been done. Until independent replication exists, treat all MERA scores as approximate rankings with unknown absolute accuracy.

### 6.5 Human detection calibration — two incompatible data points [blocks: setting realistic expectations for human QA]

Two data points exist that cannot be directly compared: RuATD 2022 (Grade B) found that human annotators detect AI-Russian at 66.6% — barely above chance. Habr practitioner reports claim that "humans familiar with AI tools detect AI text at ~90%." These numbers refer to different populations (naive annotators vs. AI-literate practitioners), different tasks (binary classification vs. editorial review), and different generator models (pre-GPT-4 generators in RuATD vs. current models). Until a study directly compares detection accuracy across population types using the same text samples and current-generation models, you cannot know whether to expect a 66% or 90% human detection rate in your editorial team.

---

## 7. Decision Framework

### Primary decision tree: "Given task X, use model Y"

```
START: What is your primary task?
│
├─ WRITING LONG-FORM CONTENT (articles, reports, analyses > 1,000 words)
│   ├─ Budget available for quality? YES → Claude Sonnet 4.6
│   └─ Need to minimize cost (100+ articles/month)? → Qwen3-235B
│       └─ Quality gap acceptable? Verify with A/B test first (Section 2.1)
│
├─ WRITING SHORT COPY (headlines, meta descriptions, social captions)
│   └─ Russian-native digital style required? → YandexGPT 5 Pro
│       └─ YandexGPT unavailable? → ChatGPT
│
├─ EDITING EXISTING TEXT (style revision, naturalness improvement)
│   └─ Use Claude (best instruction following for Russian style edits)
│
├─ LEGAL / REGULATORY / OFFICIAL DOCUMENTS
│   ├─ Russian jurisdiction + data sovereignty required? → GigaChat (on-premise)
│   └─ No sovereignty constraint? → GigaChat 2 Max or ChatGPT
│
├─ BULK CONTENT AT SCALE (SEO, large content programs)
│   └─ Qwen3-235B — 91% quality at 130× lower cost than premium models
│       └─ Always follow with quality check (Section 1.5) and human spot-check
│
├─ TEXT CLASSIFICATION / STRUCTURED EXTRACTION
│   └─ YandexGPT 5 (70% accuracy vs GPT-4o's 51% on Russian classification)
│
└─ INFORMAL / CONVERSATIONAL STYLE
    └─ ChatGPT — most flexible register; YandexGPT as fallback
```

### Secondary decision tree: "Should I trust this quality signal?"

```
START: What quality signal do you have?
│
├─ MERA LEADERBOARD RANK
│   └─ Useful for: reasoning and knowledge-recall capability comparisons
│   └─ NOT useful for: writing quality, naturalness, editorial style
│   └─ Trust level: LOW for writing decisions
│
├─ PRACTITIONER REPORT (Habr, vc.ru, Telegram)
│   └─ Directionally useful: consistent signals across 6+ sources are meaningful
│   └─ Limitations: Grade D, biased toward IT-literate Moscow professionals
│   └─ Trust level: MODERATE for direction; LOW for precise quantitative claims
│
├─ AUTOMATED AI DETECTOR SCORE (GigaCheck, GPTZero, etc.)
│   └─ Useful for: flagging RLHF-artifact-heavy texts for review
│   └─ NOT useful for: final pass/fail on editorial quality
│   └─ Trust level: LOW as standalone; MODERATE as one signal in a dashboard
│
├─ R-HLS BASIC SCORE (Section 1.5)
│   └─ Useful for: consistent, reproducible signal across your content pipeline
│   └─ Limitation: thresholds extrapolated from English, not validated for Russian
│   └─ Trust level: MODERATE for direction; use as filter, not as final gate
│
└─ YOUR OWN A/B TEST RESULTS (Section 2.1)
    └─ Most useful signal available to you
    └─ Controlled for your domain, your audience, your quality standards
    └─ Trust level: HIGHEST — this is the only test that measures your actual use case
```

### Cost-quality matrix for Russian editorial content

| Scenario | Recommended approach | Approximate cost per 3k-word article | Expected quality |
|----------|---------------------|--------------------------------------|----------------|
| High-stakes, low-volume (1–10/month) | Claude full pipeline | $0.60–1.20 | Highest available |
| Standard editorial (10–50/month) | Multi-model pipeline (Sec. 2.2) | $0.45–0.90 | High |
| Bulk SEO (50–500/month) | Qwen3-235B + human spot-check | $0.05–0.15 | Acceptable with QA |
| Data-sovereign (Russian law) | GigaChat + mandatory human edit | Variable | Medium (requires editing) |

---

## Summary: Highest-ROI Actions

Rank-ordered by impact-to-effort ratio:

1. **Implement phrase blocklist** (Section 1.3) — 30 minutes of work, immediate quality improvement on all output. [HIGH confidence, HIGH impact]
2. **Apply em-dash rule** (Section 1.4) — 5 minutes to implement as a regex check. [MODERATE confidence, HIGH impact per effort]
3. **Deploy multi-model pipeline** (Section 2.2) — 1–2 days of workflow design, 30–50% cost reduction with maintained quality. [HIGH confidence, HIGH impact]
4. **Run domain-specific A/B test** (Section 2.1) — 1 week, gives you domain-specific model selection that beats any generic ranking. [HIGH confidence that you should do it]
5. **Implement R-HLS basic script** (Section 1.5) — 1 day of development, persistent quality monitoring signal. [HIGH confidence for technical feasibility]
6. **Build Russian human corpus for threshold calibration** (Section 3.2) — 6–8 weeks, transforms R-HLS from directional to empirically grounded. [HIGH confidence this is needed; requires sustained effort]
7. **Stop citing MERA for writing quality** (Section 5.1) — zero effort, immediate credibility improvement. [HIGH confidence]

---

*Action Map | Based on: consensus_reference.md + _reflection_2.md + deep_dive_A_humanness_criteria.md | 2026-06-02*
*Synthesis date: 2026-06-02 | Field global confidence: 0.35 / 1.00 | Status: CONTESTED*
