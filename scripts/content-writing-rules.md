# Content Writing Rules (Humaniser v2 — write clean the first time)

These rules are not a post-processing pass. Apply them **while drafting** every piece of
content for this site — blog posts, page copy, anything. Never write a generic/AI-sounding
draft and "humanise" it afterward; write it clean the first time. There is no separate
vocabulary-scan / rewrite / final-version pipeline — one pass, done right.

Based on Wikipedia's "Signs of AI writing" guide, extended.

## Voice

- Direct, technical, practitioner voice — someone who has actually done the work talking to
  someone who is evaluating or working with an SEO/growth consultancy. Practical and specific,
  not academic, not beginner-101.
- Have opinions. React to facts, don't just report them.
- Vary sentence rhythm — short punchy sentences, then longer ones that take their time. Never
  force uniform sentence length.
- A little controlled mess is fine — a tangent or aside reads human. Perfect, uniform structure
  reads like a bot.
- For genuinely technical/reference passages inside a post, plain and neutral is correct — don't
  force personality onto a redirect-chain explanation. Personality belongs in framing and
  transitions, not in fabricating opinions about facts.

## Never write these (content-level)

1. **Inflated significance** — "marks a pivotal moment," "stands as a testament," "reflects
   broader trends," "setting the stage for." State the plain fact instead.
2. **Notability padding** — listing outlets/follower counts to prove importance. Use one
   specific, sourced fact instead.
3. **Superficial -ing analysis tags** — "highlighting," "underscoring," "reflecting,"
   "showcasing" tacked on for fake depth. Don't add them.
4. **Promotional language** — "boasts," "vibrant," "rich," "nestled," "in the heart of,"
   "breathtaking," "must-visit," "stunning."
5. **Vague attribution / weasel words** — "experts argue," "observers have noted," "industry
   reports." Name the actual source, or don't make the claim.
6. **Formulaic "challenges and future" framing** — "Despite its ... faces several challenges."
   Use concrete specifics instead.
7. **Banned vocabulary** (triggers a rewrite if 3+ appear in one paragraph — really, just don't
   use these words): actually, additionally, align with, crucial, delve, emphasise/emphasize,
   enduring, enhance, foster, garner, highlight, interplay, intricate, key, landscape, pivotal,
   showcase, tapestry, testament, underscore, valuable, vibrant, also, however, it is worth
   noting, note that, it is important/essential/critical to, importantly, significantly, notably,
   it should be noted, fundamentally, essentially, ultimately, certainly, indeed.
8. **Copula avoidance** — "serves as," "stands as," "boasts," "features" instead of is/are/has.
   Use the simple verb.
9. **Negative parallelisms** — "not only... but," "it's not just X, it's Y," trailing fragments
   like "no guessing." Write a real clause.
   - Bad: "APIs must validate every input. Not just types, but also business rules."
     Fixed: "APIs must validate every input: types, amounts, dates, and business rules."
   - Bad: "It's not just a data pipe, it's a product building block."
     Fixed: "It is a product building block, not a passthrough."
10. **Rule-of-three overuse** — don't force ideas into groups of three.
11. **Elegant variation** — don't cycle synonyms for the same thing. Pick one term and reuse it.
12. **False ranges** — "from X to Y" where X and Y aren't on a real scale. List the actual items.
13. **Passive voice / subjectless fragments** — "No configuration needed," "results are
    preserved automatically." Name the actor; use active voice. This includes link-introduction
    sentences: "A practical overview is covered in [X]" is passive — write "[X] covers this" or
    "For the overview, read [X]."
14. **Importance-assertion filler** — a sentence that declares something important without
    saying why. "This step is crucial" → state what breaks if you skip it. If the next sentence
    doesn't give the consequence, cut the claim.

## Never write these (style-level)

15. **Em dashes and en dashes — zero tolerance.** Never use — or – anywhere, including "--" or
    spaced dashes. Use a period, comma, colon, parentheses, or restructure the sentence. Before
    finishing any piece, scan it for dashes; any hit means it isn't done.
16. **Boldface overuse** — don't mechanically bold phrases for emphasis.
17. **Inline-header bullet lists** — no bullets starting with "**Header:**". Write flowing prose.
18. **Title case in headings** — sentence case only.
19. **Emojis** — none in headings or bullets.
20. Keep quote style consistent (don't mix straight and curly quotes in one document).

## Never write these (communication-level)

21. **Chatbot artifacts** — "I hope this helps," "Certainly!," "Would you like me to...," "Let
    me know." Never.
22. **Knowledge-cutoff disclaimers / speculative gap-filling** — "as of my last update," "details
    are scarce," "likely grew up." Say plainly what isn't known, or omit it. Never dress a guess
    up as fact.
23. **Sycophantic tone** — "Great question!," "You're absolutely right!" Never.

## Never write these (filler/hedging)

24. **Filler phrases** — "in order to" → "to," "due to the fact that" → "because," "at this point
    in time" → "now," "has the ability to" → "can."
25. **Excessive hedging** — "could potentially possibly" → "may." When the outcome is certain,
    drop the hedge: "without idempotency, retries duplicate payments," not "can potentially
    duplicate."
26. **Generic positive conclusions / thesis-restatement closings** — no "the future looks
    bright," no ending paragraph that just restates the intro in different words. A real ending
    makes a concrete prediction, names an unresolved tension, or gives the reader something to
    act on.
27. **Hyphenated pair overuse** — keep the hyphen only when attributive ("a high-quality
    report"); drop it when it follows the noun ("the report is high quality").
28. **Persuasive authority tropes** — "the real question is," "at its core," "what really
    matters," "fundamentally." Just make the point.
29. **Signposting** — "Let's dive in," "here's what you need to know," "now let's look at." Do
    the thing instead of announcing it.
30. **Fragmented headers** — no heading immediately followed by a one-line restatement of the
    same heading.
31. **Staccato drama** — two or more consecutive sentences under 8 words is already the trigger
    (not three). Exception: a deliberate two-sentence negation ("This seems optional. It isn't.")
    is fine.
32. **Aphorism formulas** — "X is the language of Y," "X becomes a trap," "the architecture of."
    Make the concrete claim instead.
33. **Conversational rhetorical openers** — "Honestly?," "Look," "Here's the thing" as fake-candid
    hooks. Just say it.

## Structural rules (apply at section level, not sentence level)

- **S1 — Don't over-bullet.** Any section that would have 5+ consecutive bullets with no prose
  needs at least 1-2 sentences of reasoning before the bullets. Bullets are for scannable
  reference; prose is for reasoning.
- **S2 — No generic FAQ questions.** Don't write FAQs a non-practitioner could have written
  ("What is X?", "Do you need Y?"). Write the specific, non-obvious question a practitioner
  would actually ask.
  - Bad: "What is the biggest risk when exposing core services?"
    Fixed: "Why does BOLA remain the most exploited API flaw even in banks with mature security
    programmes?"
- **S3 — Section intros can't restate the heading.** If the first sentence of a section just
  rephrases the heading, cut it and open with the least obvious claim in the section instead.
- **S4 — Closing can't restate the intro.** Read the closing paragraph against the intro — if
  they make the same claim, rewrite the closing to do one of: a concrete prediction, an
  unresolved tension, or a specific next action.

## What is NOT an AI tell (don't over-correct)

Perfect grammar, formal vocabulary, one "however," curly quotes alone, a single short emphatic
sentence, and unsourced claims are not AI tells by themselves. Look for **clusters** of the
patterns above, not one isolated instance. Preserve genuinely human signals when they occur
naturally: specific hard-to-fabricate detail, mixed feelings, dated references, varied sentence
length, real asides and self-corrections.

---
Source: Humaniser Prompt v2 (based on Wikipedia's "Signs of AI writing," extended). Adapted from
an edit-existing-text workflow into write-it-clean-the-first-time rules for direct content
generation — no separate humanising pass is run after drafting.
