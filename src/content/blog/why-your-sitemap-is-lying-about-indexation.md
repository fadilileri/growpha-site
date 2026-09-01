---
title: "XML Sitemaps Aren't Telling You the Truth | Growpha"
description: "Your sitemap says 10,000 URLs are submitted. Google Search Console tells a different story. Here's how to read the gap and fix indexation at scale."
pubDate: 'Sep 1 2026'
heroImage: '../../assets/blog-placeholder-5.jpg'
category: 'Technical SEO'
keywords: ['xml sitemap seo', 'sitemap indexation issues', 'sitemap vs index coverage']
aiSummary:
  tldr: 'A sitemap listing thousands of submitted URLs says nothing about how many of them Google indexes, and the gap between the two numbers usually points to low-value pages, duplicate content, or crawl budget waste diluting the file. Reading Search Console coverage data by URL segment, rather than as one site-wide percentage, finds exactly which templates are dragging the ratio down. Pruning the sitemap to canonical, genuinely indexable URLs restores trust with Google faster than letting it grow. On large sites, this is the same problem as crawl budget waste seen from a different angle.'
  readingLevel: 'Intermediate'
  keyTakeaways:
    - 'Sitemap submission is not a request to index; Google evaluates each URL separately on quality.'
    - 'Segment the Search Console coverage report by URL template instead of reading one overall percentage.'
    - 'Pages sitting in "Crawled, currently not indexed" reflect a quality judgment, not a crawl delay.'
    - 'Remove noindexed, parameterised, and thin URLs from the sitemap rather than leaving them in.'
    - 'Split large sitemaps by section so a drop in one segment becomes visible without auditing the whole file.'
qualityAssessment:
  - label: 'Topical Depth'
    score: 8
    description: 'Goes beyond "submit a sitemap" advice into the specific mechanics of why sitemap size and indexation rate diverge on large sites.'
  - label: 'E-E-A-T Signals'
    score: 7
    description: 'Reflects hands-on audit experience with segment-level Search Console analysis rather than generic textbook explanation.'
  - label: 'Search Intent Match'
    score: 8
    description: 'Answers the exact question a site owner has when they notice their submitted and indexed counts do not match.'
  - label: 'Content Uniqueness'
    score: 7
    description: 'The segment-by-template auditing process and the framing of sitemap bloat as a crawl budget symptom go past commonly repeated sitemap tips.'
definitions:
  - term: 'XML sitemap'
    definition: 'A file listing the URLs on a site that the owner wants search engines to be aware of, submitted through Search Console or referenced in robots.txt.'
  - term: 'Index coverage report'
    definition: "Google Search Console's report showing which submitted URLs are indexed, excluded, or have errors, broken down by specific reason."
  - term: 'Crawl budget'
    definition: 'The number of pages Googlebot is willing and able to crawl on a given site within a period, limited by server capacity and perceived site value.'
  - term: 'Canonical URL'
    definition: 'The single version of a page that a site designates as the authoritative one when duplicate or near-duplicate versions exist.'
  - term: 'Noindex tag'
    definition: 'A directive telling search engines not to include a specific page in their index, even if the page can be crawled.'
---

A sitemap listing 10,000 submitted URLs looks like proof that a site is in good shape. Open Google Search Console's Pages report next to it and the number staring back is often half that, sometimes less. That gap is not a glitch in the reporting. It is where most indexation problems on large sites take root.

## Submitted is not the same claim as indexed

The sitemap tells Google which URLs exist and roughly how they relate to each other. It does not tell Google to index them. Submission is an invitation to crawl, and Google decides separately whether a crawled page earns a place in the index based on its own quality bar. A site owner who treats "10,000 URLs submitted" as a health metric is measuring the wrong thing: the sitemap counts intent, Search Console's coverage report counts outcome.

## Why a clean sitemap file still doesn't guarantee indexation

The sitemap itself can be technically valid, correct XML syntax, no broken links, and still produce poor indexation if what it contains is the problem. Three causes show up on almost every large-site audit.

Low-value pages inflate the count without adding anything Google wants to rank. Thin category pages, auto-generated location pages, or old blog posts with a paragraph of content sit in the sitemap next to pages that deserve to rank, and Google reads the whole file as a mixed signal rather than a curated list.

Crawl budget waste compounds the problem on sites large enough that Google cannot crawl everything on every visit. If the sitemap is packed with URLs that rarely change or never mattered, Googlebot spends requests confirming pages nobody needed re-crawled, leaving less attention for the pages that genuinely update on a regular basis.

Duplicate and thin content dilutes the sitemap's signal directly. Filtered URL variants, near-identical location pages, or paginated series that all point at the same core content tell Google the file is closer to a full site export than an index-worthy list. Google responds by trusting the whole file less, not just skipping the individual bad URLs.

## Reading the gap in Search Console

Open the Pages report and pull the excluded URL categories rather than the headline number. "Discovered, currently not indexed" and "Crawled, currently not indexed" matter most: the first means Google hasn't gotten to the page yet, the second means Google looked and passed. A sitemap full of URLs sitting in the second bucket points to a quality judgment, not a crawl delay, and no amount of resubmitting changes that outcome.

## Auditing the sitemap-to-index ratio

The process that finds where the gap comes from runs in four steps:

1. Export the full sitemap URL list and the Search Console coverage export for the same period.
2. Segment both by URL pattern or template: blog posts, product pages, category pages, tag pages, location pages, whatever the site's structure produces.
3. Calculate the indexed percentage per segment, not just for the site overall. A site sitting at 70% indexed can still be hiding a single template stuck at 15%.
4. Flag any segment below the site's average as the priority for a content fix or removal from the sitemap.

This segment-level view is what separates "our indexation rate looks fine" from finding out that every location page built for a service area with no real physical presence is dragging the whole ratio down.

## Pruning the sitemap down to what belongs

A sitemap containing only canonical, indexable, genuinely wanted URLs recovers trust with Google faster than one that keeps growing. That means dropping parameterised and filtered variants, removing anything already carrying a noindex tag (listing a noindexed URL in the sitemap sends a contradictory signal), and cutting pages so thin they were never going to earn a place in the index regardless of technical health. Past a few thousand URLs, splitting the sitemap by section makes this an easier ongoing check, since a drop in one segment's indexed rate becomes visible without wading through the entire file.

None of this replaces content quality work. A pruned sitemap does not make a thin page rank on its own. What it does is stop diluting the signal Google reads from every other URL sitting next to it, which is often the difference between a page getting a fair crawl and getting ignored by default.

## Where this connects to crawl budget

On sites with tens of thousands of URLs, sitemap bloat and crawl budget waste are the same problem seen from two angles. A sitemap padded with low-value URLs is, in effect, a request for Google to keep spending crawl attention on pages that will never earn rankings. Fixing the sitemap first is usually the fastest way to find out whether the real issue is indexation or crawl allocation: a clean sitemap that still shows a poor ratio points straight at the deeper crawl budget problem sitting underneath it.
