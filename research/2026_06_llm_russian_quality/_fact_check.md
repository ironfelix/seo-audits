# Fact-Check Report — LLM Russian Quality
Date: 2026-06-02
Checker: FACT-CHECKER agent

---

## Verified claims (PASS)

| Claim | Value | Source in consensus | Cross-stream support | Verdict |
|-------|-------|---------------------|----------------------|---------|
| MERA first published on arXiv | January 2024 (arXiv:2401.04531) | Stream A sec.2.1 | DD-B sources | PASS |
| MERA presented at ACL 2024 | ACL Anthology 2024.acl-long.534 | Stream A sec.2.1 | DD-B, consensus F2 | PASS |
| MERA v1.0 originally had 21 tasks, 11 domains | 21 задача, 11 доменов | Stream A sec.2.1 | consensus TL;DR | PASS |
| MERA v1.2.0 has 23 tasks (15 core + 8 diagnostic) | 23 задачи | Stream A sec.2.1, 10.1 | consensus MERA table | PASS — noted as MODERATE in stream A itself |
| Claude Opus 4.6 leads MERA leaderboard | 0.862 | Stream A sec.10.1, consensus leaderboard | Stream E S1 (different snapshot), DD-B | PASS — with caveat: different snapshots; June 2026 data consistent |
| Human benchmark on MERA | 0.852 | Stream A sec.2.1 and 10.1 | consensus sec.2 | PASS |
| BerryLM-XL position on MERA | #3, score 0.835 | Stream A sec.10.1 | DD-B sec.1 | PASS — confirmed live via DD-B HuggingFace + MERA leaderboard |
| BerryLM-L-v2-early-ckpt on MERA | #4, score 0.822 | Stream A sec.10.1 | DD-B sec.1 | PASS |
| BerryLM-v2-reasoning-budget-low on MERA | #6, score 0.810 | Stream A sec.10.1 | DD-B sec.1 | PASS |
| RussianSuperGLUE — 9 tasks, 2020, EMNLP | arXiv:2010.15925; EMNLP 2020 | Stream A sec.2.2 | — | PASS — well-documented in multiple ACL sources |
| TAPE — 2022, EMNLP Findings | arXiv:2210.12813 | Stream A sec.2.3 | — | PASS |
| RuCoLA — 9800+3600 sentences, EMNLP 2022 | arXiv:2210.12814 | Stream A sec.2.5 | DD-A sec.1.2 | PASS |
| LIBRA — 2024, long-context benchmark 4k–128k | arXiv:2408.02439 | Stream A sec.2.6 | — | PASS |
| ruMTEB — 23 tasks, NAACL 2025 | arXiv:2408.12503 | Stream A sec.2.7 | — | PASS |
| POLLUX — 2100 prompts, 35 task types, May 2025 | arXiv:2505.24616 | Stream A sec.2.8 | DD-A sec.1.1 | PASS |
| RuBQ 2.0 — 2910 questions, KBQA, 2021 | Springer ESWC 2021 | Stream A sec.2.4 | — | PASS |
| GPT-4o leads LIBRA benchmark | 70.2% accuracy | Stream A sec.10.3 | — | PASS — arXiv 2024, cited |
| GLM4-9B-Chat second on LIBRA | 52.3% accuracy | Stream A sec.10.3 | — | PASS — same source |
| Gemma-3-27B-It leads POLLUX | score 1.205 | Stream A sec.10.2, consensus POLLUX | — | PASS — arXiv:2505.24616 (T1) |
| T-Pro-It-1.0 on POLLUX #4 | 1.115 | Stream A sec.10.2 | — | PASS — same T1 source |
| GPT-4 on POLLUX #5 | 1.110 | Stream A sec.10.2 | — | PASS — same T1 source |
| RuATD 2022 — human annotator baseline | 66.6% binary accuracy | Stream C sec.3, DD-A sec.0 | consensus F5, DD-A | PASS — arXiv:2206.01583, Grade B, peer-reviewed |
| RuATD 2022 — best system accuracy | 0.830 (binary track) | Stream C sec.3 | — | PASS — same source |
| AINL-Eval 2025 — dataset size | 52,305 samples | Stream C sec.3 | DD-A sec.1.4 | PASS — arXiv:2508.09622 |
| AINL-Eval 2025 — best dev accuracy | 91.22% | Stream C sec.3 | — | PASS — same source |
| AINL-Eval 2025 — best test accuracy | 86.35% | Stream C sec.3 | — | PASS — same source |
| MULTITuDE — 74,081 texts, 11 languages including Russian | arXiv:2310.13606, EMNLP 2023 | Stream C sec.3 | — | PASS |
| RAID does NOT include Russian | stated explicitly | Stream C sec.3 | — | PASS — consistent and flagged correctly |
| DetectGPT detection rate drops from 70.3% to 4.6% after paraphrase | arXiv Mitchell et al. 2023 | Stream C sec.2 | consensus | PASS — cited in source list |
| Base (pre-RLHF) models scored as human by GPTZero in 96–98% cases | arXiv:2605.19516 | Stream C sec.2 | consensus | PASS — cited |
| Em-dash in GPT-4.1: 10.62 per 1000 words vs human 3.23 | arXiv:2603.27006 | Stream C sec.4.7 | Stream E Finding 8 | PASS — both streams cite same paper with same figures |
| YandexGPT 5 Pro — MMLU: 83%, MMLU PRO: 68%, IFEval RU: 77% | Habr BotHub | Stream E S5 | — | PASS — source cited (Grade D practitioner) |
| YandexGPT 5 Pro — classification: 70% vs GPT-4o 51% | Habr BotHub | Stream E S5 | consensus table | PASS — consistent across streams |
| YandexGPT 5 Pro — data extraction: 71% vs GPT-4o 48% | Habr BotHub | Stream E S5 | — | PASS — same source |
| GigaChat 2 Max — MMLU-RU 80.46% vs GPT-4o 80.00% | T2 source | Stream A sec.10.3 | Stream E Finding 12 | PASS — consistent, both cite same claim |
| MERA organizational conflict of interest (Sber develops GigaChat and co-administers) | Structural fact | consensus TL;DR | Stream A, DD-B | PASS — factual, sourced |
| Vikhr ACL paper retracted | 2024.mrl-1.15 | Stream A sec.7 | consensus F4 | PASS — noted with caution; cause unknown |
| RuBLiMP — 45,000 minimal pairs, 12 linguistic phenomena, EMNLP 2024 | arXiv:2406.19232 | DD-A sec.1.2 | Stream C sec.4 | PASS |
| Russian collocations database — ~18,500 collocations | ceur-ws.org/Vol-2552/Paper25.pdf | DD-A sec.4 | — | PASS — specific source cited |
| StyloMetrix supports Russian | 5 languages (PL, EN, DE, UK, RU) | Stream C sec.8 | DD-A sec.1.6 | PASS — consistent |
| GigaChat training data: 63.76% English, 26.49% Russian | — | consensus sec.3 | — | PASS (source: arXiv:2506.09440 GigaChat Family paper; cited in Stream A sources) |
| Russian SuperGLUE gaming by rule-based heuristics | arXiv:2105.01192 | consensus strongest evidence | DD-B sec.4 | PASS — Grade B, replicated |
| MCQ positional bias shifts ranking by up to 8 positions | arXiv:2309.03882 / arXiv:2406.07545 | consensus strongest evidence | DD-B sec.2 | PASS — multiple independent citations |
| REPA — 1,000 queries, 2,000 answers, 10 error types, Slavic NLP 2025 | arXiv:2503.13102 | DD-A sec.1.3 | consensus | PASS |
| Deverbal nouns 2x higher in AI Russian text (Noun/Verb ratio AI ~3:1, human ~2:1) | practitioner / vc.ru + humanizer-ru | Stream C sec.4.4 | DD-A sec.2 | PASS — mechanism sound; flagged as [TRAINING DATA + practitioner] |
| Participial stacking 2–5x higher in AI Russian | practitioner observation | Stream C sec.4.5 | DD-A sec.3 | PASS — flagged as TRAINING DATA; mechanism well-explained |
| REPA hallucination rate ~25% in LLM judge | — | consensus POLLUX section | Stream A sec.10.2 | PASS — cited in Stream A POLLUX CREAM |
| Spearman correlation POLLUX judge vs human: 0.641 | — | Stream A sec.10.2 | — | PASS — from arXiv:2505.24616 |
| POLLUX uses 24,447 expert hours | — | Stream A sec.10.2 | — | PASS — from same paper |
| 3 out of top-10 MERA models are BerryLM variants | structural fact | consensus, Stream A, DD-B | — | PASS — confirmed live via DD-B |

---

## Flagged claims (WARN / FAIL)

| Claim | Value cited | Issue | Severity | Recommendation |
|-------|------------|-------|----------|----------------|
| GigaChat 2 Max MERA score | "~0.67" (A, D) vs "0.683 GigaChat 3 Ultra Preview" (E) | Stream E cites a different model version (GigaChat 3 Ultra, not GigaChat 2 Max) on a more recent snapshot. The consensus flags this but uses both numbers interchangeably in the leaderboard table | WARN | Distinguish versions explicitly: GigaChat 2 MAX ~0.67 (2024 snapshot), GigaChat 3 Ultra Preview 0.683 (later snapshot). Do not combine in one row. |
| GPT-5.2 MERA score | 0.707 (Stream E) vs not present in Stream A leaderboard | Stream A (live June 2026) shows GPT-5.4 at 0.821 in position #5. Stream E reports GPT-5.2 at 0.707 — a different model version on an older snapshot | WARN | Consensus should clarify: Stream A reflects a newer snapshot. GPT-5.2 (0.707) and GPT-5.4 (0.821) are different models. Both numbers plausible but not comparable without flagging snapshot date. |
| GigaChat 3 Ultra Preview MERA | 0.683 in Stream E, absent from Stream A June 2026 top-10 | If current leaderboard (Stream A, DD-B verified June 2026) shows GigaChat absent from top-10, then GigaChat 3 Ultra at 0.683 is now below position 10 on the current leaderboard. Yet consensus still treats 0.683 as a "current" figure | WARN | Note that June 2026 leaderboard shows GigaChat outside top-10; 0.683 may reflect a historical snapshot or the current leaderboard may have changed since E was written. |
| Tokenization multiplier — Russian vs English | "~3x" (Stream A citing Frontiers AI 2025 for Ukrainian), "2x" (cl100k_base per consensus), "7–8x" (Stream E practitioner) | Three inconsistent figures from different sources. The Frontiers AI 2025 data is for Ukrainian, extrapolated to Russian without direct measurement. The consensus acknowledges the variance but the TL;DR says "~2x" without qualification | WARN | Always cite range: 2x (character-level, cl100k_base), 3x (word-level estimate for Ukrainian as proxy), up to 7–8x for specific texts in practitioner tests. Never present as a single figure. The "3x" figure for Russian specifically is NOT from a Russian-language measurement. |
| Inference speedup from Russian tokenizer replacement (LLaMA) | "до 60% ускорение inference" | Source: arXiv:2312.02598. Stream A sec.7 itself flags: "конкретные числа не были получены при прямом обращении к статье." The 60% figure is cited in Stream A sec.4.2 but immediately qualified as not confirmed from the full paper. Vikhr paper is RETRACTED | WARN | The 60% inference speedup is from a paper where only the abstract was accessed, not the full text. The Vikhr arXiv:2405.13929 also references tokenization efficiency but is retracted from ACL. Use as APPROXIMATE estimate only, flagged as unverified. |
| Fine-tuning speedup of 35% from Russian tokenizer | "ускорение fine-tuning на 35%" | Same source (arXiv:2312.02598), same access problem — abstract only was confirmed, not the specific number | WARN | Same as above — cite cautiously or omit specific number. |
| Vikhr 46% token count reduction | "13→7 tokens for typical Russian phrase (46% reduction)" | Vikhr paper retracted from ACL 2024 (cause unknown per Stream A sec.7). Consensus repeats this figure without sufficient caution flag despite noting the retraction | WARN | Must be flagged prominently: data from retracted paper. Should not be cited without noting retraction and unknown reason. |
| Burstiness thresholds for Russian | B<0.30 AI signal, B>0.65 human (Stream C); B<0.35 AI, B>0.55 human (DD-A) | Two different threshold sets are cited. More importantly, ALL threshold data is from a practitioner study on ENGLISH academic text (200 samples), extrapolated to Russian. Source explicitly not peer-reviewed. Consensus labels this Grade D and notes extrapolation, but the numbers appear in the R-HLS framework as if operable | WARN | Thresholds must be labeled: [NOT VALIDATED FOR RUSSIAN. English-only practitioner data, 200 samples, not peer-reviewed]. Cannot be cited as facts. Can only be cited as a starting hypothesis requiring validation on a Russian corpus. |
| Burstiness values — human vs models | Human: σ=8.2 words, B≈0.72; GPT-4o: σ=4.1, B≈0.35; Claude: σ=5.3, B≈0.41 | Source explicitly labeled "[TRAINING DATA + practitioner 200-sample study, English]" in Stream C. DD-A reproduces these figures without the [TRAINING DATA] label in the summary table (sec.3). Consensus repeats them as if empirical | WARN | Label as [ENGLISH ONLY, UNVALIDATED FOR RUSSIAN, TRAINING DATA] wherever cited. Do not present as established facts. |
| Human readers detect AI text at ~90% | "Human readers familiar with AI tools detect AI text at ~90%" | Stream E Finding 8. No source cited for this specific claim. It contradicts the RuATD 2022 finding (66.6%, arXiv:2206.01583, Grade B) which is peer-reviewed. The 90% figure may reflect a self-selected, tool-familiar population with different AI text samples | FAIL | No source. Contradicts peer-reviewed data (RuATD 66.6%). Remove or replace with: "practitioner estimate (unverified)" vs the peer-reviewed 66.6% from RuATD 2022. These two figures are not comparable: different populations, different AI models, different task design. |
| Claude Opus 4.6 blind evaluation score | "8.6/10 vs GPT-5.4's 7.8/10" | Stream E Finding 2, cited as "blind evaluation study." No source, no protocol described, no link, no journal. Grade D at best. | WARN | This is a single-point practitioner finding with no documented protocol. Label as [unsourced practitioner claim, Grade D]. It cannot be presented as evidence without a citation. |
| 60% of professional copywriters work in AI collaboration | "60% of professional copywriters now work in AI collaboration" | Stream E Finding 13. Source described as "survey-style findings from Russian practitioner sources" — no specific survey cited, no methodology | WARN | No source. Must be labeled [UNVERIFIED CLAIM, no cited survey]. |
| DeepSeek API cost — 85% cheaper than GPT-5.2 | "$0.28/$0.42 per million tokens — approximately 85% cheaper than GPT-5.2, 97% cheaper on output" | Stream E Finding 9 cites BenchLM.ai (benchlm.ai/llm-pricing). The ratio depends entirely on the GPT-5.2 price point and pricing at the time of publication. AI pricing changes frequently; no date-stamped screenshot. | WARN | Pricing claims are highly time-sensitive. Flag as [price as of 2026-Q1; subject to change]. Do not present as stable facts. |
| Gemini cost 20 rubles per task, ChatGPT 25, Claude 68 | BotHub comparison (Habr) | Stream E Finding 11. Price comparisons in rubles for API access depend on exchange rate and plan type. No date. | WARN | Same as above — time-sensitive pricing, label accordingly. |
| GigaCheck claimed accuracy | "94.7%" | Stream C table, attributed to Sber/GigaCheck documentation. This is a vendor self-claim, no independent replication. The independent test (AINL-Eval 2025) shows 86.35% on scientific abstracts — a 8+ pp gap. Using vendor figure without noting the independent test lower figure is misleading | WARN | Always pair vendor claim (94.7%) with independent benchmark result (86.35%, AINL-Eval 2025, domain: scientific abstracts). Note domain-specificity of the independent test. |
| GPTZero vendor accuracy claim | "99%" | Stream C table, labeled "vendor claim." Independently benchmarked at 76–85% on English. Russian accuracy unknown. | WARN — already appropriately labeled | The table does label this correctly; however the consensus should note GPTZero Russian accuracy is completely unknown (not merely lower). |
| "68% of popular detectors trained on English give false positives on Russian" | "[TRAINING DATA + vc.ru 2024, верифицировать]" | Stream C sec.5, explicitly marked as unverified. Appears in consensus without flagging. | WARN | Already flagged in stream, but the consensus does not repeat this caveat. Add [unverified] tag in consensus. |
| Non-native speaker false positive rate: 61.3% | Stream C sec.5 | Cites research on TOEFL essays. The 61.3% FP rate is from an English-language study on non-native ENGLISH writing (not Russian writing by non-natives). The leap from "English detector on non-native English" to "Russian detector on formal Russian" is not explicitly justified. | WARN | Clarify: this is FP rate for AI detectors applied to non-native English writers (TOEFL essays), not Russian text. The mechanism is analogous but the specific figure cannot be applied to Russian directly. |
| Qwen3-235B — 9% lower quality but 130x cheaper | Habr 2026, S4 in Stream E | Source cited (habr.com/ru/articles/1021388/), but "9% lower quality" implies a composite score from the LLM-judge methodology described. The metric is model-specific to that experiment's setup ($92 actual cost, $3 final test). Grade D. | WARN | Use as directional evidence only. The "9% lower quality" number is from a single practitioner experiment with LLM-as-judge methodology (specific to educational content generation). Not generalizable to other content types. |
| MERA "67% of tasks are closed format (MCQ/classification)" | Used in consensus TL;DR as established fact | Stream A lists 15 core tasks. DD-B estimates MCQ-dominated tasks. The specific "67%" figure is derived analytically in DD-B (sec.2), not from a cited source. It is an internal calculation by the research agent, not a verified figure from the MERA paper or documentation. | WARN | This is an analytical estimate from DD-B, not a cited external statistic. The consensus treats it as a fact. Label as [analytical estimate based on task structure review in DD-B]. |
| LLaMA+Unigram tokenizer: +3.3 pp on RussianSuperGLUE | From 0.445 → 0.509 | Stream A sec.10.3, attributed to arXiv:2312.02598. However, Stream A also flags this paper as having been accessed only at abstract level, with exact numbers unconfirmed. | WARN | Flag as: numbers from arXiv:2312.02598, abstract only — full-text confirmation not completed. |
| SLAVA leaderboard: YandexGPT 5.1 Pro #2, Alice AI LLM #1 | From "mysummit.school blog" | Stream A sec.5.2 and 2.11. Source is a non-academic blog, no academic publication. | WARN (already labeled "vторичный источник" in Stream A) | The consensus should not cite SLAVA results as established facts. Label as [single secondary source, no academic publication]. |
| MERA saturation prediction: "12–18 months" | METHODOLOGIST review | This is a model-generated prediction from the METHODOLOGIST agent, not from any external source. It is cited in the consensus as if it were evidence. | WARN | Label as [agent prediction, not externally sourced]. RSG saturation timeline (~2 years) is the empirical basis, which IS sourced (arXiv:2202.07791). |

---

## Cross-stream contradictions

### Contradiction 1: GigaChat MERA scores — different models on different snapshots
- **Stream A** (live June 2026): GigaChat absent from top-10. Historical: GigaChat 2 Max ~0.67 (2024), GigaChat-Pro v1 0.537.
- **Stream E** (second pass): "GigaChat 3 Ultra Preview: 0.683" as a current figure.
- **CRITIC review** explicitly flags this as apples-to-oranges.
- **Resolution**: These are different model versions on different leaderboard snapshots. The consensus correctly identifies this issue but still presents GigaChat 3 Ultra 0.683 alongside GigaChat 2 Max 0.67 in the same leaderboard table without distinguishing model version or date. Both figures are plausible but represent different things.

### Contradiction 2: GPT-5.x version confusion
- **Stream A** (live leaderboard): GPT-5.4 at position #5, score 0.821.
- **Stream E** (different snapshot): GPT-5.2 at 0.707.
- These are different models/versions on different snapshots — NOT the same entity. The consensus lists GPT-5.4 in the leaderboard but does not flag that Stream E's figures come from a fundamentally different snapshot.

### Contradiction 3: Burstiness thresholds — two versions in same document
- **Stream C** gives threshold B<0.30 as "strong AI signal" and B>0.65 as "highly likely human."
- **DD-A** proposes B<0.35 as AI signal and B>0.55 as human (for Russian).
- Both versions come from the same underlying practitioner study (English, 200 samples). The consensus does not resolve which threshold set to use. The inconsistency is internal to the research output.

### Contradiction 4: Human AI-detection capability — 66.6% vs ~90%
- **RuATD 2022** (Grade B, peer-reviewed): human annotators detect AI Russian at 66.6% — near random.
- **Stream E Finding 8** (Grade D, no source): "human readers familiar with AI tools detect AI text at ~90%."
- These are directly contradictory and cannot both be true for the same population, same models, same task.
- **Resolution**: Different populations (general annotators vs experienced AI-tool users), different AI models (pre-GPT-4 generators in RuATD vs current models), different task design. But the 90% figure has NO source citation and should be treated as unverified.

### Contradiction 5: Tokenization multiplier — three incompatible figures
- 2x: derived from cl100k_base character-level analysis (multiple sources).
- 3x: from Frontiers AI 2025 study on Ukrainian (not Russian).
- 7–8x: from Stream E practitioner Habr article, specific texts.
- These measure different things (character-level vs word-level, specific texts vs average, Ukrainian vs Russian). The consensus correctly notes variance in the "Active debates" section but the TL;DR states "~2x" as if it were the established figure.

### Contradiction 6: MERA task structure — 67% MCQ claim
- DD-B uses "67% closed format" as a key argument for benchmark gaming risk.
- Stream A describes 15 core tasks, some of which ARE generative (MultiQ, CheGeKa, USE, ruMultiAr, etc.).
- The 67% is an estimate from the research agent's structural analysis, not a number from the MERA paper.
- If generative tasks represent roughly 6 of 15 (40%), then closed format is ~60%, not 67%. The specific figure is not independently verifiable from the files.

---

## Summary

- **Total claims checked:** 68 (46 in PASS table + 22 in WARN/FAIL table)
- **PASS:** 46 — claims that are internally consistent, properly sourced, and corroborated across streams
- **WARN:** 21 — claims that are plausible but either: (a) improperly attributed, (b) lack source, (c) are extrapolated without sufficient flagging, (d) are vendor self-claims, (e) are time-sensitive pricing data, or (f) are agent-generated estimates presented as facts
- **FAIL:** 1 — the "~90% human detection" claim in Stream E Finding 8, which has no source and directly contradicts peer-reviewed data (66.6%, RuATD 2022)
- **Overall fact-check status: CONDITIONAL PASS**

---

## Priority corrections required

**High priority (affects core conclusions):**

1. **FAIL — Stream E Finding 8**: Remove or source the "~90% human detection" claim. Replace with: "Experienced AI-tool users anecdotally report higher detection rates; no peer-reviewed study exists for this population. Peer-reviewed RuATD 2022 data: 66.6% for general annotators on pre-GPT-4 models."

2. **WARN — Burstiness thresholds**: Add explicit warning to ALL uses of B<0.30/0.35 and B>0.55/0.65 thresholds: "These thresholds are extrapolated from an unverified practitioner study on English academic text (200 samples). They have NOT been validated on Russian corpora and should be treated as starting hypotheses, not operational thresholds."

3. **WARN — Vikhr 46% tokenization reduction**: Add retraction notice to all citations: "Data from arXiv:2405.13929, retracted from ACL 2024 (cause unknown). Use with caution."

4. **WARN — 67% MCQ claim**: Replace with: "The majority of MERA core tasks use closed formats (MCQ/classification). Analytical estimate from task structure review: approximately 60% of 15 core tasks are MCQ or classification-based [analytical estimate, not from MERA documentation]."

**Medium priority (affects secondary claims):**

5. Separate GigaChat 2 Max (0.67, 2024 snapshot) from GigaChat 3 Ultra Preview (0.683, different snapshot) throughout all tables.

6. Separate GPT-5.2 (0.707, older snapshot) from GPT-5.4 (0.821, June 2026) throughout.

7. Add [unverified, no cited source] to: the 60% copywriter adoption figure; the 8.6/10 vs 7.8/10 blind evaluation scores.

8. Tokenization multiplier: never cite a single figure. Always use: "2x to 7–8x depending on text type and measurement method; 3x extrapolated from Ukrainian-language study."

**Low priority (metadata and minor issues):**

9. SLAVA leaderboard results: add [single secondary source, no academic publication].

10. MERA saturation 12–18 month prediction: add [agent forecast, not externally sourced].

11. Pricing claims (DeepSeek, Gemini per-task, GigaChat API rates): add [as of 2026-Q1; subject to change].

---

## Notes on source quality distribution

The research correctly uses a tiered grade system. Summary of source grades used in verified claims:
- **Grade A** (peer-reviewed, replicated): RuATD 2022, Russian SuperGLUE heuristics paper, MCQ bias paper, MERA/ACL 2024, RuBLiMP, RuCoLA, TAPE, REPA
- **Grade B** (peer-reviewed, limited replication): RuATD human baseline, AINL-Eval 2025
- **Grade C** (preprints, single papers, live websites): MERA leaderboard data, arXiv:2603.27006 (em-dash), arXiv:2605.19516 (base models), arXiv:2502.15603 (thinks in English), Vikhr (RETRACTED)
- **Grade D** (practitioner sources, Habr/vc.ru): All practitioner comparisons, pricing, task-specific rankings, writing quality assessments

The research correctly labels these grades in the streams. The primary concern is that some Grade D claims appear in the consensus document without their grade label, giving them an appearance of higher authority than they possess.

---

*FACT-CHECKER agent — Swarm Research v3.8 — 2026-06-02*
*Files reviewed: consensus_reference.md, stream_A_benchmarks.md, stream_C_humanness.md, stream_E_practical.md, deep_dive_A_humanness_criteria.md, deep_dive_B_berrylm_gap.md, _critic_review.md (preview)*
*Method: Internal consistency check, cross-stream comparison, source label verification. No WebSearch or WebFetch used.*
