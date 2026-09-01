---
title: 'Hreflang Mistakes Splitting Your International Rankings | Growpha'
description: 'Hreflang is one of the most misimplemented tags in SEO. Here are the specific mistakes fragmenting your international search visibility.'
pubDate: 'Sep 1 2026'
heroImage: '../../assets/blog-placeholder-2.jpg'
category: 'International SEO'
keywords: ['hreflang tags', 'hreflang mistakes', 'hreflang implementation guide']
aiSummary:
  tldr: 'Hreflang fails silently rather than throwing errors, and the three most common causes are missing return tags, incorrect language-region codes, and annotations pointing at redirected or non-canonical URLs. Any one of these can make Google discard the entire regional cluster or serve the wrong version to users. Since Search Console no longer has a dedicated hreflang report, validation now depends on crawl-based tools that can cross-reference every tag pair at scale. The return-tag requirement causes more silent failures than any other single mistake.'
  readingLevel: 'Intermediate'
  keyTakeaways:
    - 'Every URL in a hreflang set must link back to every other URL in the set, including itself.'
    - 'A missing return tag breaks the whole relationship for that language pair, not just one direction.'
    - 'Region codes and language codes are different fields; mixing them up produces invalid annotations.'
    - 'Hreflang pointing at a redirected or non-canonical URL gets treated as an unreliable signal.'
    - "Crawl-based hreflang audits now replace Search Console's retired International Targeting report."
qualityAssessment:
  - label: 'Topical Depth'
    score: 8
    description: 'Covers the three specific failure modes in enough technical detail to diagnose them, not just name them.'
  - label: 'E-E-A-T Signals'
    score: 8
    description: 'Correctly notes that Search Console dropped its International Targeting report, which is the kind of current, specific detail generic hreflang content usually gets wrong.'
  - label: 'Search Intent Match'
    score: 9
    description: 'Written for someone actively debugging a hreflang problem, not someone learning what hreflang is for the first time.'
  - label: 'Content Uniqueness'
    score: 7
    description: 'The framing around silent failure and the practical validation workaround go beyond the standard hreflang explainer.'
definitions:
  - term: 'Hreflang'
    definition: 'An HTML attribute that tells search engines which language and regional version of a page to show users, based on their location and language settings.'
  - term: 'Return tag (reciprocal hreflang)'
    definition: 'The requirement that every URL referenced in a hreflang cluster must itself include hreflang annotations pointing back to all the other URLs in that cluster, including itself.'
  - term: 'ISO language-region code'
    definition: 'The two-part code format used in hreflang, combining an ISO 639-1 language code with an optional ISO 3166-1 region code, such as en-GB for English as used in the United Kingdom.'
  - term: 'Canonical tag'
    definition: 'An HTML element specifying which version of a page should be treated as the primary one when duplicate or near-duplicate versions exist.'
  - term: 'International Targeting report'
    definition: "A Search Console report that once surfaced hreflang errors directly; Google retired it, which shifted hreflang validation onto third-party crawling tools."
---

Hreflang looks like three or four lines of markup repeated across a handful of URLs. It's the tag most likely to be implemented wrong across an entire site, and a broken hreflang cluster never throws a visible error. It just stops doing its job while every other signal on the page looks fine.

## The return tag rule that trips up almost everyone

Hreflang works on reciprocity. If a page in the US version references its UK equivalent, that UK page must reference the US version back, and both pages should reference themselves too. Miss the return tag on one side and Google discards the entire relationship for that pair, not just the direction that's broken. This is the single most common cause of hreflang clusters that look complete in the code but do nothing in the SERP, usually because a new regional page got added later without anyone going back to update the older pages that should now point to it.

## Incorrect language-region codes

Hreflang uses a specific code format: a language code, optionally paired with a region code. The mistakes that show up constantly are treating the region field as a country name rather than an ISO code (writing "uk" instead of "gb"), assuming a language code alone implies a region ("en" used for a UK-specific page when the intent was English speakers in the UK specifically), or copying a code from one section of the site into another without checking it matches the actual content. Google validates these strictly. An invalid or ambiguous code doesn't get a best-effort interpretation; it gets ignored.

## Hreflang pointing at redirected or non-canonical URLs

If a hreflang annotation points at a URL that redirects, or at a URL that isn't the canonical version of that page, Google treats the whole annotation as unreliable. This happens often after a site migration or a URL restructure: the hreflang tags get carried over from the old implementation and nobody checks whether the destinations still resolve directly. A hreflang cluster with even one redirecting link in it can lose credibility for the entire set, not just the broken entry.

## What happens when these break

Two outcomes, and both cost visibility. Google can drop the hreflang relationship entirely and treat each regional page as standalone content, which means the US and UK versions of the same page start competing against each other for the same queries instead of Google serving the right one to the right audience. Or Google keeps crawling the pages as separate content but serves the wrong regional version anyway, because without a working hreflang signal it falls back to its own judgment about which page best matches the query and the user's location.

## Validating hreflang without the report Google removed

Search Console used to have a dedicated International Targeting report that surfaced hreflang errors directly. Google retired it, and there's no replacement inside Search Console itself. Validation now runs almost entirely through crawl-based tools, Screaming Frog, Ahrefs' site audit, or Sitebulb, that can pull every hreflang tag on a domain and cross-reference the return-tag requirement automatically across thousands of URLs. Running that crawl and checking specifically for orphaned annotations, one-way references, and hreflang targets that return a redirect status code catches the majority of real-world breakages before they show up as ranking confusion.

## The rule worth checking first

Of the three mistakes here, the missing return tag causes the most damage relative to how easy it is to introduce. A single new regional page launched without updating the rest of the cluster can quietly undo hreflang across a site that had it working correctly for years. Any hreflang audit should start there before touching codes or canonical alignment, because fixing return tags alone resolves a large share of hreflang problems on sites that have been expanding into new markets over time.
