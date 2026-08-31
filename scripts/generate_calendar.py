import csv

# Each row: Day, Order, Title, Pillar, MainKeyword, Volume, Secondary1, Secondary2, MetaTitle, MetaDescription, Slug, ContentBrief
rows = []

def add(day, order, title, pillar, kw, vol, sec1, sec2, mt, md, slug, brief):
    rows.append([day, order, title, pillar, kw, vol, sec1, sec2, mt, md, slug, brief])

# ---- Technical SEO (T1-T15) ----
add(1,1,"Why Your Sitemap Is Lying About What Google Actually Indexes","Technical SEO","xml sitemap seo",50,"sitemap indexation issues","sitemap vs index coverage",
    "XML Sitemaps Aren't Telling You the Truth | Growpha",
    "Your sitemap says 10,000 URLs are submitted. Google Search Console tells a different story. Here's how to read the gap and fix indexation at scale.",
    "why-your-sitemap-is-lying-about-indexation",
    "Explain the gap between 'submitted' and 'indexed' URLs in Search Console and why a clean sitemap does not guarantee indexation. Cover the real causes: low-value pages, crawl budget waste, and duplicate/thin content diluting the sitemap's signal. Give a practical process for auditing sitemap-to-index ratio and pruning it to only canonical, indexable URLs. Close with how this connects to crawl budget on larger sites.")

add(3,2,"The Canonicalization Mistakes That Split Your Ranking Signals in Half","Technical SEO","canonical tag seo",1300,"canonical tag mistakes","self-referencing canonical",
    "Canonicalization Mistakes Splitting Your Rankings | Growpha",
    "Conflicting canonical tags quietly split ranking signals across duplicate URLs. Here are the specific mistakes that cause it and how to fix them.",
    "canonicalization-mistakes-splitting-ranking-signals",
    "Walk through the most common canonical tag errors: parameter URLs without canonicals, cross-domain canonical misuse, and canonicals that point to non-indexable pages. Explain concretely how each mistake causes Google to split authority across multiple URL variants instead of consolidating it. Give a step-by-step canonical audit process using Screaming Frog and Search Console's coverage report. End with the fix priority order for a technical SEO engagement.")

add(5,3,"Log File Analysis: What Googlebot Is Actually Doing on Your Site","Technical SEO","log file analysis seo",390,"googlebot crawl behavior","server log seo audit",
    "Log File Analysis: What Googlebot Really Crawls | Growpha",
    "Analytics tools show visitor behavior. Log files show Googlebot's. Here's how to read raw server logs to find crawl waste and indexation blockers.",
    "log-file-analysis-what-googlebot-is-doing",
    "Explain why log file analysis reveals things Search Console and crawlers cannot: actual crawl frequency, wasted crawl budget on low-value URLs, and status codes Googlebot is really seeing. Describe a practical workflow for pulling and segmenting log files (by user-agent, status code, and URL pattern) at scale. Give 2-3 concrete patterns to look for, such as crawl spent on parameter URLs or old redirect chains. Close with how this informs a technical SEO roadmap.")

add(7,4,"Faceted Navigation Is Quietly Destroying Your Crawl Budget","Technical SEO","faceted navigation seo",1600,"faceted navigation crawl budget","filter urls seo",
    "Faceted Navigation Is Destroying Your Crawl Budget | Growpha",
    "Every filter combination on an e-commerce site creates a new crawlable URL. Here's how faceted navigation quietly wastes crawl budget at scale.",
    "faceted-navigation-crawl-budget-problem",
    "Explain how faceted/filtered navigation on e-commerce and marketplace sites generates near-infinite URL combinations that Googlebot tries to crawl. Cover the resulting symptoms: wasted crawl budget, duplicate/thin content, and diluted ranking signals across near-identical pages. Give the standard toolkit for controlling it — robots.txt disallow rules, canonical tags, parameter handling, and selective indexation of high-value facet combinations. Close with how to prioritise which facets deserve to be indexable at all.")

add(9,5,"JavaScript Rendering and SEO: What Actually Breaks in Production","Technical SEO","javascript seo",3600,"javascript rendering seo issues","client side rendering seo",
    "JavaScript SEO: What Actually Breaks in Production | Growpha",
    "JS frameworks look fine in a browser but can be invisible to search engines. Here's what actually breaks in production JavaScript SEO.",
    "javascript-rendering-seo-what-breaks-in-production",
    "Cover the real-world JavaScript SEO failure patterns: content that only renders after a client-side fetch, internal links built with onClick handlers instead of anchor tags, and render-blocking scripts delaying Googlebot's rendering pass. Explain how to diagnose these using the URL Inspection tool's rendered HTML versus raw HTML. Recommend concrete fixes: server-side rendering, dynamic rendering, or hybrid rendering depending on the framework. Close with how this connects to Core Web Vitals and INP.")

add(12,1,"The Redirect Chains Costing You Rankings You Don't Know About","Technical SEO","redirect chains seo",20,"redirect chain audit","301 redirect best practices",
    "Redirect Chains That Are Quietly Costing You Rankings | Growpha",
    "Multiple 301 hops between the old URL and the final destination bleed link equity and slow crawling. Here's how to find and fix redirect chains.",
    "redirect-chains-costing-you-rankings",
    "Explain how redirect chains form over time — through repeated site migrations, URL restructures, and CMS changes stacking on top of each other. Cover the concrete cost: diluted link equity per hop, slower page load for users, and wasted crawl budget for Googlebot. Give a practical method for auditing chains at scale with Screaming Frog's redirect chain report. End with the fix: always redirect straight to the final destination, never chain.")

add(14,2,"Why Your Structured Data Passes Validation But Still Doesn't Show Rich Results","Technical SEO","rich results not showing",260,"schema markup not working","google rich results troubleshooting",
    "Structured Data Valid But No Rich Results? Here's Why | Growpha",
    "Your schema passes the Rich Results Test but nothing shows in the SERP. Here are the real reasons valid structured data still doesn't display.",
    "structured-data-valid-no-rich-results",
    "Explain the gap between 'technically valid' schema and Google actually choosing to display it — eligibility is not a guarantee. Cover the common real causes: missing required vs recommended fields, content on the page not matching the marked-up data, manual actions, or the feature simply being deprecated for that content type. Give a troubleshooting checklist using Search Console's Enhancement reports rather than just the validator. Close with realistic expectations for how long rich results take to appear after a fix.")

add(16,3,"Site Migrations: The 12-Point Checklist That Prevents Traffic Collapse","Technical SEO","website migration seo checklist",1300,"site migration seo checklist","domain migration traffic loss",
    "Site Migration SEO Checklist: 12 Points to Prevent Traffic Loss | Growpha",
    "Most migration traffic collapses are preventable. Here is the 12-point technical SEO checklist Growpha runs before, during, and after every migration.",
    "site-migration-seo-checklist-12-points",
    "Structure the post around a genuine pre-migration, during-migration, and post-migration checklist — not a generic listicle. Cover URL mapping and 1:1 redirects, canonical and hreflang preservation, XML sitemap updates, and a content parity audit before launch. Include the post-launch monitoring window: daily Search Console coverage checks and crawl stats for the first two weeks. Close with the most common cause of migration traffic collapse Growpha sees: incomplete redirect mapping.")

add(18,4,"INP Is the Metric Killing Your Rankings — Here's What Actually Fixes It","Technical SEO","inp core web vitals",50,"interaction to next paint fix","inp optimization",
    "INP Is Killing Your Rankings — Here's the Actual Fix | Growpha",
    "INP replaced FID as a Core Web Vital and most sites are quietly failing it. Here's what actually improves Interaction to Next Paint scores.",
    "inp-core-web-vitals-actual-fix",
    "Explain what INP measures differently from FID — full interaction latency, not just first input delay — and why that makes it harder to pass. Cover the real culprits: heavy third-party scripts, long JavaScript main-thread tasks, and unoptimised event handlers. Give concrete fixes: code splitting, deferring non-critical scripts, and debouncing expensive interactions. Close with how to measure INP in the field using CrUX rather than lab tools alone.")

add(20,5,"Orphan Pages: The Silent Indexation Killer Most Audits Miss","Technical SEO","orphan pages seo",390,"orphan page audit","internal linking orphan pages",
    "Orphan Pages: The Indexation Killer Most Audits Miss | Growpha",
    "A page with no internal links pointing to it is invisible to both users and Googlebot. Here's how to find and fix orphan pages at scale.",
    "orphan-pages-silent-indexation-killer",
    "Define orphan pages precisely — pages that exist and may even be in the sitemap, but have zero internal links pointing to them — and explain why that starves them of both crawl priority and ranking signal. Cover how orphan pages accumulate over time: content migrations, CMS restructures, and abandoned campaign landing pages. Give a practical detection method combining a full site crawl against the XML sitemap and internal link graph. Close with the fix: either link them into the site architecture deliberately or remove them.")

add(23,1,"Why \"Crawled — Currently Not Indexed\" Is the Warning Sign You're Ignoring","Technical SEO","crawled currently not indexed",720,"google search console indexing issues","pages not indexed fix",
    "Crawled - Currently Not Indexed: What It Really Means | Growpha",
    "This Search Console status isn't random. It's Google telling you your content isn't good enough to index. Here's how to actually fix it.",
    "crawled-currently-not-indexed-fix",
    "Explain what this specific Search Console status genuinely signals — Google chose not to index the page after crawling it, usually a quality or duplication judgement, not a technical error. Cover the most common real causes: thin or duplicate content, low-value programmatic pages, and pages that don't meaningfully differ from similar ones on the site. Give a triage method for deciding which affected URLs are worth improving versus noindexing outright. Close with realistic timelines for recovery once fixes are made.")

add(25,2,"Pagination and SEO: The Rel=Next/Prev Myth and What Actually Works","Technical SEO","pagination seo",1900,"rel next prev deprecated","paginated content seo best practices",
    "Pagination SEO in 2026: What Actually Works Now | Growpha",
    "rel=next/prev was deprecated by Google years ago but the myth persists. Here's how to actually handle paginated series for SEO today.",
    "pagination-seo-what-actually-works",
    "Clarify upfront that Google stopped using rel=next/prev as a ranking signal, and that many sites still implement it under a false belief it helps. Explain what Google actually relies on now: internal linking structure, self-referencing canonicals per page, and content-based judgement of the series. Give practical guidance for category and blog pagination specifically, including when to consolidate versus paginate. Close with how this applies differently to e-commerce category pages versus blog archives.")

add(27,3,"How Duplicate Content Actually Gets Penalized (And How It Doesn't)","Technical SEO","duplicate content penalty",480,"duplicate content myth","google duplicate content filter",
    "How Duplicate Content Actually Gets Penalized | Growpha",
    "There is no 'duplicate content penalty' in the way most people think. Here's what Google actually does with duplicate content, and what really hurts you.",
    "duplicate-content-penalty-myth-explained",
    "Correct the common misconception of an algorithmic 'duplicate content penalty' — explain that Google typically filters/consolidates rather than penalises, choosing one version to show. Cover the situations where duplicate content genuinely does cause harm: diluted ranking signals across near-identical pages competing with each other, and syndicated content outranking the original. Give the real fix toolkit: canonicalization, 301s, and consolidating thin variants. Close with the one scenario that IS treated as a manual action: large-scale scraped or auto-generated duplicate content.")

add(29,4,"The Robots.txt Mistakes That Are Blocking Your Own Rankings","Technical SEO","robots.txt seo",260,"robots.txt mistakes","blocked by robots.txt fix",
    "Robots.txt Mistakes Quietly Blocking Your Own Rankings | Growpha",
    "A single misplaced Disallow rule can deindex an entire site section. Here are the robots.txt mistakes Growpha finds most often in technical audits.",
    "robots-txt-mistakes-blocking-rankings",
    "Cover the most damaging real-world robots.txt mistakes: accidentally blocking CSS/JS Google needs to render pages, disallowing entire directories that contain valuable content, and confusing 'noindex' intent with a Disallow rule (which actually prevents Google from seeing a noindex tag at all). Explain the specific failure mode where blocking a page in robots.txt causes it to still appear in search results without a snippet, confusing site owners. Give a quick audit method using Search Console's robots.txt tester. Close with the rule of thumb: block only what truly should never be crawled.")

add(30,5,"Core Web Vitals for Single Page Applications: The Fixes Standard Advice Misses","Technical SEO","core web vitals spa",0,"spa core web vitals fix","react vue core web vitals",
    "Core Web Vitals for SPAs: What Standard Advice Misses | Growpha",
    "Generic Core Web Vitals advice breaks down for React, Vue, and Angular apps. Here's what actually needs to change for single-page applications.",
    "core-web-vitals-single-page-applications",
    "Explain why standard Core Web Vitals guidance (written for traditional multi-page sites) often doesn't map cleanly to SPAs, where client-side routing changes what 'page load' even means. Cover the SPA-specific issues: LCP measured against the wrong element after a route change, INP degrading from heavy client-side re-renders, and CLS from lazy-loaded components. Give framework-aware fixes for React/Vue/Angular specifically. Close with how to correctly instrument CWV tracking for client-side navigation.")

# ---- International SEO (I1-I13) ----
add(1,2,"Hreflang Mistakes That Are Splitting Your International Rankings","International SEO","hreflang tags",4400,"hreflang mistakes","hreflang implementation guide",
    "Hreflang Mistakes Splitting Your International Rankings | Growpha",
    "Hreflang is one of the most misimplemented tags in SEO. Here are the specific mistakes fragmenting your international search visibility.",
    "hreflang-mistakes-international-rankings",
    "Cover the most common hreflang implementation errors: missing return tags, incorrect language-region codes, and hreflang pointing to non-canonical or redirected URLs. Explain concretely how each mistake causes Google to either ignore the hreflang cluster entirely or serve the wrong regional version to users. Give a validation method using Search Console's International Targeting report and a crawl-based hreflang audit. Close with the return-tag rule that trips up the most sites.")

add(3,3,"Expanding Into the GCC: The International SEO Checklist for New Markets","International SEO","international seo",6600,"gcc market expansion seo","new market seo checklist",
    "GCC Market Expansion: The International SEO Checklist | Growpha",
    "Expanding into the GCC needs more than translated pages. Here's the international SEO checklist Growpha runs for businesses entering new markets.",
    "gcc-expansion-international-seo-checklist",
    "Lay out a genuine pre-launch checklist for expanding an existing site into GCC markets: site architecture decision (subdirectory vs subdomain vs ccTLD), hreflang setup, market-specific keyword research rather than translated keywords, and local business signals. Cover the common mistake of treating Arabic markets as a single audience when Saudi, UAE, and Egypt search behaviour genuinely differ. Include a note on right-to-left (RTL) technical considerations. Close with a realistic timeline for a new-market SEO ramp.")

add(5,4,"ccTLD vs Subdirectory vs Subdomain: The Real Decision Framework for MENA Expansion","International SEO","cctld vs subdomain seo",0,"international site structure decision","mena market seo architecture",
    "ccTLD vs Subdirectory vs Subdomain for MENA Expansion | Growpha",
    "The ccTLD vs subdirectory vs subdomain decision shapes your international SEO for years. Here's the actual framework for choosing, for MENA expansion specifically.",
    "cctld-subdirectory-subdomain-mena-expansion",
    "Present the three structural options plainly with their real SEO trade-offs: ccTLDs signal the strongest local relevance but split domain authority and cost more to maintain; subdirectories consolidate authority but can dilute local trust signals; subdomains sit in between. Apply this specifically to MENA expansion, where local trust signals (a .ae or .sa domain) can matter more than in some other regions. Give a decision framework based on company size, number of markets, and resourcing for ongoing content. Close with what Growpha actually recommends for most mid-size UAE-based businesses expanding regionally.")

add(7,5,"Why Your Arabic-Language Site Isn't Ranking (It's Not the Translation)","International SEO","arabic seo",320,"arabic language seo","arabic keyword research",
    "Why Your Arabic Site Isn't Ranking (Hint: It's Not the Translation) | Growpha",
    "A grammatically perfect Arabic translation still fails to rank if the underlying SEO strategy is wrong. Here's what's actually holding Arabic sites back.",
    "why-arabic-site-isnt-ranking",
    "Challenge the common assumption that Arabic SEO underperformance is a translation quality problem. Cover the real, more common causes: keyword research done in English and then translated (missing how Arabic speakers actually phrase queries), dialectal variation between Gulf, Levantine, and Egyptian Arabic search behaviour, and RTL technical rendering issues affecting crawlability. Give a practical fix: native Arabic keyword research tools and dialect-aware content briefs. Close with why machine-translated content specifically underperforms for E-E-A-T signals.")

add(10,1,"Geotargeting in Search Console: What It Actually Controls","International SEO","geotargeting search console",0,"international targeting settings","country geotargeting seo",
    "Geotargeting in Search Console: What It Actually Controls | Growpha",
    "Search Console's International Targeting setting doesn't do what most people think. Here's exactly what geotargeting controls and doesn't.",
    "geotargeting-search-console-explained",
    "Correct the common misunderstanding that geotargeting settings meaningfully boost rankings in a target country the way ccTLDs or hreflang do. Explain precisely what it does control: it's a signal used specifically for generic top-level domains (.com) without other strong location signals, and has no effect at all on ccTLD sites. Cover when it's actually useful versus when hreflang or ccTLD choice already makes it redundant. Close with the more reliable geotargeting signals Google weighs more heavily: hreflang, local backlinks, and local business schema.")

add(12,2,"International Site Architecture: Structuring for Multiple GCC Markets","International SEO","international site structure",0,"multi country site architecture","gcc site structure seo",
    "International Site Architecture for Multiple GCC Markets | Growpha",
    "Structuring one site for UAE, Saudi, and wider GCC markets requires deliberate architecture decisions. Here's how Growpha approaches it.",
    "international-site-architecture-gcc-markets",
    "Cover the architectural decisions needed when a single business targets multiple GCC countries with genuinely different market conditions: URL structure per country, shared versus country-specific content, and how much localisation (pricing, currency, local case studies) each market needs versus shared core content. Explain the internal linking implications of a multi-market structure and how it affects crawl budget. Give a practical example structure for a UAE-headquartered business expanding to Saudi Arabia and Qatar. Close with the maintenance overhead trade-off businesses need to plan for.")

add(14,3,"The Currency and Language Signals Google Actually Uses for Local Intent","International SEO","international seo signals",0,"currency signals seo","local intent international seo",
    "The Currency and Language Signals Google Uses for Local Intent | Growpha",
    "Beyond hreflang, Google reads currency, language, and content signals to judge local relevance. Here's what actually moves the needle.",
    "currency-language-signals-local-intent-seo",
    "Explain the secondary signals Google uses alongside hreflang to judge whether a page genuinely serves a local market: displayed currency, local phone number formats, local business schema, and content that references local context (regulations, local competitors, local case studies) rather than generic global copy. Give examples of how a UAE-targeted page should differ from a generic English page beyond just language. Close with why these signals matter more as hreflang implementations become more common and less differentiating on their own.")

add(16,4,"Duplicate Content Across International Sites: When It's Actually a Problem","International SEO","duplicate content international seo",0,"international duplicate content hreflang","multi region duplicate content",
    "Duplicate Content Across International Sites: The Real Risk | Growpha",
    "Near-identical content across country versions of a site is normal, not a penalty risk, when hreflang is implemented correctly. Here's when it actually is a problem.",
    "duplicate-content-international-sites-when-problem",
    "Reassure upfront that hreflang exists precisely to handle near-duplicate content across language/country versions, and Google does not penalise this when implemented correctly. Cover the genuine risk scenario: when hreflang is broken or missing and Google has to independently judge multiple near-identical pages as competing duplicates. Give the diagnostic method for telling the two situations apart in Search Console. Close with the fix priority: hreflang correctness first, content differentiation second.")

add(18,5,"Localization vs Translation: Why Machine-Translated Content Fails in Arabic Markets","International SEO","website localization vs translation",50,"machine translation seo problems","arabic content localization",
    "Localization vs Translation: Why Machine Translation Fails | Growpha",
    "Machine-translated Arabic content technically works but rarely ranks or converts. Here's the real difference localization makes.",
    "localization-vs-translation-arabic-markets",
    "Define the distinction clearly: translation converts words, localization adapts the message, tone, examples, and search intent to the target market. Cover the specific ways machine-translated Arabic content fails: awkward phrasing that signals low quality to both users and E-E-A-T evaluation, missed cultural context, and keyword targeting based on literal translation rather than how people actually search. Give examples of localization done right for GCC markets specifically. Close with when machine translation is acceptable as a first draft versus when it actively hurts a brand's authority.")

add(21,1,"Cross-Border Link Building: Earning Authority in a New Regional Market","International SEO","international link building",390,"cross border backlinks","regional authority building",
    "Cross-Border Link Building for New Regional Markets | Growpha",
    "Domain authority from one market doesn't automatically transfer to a new region. Here's how to build genuine link authority when expanding cross-border.",
    "cross-border-link-building-new-market",
    "Explain why global domain authority doesn't automatically confer local trust or rankings when entering a genuinely new regional market like the GCC. Cover practical tactics for earning regional links: local press and digital PR, local business directories and associations, and partnerships with regionally established sites. Address the common mistake of applying a Western link-building playbook (generic guest posts) without adapting for local publisher and audience norms. Close with realistic timelines for building enough regional authority to compete with local incumbents.")

add(23,2,"hreflang Return Tags: The Silent Error Breaking Your International SEO","International SEO","hreflang return tags",90,"hreflang reciprocal tags","hreflang error validation",
    "hreflang Return Tags: The Silent Error Breaking Your SEO | Growpha",
    "A hreflang tag without a matching reciprocal tag on the target page gets ignored by Google entirely. Here's how to find and fix return tag errors.",
    "hreflang-return-tags-silent-error",
    "Explain the return tag requirement precisely: if Page A hreflang-links to Page B, Page B must reciprocally link back to Page A, or Google discards the entire cluster's hreflang signal. Cover why this is such a common, silent failure — it often breaks after partial site updates or CMS migrations where only some pages get updated. Give a crawl-based method for auditing return tags at scale rather than checking manually. Close with the Search Console report that surfaces this specific error.")

add(25,3,"Multi-Regional Keyword Research: Why Search Intent Changes Across the GCC","International SEO","multi regional keyword research",0,"gcc keyword research differences","regional search intent",
    "Multi-Regional Keyword Research Across the GCC | Growpha",
    "The same product gets searched differently in Dubai, Riyadh, and Doha. Here's how search intent shifts across GCC markets and how to research it properly.",
    "multi-regional-keyword-research-gcc",
    "Give concrete examples of how search terminology and intent shift across UAE, Saudi Arabia, and Qatar for the same underlying product or service category. Explain why running one keyword list translated across markets misses this and undercounts real opportunity. Cover a practical research method: market-specific keyword tools, competitor analysis per country, and validating volume per regional Semrush/Google Ads database rather than assuming shared search behaviour. Close with how this should reshape content planning for a genuinely multi-market GCC strategy.")

add(27,4,"International SEO Audits: The Region-Specific Checks Generic Audits Miss","International SEO","international seo audit",1300,"multi country seo audit","hreflang audit checklist",
    "International SEO Audits: What Generic Audits Miss | Growpha",
    "A standard technical SEO audit doesn't catch international-specific issues. Here's what a proper multi-market audit needs to check.",
    "international-seo-audit-region-specific-checks",
    "Contrast a standard single-market technical audit with what an international audit specifically needs to add: hreflang implementation and return tag validation, per-region indexation checks, geotargeting configuration, and content parity/localisation quality across markets. Give a checklist structure an auditor should follow region by region, not just site-wide. Close with the most common finding Growpha sees in international audits: hreflang implemented but silently broken for months.")

# ---- Local SEO (L1-L14) ----
add(1,3,"Google Business Profile Optimisation for Dubai Free Zone Businesses","Local SEO","google business profile optimization",3600,"gbp optimization dubai","free zone business local seo",
    "Google Business Profile Optimisation for Dubai Free Zones | Growpha",
    "Free zone businesses face specific GBP verification and category challenges. Here's how to optimise a Google Business Profile properly in Dubai.",
    "google-business-profile-dubai-free-zone",
    "Cover the specific challenges free zone businesses face with Google Business Profile: verification difficulties tied to virtual or shared office addresses, category selection for services that don't map cleanly to Google's taxonomy, and building enough proximity/relevance signal despite non-traditional premises. Give a practical optimisation checklist: category selection, service area configuration, photos, and review generation cadence. Close with how this connects to the wider local pack ranking factors for Dubai specifically.")

add(3,4,"Why Local Pack Rankings in Dubai Are Different From Anywhere Else","Local SEO","local pack seo",1000,"dubai local pack rankings","local seo ranking factors",
    "Why Dubai's Local Pack Rankings Work Differently | Growpha",
    "Standard local pack advice doesn't fully apply in Dubai's dense, multi-language, free-zone-heavy market. Here's what's actually different.",
    "dubai-local-pack-rankings-different",
    "Explain the structural factors that make Dubai's local pack landscape distinct: extremely high business density in small geographic areas (Business Bay, JLT, DIFC), free zone address ambiguity affecting proximity signals, and a bilingual Arabic/English search population searching the same query differently. Cover how this changes local SEO priorities compared to a typical Western city. Give practical adaptations: hyperlocal content by district rather than just 'Dubai', and citation consistency across both English and Arabic business listings. Close with a realistic view of how competitive Dubai local pack rankings have become.")

add(5,5,"The UAE Business Directory Citations That Actually Move Local Rankings","Local SEO","local citations seo",2900,"uae business directories","nap citation building",
    "UAE Business Directories That Actually Move Local Rankings | Growpha",
    "Not all citation directories carry equal weight. Here are the UAE-specific directories worth prioritising for local SEO, and which ones don't matter.",
    "uae-business-directories-local-rankings",
    "Give a realistic, prioritised view of which UAE and regional business directories genuinely contribute to local SEO versus which are low-value citation farms. Cover the importance of NAP (name, address, phone) consistency across whichever directories are chosen. Explain why quality and consistency matter more than citation volume for local ranking signals. Close with a practical sequencing: government/official directories and industry associations first, generic directories second.")

add(8,1,"Local SEO for Multi-Location UAE Retailers: The Architecture That Works","Local SEO","multi location seo",1900,"multi location retailer seo","location page architecture",
    "Local SEO for Multi-Location UAE Retailers | Growpha",
    "Retailers with multiple UAE locations need dedicated location page architecture, not one generic contact page. Here's the structure that works.",
    "multi-location-seo-uae-retailers",
    "Explain why a single generic 'locations' page fails multi-branch retailers and what a proper location page architecture looks like instead: one unique, substantive page per branch with local content, not templated boilerplate. Cover Google Business Profile management at scale across multiple branches and the risk of duplicate/thin location pages competing with each other. Give a practical framework for how much unique content each location page genuinely needs. Close with how this scales for retailers with 10+ UAE locations.")

add(10,2,"Review Generation Strategy for UAE Service Businesses","Local SEO","review generation strategy",110,"google review generation uae","customer review strategy",
    "Review Generation Strategy for UAE Service Businesses | Growpha",
    "Reviews are one of the strongest local ranking signals, but most UAE service businesses have no deliberate strategy for generating them. Here's one.",
    "review-generation-strategy-uae-service-businesses",
    "Explain why review volume and recency are a meaningfully weighted local ranking factor, and why most service businesses leave review generation to chance. Give a practical, compliant strategy: timing the ask right after service completion, SMS/WhatsApp-based review requests (relevant for UAE consumer behaviour), and responding to every review to signal active management. Address what NOT to do — incentivised or fake reviews — and the real risk of Google removing them. Close with a realistic monthly review-generation cadence to aim for.")

add(12,3,"NAP Consistency Audits: The UAE-Specific Pitfalls","Local SEO","nap consistency",590,"nap consistency audit","business listing consistency",
    "NAP Consistency Audits: UAE-Specific Pitfalls | Growpha",
    "Name, address, and phone inconsistency quietly undermines local rankings. Here are the specific NAP pitfalls UAE businesses run into.",
    "nap-consistency-audit-uae-pitfalls",
    "Explain why NAP (name, address, phone) consistency across the web is a foundational local trust signal Google cross-references. Cover UAE-specific pitfalls: address format inconsistency (building/floor/office numbering conventions vary across listings), phone number formatting with and without the country code, and business name variations across free zone registration versus trading name. Give a practical audit method for finding inconsistencies across major directories. Close with a maintenance process for keeping NAP consistent after data is cleaned up once.")

add(14,4,"Local Content Strategy for DIFC, JLT, and Business Bay Service Providers","Local SEO","local content strategy",50,"difc business content marketing","hyperlocal content dubai",
    "Local Content Strategy for DIFC, JLT, and Business Bay | Growpha",
    "Generic Dubai content doesn't differentiate a DIFC law firm from a Business Bay consultancy. Here's how to build genuinely hyperlocal content.",
    "local-content-strategy-difc-jlt-business-bay",
    "Explain why generic 'Dubai' content fails to differentiate businesses competing within specific business districts that have their own client profiles and competitive sets. Give a hyperlocal content framework: district-specific case studies, references to local business ecosystems (DIFC's financial services focus, JLT's SME density, Business Bay's mixed-use profile), and location-specific service pages where relevant. Cover how this supports both local pack rankings and genuine relevance to the target audience. Close with a caution against over-optimising to the point of sounding unnatural.")

add(16,5,"Why \"Near Me\" Searches Behave Differently in Dubai Than in Western Markets","Local SEO","near me searches",70,"near me search behavior dubai","mobile local search uae",
    "Why 'Near Me' Searches Behave Differently in Dubai | Growpha",
    "Dubai's car-dependent geography and district-based living change how 'near me' search behaviour actually works compared to Western cities.",
    "near-me-searches-dubai-different",
    "Explain how Dubai's urban geography — car-dependent, district-clustered, with significant distances between residential and business areas — changes what 'near me' actually means to a searcher compared to a walkable Western city. Cover the practical implication: a wider realistic service radius and different proximity weighting expectations for local businesses. Give guidance on how businesses should configure service areas and content accordingly. Close with how this affects local pack competition analysis.")

add(19,1,"Google Maps Ranking Factors for UAE Businesses in 2026","Local SEO","google maps ranking factors",140,"google maps seo uae","maps ranking 2026",
    "Google Maps Ranking Factors for UAE Businesses in 2026 | Growpha",
    "Google Maps rankings weigh proximity, relevance, and prominence differently than organic search. Here's what actually moves the needle for UAE businesses.",
    "google-maps-ranking-factors-uae-2026",
    "Break down Google's three stated local ranking pillars — relevance, distance, and prominence — and translate each into concrete, current actions for a UAE business. Cover prominence specifically: review signals, citation consistency, and off-site mentions matter more here than most businesses realise. Address common misconceptions, like assuming website SEO alone drives Maps rankings. Close with the realistic weighting businesses should give Maps optimisation versus organic website SEO in a combined local strategy.")

add(21,2,"Local Link Building for GCC Businesses: Where the Real Authority Comes From","Local SEO","local link building",2400,"gcc local link building","regional authority signals",
    "Local Link Building for GCC Businesses | Growpha",
    "Generic link building tactics underperform for local GCC authority. Here's where real local link equity actually comes from in this market.",
    "local-link-building-gcc-businesses",
    "Explain why generic global link building tactics (broad guest posting, resource pages) underperform for building local trust in GCC markets specifically. Cover the sources that actually carry local weight: chamber of commerce and trade association listings, regional business press coverage, and partnerships with other established local businesses. Give a practical prioritisation for a business with limited link-building budget. Close with how local link building complements, rather than replaces, Google Business Profile signals.")

add(23,3,"Free Zone vs Mainland: Does Your Business Structure Affect Local SEO?","Local SEO","free zone vs mainland uae",10,"uae business structure seo","mainland license local seo",
    "Free Zone vs Mainland: Does Business Structure Affect SEO? | Growpha",
    "Free zone and mainland UAE company structures have real, practical implications for local SEO — not because Google cares about licensing, but because of what follows from it.",
    "free-zone-vs-mainland-local-seo-uae",
    "Clarify upfront that Google's algorithm has no awareness of free zone versus mainland licensing status directly. Then explain the indirect but real effects: free zone address types affecting Google Business Profile verification, mainland businesses' ability to serve all of the UAE affecting service-area configuration, and how this shapes local pack eligibility for certain business categories. Give practical guidance for businesses navigating GBP setup under each structure. Close with when this distinction genuinely matters for a local SEO strategy versus when it's a non-issue.")

add(25,4,"Multi-Language Local SEO: Arabic and English on the Same GMB Profile","Local SEO","multilingual seo",2900,"bilingual google business profile","arabic english gbp",
    "Multi-Language Local SEO: Arabic and English on One GBP | Growpha",
    "Running a single Google Business Profile in both Arabic and English requires deliberate decisions. Here's how to do it without diluting either signal.",
    "multi-language-local-seo-arabic-english-gbp",
    "Explain the practical mechanics of managing a bilingual Google Business Profile: business name conventions, description language choices, and how Google surfaces different profile languages to different searchers. Cover the common mistake of neglecting the Arabic side of a profile entirely, missing a large share of local search volume. Give guidance on keeping both language versions equally complete and consistent. Close with how this connects to the website's own bilingual SEO setup.")

add(27,5,"Service-Area Business SEO in the UAE: The Local Pack Strategy That Works","Local SEO","service area business seo",590,"service area business gbp","no storefront local seo",
    "Service-Area Business SEO in the UAE | Growpha",
    "Businesses without a public storefront — trades, home services, mobile consultancies — need a different local SEO approach. Here's what works in the UAE.",
    "service-area-business-seo-uae",
    "Explain the specific Google Business Profile configuration for service-area businesses (hiding the address, defining service areas) and how this changes local pack eligibility compared to storefront businesses. Cover the content strategy implication: service-area businesses need to build relevance for each area they serve through genuine local content, not just GBP settings. Address common setup mistakes that get service-area profiles suspended or restricted. Close with realistic expectations for local pack visibility without a physical storefront.")

add(29,5,"Multi-Location Schema Markup for UAE Franchise Businesses","Local SEO","local business schema markup",170,"franchise schema markup","multi location structured data",
    "Multi-Location Schema Markup for UAE Franchise Businesses | Growpha",
    "Franchise and multi-branch UAE businesses need location-specific structured data, not one generic LocalBusiness schema. Here's how to implement it properly.",
    "multi-location-schema-markup-uae-franchise",
    "Explain why a single site-wide LocalBusiness schema fails multi-branch and franchise businesses, and what location-specific structured data should look like instead. Cover the practical implementation: unique schema per location page with correct address, geo-coordinates, and opening hours, nested appropriately under an Organization schema for the parent brand. Give guidance on validating this at scale across dozens of location pages. Close with how correct schema supports both local pack eligibility and rich result display.")

# ---- On-Page SEO (O1-O13) ----
add(1,4,"Title Tag Optimisation: What Actually Moves Click-Through Rate in 2026","On-Page SEO","title tag optimization",480,"title tag ctr","seo title best practices",
    "Title Tag Optimisation: What Actually Moves CTR in 2026 | Growpha",
    "Keyword-stuffed title tags don't win clicks anymore. Here's what actually moves click-through rate in the SERP today.",
    "title-tag-optimization-ctr-2026",
    "Move past the outdated advice of just 'include the keyword at the front' and cover what genuinely drives CTR now: specificity, numbers where relevant, and matching the actual search intent rather than a generic keyword match. Give real before/after title examples showing the difference. Cover length constraints and how Google truncates or rewrites titles it judges as a poor SERP match. Close with a practical A/B testing approach for title tags at scale using Search Console CTR data.")

add(3,5,"Internal Linking Architecture: The Silo Structure Most Sites Get Wrong","On-Page SEO","internal linking strategy",1300,"silo structure seo","internal link architecture",
    "Internal Linking Architecture: The Silo Structure Most Sites Miss | Growpha",
    "Random internal linking wastes your strongest pages' authority. Here's how proper silo-based internal linking architecture actually works.",
    "internal-linking-silo-structure",
    "Explain the concept of topical silos — grouping related content and linking within the cluster to reinforce topical relevance — and why most sites link randomly instead. Cover the common mistake of every page linking to the homepage and nowhere else meaningfully. Give a practical framework for auditing and restructuring internal links around pillar and cluster content. Close with how this connects directly to the topical authority a site can build over time.")

add(6,1,"Content Depth vs Word Count: What Google Actually Rewards","On-Page SEO","content length seo",50,"content depth vs word count","comprehensive content seo",
    "Content Depth vs Word Count: What Google Actually Rewards | Growpha",
    "Longer isn't automatically better. Here's the real difference between content depth and word count, and which one Google's rankings actually reward.",
    "content-depth-vs-word-count-seo",
    "Directly challenge the 'longer content ranks better' assumption with the more accurate framing: depth (comprehensive coverage of what a searcher needs) correlates with rankings, and length is often just a byproduct of genuine depth, not the cause. Give examples of thin long content that fails versus concise content that fully satisfies intent. Cover how to audit existing content for genuine depth gaps versus padding. Close with a practical content brief structure that optimises for depth rather than a word count target.")

add(8,2,"The Heading Hierarchy Mistakes Quietly Diluting Your Topical Relevance","On-Page SEO","heading tags seo",1300,"h1 h2 heading structure","heading hierarchy seo mistakes",
    "Heading Hierarchy Mistakes Diluting Your Topical Relevance | Growpha",
    "Skipped heading levels and keyword-stuffed H2s confuse both users and search engines. Here are the heading structure mistakes worth fixing.",
    "heading-hierarchy-mistakes-topical-relevance",
    "Cover the common heading structure errors: multiple H1s per page, skipped heading levels (H2 straight to H4), and headings used purely for visual styling rather than genuine content structure. Explain how a clean, logical heading hierarchy helps both accessibility and search engines understand a page's topical structure. Give a practical audit and fix method for large sites with inconsistent heading usage. Close with how this connects to featured snippet eligibility.")

add(10,3,"Semantic Keyword Mapping: Beyond Exact-Match in 2026","On-Page SEO","semantic keyword research",210,"semantic seo","topic clusters keyword mapping",
    "Semantic Keyword Mapping: Beyond Exact-Match in 2026 | Growpha",
    "Exact-match keyword targeting is outdated. Here's how semantic keyword mapping actually works for content that ranks for entire topic clusters.",
    "semantic-keyword-mapping-2026",
    "Explain the shift from exact-match keyword targeting to semantic/topical mapping, where Google evaluates comprehensive topical coverage rather than exact phrase matches. Give a practical method for mapping a topic's full semantic field — related entities, subtopics, and common questions — before writing. Cover how this changes content brief creation compared to older keyword-density approaches. Close with an example of one topic mapped semantically versus the old exact-match approach.")

add(12,4,"Why Your Meta Descriptions Aren't Improving Rankings (And What They Do Instead)","On-Page SEO","meta description seo",1300,"meta description best practices","meta description ctr",
    "Why Meta Descriptions Don't Improve Rankings (And What They Do) | Growpha",
    "Meta descriptions are not a direct ranking factor, but they still matter enormously for CTR. Here's the real role they play in SEO.",
    "meta-descriptions-rankings-what-they-actually-do",
    "Clarify directly that meta descriptions are not a ranking factor Google uses in its algorithm, correcting a persistent misconception. Explain their real function: influencing click-through rate, which indirectly affects performance and can influence rankings over time through engagement signals. Cover why Google frequently rewrites meta descriptions and how to write ones that survive being kept. Close with practical meta description writing guidance focused on matching intent and driving clicks.")

add(17,1,"Content Cannibalization: Finding and Fixing Pages That Compete With Each Other","On-Page SEO","keyword cannibalization",6600,"content cannibalization fix","competing pages same keyword",
    "Content Cannibalization: Finding Pages That Compete With Each Other | Growpha",
    "Multiple pages targeting the same keyword split ranking signals and often rank worse than one consolidated page would. Here's how to find and fix it.",
    "content-cannibalization-finding-fixing",
    "Explain how cannibalization happens — usually organically, as a site adds content over time without a clear content map — and why it actually hurts rather than helps rankings. Give a practical detection method using Search Console query data to find multiple URLs ranking for the same query inconsistently. Cover the fix options: consolidation via 301, differentiation of search intent, or canonicalization. Close with how a content map prevents cannibalization before it starts.")

add(19,2,"Image SEO Beyond Alt Text: What Actually Affects Rankings","On-Page SEO","image seo",4400,"image seo best practices","image optimization rankings",
    "Image SEO Beyond Alt Text: What Actually Affects Rankings | Growpha",
    "Alt text is only one piece of image SEO. Here's what else actually affects rankings and image search visibility.",
    "image-seo-beyond-alt-text",
    "Go beyond the well-known alt text advice to cover the fuller image SEO picture: file naming conventions, compression and format choices (WebP/AVIF) for Core Web Vitals impact, structured data for product/article images, and image sitemaps for large image-heavy sites. Explain how image search itself remains an underused traffic channel most sites neglect. Close with a practical image SEO checklist for e-commerce specifically, where product images carry real search value.")

add(21,3,"On-Page Optimisation for Featured Snippets: The Structure That Wins Position Zero","On-Page SEO","position zero seo",70,"featured snippet formatting","how to win position zero",
    "On-Page Optimisation for Featured Snippets (Position Zero) | Growpha",
    "Featured snippets reward a specific on-page structure, not just good content. Here's the formatting pattern that actually wins position zero.",
    "on-page-optimization-featured-snippets-position-zero",
    "Explain that featured snippets are won primarily through structure and formatting matching the query type — direct answer paragraphs for definitions, numbered lists for processes, tables for comparisons. Give concrete formatting examples for each snippet type. Cover how to identify snippet opportunities using existing rankings in positions 2-10 as the target list. Close with how AI Overviews are changing the value and mechanics of chasing position zero.")

add(23,4,"Topical Authority Mapping: Building Content Clusters That Actually Rank","On-Page SEO","topical authority mapping",10,"content cluster strategy","pillar cluster model",
    "Topical Authority Mapping: Content Clusters That Actually Rank | Growpha",
    "Random content publishing doesn't build topical authority. Here's how to map content clusters deliberately so they actually compound in rankings.",
    "topical-authority-mapping-content-clusters",
    "Explain the pillar-and-cluster content model properly: one comprehensive pillar page supported by multiple cluster pages covering subtopics, all interlinked deliberately. Give a practical mapping exercise for identifying a topic's full subtopic landscape before writing anything. Cover how this differs from simply publishing frequently without a coherent structure. Close with how topical authority mapping should drive the editorial calendar rather than the other way around.")

add(25,5,"Anchor Text Strategy for Internal Links: The Rules Most Sites Break","On-Page SEO","anchor text internal links",10,"internal anchor text best practices","descriptive anchor text seo",
    "Anchor Text Strategy for Internal Links | Growpha",
    "'Click here' and 'read more' waste one of SEO's easiest wins. Here's the anchor text strategy for internal links most sites get wrong.",
    "anchor-text-strategy-internal-links",
    "Explain why internal anchor text is a controllable, easy-to-improve signal most sites neglect, defaulting to generic phrases like 'click here' or 'read more'. Give guidance on writing descriptive, keyword-relevant anchor text without over-optimising into exact-match repetition that looks manipulative. Cover how to audit existing internal anchor text at scale and prioritise fixes on the most important pages. Close with the balance between descriptive anchors and natural, varied phrasing.")

add(28,1,"Content Freshness Signals: When Updating a Page Actually Helps Rankings","On-Page SEO","content freshness",110,"content update seo impact","refreshing old content",
    "Content Freshness Signals: When Updates Actually Help Rankings | Growpha",
    "Changing the published date without real changes does nothing. Here's when content freshness updates genuinely move rankings, and when they don't.",
    "content-freshness-signals-when-updates-help",
    "Correct the common shortcut of just changing a page's date without substantive changes, explaining that Google's freshness signals respond to genuine content changes, not metadata. Cover the situations where freshness updates matter most: time-sensitive topics, statistics that go stale, and pages that have slipped in rankings due to newer competing content. Give a practical prioritisation method for which pages are worth refreshing versus leaving alone. Close with how to measure whether a refresh actually worked.")

# ---- Off-Page SEO (F1-F14) ----
add(1,5,"Digital PR for B2B: Earning Links Without a Consumer Story","Off-Page SEO","digital pr for b2b",0,"b2b digital pr strategy","b2b link building without data study",
    "Digital PR for B2B: Earning Links Without a Consumer Story | Growpha",
    "B2B brands can't rely on consumer-friendly viral hooks. Here's how digital PR actually works for B2B companies without a mass-market story.",
    "digital-pr-for-b2b-without-consumer-story",
    "Address the real challenge B2B brands face with digital PR: no obviously newsworthy consumer angle. Cover practical B2B digital PR approaches: original industry research and surveys, executive commentary and thought leadership for trade press, and data-driven insights from proprietary business data. Give examples of B2B stories that earned genuine coverage without a consumer hook. Close with realistic expectations for link volume and quality from B2B digital PR compared to consumer campaigns.")

add(4,1,"Toxic Backlink Audits: When to Disavow and When to Ignore","Off-Page SEO","toxic backlinks",590,"backlink disavow guide","spammy backlinks seo",
    "Toxic Backlink Audits: When to Disavow, When to Ignore | Growpha",
    "Most toxic-looking backlinks don't need a disavow file. Here's how to genuinely assess link risk and when disavowing actually makes sense.",
    "toxic-backlink-audits-disavow-or-ignore",
    "Correct the over-cautious instinct many site owners have to disavow any link that looks spammy, explaining that Google's algorithm already discounts most low-quality links automatically. Give a real risk-assessment framework: manual action history, link velocity spikes, and genuinely manipulative link schemes as the actual triggers for disavowing. Cover the risk of over-disavowing legitimate links by mistake. Close with when a disavow file is genuinely warranted versus when the better move is to do nothing.")

add(6,2,"Broken Link Building: Does It Still Work in 2026?","Off-Page SEO","broken link building",2400,"broken link building tactic","dead link outreach",
    "Broken Link Building: Does It Still Work in 2026? | Growpha",
    "Broken link building was once a reliable tactic. Here's an honest look at whether it still earns links in 2026, and how to run it if it does.",
    "broken-link-building-still-work-2026",
    "Give an honest assessment of broken link building's current effectiveness — response rates have dropped significantly as the tactic became widely known and automated. Cover when it still works: niche, well-maintained resource pages with genuinely engaged site owners. Give a realistic, updated outreach approach that differs from the templated pitches most site owners now ignore. Close with a comparison to which alternative link-building tactics now deliver better ROI for the same effort.")

add(8,3,"Competitor Backlink Gap Analysis: The Framework That Finds Real Opportunities","Off-Page SEO","backlink gap analysis",880,"competitor backlink analysis","link gap opportunities",
    "Competitor Backlink Gap Analysis: A Framework That Works | Growpha",
    "Most backlink gap reports return noise. Here's a framework for finding genuinely pursuable link opportunities from competitor backlink data.",
    "competitor-backlink-gap-analysis-framework",
    "Explain the standard backlink gap analysis approach (comparing competitor backlink profiles for domains linking to them but not you) and why raw gap reports are usually full of low-value, unpursuable links. Give a practical filtering framework: relevance, authority, and realistic acquisition likelihood as the three filters to apply before treating anything as an opportunity. Cover how to prioritise the resulting shortlist for outreach. Close with a realistic conversion rate to expect from gap-analysis-driven outreach.")

add(10,4,"Guest Posting in 2026: What Actually Passes Authority (And What Doesn't)","Off-Page SEO","guest posting seo",140,"guest post link value","guest blogging worth it",
    "Guest Posting in 2026: What Actually Passes Authority | Growpha",
    "Not all guest posts are equal, and some pass almost no SEO value at all. Here's what actually determines whether a guest post is worth the effort.",
    "guest-posting-2026-what-passes-authority",
    "Give an honest, current assessment of guest posting's value, distinguishing genuinely valuable placements (relevant, editorially-vetted publications with real traffic) from low-value guest post farms that add risk without benefit. Cover the signals that indicate a guest post opportunity is worth pursuing versus a paid link scheme in disguise. Give practical guidance on pitching genuinely relevant publications rather than mass outreach. Close with how to evaluate ROI on guest posting realistically against the time invested.")

add(12,5,"HARO and Journalist Outreach: Building Authority Through Expert Commentary","Off-Page SEO","haro link building",880,"journalist outreach seo","expert commentary links",
    "HARO and Journalist Outreach for Authority Building | Growpha",
    "Responding to journalist queries is one of the more sustainable white-hat link tactics left. Here's how to actually get picked up and cited.",
    "haro-journalist-outreach-authority-building",
    "Explain how HARO-style journalist outreach works and why it remains one of the more durable, white-hat authority-building tactics. Give practical guidance for standing out among hundreds of pitches: specificity, credentials that establish genuine expertise, and response speed. Cover realistic response rates and how to build a sustainable weekly cadence rather than one-off attempts. Close with how this ties into broader E-E-A-T signal-building for a founder or expert's personal brand.")

add(15,1,"Anchor Text Distribution: The Ratios That Keep Your Link Profile Natural","Off-Page SEO","anchor text distribution",40,"natural anchor text ratio","backlink anchor text mix",
    "Anchor Text Distribution: Keeping Your Link Profile Natural | Growpha",
    "Over-optimised exact-match anchor text is one of the clearest manipulation signals Google's algorithm watches for. Here's a natural anchor text ratio to aim for.",
    "anchor-text-distribution-natural-link-profile",
    "Explain why anchor text distribution is one of the clearer signals Google uses to detect manipulative link building, and what a genuinely natural distribution looks like (mostly branded and naked URL anchors, with exact-match keyword anchors as a small minority). Give realistic target ratios based on natural link acquisition patterns. Cover how to audit an existing link profile's anchor text distribution and what a warning sign looks like. Close with how to guide anchor text naturally through outreach without controlling it too tightly.")

add(17,2,"Link Velocity: How Fast Is Too Fast When Building Authority","Off-Page SEO","link velocity",210,"link building pace","natural link acquisition speed",
    "Link Velocity: How Fast Is Too Fast? | Growpha",
    "A sudden spike in backlinks can look manipulative even when the links are genuine. Here's how to think about link velocity and pacing.",
    "link-velocity-how-fast-is-too-fast",
    "Explain link velocity as a signal Google's algorithm considers, and why an unnaturally sudden spike in backlinks — even from legitimate sources — can look like a paid link campaign. Give realistic pacing guidance based on a site's existing authority and typical growth patterns for its industry. Cover the exception: genuinely viral content or major PR moments that naturally produce a spike. Close with why steady, sustained link acquisition outperforms sporadic bursts for most businesses.")

add(19,3,"Brand Mentions as a Ranking Signal: Do Unlinked Mentions Actually Matter?","Off-Page SEO","unlinked brand mentions",320,"unlinked mentions seo value","brand mention link building",
    "Do Unlinked Brand Mentions Actually Help Rankings? | Growpha",
    "Google has discussed treating unlinked brand mentions as a trust signal. Here's the honest current state of the evidence, and what to do about it.",
    "unlinked-brand-mentions-ranking-signal",
    "Give an honest, evidence-based take on unlinked brand mentions as a ranking factor, referencing Google's own public statements about entity recognition rather than overclaiming certainty. Cover the practical value regardless of direct ranking impact: brand mentions build genuine entity recognition relevant to AI search visibility as well. Give guidance on monitoring and, where appropriate, following up to convert valuable unlinked mentions into links. Close with why this shouldn't replace a genuine link-building strategy but complements it.")

add(21,4,"Resource Page Link Building: A Framework That Still Works","Off-Page SEO","resource page link building",1000,"resource page outreach","curated link list outreach",
    "Resource Page Link Building: A Framework That Still Works | Growpha",
    "Resource pages are one of the few classic link-building tactics that remain genuinely effective. Here's a current framework for running it well.",
    "resource-page-link-building-framework",
    "Explain why resource page link building has aged better than some other classic tactics, since it targets pages explicitly curated to be useful reference lists. Give a practical framework: finding genuinely active, well-maintained resource pages through targeted search operators, and pitching based on adding real value rather than a generic request. Cover realistic acceptance rates and how to prioritise targets by relevance and authority. Close with common mistakes that get outreach emails ignored.")

add(23,5,"The Link Building Tactics That Trigger Manual Actions","Off-Page SEO","google manual action",260,"link scheme penalty","manual action link building",
    "Link Building Tactics That Trigger Manual Actions | Growpha",
    "Some link building tactics carry real manual action risk. Here's what specifically triggers Google's link spam enforcement, and what's actually safe.",
    "link-building-tactics-manual-actions",
    "Give a clear, non-alarmist breakdown of the link building patterns that genuinely trigger manual actions: large-scale paid link schemes, private blog networks, and excessive reciprocal linking arrangements. Distinguish these from tactics that are sometimes mistakenly feared as risky but generally aren't, like guest posting done properly or resource page outreach. Cover what happens practically if a manual action is issued and the recovery process. Close with a realistic risk framework for evaluating any link building tactic before adopting it.")

add(26,1,"Building Authority Through Original Research and Data Studies","Off-Page SEO","original research content marketing",0,"data study link building","proprietary data content",
    "Building Authority Through Original Research and Data Studies | Growpha",
    "Original data studies remain one of the most reliable ways to earn genuine, high-authority links. Here's how to plan and execute one properly.",
    "original-research-data-studies-authority",
    "Explain why original research and data studies consistently outperform other content formats for earning genuine editorial links, since journalists and industry sites need citable, novel data. Give a practical process: identifying a genuinely interesting data question, sourcing or generating the data (surveys, proprietary business data, or aggregated public data with new analysis), and packaging findings for easy citation. Cover promotion strategy once the study is published. Close with realistic resourcing needed to execute a data study well.")

add(28,2,"Competitor Link Reclamation: Finding Links You've Already Earned But Lost","Off-Page SEO","link reclamation",2400,"lost backlinks recovery","broken backlink reclamation",
    "Competitor Link Reclamation: Finding Links You've Lost | Growpha",
    "Sites lose valuable backlinks constantly through redesigns, broken pages, and forgotten mentions. Here's how to find and reclaim them.",
    "link-reclamation-finding-lost-backlinks",
    "Explain how sites accumulate lost link equity over time: pages that get removed or restructured without redirects, and mentions that lose their link during a publisher's own site redesign. Give a practical method for auditing lost backlinks using historical backlink data and identifying which are worth actively reclaiming. Cover the outreach approach for asking a publisher to restore or update a broken link. Close with the quick technical win of redirecting removed pages that had earned links.")

add(30,1,"Digital PR Measurement: Proving ROI Beyond Domain Rating","Off-Page SEO","digital pr",4400,"digital pr roi measurement","digital pr kpis",
    "Digital PR Measurement: Proving ROI Beyond Domain Rating | Growpha",
    "Domain rating alone doesn't prove digital PR's business value. Here's how to actually measure and report digital PR ROI to stakeholders.",
    "digital-pr-measurement-roi-beyond-domain-rating",
    "Address the common gap between digital PR activity metrics (links earned, domain ratings of publishers) and genuine business impact stakeholders care about. Give a fuller measurement framework: referral traffic quality, branded search lift following major coverage, and downstream ranking improvements for target pages linked from earned coverage. Cover how to build a realistic attribution model given digital PR's indirect, compounding nature. Close with how to report this in a way that satisfies both SEO and broader marketing stakeholders.")

# ---- YouTube SEO (Y1-Y13) ----
add(2,1,"YouTube Search vs Google Search: Why Your Optimisation Strategy Needs to Differ","YouTube SEO","youtube seo",6600,"youtube vs google search algorithm","youtube search ranking factors",
    "YouTube Search vs Google Search: Different Strategies Needed | Growpha",
    "YouTube's algorithm weighs watch time and session behaviour very differently from Google's web ranking factors. Here's how to optimise for each properly.",
    "youtube-search-vs-google-search-strategy",
    "Explain the fundamentally different priorities of YouTube's ranking algorithm — watch time, session duration, and engagement — versus Google's web search factors focused more on relevance and authority signals. Give concrete examples of tactics that work for one platform but do little for the other. Cover how a business should split effort and expectations between the two channels. Close with the cross-platform opportunity: how strong YouTube performance can also surface videos directly in Google's web results.")

add(4,2,"Video Metadata Optimisation: The Fields That Actually Affect Rankings","YouTube SEO","youtube video seo",1000,"youtube metadata optimization","video title description tags",
    "Video Metadata Optimisation: What Actually Affects Rankings | Growpha",
    "Not every YouTube metadata field carries equal ranking weight. Here's which fields actually influence video search rankings versus which are largely cosmetic.",
    "youtube-video-metadata-optimization",
    "Break down each YouTube metadata field — title, description, tags, and category — and give an honest assessment of how much ranking weight each genuinely carries based on how YouTube's system actually works. Cover the outsized importance of the first few lines of the description and the title's keyword placement. Give practical guidance on writing metadata that serves both search and click-through rate. Close with the fields most creators over-invest in for little return (tags) versus under-invest in (description depth).")

add(6,3,"YouTube Channel Architecture: Structuring Playlists for Search Visibility","YouTube SEO","youtube channel seo",40,"youtube playlist strategy","channel structure seo",
    "YouTube Channel Architecture: Structuring Playlists for Search | Growpha",
    "Random uploads without playlist structure limit a channel's search visibility and session time. Here's how to architect a channel properly.",
    "youtube-channel-architecture-playlist-structure",
    "Explain how playlist structure affects both discoverability (playlists rank in their own right) and session duration (autoplay within a well-ordered playlist keeps viewers watching longer). Give a practical framework for organising a channel's existing and future content into topic-based playlists. Cover playlist metadata optimisation as its own discipline, distinct from individual video optimisation. Close with how this connects to building topical authority on YouTube the same way it works for a website.")

add(8,4,"Thumbnail and CTR Optimisation: What Actually Drives YouTube's Algorithm","YouTube SEO","youtube thumbnail ctr",20,"youtube thumbnail best practices","click through rate youtube",
    "Thumbnail and CTR Optimisation for YouTube's Algorithm | Growpha",
    "Click-through rate from impressions is one of YouTube's strongest early ranking signals. Here's what actually makes a thumbnail perform.",
    "thumbnail-ctr-optimization-youtube-algorithm",
    "Explain why CTR from the browse and search surfaces is such a heavily weighted early signal for how much YouTube continues to promote a video. Give concrete, evidence-based thumbnail design principles: clarity at small sizes, contrast, and honest curiosity gaps rather than misleading clickbait that hurts retention. Cover how to A/B test thumbnails using YouTube Studio's testing feature. Close with the relationship between thumbnail-driven CTR and the retention data that follows, since a good thumbnail with poor retention still hurts long-term performance.")

add(10,5,"Video Transcripts and SEO: An Underused Ranking Signal","YouTube SEO","video transcripts seo",10,"youtube transcript seo benefit","closed captions seo",
    "Video Transcripts and SEO: An Underused Signal | Growpha",
    "Accurate transcripts help both YouTube's algorithm and Google's web indexing understand video content. Here's why most channels neglect this.",
    "video-transcripts-seo-underused-signal",
    "Explain how transcripts and closed captions give YouTube's algorithm (and Google's web crawlers, for embedded videos) far richer content understanding than metadata alone can provide. Cover the accessibility benefit as a secondary but genuine reason to prioritise accurate transcripts over auto-generated ones. Give practical guidance on transcript accuracy and how it can be repurposed into blog content or show notes. Close with how this supports both YouTube search and cross-platform SEO for embedded video content.")

add(13,1,"YouTube Shorts vs Long-Form: What Actually Drives Channel Growth in 2026","YouTube SEO","youtube shorts vs long form",20,"shorts vs long form strategy","youtube shorts algorithm",
    "YouTube Shorts vs Long-Form: What Drives Growth in 2026 | Growpha",
    "Shorts and long-form videos serve genuinely different growth functions on YouTube. Here's how to balance both for real channel growth.",
    "youtube-shorts-vs-long-form-channel-growth",
    "Give an honest, current comparison of what Shorts and long-form content each actually contribute to channel growth — Shorts for reach and subscriber acquisition, long-form for watch time, ad revenue, and deeper topical authority. Cover the common mistake of treating them as competing formats rather than complementary parts of a channel strategy. Give a practical guidance on allocation for a B2B or service-business channel specifically, where audience size matters less than lead quality. Close with how Shorts can funnel viewers into long-form content.")

add(15,2,"Cross-Platform SEO: Getting YouTube Videos to Rank in Google Search Results","YouTube SEO","youtube video google ranking",0,"video rich results google","video seo cross platform",
    "Cross-Platform SEO: Getting YouTube Videos to Rank on Google | Growpha",
    "A well-optimised video can rank directly in Google's web search results, not just on YouTube. Here's how to make that happen deliberately.",
    "cross-platform-seo-youtube-videos-google-ranking",
    "Explain the mechanism by which YouTube videos can surface directly in Google's organic web search results, including video rich results and the video carousel. Cover the on-page and metadata factors that increase this likelihood: video schema markup, embedding the video on a relevant page with substantive supporting text, and matching search intent for informational queries. Give practical guidance on which query types are most likely to surface video results. Close with how this expands a video's reach well beyond YouTube's own search.")

add(17,3,"YouTube Keyword Research: The Tools and Method That Actually Work","YouTube SEO","youtube keyword research",4400,"youtube keyword tool","video keyword research method",
    "YouTube Keyword Research: The Method That Actually Works | Growpha",
    "Web SEO keyword tools don't capture YouTube-specific search behaviour well. Here's a keyword research method built specifically for video content.",
    "youtube-keyword-research-method",
    "Explain why standard web SEO keyword tools often miss YouTube-specific search volume and phrasing, since video search behaviour differs from web search behaviour for the same topic. Give a practical method combining YouTube's own autocomplete and search suggestions, dedicated video keyword tools, and analysis of what's already ranking for the target topic. Cover how to judge competition realistically by watching what's currently ranking, not just checking a difficulty score. Close with how to build this into a repeatable video content planning process.")

add(21,5,"Building Topical Authority on YouTube the Same Way You Do on a Website","YouTube SEO","youtube seo strategy",260,"youtube topical authority","channel content strategy",
    "Building Topical Authority on YouTube | Growpha",
    "Topical authority isn't just a web SEO concept. Here's how to apply the same pillar-and-cluster thinking to build authority on a YouTube channel.",
    "building-topical-authority-youtube",
    "Apply the pillar-and-cluster content model to YouTube specifically: a comprehensive cornerstone video on a core topic supported by multiple related videos linked through playlists, cards, and descriptions. Explain why channels that publish scattered, unrelated topics struggle to build the same recognition and recommendation strength as focused channels. Give a practical content mapping exercise for a channel's core topic areas. Close with how this compounds channel authority the same way topical authority compounds for a website over time.")

add(24,1,"YouTube End Screens and Cards: The Retention Strategy Most Channels Get Wrong","YouTube SEO","youtube end screens",170,"youtube cards strategy","end screen optimization",
    "YouTube End Screens and Cards: The Retention Strategy Most Get Wrong | Growpha",
    "End screens and cards are often an afterthought, but used well they meaningfully extend session time. Here's how to actually use them effectively.",
    "youtube-end-screens-cards-retention-strategy",
    "Explain the retention and session-time value of well-placed end screens and cards, which keep viewers within a channel's content rather than leaving YouTube. Cover the common mistake of using generic 'subscribe' end screens instead of directing viewers to genuinely relevant next videos. Give practical timing and placement guidance for cards throughout a video, not just at the end. Close with how this connects to YouTube's algorithm rewarding session duration across a channel, not just single-video watch time.")

add(26,2,"Repurposing Blog Content Into YouTube Videos Without Losing SEO Value","YouTube SEO","turn blog posts into videos",20,"repurpose content video","blog to video content strategy",
    "Repurposing Blog Content Into YouTube Videos | Growpha",
    "Turning existing blog content into video extends its reach without starting from scratch. Here's how to do it without diluting either format's SEO value.",
    "repurposing-blog-content-youtube-videos",
    "Give a practical framework for identifying which existing blog posts are strong candidates for video repurposing — typically process-driven or visually explainable topics rather than purely textual analysis. Cover how to adapt the structure for video pacing rather than just reading the blog post aloud. Address the SEO relationship between the two formats: the video description linking back to the source article, and the article potentially embedding the video for engagement. Close with a realistic content workflow for a small team producing both formats.")

add(28,3,"YouTube SEO for B2B Brands: Does It Actually Generate Leads?","YouTube SEO","b2b youtube marketing",0,"b2b youtube lead generation","youtube for business growth",
    "YouTube SEO for B2B Brands: Does It Actually Generate Leads? | Growpha",
    "B2B YouTube channels often struggle to prove ROI. Here's an honest look at whether YouTube SEO genuinely generates leads for B2B businesses.",
    "youtube-seo-b2b-brands-lead-generation",
    "Give an honest, non-hyped assessment of YouTube's lead generation potential for B2B brands specifically, where audience size is typically much smaller than consumer channels. Cover the realistic value: building trust and authority with a niche, high-intent audience rather than chasing view counts. Give examples of B2B content formats that do work — product walkthroughs, founder-led thought leadership, and case study breakdowns. Close with realistic expectations for timeline and volume of leads a B2B YouTube strategy can produce.")

# ---- AI/LLM SEO (A1-A14) ----
add(2,2,"AI Overviews Are Changing Click-Through Rates — Here's the Actual Data","AI/LLM SEO","ai overviews seo",480,"ai overviews ctr impact","google ai overviews data",
    "AI Overviews Are Changing CTR — Here's the Actual Data | Growpha",
    "AI Overviews are measurably reducing organic click-through rates for many query types. Here's what the current data actually shows.",
    "ai-overviews-changing-ctr-data",
    "Present a grounded, evidence-based view of how AI Overviews are affecting organic CTR, distinguishing which query types (informational, definitional) are hit hardest from those less affected (transactional, branded). Cover the emerging pattern of 'zero-click' searches increasing for certain topics. Give practical strategic implications: doubling down on queries less affected by AI Overviews and building AI citation visibility as a parallel channel. Close with what this means for how SEO success should be measured going forward.")

add(4,3,"Entity SEO: Building the Knowledge Graph Signals AI Systems Rely On","AI/LLM SEO","entity seo",1300,"knowledge graph optimization","entity based seo",
    "Entity SEO: Building the Knowledge Graph Signals AI Relies On | Growpha",
    "AI systems reason in entities and relationships, not just keywords. Here's how to build the entity signals that both Google's Knowledge Graph and LLMs rely on.",
    "entity-seo-knowledge-graph-signals",
    "Explain the shift from keyword-based to entity-based understanding in modern search and AI systems, where a business, person, or concept needs to be clearly and consistently defined across the web. Cover practical entity-building tactics: structured data (Organization, Person schema), Wikipedia and Wikidata presence, and consistent NAP and description language across all properties. Give a framework for auditing how clearly an entity is currently defined online. Close with why entity clarity increasingly matters more than any single page's keyword optimisation.")

add(6,4,"Structuring Content for AI Retrieval: The Chunking Strategy That Works","AI/LLM SEO","ai search optimization",3600,"content chunking for ai","structuring content for llms",
    "Structuring Content for AI Retrieval: The Chunking Strategy | Growpha",
    "AI systems retrieve and cite content in chunks, not whole pages. Here's how to structure content so it survives that chunking process intact.",
    "structuring-content-ai-retrieval-chunking",
    "Explain how AI systems and RAG-based retrieval break content into smaller chunks rather than processing whole pages, and why this changes how content should be structured. Give practical guidance: self-contained sections with clear headers, front-loaded answers before elaboration, and avoiding context that only makes sense with surrounding paragraphs. Cover how this differs from writing purely for human readers scanning top to bottom. Close with how this content structure also happens to improve featured snippet eligibility as a side benefit.")

add(8,5,"Getting Cited by ChatGPT and Perplexity: What Actually Influences AI Citations","AI/LLM SEO","ai search visibility",1000,"chatgpt citations seo","perplexity citation sources",
    "Getting Cited by ChatGPT and Perplexity: What Influences It | Growpha",
    "AI citation isn't the same game as ranking on page one. Here's what actually appears to influence whether ChatGPT and Perplexity cite a source.",
    "getting-cited-chatgpt-perplexity-ai-citations",
    "Give a grounded, honestly-hedged view (since this is an evolving area) of the patterns that correlate with AI citation: clear, well-structured factual content, strong existing topical authority, and appearing in sources these systems already trust and crawl frequently. Cover the practical difference between optimising for traditional rankings and optimising for AI citation specifically. Give a monitoring approach for tracking citation frequency across major AI search tools. Close with why building genuine topical authority remains the most reliable lever, even as the exact mechanics evolve.")

add(11,1,"Schema Markup for AI Search: What LLMs Actually Parse","AI/LLM SEO","schema markup",8100,"schema markup ai search","structured data llm",
    "Schema Markup for AI Search: What LLMs Actually Parse | Growpha",
    "Structured data isn't just for rich results anymore. Here's how schema markup helps AI systems parse and understand page content more reliably.",
    "schema-markup-ai-search-llm-parsing",
    "Explain how structured data gives AI systems an unambiguous, machine-readable summary of a page's content, reducing the risk of misinterpretation compared to parsing unstructured prose alone. Cover the schema types most relevant for AI understanding: Organization, Article, FAQPage, and Product where applicable. Give practical implementation guidance and common validation mistakes. Close with why comprehensive, accurate schema is a relatively low-effort, high-leverage investment for AI search visibility.")

add(13,2,"Why Traditional Keyword Rankings Don't Predict AI Search Visibility","AI/LLM SEO","ai search rankings",320,"ai search vs google rankings","keyword rankings ai visibility",
    "Why Keyword Rankings Don't Predict AI Search Visibility | Growpha",
    "Ranking #1 on Google doesn't guarantee AI citation, and lower-ranked pages sometimes get cited over top results. Here's why the two don't correlate cleanly.",
    "keyword-rankings-dont-predict-ai-visibility",
    "Explain the disconnect between traditional ranking position and AI citation likelihood, since AI systems weigh factors like content clarity and direct-answer structure differently from Google's ranking algorithm. Give examples of the kind of content that gets cited despite modest traditional rankings, and vice versa. Cover why this means AI visibility needs its own tracking and optimisation approach rather than assuming good rankings are sufficient. Close with practical first steps for a business wanting to measure this gap for its own content.")

add(15,3,"Brand Entity Clarity: Why AI Systems Misrepresent Some Businesses","AI/LLM SEO","brand entity seo",20,"ai brand misrepresentation","entity clarity for ai",
    "Brand Entity Clarity: Why AI Systems Misrepresent Businesses | Growpha",
    "When AI systems get basic facts about a business wrong, it's usually an entity clarity problem. Here's why it happens and how to fix it.",
    "brand-entity-clarity-ai-misrepresentation",
    "Explain the common scenario of AI systems confidently stating incorrect information about a business — wrong founding date, wrong service scope, or confusion with a similarly-named company — and trace it to unclear or conflicting entity signals across the web. Give a practical audit method: checking what major AI tools currently say about the business and comparing it to source-of-truth information. Cover the fix: consistent, structured, and widely-distributed accurate information (schema, Wikipedia/Wikidata, consistent bios). Close with why this matters increasingly as more purchase research happens through AI assistants.")

add(17,4,"AI Search Visibility Audits: What to Measure Beyond Google Rankings","AI/LLM SEO","ai search visibility audit",30,"ai visibility audit framework","measuring ai search presence",
    "AI Search Visibility Audits: What to Measure | Growpha",
    "A traditional SEO audit doesn't capture AI search visibility. Here's what an AI-specific visibility audit should actually measure.",
    "ai-search-visibility-audit-what-to-measure",
    "Lay out a practical framework for auditing a business's current AI search visibility distinct from traditional rankings: citation frequency across major AI tools for relevant queries, entity accuracy, and content structural readiness for AI retrieval. Give a repeatable method for running this audit manually given the current lack of mature dedicated tooling. Cover how to benchmark against competitors' AI visibility. Close with how findings should translate into a prioritised action plan.")

add(19,5,"Content Structure for Featured Snippets vs AI Overviews: The Difference That Matters","AI/LLM SEO","featured snippets optimization",260,"featured snippet vs ai overview content","content structure ai overview",
    "Featured Snippets vs AI Overviews: The Structural Difference | Growpha",
    "Featured snippets and AI Overviews reward similar but not identical content structures. Here's the meaningful difference worth understanding.",
    "featured-snippets-vs-ai-overviews-content-structure",
    "Compare the content structuring needs of classic featured snippets (a single, extractable paragraph or list matching a query almost verbatim) with AI Overviews, which synthesise across multiple sources rather than lifting one exact passage. Explain why content built purely for snippet extraction can still miss AI Overview inclusion if it isn't part of the broader synthesis Google draws from. Give practical guidance for structuring content to serve both formats simultaneously. Close with how to monitor presence in each separately.")

add(22,1,"How LLMs Actually Source and Weight Information for Answers","AI/LLM SEO","llm seo",1600,"how llms source information","ai model information weighting",
    "How LLMs Actually Source and Weight Information | Growpha",
    "Understanding how large language models retrieve and weigh source information helps explain what content actually gets used in AI answers.",
    "how-llms-source-weight-information",
    "Give an accessible, technically grounded explanation of how LLM-based search systems typically combine retrieval (finding relevant sources) with generation (synthesising an answer), and what factors appear to influence which sources get weighted more heavily. Cover the practical implication: being retrievable (crawlable, well-structured, factually clear) matters before any weighting even applies. Address the limits of current public understanding here honestly, since these systems aren't fully transparent. Close with the practical takeaway: strong fundamentals still matter most, regardless of the exact weighting mechanics.")

add(24,2,"Conversational Search Optimisation: Writing for How People Actually Ask AI","AI/LLM SEO","conversational search",390,"conversational query optimization","natural language search content",
    "Conversational Search Optimisation: Writing for How People Ask AI | Growpha",
    "People phrase questions to AI assistants very differently than they type Google queries. Here's how to write content that matches conversational search.",
    "conversational-search-optimization-ai-queries",
    "Explain the shift in query phrasing when people talk to AI assistants versus typing short keyword-style Google searches — longer, more natural, often multi-part questions. Give practical guidance for structuring content to directly answer these longer conversational questions, including anticipating follow-up questions within the same piece. Cover how this connects to the phrase questions and 'People Also Ask' data as a research source for conversational phrasing. Close with an example of a topic rewritten from keyword-style to conversational-style structure.")

add(28,4,"Wikipedia's Role in AI Knowledge Graphs: Why It Still Matters in 2026","AI/LLM SEO","wikipedia knowledge graph",90,"wikipedia ai training data","wikipedia entity signal ai",
    "Wikipedia's Role in AI Knowledge Graphs in 2026 | Growpha",
    "Wikipedia remains a foundational source for both Google's Knowledge Graph and many AI systems' training and retrieval. Here's why it still matters.",
    "wikipedias-role-ai-knowledge-graphs-2026",
    "Explain Wikipedia's outsized influence as a trusted, heavily-cited source for both Google's Knowledge Graph and many AI systems' underlying data, despite the rise of newer AI-specific sources. Cover why a well-sourced, compliant Wikipedia presence disproportionately helps entity recognition compared to its relatively modest direct search traffic. Give realistic expectations for what a Wikipedia page can and cannot do for AI visibility on its own. Close with how this connects to the broader entity-building strategy businesses should pursue.")

add(30,2,"Voice Search and AI Assistants: Optimising Beyond Text-Based Queries","AI/LLM SEO","voice search optimization",2900,"voice search seo","ai assistant search optimization",
    "Voice Search and AI Assistants: Optimising Beyond Text | Growpha",
    "Voice queries and AI assistant interactions follow different patterns than typed search. Here's how to optimise content for both.",
    "voice-search-ai-assistants-optimization",
    "Cover how voice search queries (through smart speakers and AI assistants) tend to be longer, more conversational, and more likely to be local or immediate-need in intent compared to typed queries. Explain the overlap between voice search optimisation and the conversational/AI search optimisation already becoming standard practice. Give practical guidance: FAQ-style content, concise direct answers near the top of a page, and local business schema for 'near me'-style voice queries. Close with realistic measurement challenges for voice search specifically, since most platforms don't expose query-level data.")

# ---- Content Marketing (C1-C14) ----
add(2,3,"Content Gap Analysis: Finding What Your Competitors Haven't Written Yet","Content Marketing","content gap analysis",2400,"content gap analysis tool","competitor content research",
    "Content Gap Analysis: Finding What Competitors Haven't Written | Growpha",
    "Competing head-on for the same keywords as established competitors is slow. Here's how to find genuine content gaps they've missed instead.",
    "content-gap-analysis-competitor-research",
    "Explain the strategic value of content gap analysis over simply targeting the same keywords competitors already dominate — finding underserved subtopics within a shared topical space. Give a practical method combining competitor content audits, keyword gap tools, and genuine audience research (forums, reviews, support tickets) to find real unanswered questions. Cover how to prioritise gaps by realistic opportunity versus effort. Close with how this should feed directly into the content calendar.")

add(4,4,"Content Operations at Scale: The Workflow That Doesn't Sacrifice Quality","Content Marketing","content operations",880,"content ops workflow","scaling content production quality",
    "Content Operations at Scale Without Sacrificing Quality | Growpha",
    "Scaling content output usually means sacrificing quality, unless the operational workflow is built deliberately. Here's what that workflow looks like.",
    "content-operations-scale-without-sacrificing-quality",
    "Address the common tension between scaling content volume and maintaining quality, and argue that this is usually a workflow problem, not an inevitable trade-off. Give a practical content operations structure: standardised briefs, a clear editorial review stage, and a QA checklist before publication. Cover how AI tools fit into this workflow responsibly — accelerating research and drafting without replacing editorial judgement. Close with the warning signs that a content operation is scaling past what its quality controls can handle.")

add(6,5,"Pillar Page Strategy: Building Topic Clusters That Actually Rank","Content Marketing","pillar page strategy",140,"pillar page content model","topic cluster strategy",
    "Pillar Page Strategy: Topic Clusters That Actually Rank | Growpha",
    "A pillar page without a genuine cluster of supporting content underneath it rarely reaches its potential. Here's how to build the model properly.",
    "pillar-page-strategy-topic-clusters",
    "Explain the pillar-and-cluster content model in practical terms: one comprehensive pillar page covering a broad topic, supported by narrower cluster pages covering subtopics in depth, all interlinked. Cover the common mistake of publishing a pillar page without building out the supporting clusters that actually make the model work. Give a realistic timeline and resourcing estimate for building out a full pillar-cluster set for one topic. Close with how to measure whether the strategy is working beyond just the pillar page's own rankings.")

add(11,2,"Distribution Strategy: Why Great Content Still Fails Without a Promotion Plan","Content Marketing","content distribution strategy",720,"content promotion strategy","content distribution channels",
    "Distribution Strategy: Why Great Content Still Fails Without One | Growpha",
    "Publishing great content and hoping it gets found is not a strategy. Here's why distribution planning matters as much as the content itself.",
    "content-distribution-strategy-promotion-plan",
    "Challenge the 'publish and it will be found' assumption directly, explaining that most content — even genuinely good content — needs deliberate distribution to gain initial traction. Give a practical distribution framework across owned (email, social), earned (outreach, PR), and paid (targeted promotion) channels appropriate for a B2B or service business. Cover how to plan distribution alongside content creation rather than as an afterthought. Close with a realistic distribution checklist to run before hitting publish.")

add(13,3,"Content Briefs That Actually Work: The Template Behind Consistent Rankings","Content Marketing","content brief template",1000,"seo content brief template","content brief structure",
    "Content Briefs That Actually Work: A Template That Delivers | Growpha",
    "A weak content brief produces weak content regardless of the writer's skill. Here's the brief structure that consistently produces content that ranks.",
    "content-briefs-that-work-template",
    "Explain why content brief quality is often the real bottleneck behind inconsistent content performance, more than writer skill. Give a genuine, usable brief structure: target keyword and search intent, competitor analysis summary, required subtopics to cover for topical completeness, and a clear angle differentiating the piece. Cover how to build briefs efficiently at scale without losing the specificity that makes them useful. Close with the difference between a brief that constrains creativity usefully versus one that's so rigid it produces generic content.")

add(15,4,"Measuring Content ROI: Beyond Traffic and Time on Page","Content Marketing","content marketing roi",1900,"content roi measurement","content marketing metrics that matter",
    "Measuring Content ROI: Beyond Traffic and Time on Page | Growpha",
    "Traffic and time on page don't prove content marketing's business value. Here's a more complete framework for measuring genuine content ROI.",
    "measuring-content-roi-beyond-traffic",
    "Critique the common but insufficient content marketing metrics — traffic and time on page — as vanity metrics that don't connect to business outcomes on their own. Give a fuller measurement framework: assisted conversions, pipeline influence, and organic traffic quality (branded vs non-branded, converting vs non-converting segments). Cover the realistic attribution challenges for content marketing specifically, given its typically longer, less direct conversion path. Close with how to present content ROI credibly to stakeholders who want a clean number.")

add(17,5,"Repurposing Content Across Channels Without Diluting SEO Value","Content Marketing","content repurposing",1000,"content repurposing strategy","multichannel content strategy",
    "Repurposing Content Across Channels Without Diluting SEO | Growpha",
    "Repurposing one piece of content across channels extends its reach, but done carelessly it can create duplicate content and cannibalization risk. Here's how to do it right.",
    "repurposing-content-across-channels-seo",
    "Give a practical framework for repurposing core content (a long-form article, for example) into social posts, email, video, and other formats without creating SEO conflicts like duplicate content across owned properties. Cover when full duplication is fine (syndication with canonical tags) versus when genuine adaptation is needed. Address the common mistake of over-fragmenting one topic into many thin, competing pages instead of repurposing format rather than splitting substance. Close with a realistic repurposing workflow for a lean content team.")

add(20,1,"Why Most Content Marketing Fails to Build Topical Authority","Content Marketing","topical authority",2400,"why content marketing fails","building topical authority mistakes",
    "Why Most Content Marketing Fails to Build Topical Authority | Growpha",
    "Publishing consistently isn't the same as building topical authority. Here's why most content marketing programs fail to compound, and what actually works.",
    "why-content-marketing-fails-topical-authority",
    "Diagnose the common pattern of content marketing programs that publish consistently for months or years without building meaningful topical authority or ranking improvement, tracing it to scattered topic selection without a coherent strategy. Contrast this with programs that deliberately map and build out a topical area systematically. Give the practical shift needed: a topic map before an editorial calendar, not the other way around. Close with realistic timelines for topical authority to compound once a coherent strategy is in place.")

add(22,2,"Editorial Standards for Scaled Content Production","Content Marketing","content editorial guidelines",0,"editorial standards content team","content quality control process",
    "Editorial Standards for Scaled Content Production | Growpha",
    "Scaling content production without clear editorial standards produces inconsistent quality and voice. Here's how to set standards that actually hold at scale.",
    "editorial-standards-scaled-content-production",
    "Explain why editorial standards become more, not less, important as content production scales across multiple writers or an AI-assisted workflow. Give a practical editorial standards document structure: voice and tone guidelines, factual accuracy requirements, formatting conventions, and a review checklist before publication. Cover how to enforce standards without creating bottleneck-level review processes that slow output too much. Close with how editorial standards should evolve as a team and its tools change over time.")

add(24,3,"Content Refresh Strategy: The Signals That Tell You When to Update","Content Marketing","content refresh strategy",20,"content update priority signals","when to refresh old content",
    "Content Refresh Strategy: When to Update, and Why | Growpha",
    "Refreshing content indiscriminately wastes effort. Here are the actual signals that tell you which pages genuinely need an update, and when.",
    "content-refresh-strategy-when-to-update",
    "Give a practical prioritisation framework for content refreshes based on real signals: pages that have slipped in rankings, pages with outdated statistics or references, and pages targeting queries where competitor content has meaningfully improved. Cover how to distinguish a genuine refresh opportunity from a page that's simply reached a natural ceiling. Give guidance on how substantial a refresh needs to be to actually move rankings versus a superficial update. Close with a realistic cadence for running refresh audits across an existing content library.")

add(26,4,"Aligning Content Strategy With the Buyer Journey, Not Just Search Volume","Content Marketing","content marketing funnel",1000,"content strategy buyer journey stages","funnel content mapping",
    "Aligning Content Strategy With the Buyer Journey | Growpha",
    "Chasing high-volume keywords alone often misses where buyers actually are in their decision process. Here's how to map content to the full buyer journey instead.",
    "content-strategy-buyer-journey-alignment",
    "Challenge the common approach of prioritising content purely by search volume, without considering where in the buyer journey that search intent sits. Give a practical framework for mapping content across awareness, consideration, and decision stages, and matching content format and depth to each. Cover the common gap most B2B content programs have: strong top-of-funnel content but weak decision-stage content that actually supports a sale. Close with how to audit an existing content library against this framework.")

add(28,5,"Aligning Editorial Calendars With Product Launches","Content Marketing","editorial calendar",1900,"content calendar product launch","launch content strategy",
    "Aligning Editorial Calendars With Product Launches | Growpha",
    "Content and product launches often run on separate timelines, missing the window when interest is highest. Here's how to align editorial planning with launches properly.",
    "aligning-editorial-calendars-product-launches",
    "Address the common disconnect between marketing's editorial calendar and product or business development timelines, which means content often arrives too late to capture peak interest around a launch. Give a practical planning framework for building supporting content — announcement pieces, use-case content, and FAQ-style pages — ahead of a launch rather than reactively afterward. Cover how to handle SEO timing specifically, since new pages need lead time to index and rank before the launch moment. Close with a realistic planning lead time to work backward from a launch date.")

add(30,3,"Building Author Authority Signals for E-E-A-T in 2026","Content Marketing","author authority seo",0,"eeat author signals","content author bio seo",
    "Building Author Authority Signals for E-E-A-T | Growpha",
    "Anonymous or thin author bylines undermine E-E-A-T signals Google increasingly weighs. Here's how to build genuine author authority into content.",
    "building-author-authority-signals-eeat",
    "Explain why author-level E-E-A-T signals have become more prominent as Google works to distinguish genuinely expert content from generic or AI-generated filler. Give practical guidance: detailed author bios establishing real credentials, Person schema markup, and consistent author bylines across a body of work that builds recognisable expertise over time. Cover the specific consideration for founder-led content, where the author's personal brand and the company's brand reinforce each other. Close with how this connects to the broader entity-building work already needed for AI search visibility.")

# ---- AI Automations (M1-M14) ----
add(2,4,"Automating SEO Reporting With n8n: A Practical Workflow","AI Automations","seo automation",1900,"n8n seo workflow","automated seo reporting tool",
    "Automating SEO Reporting With n8n: A Practical Workflow | Growpha",
    "Manually pulling SEO reports from multiple tools each week wastes hours. Here's a practical n8n workflow that automates it end to end.",
    "automating-seo-reporting-n8n-workflow",
    "Describe a concrete n8n workflow for automating recurring SEO reporting: pulling data from Search Console and Analytics APIs on a schedule, formatting it into a consistent report structure, and delivering it via email or Slack automatically. Cover the setup effort required versus the ongoing time saved for an agency or in-house team running this weekly or monthly. Give guidance on what to automate versus what still needs human interpretation and commentary. Close with how this frees up time for higher-value analysis work.")

add(4,5,"Python for SEO: Automating Technical Audits at Scale","AI Automations","python for seo",1300,"python seo scripts","technical seo automation python",
    "Python for SEO: Automating Technical Audits at Scale | Growpha",
    "Manual technical audits don't scale past a certain site size. Here's how Python scripting automates the repetitive parts of a technical SEO audit.",
    "python-for-seo-automating-technical-audits",
    "Explain the practical case for Python in technical SEO specifically for large sites where manual review of every page is impossible: automating crawl data analysis, bulk status code checks, and pattern detection across thousands of URLs. Give examples of common audit tasks well-suited to scripting versus those still requiring manual judgement. Cover the realistic learning curve for an SEO professional picking up enough Python for this use case. Close with how this fits into a broader technical SEO workflow alongside tools like Screaming Frog.")

add(7,1,"AI-Assisted Content Briefs: Where Automation Helps and Where It Hurts","AI Automations","ai content briefs",20,"ai generated content briefs","ai content brief tools",
    "AI-Assisted Content Briefs: Where It Helps, Where It Hurts | Growpha",
    "AI can accelerate content brief creation, but leaning on it entirely produces generic briefs. Here's where automation genuinely helps and where it backfires.",
    "ai-assisted-content-briefs-helps-hurts",
    "Give an honest, balanced view of AI's role in content brief creation: genuinely useful for accelerating competitor research summaries and initial subtopic identification, but weak at capturing genuine strategic differentiation or brand-specific angles. Cover the risk of AI-generated briefs converging toward generic, already-published angles rather than genuinely differentiated content. Give a practical hybrid workflow where AI handles research acceleration and a human sets the strategic angle. Close with how to know when a brief has become too generic to produce differentiated content.")

add(9,2,"Automating Rank Tracking and Alert Systems Without Expensive Tools","AI Automations","rank tracking automation",10,"free rank tracking automation","seo alert system",
    "Automating Rank Tracking and Alerts Without Expensive Tools | Growpha",
    "Enterprise rank tracking tools carry a real cost. Here's how to build a lighter-weight automated rank tracking and alert system without that overhead.",
    "automating-rank-tracking-alerts-without-expensive-tools",
    "Address the real cost consideration of enterprise rank tracking tools for smaller businesses and agencies managing lean budgets. Give a practical alternative workflow using automation platforms (n8n or Make) connected to available ranking data sources, with automated alerts triggered by significant ranking drops. Cover the trade-offs of a lighter-weight system compared to a full enterprise tool. Close with when it genuinely makes sense to upgrade to a paid tool versus when the automated lightweight approach is sufficient.")

add(11,3,"Building a Content QA Pipeline With AI Automation","AI Automations","content qa process",0,"ai content quality assurance","automated content review workflow",
    "Building a Content QA Pipeline With AI Automation | Growpha",
    "Manual content QA doesn't scale with higher publishing volume. Here's how to build an AI-assisted quality assurance pipeline that catches real issues.",
    "content-qa-pipeline-ai-automation",
    "Describe a practical content QA workflow using AI automation to catch common issues before publication: broken links, missing metadata, factual inconsistencies flagged for human review, and basic style guide compliance. Cover what should remain a human review step regardless of automation — factual accuracy for sensitive topics and genuine editorial judgement. Give guidance on building this incrementally rather than trying to automate the entire QA process at once. Close with the error patterns Growpha has found this catches most reliably.")

add(13,4,"Automating Internal Link Suggestions With AI Workflows","AI Automations","internal link automation",0,"ai internal linking tool","automated internal link suggestions",
    "Automating Internal Link Suggestions With AI Workflows | Growpha",
    "Manually finding internal linking opportunities across a large content library is slow. Here's how AI-assisted workflows can surface genuine linking opportunities at scale.",
    "automating-internal-link-suggestions-ai",
    "Explain the practical challenge of manual internal link auditing on a large site with hundreds or thousands of pages, and how an AI-assisted workflow can surface genuine, contextually relevant linking opportunities faster than manual review. Cover the risk of over-automating this into unnatural, over-optimised anchor text patterns, and the need for human review before implementation. Give a practical workflow combining a content database, semantic similarity matching, and human approval. Close with the realistic scale at which this automation actually pays off versus when manual linking is still faster.")

add(15,5,"Using AI to Automate Competitor Monitoring at Scale","AI Automations","competitor monitoring tools",1000,"automated competitor tracking","ai competitor analysis workflow",
    "Using AI to Automate Competitor Monitoring at Scale | Growpha",
    "Manually checking competitor rankings, content, and backlinks weekly doesn't scale across multiple competitors. Here's an automated monitoring workflow that does.",
    "automating-competitor-monitoring-ai-scale",
    "Describe a practical automated competitor monitoring workflow covering new content published, ranking movement on shared target keywords, and new backlinks earned, consolidated into a single recurring digest. Cover the strategic value of catching competitor moves quickly versus discovering them months later during a quarterly review. Give guidance on which competitor signals are worth automated tracking versus which need periodic manual deep-dives. Close with how this feeds into a genuinely responsive content and SEO strategy rather than a static annual plan.")

add(18,1,"Automated SEO Audits: What AI Can Catch and What Still Needs a Human","AI Automations","automated seo audit",260,"ai seo audit tool","limits of automated seo audits",
    "Automated SEO Audits: What AI Catches, What Needs a Human | Growpha",
    "AI-powered audit tools catch a lot of technical issues fast, but they still miss strategic judgement calls. Here's an honest breakdown of the current split.",
    "automated-seo-audits-ai-vs-human",
    "Give an honest, current assessment of what automated and AI-assisted audit tools reliably catch — broken links, missing metadata, technical crawl errors, structured data issues — versus what still requires human strategic judgement, like prioritisation, business context, and content quality assessment. Cover the risk of over-relying on an automated audit's output without human interpretation, producing a long list of low-priority issues with no clear roadmap. Give a practical hybrid audit workflow. Close with how Growpha uses automation to speed up, not replace, the audit process.")

add(20,2,"Building a Client Reporting Dashboard With n8n and Google Sheets","AI Automations","seo reporting dashboard",2900,"n8n google sheets dashboard","automated client reporting",
    "Building a Client Reporting Dashboard With n8n and Sheets | Growpha",
    "Manually compiling client SEO reports each month is repetitive and error-prone. Here's how to build a live dashboard using n8n and Google Sheets instead.",
    "client-reporting-dashboard-n8n-google-sheets",
    "Describe a practical setup for a live, automatically-updating client reporting dashboard: n8n workflows pulling data from Search Console, Analytics, and rank tracking sources into a structured Google Sheet, refreshed on a schedule. Cover the advantage for an agency managing multiple clients: consistent reporting format without manual compilation each month. Give guidance on which metrics genuinely belong on a client-facing dashboard versus internal working data. Close with the setup time investment versus ongoing time saved across a client roster.")

add(22,3,"Automating Schema Markup Generation Across Large Sites","AI Automations","schema markup automation",0,"bulk schema markup generation","automated structured data",
    "Automating Schema Markup Generation Across Large Sites | Growpha",
    "Manually writing schema markup for thousands of product or location pages isn't practical. Here's how to automate structured data generation at scale.",
    "automating-schema-markup-generation-large-sites",
    "Explain the practical challenge of implementing structured data across large e-commerce or multi-location sites where manual, page-by-page schema writing isn't feasible. Give a practical approach: templated schema generation driven by existing CMS or database fields, validated in bulk before deployment. Cover common validation pitfalls when automating schema at scale, like missing required fields for edge-case content types. Close with a QA process for catching schema errors before they affect a large number of pages simultaneously.")

add(24,4,"AI Workflow Automation for Local SEO Citation Management","AI Automations","local citation management",210,"automated citation management","ai local seo automation",
    "AI Workflow Automation for Local SEO Citation Management | Growpha",
    "Manually checking and updating business citations across dozens of directories doesn't scale for multi-location businesses. Here's how automation handles it.",
    "ai-workflow-automation-local-citation-management",
    "Describe the practical challenge multi-location businesses face keeping NAP data consistent across dozens of directories, especially after any business detail changes. Give a practical automated workflow for monitoring citation consistency and flagging discrepancies for correction, rather than manual periodic checks. Cover the limits of automation here — actually updating some directories still requires manual or paid-service intervention. Close with how this connects to the broader local SEO citation strategy already covered.")

add(26,5,"Automating Content Distribution Across Multiple Channels","AI Automations","content distribution automation",70,"automated content syndication","multi channel content automation",
    "Automating Content Distribution Across Multiple Channels | Growpha",
    "Manually posting and adapting every piece of content across channels is a real time cost. Here's how to automate distribution without losing quality control.",
    "automating-content-distribution-multiple-channels",
    "Describe a practical automated distribution workflow: triggering social posts, email newsletter inclusion, and internal notification the moment a new piece of content publishes, using automation tools connected to the CMS. Cover the balance between automation efficiency and the quality risk of fully automated, unreviewed distribution copy. Give guidance on which distribution steps are safe to fully automate versus which still need a human review gate. Close with realistic time savings for a lean marketing team.")

add(29,1,"When Automation Makes SEO Worse: The Workflows That Backfire","AI Automations","ai seo mistakes",170,"automation gone wrong seo","ai seo risks",
    "When Automation Makes SEO Worse: Workflows That Backfire | Growpha",
    "Not every SEO automation is a good idea. Here are the specific automated workflows that have actually damaged sites, and how to avoid the same mistakes.",
    "when-automation-makes-seo-worse",
    "Give an honest, cautionary counterpoint to the general enthusiasm for SEO automation, covering real failure cases: fully automated content publishing without review producing thin or duplicate content at scale, automated internal linking creating unnatural patterns, and bulk schema generation shipping errors across thousands of pages before being caught. Explain the common root cause: automating a process before it's been proven and refined manually first. Give a practical framework for deciding what's safe to automate versus what needs a human gate. Close with Growpha's own principle for introducing automation responsibly.")

add(30,4,"Automating A/B Test Analysis for On-Page SEO Changes","AI Automations","seo ab testing",590,"seo split testing automation","automated ab test analysis",
    "Automating A/B Test Analysis for On-Page SEO Changes | Growpha",
    "Manually analysing SEO split test results across many pages and metrics is slow and error-prone. Here's how automation speeds up test analysis reliably.",
    "automating-ab-test-analysis-on-page-seo",
    "Explain the practical use case for SEO A/B testing (testing title tag or on-page changes across a page group) and the analysis burden that comes with interpreting statistical significance across multiple metrics and timeframes. Give a practical automated workflow for pulling test group performance data and flagging statistically meaningful results automatically, rather than manual spreadsheet analysis. Cover the risk of over-trusting automated significance flags without understanding the underlying statistics. Close with how this speeds up the test-and-iterate cycle for on-page SEO changes.")

# ---- Wikipedia Creation (W1-W13) ----
add(2,5,"Wikipedia Notability Guidelines: What Actually Qualifies a Business","Wikipedia Creation","wikipedia notability guidelines",110,"wikipedia notability requirements business","does my business qualify for wikipedia",
    "Wikipedia Notability Guidelines: What Actually Qualifies | Growpha",
    "Most businesses that want a Wikipedia page don't yet meet notability guidelines. Here's what actually qualifies, in plain terms.",
    "wikipedia-notability-guidelines-what-qualifies",
    "Explain Wikipedia's notability guidelines for organisations in plain, practical terms: substantial coverage in multiple independent, reliable secondary sources, not just any media mention. Give concrete examples distinguishing sufficient coverage (in-depth feature articles) from insufficient coverage (press releases, sponsored content, brief mentions). Cover the honest reality that many businesses simply don't yet qualify, and what that means for their options. Close with the assessment process Growpha runs before accepting any Wikipedia engagement.")

add(5,1,"Why Most Wikipedia Article Submissions Get Rejected","Wikipedia Creation","wikipedia article submission",40,"wikipedia article rejected reasons","articles for creation rejection",
    "Why Most Wikipedia Article Submissions Get Rejected | Growpha",
    "The majority of Wikipedia article drafts submitted through Articles for Creation get declined. Here's why, and how to avoid the most common reasons.",
    "why-wikipedia-submissions-get-rejected",
    "Give a realistic breakdown of why most Wikipedia article submissions fail: insufficient sourcing against notability guidelines, promotional tone that fails neutral point of view requirements, and conflict of interest issues when submitted directly by the subject. Cover the specific reviewer expectations that catch first-time submitters off guard. Give practical guidance for improving submission odds: rigorous sourcing first, neutral tone throughout, and transparency about any affiliation. Close with realistic expectations for the review and resubmission process timeline.")

add(7,2,"Building a Source Portfolio Before You Attempt a Wikipedia Article","Wikipedia Creation","wikipedia notability criteria",20,"wikipedia sourcing strategy","secondary sources wikipedia article",
    "Building a Source Portfolio Before a Wikipedia Attempt | Growpha",
    "Attempting a Wikipedia article before the sourcing exists almost guarantees rejection. Here's how to build a credible source portfolio first.",
    "building-source-portfolio-wikipedia-article",
    "Explain why source quality and independence should be assessed and, where needed, built up before ever attempting a Wikipedia submission, rather than writing the article first and hoping sources will suffice. Give practical guidance on what counts as a genuinely independent, reliable secondary source versus what doesn't (owned media, paid placements, press releases). Cover realistic paths to building genuine press coverage if the current portfolio is insufficient. Close with how to honestly assess whether a subject is ready to attempt Wikipedia yet.")

add(9,3,"Wikipedia's Conflict of Interest Rules: What You Can and Can't Do","Wikipedia Creation","wikipedia conflict of interest",30,"wikipedia coi disclosure rules","editing wikipedia about yourself",
    "Wikipedia's Conflict of Interest Rules: What's Allowed | Growpha",
    "Editing a Wikipedia article about your own business carries specific disclosure obligations. Here's exactly what Wikipedia's conflict of interest rules require.",
    "wikipedia-conflict-of-interest-rules-explained",
    "Explain Wikipedia's conflict of interest policy precisely: subjects and their representatives are strongly discouraged from directly editing articles about themselves, and paid editing specifically requires formal disclosure. Cover what is permitted instead — suggesting edits via the talk page, or using the formal paid-editing disclosure process. Give practical guidance for businesses navigating this compliantly. Close with the real reputational risk of violating conflict of interest rules if discovered, which can result in article deletion or a documented COI flag.")

add(13,5,"Wikipedia Article Maintenance: What Happens After Publication","Wikipedia Creation","wikipedia page maintenance",0,"maintaining wikipedia article after publication","wikipedia article ongoing monitoring",
    "Wikipedia Article Maintenance: What Happens After Publication | Growpha",
    "Getting a Wikipedia article published isn't the end of the process. Here's what ongoing maintenance actually looks like, and who's allowed to do it.",
    "wikipedia-article-maintenance-after-publication",
    "Explain that a published Wikipedia article requires ongoing monitoring, since anyone can edit it and inaccurate or outdated information can appear over time. Cover what compliant maintenance looks like given conflict-of-interest restrictions: monitoring for changes, flagging factual errors via the talk page rather than direct edits, and keeping a source portfolio ready for legitimate future updates. Give realistic expectations for how much active maintenance a typical business article needs. Close with how to handle a serious inaccuracy or vandalism situation properly.")

add(18,2,"Why a Wikipedia Presence Matters for AI Search Visibility","Wikipedia Creation","wikipedia ai search",10,"wikipedia ai visibility benefit","wikipedia knowledge graph business",
    "Why a Wikipedia Presence Matters for AI Search Visibility | Growpha",
    "Wikipedia's influence extends well beyond its own traffic, feeding directly into Google's Knowledge Graph and many AI systems. Here's why it still matters.",
    "wikipedia-presence-ai-search-visibility",
    "Connect Wikipedia presence directly to the entity-based understanding both Google's Knowledge Graph and AI systems rely on, explaining why a compliant Wikipedia article can meaningfully improve how confidently these systems represent a business. Cover realistic expectations: Wikipedia alone won't guarantee AI citation, but it's a strong contributing signal within a broader entity strategy. Give guidance on how to think about Wikipedia's ROI beyond its own direct traffic. Close with why this makes notability assessment worth doing properly rather than rushing a submission.")

add(20,3,"Common Wikipedia Editorial Tone Mistakes That Get Articles Flagged","Wikipedia Creation","wikipedia neutral tone",0,"wikipedia promotional tone flagged","neutral point of view wikipedia",
    "Common Wikipedia Editorial Tone Mistakes That Get Flagged | Growpha",
    "Even well-sourced Wikipedia drafts get flagged or rejected for promotional tone. Here are the specific writing patterns that trigger neutrality concerns.",
    "wikipedia-editorial-tone-mistakes-flagged",
    "Give concrete examples of promotional language patterns that violate Wikipedia's neutral point of view policy: superlatives without attribution, marketing-style phrasing, and selectively including only favourable coverage. Contrast these examples with genuinely neutral, encyclopaedic phrasing covering the same facts. Cover why even factually accurate content can still get flagged if the tone reads as promotional. Close with a practical self-editing checklist to run before submitting a draft.")

add(22,4,"Building Credible Secondary Source Coverage Before a Wikipedia Attempt","Wikipedia Creation","wikipedia editor for hire",20,"getting press coverage for wikipedia","secondary source coverage strategy",
    "Building Credible Secondary Source Coverage Before Wikipedia | Growpha",
    "If a subject doesn't yet have enough independent press coverage, the right move is building it first, not rushing a submission. Here's how.",
    "building-secondary-source-coverage-wikipedia",
    "Address the situation where a subject is close to but not yet meeting Wikipedia's sourcing bar, and explain why building genuine, independent press coverage first is the right sequence rather than attempting Wikipedia prematurely. Give practical, legitimate approaches: targeted digital PR toward outlets Wikipedia editors recognise as reliable, and industry press rather than low-quality content mills. Cover realistic timelines for building a sufficient source portfolio this way. Close with how this connects to the broader digital PR discipline already covered in Growpha's off-page work.")

add(24,5,"Wikipedia Deletion Discussions: How to Respond When an Article Is Challenged","Wikipedia Creation","wikipedia articles for deletion",20,"wikipedia afd process","responding to deletion nomination",
    "Wikipedia Deletion Discussions: How to Respond | Growpha",
    "A Wikipedia article being nominated for deletion isn't necessarily fatal, but the response matters. Here's how the Articles for Deletion process works and how to respond properly.",
    "wikipedia-deletion-discussions-how-to-respond",
    "Explain how the Articles for Deletion (AfD) process works: a nomination opens a community discussion where editors weigh in on whether the subject meets notability standards. Cover the compliant way to respond given conflict-of-interest restrictions — providing additional sourcing via the talk page rather than arguing directly in the discussion as the subject. Give realistic guidance on what actually saves an article in these discussions (genuinely stronger sourcing) versus what doesn't (arguing the subject deserves a page). Close with what happens if an article is ultimately deleted and whether a future attempt remains possible.")

add(27,1,"Regional Notability: Getting Wikipedia Coverage for UAE and GCC Businesses","Wikipedia Creation","wikipedia page creation service",140,"uae business wikipedia page","gcc wikipedia notability",
    "Regional Notability: Wikipedia Coverage for UAE and GCC Businesses | Growpha",
    "UAE and GCC businesses face specific notability challenges given the regional media landscape. Here's how regional notability actually works for Wikipedia.",
    "regional-notability-wikipedia-uae-gcc-businesses",
    "Address the specific challenge UAE and GCC businesses often face: a smaller pool of internationally-recognised press compared to US or UK markets, which can make meeting Wikipedia's sourcing bar harder despite genuine regional prominence. Cover which regional publications Wikipedia editors generally regard as reliable secondary sources. Give practical guidance for building a source portfolio that satisfies notability guidelines using a mix of regional and international coverage. Close with realistic expectations for UAE and GCC businesses considering a Wikipedia attempt.")

add(29,2,"Wikidata and Wikipedia: The Entity Signals Most Businesses Ignore","Wikipedia Creation","wikidata seo",30,"wikidata business entry","wikidata vs wikipedia",
    "Wikidata and Wikipedia: The Entity Signals Most Businesses Miss | Growpha",
    "Wikidata is a distinct, structured database many businesses overlook entirely, even after securing a Wikipedia page. Here's why it deserves separate attention.",
    "wikidata-wikipedia-entity-signals-ignored",
    "Explain the distinction between Wikipedia (an encyclopaedia) and Wikidata (a structured, machine-readable database of facts), and why many businesses that secure a Wikipedia page never properly complete or maintain their Wikidata entry. Cover why Wikidata's structured format makes it particularly valuable for machine understanding, including by AI systems and Google's Knowledge Graph. Give practical guidance on setting up and maintaining a Wikidata entry compliantly. Close with how this complements, rather than duplicates, the value of a Wikipedia article.")

# ---- Web Development (D1-D13) ----
add(3,1,"Shopify Core Web Vitals: The Theme-Level Fixes That Actually Work","Web Development","shopify core web vitals",70,"shopify site speed core web vitals","shopify theme performance fixes",
    "Shopify Core Web Vitals: Theme-Level Fixes That Work | Growpha",
    "Most Shopify Core Web Vitals problems trace back to theme choices and app bloat, not Shopify's platform itself. Here's what actually fixes them.",
    "shopify-core-web-vitals-theme-fixes",
    "Clarify that Shopify's platform infrastructure is generally fast, and most Core Web Vitals failures on Shopify stores trace back to theme code quality and third-party app scripts. Give concrete, theme-level fixes: lazy loading images properly, reducing render-blocking JavaScript from apps, and optimising Liquid template efficiency. Cover how to diagnose whether a specific app is causing a CWV problem. Close with a realistic prioritisation for merchants dealing with multiple CWV issues at once.")

add(5,2,"WordPress Performance Optimisation: Beyond Caching Plugins","Web Development","wordpress performance optimization",320,"wordpress speed optimization","wordpress performance beyond caching",
    "WordPress Performance Optimisation: Beyond Caching Plugins | Growpha",
    "Installing a caching plugin is only the first step. Here's what WordPress performance optimisation actually requires beyond that.",
    "wordpress-performance-optimization-beyond-caching",
    "Acknowledge caching as a necessary but insufficient step, then cover what genuinely moves WordPress performance further: database optimisation, image delivery (proper formats and CDN usage), hosting quality, and reducing plugin bloat. Give a practical diagnostic approach for identifying which specific factor is the current bottleneck on a given site. Cover the trade-off between plugin convenience and the performance cost each one adds. Close with a realistic performance optimisation checklist beyond just 'install a caching plugin'.")

add(7,3,"Shopify App Bloat: How Third-Party Apps Are Killing Your Site Speed","Web Development","shopify site speed",70,"shopify app bloat performance","too many shopify apps slow",
    "Shopify App Bloat: How Apps Are Killing Your Site Speed | Growpha",
    "Every Shopify app adds its own script to the page, and most stores accumulate far more than they actively need. Here's how to audit and cut app bloat.",
    "shopify-app-bloat-site-speed",
    "Explain how each installed Shopify app typically injects its own JavaScript, and how this compounds across a typical store that has accumulated apps over years without removing unused ones. Give a practical audit method for identifying which installed apps are actually in active use versus forgotten legacy installs still loading scripts. Cover how to safely remove or replace heavy apps with lighter alternatives or native Shopify functionality. Close with a realistic performance improvement range merchants can expect from a thorough app audit.")

add(9,4,"WordPress SEO Plugins: What They Actually Do (And What They Don't)","Web Development","wordpress seo plugins",2900,"wordpress seo plugin comparison","what seo plugins actually do",
    "WordPress SEO Plugins: What They Actually Do | Growpha",
    "SEO plugins handle useful technical basics but don't do SEO for you. Here's an honest breakdown of what WordPress SEO plugins actually accomplish.",
    "wordpress-seo-plugins-what-they-actually-do",
    "Give an honest, non-promotional breakdown of what popular WordPress SEO plugins genuinely handle well — sitemap generation, basic schema markup, and meta tag management — versus what they can't do, like strategic keyword research, content quality, or link building. Cover the common misconception that installing a plugin and getting a 'green light' score equals good SEO. Give guidance on which plugin features are worth configuring carefully versus which are largely cosmetic. Close with what still requires genuine SEO expertise regardless of which plugin is installed.")

add(11,5,"Shopify URL Structure and SEO: The Architecture Decisions That Matter","Web Development","shopify url structure",70,"shopify url structure seo","shopify collection url best practices",
    "Shopify URL Structure and SEO: What Actually Matters | Growpha",
    "Shopify's platform constraints limit some URL structure choices, but the ones merchants do control matter for SEO. Here's what to get right.",
    "shopify-url-structure-seo-architecture",
    "Explain Shopify's platform-level URL structure constraints (fixed /products/ and /collections/ prefixes that can't be fully customised) and what that means for realistic SEO expectations. Cover the URL decisions merchants do control: individual product and collection handle naming, and how to keep them clean and keyword-relevant. Address common URL structure mistakes specific to Shopify stores, like inconsistent handle naming conventions across a large catalogue. Close with how much URL structure genuinely matters relative to other Shopify SEO priorities.")

add(14,1,"Headless WordPress: Is It Worth It for SEO in 2026?","Web Development","headless wordpress seo",40,"headless wordpress pros cons","headless cms seo impact",
    "Headless WordPress: Is It Worth It for SEO in 2026? | Growpha",
    "Headless WordPress promises performance gains but introduces real SEO implementation complexity. Here's an honest assessment of the trade-off in 2026.",
    "headless-wordpress-worth-it-seo-2026",
    "Give a balanced, current assessment of headless WordPress for SEO: the genuine performance and flexibility benefits of decoupling the frontend, weighed against the real implementation complexity of correctly handling metadata, structured data, and rendering that traditional WordPress themes handle automatically. Cover the specific technical risks: broken canonical tags, missing schema, or rendering issues if the headless frontend isn't built with SEO as a first-class concern. Give guidance on when headless is genuinely worth the investment versus when traditional WordPress remains the more pragmatic choice. Close with what to require from a development team building a headless SEO-critical site.")

add(16,2,"Shopify Collection Pages: The SEO Structure Most Stores Get Wrong","Web Development","shopify collection page seo",30,"shopify collection page optimization","collection page seo structure",
    "Shopify Collection Pages: The SEO Structure Most Get Wrong | Growpha",
    "Collection pages are often a Shopify store's strongest organic entry points, yet most treat them as an afterthought. Here's the structure that actually works.",
    "shopify-collection-pages-seo-structure",
    "Explain why collection pages are frequently a Shopify store's highest-potential organic pages, since they target broader category-level search intent that product pages can't capture as effectively. Cover the common mistakes: thin or missing collection descriptions, no unique content differentiating similar collections, and weak internal linking into and between collections. Give a practical collection page optimisation structure: unique intro copy, faceted navigation handling, and strategic internal links to related collections and top products. Close with how to prioritise which collections deserve the most SEO investment.")

add(18,3,"WordPress Site Migrations Without Losing Rankings","Web Development","wordpress migration seo",0,"wordpress migration checklist seo","wordpress site move rankings",
    "WordPress Site Migrations Without Losing Rankings | Growpha",
    "WordPress migrations — hosting changes, redesigns, or platform moves — carry real ranking risk if not handled carefully. Here's how to do it without losing traffic.",
    "wordpress-site-migrations-without-losing-rankings",
    "Give a practical WordPress-specific migration checklist covering the scenarios that commonly trigger a migration: hosting provider changes, theme or full redesign projects, and moving from WordPress.com to self-hosted or vice versa. Cover URL preservation and redirect mapping as the highest-priority step, along with re-verifying Search Console and resubmitting sitemaps post-migration. Address WordPress-specific pitfalls like plugin conflicts introduced during the move affecting rendering. Close with the post-migration monitoring window to watch closely.")

add(20,4,"Shopify Theme Selection: The Performance Factors Most Merchants Ignore","Web Development","shopify theme performance",20,"fastest shopify themes seo","shopify theme selection performance",
    "Shopify Theme Selection: Performance Factors Most Ignore | Growpha",
    "Theme selection happens early and is rarely revisited, even though it sets a performance ceiling for everything built on top. Here's what to actually evaluate.",
    "shopify-theme-selection-performance-factors",
    "Explain why theme choice sets a meaningful performance ceiling that later optimisation work can only partially compensate for, making it worth evaluating carefully upfront rather than by visual design alone. Give practical evaluation criteria: baseline Core Web Vitals scores before any customisation, code quality and how efficiently the theme handles common features like filtering, and how well it's maintained by its developer. Cover the trade-off between heavily-featured themes and genuinely fast, lean ones. Close with how to test a theme's real-world performance before committing a store's design to it.")

add(22,5,"WordPress Multisite and SEO: The Architecture Considerations","Web Development","wordpress multisite seo",70,"wordpress multisite seo pros cons","multisite architecture seo",
    "WordPress Multisite and SEO: Architecture Considerations | Growpha",
    "WordPress Multisite offers real operational benefits for managing multiple related sites, but it introduces specific SEO architecture decisions. Here's what to consider.",
    "wordpress-multisite-seo-architecture",
    "Explain what WordPress Multisite actually is and the operational case for using it — managing multiple related sites (multi-brand, multi-region) from one shared installation. Cover the SEO-specific considerations: whether subdomains or subdirectories should be used for the network's sites, how canonical and hreflang considerations apply across the network, and shared versus independent SEO plugin configuration per site. Give guidance on when Multisite's operational convenience is worth the added SEO architecture complexity versus separate standalone installations. Close with a realistic use case where Multisite makes sense for a growing multi-brand business.")

add(25,1,"Shopify Metafields for SEO: An Underused Optimisation Layer","Web Development","shopify metafields",260,"shopify metafields seo use","custom metafields shopify",
    "Shopify Metafields for SEO: An Underused Layer | Growpha",
    "Metafields let merchants store structured, page-specific data beyond Shopify's default fields, and most stores never use them for SEO. Here's how they help.",
    "shopify-metafields-seo-underused-layer",
    "Explain what Shopify metafields are in practical terms — custom structured fields attached to products, collections, or pages beyond the platform's defaults — and why most merchants never use them for SEO purposes. Give concrete SEO use cases: structured data enrichment (additional product attributes for schema), and dynamic, unique meta description generation at scale for large catalogues. Cover the technical setup required, including theme code changes to actually surface metafield data. Close with a realistic use case for a large product catalogue where metafields solve a genuine scaling problem.")

add(27,2,"Custom Post Types in WordPress: Structuring Content for SEO","Web Development","wordpress custom post types",110,"custom post type seo benefits","wordpress content type structure",
    "Custom Post Types in WordPress: Structuring for SEO | Growpha",
    "Forcing every content type into the default Post or Page structure limits both usability and SEO structure. Here's how custom post types help.",
    "custom-post-types-wordpress-seo-structure",
    "Explain the practical case for custom post types over cramming distinct content types (case studies, team members, locations) into generic Posts or Pages: cleaner information architecture, dedicated templates, and clearer topical grouping for search engines. Cover the SEO-specific considerations: ensuring custom post type archives are properly indexable and internally linked, and that they're included correctly in the XML sitemap. Give a practical example of when a business should introduce a custom post type versus when a standard page suffices. Close with common technical pitfalls when custom post types are added without SEO configuration.")

add(29,3,"Shopify vs Headless Commerce: The SEO Trade-Offs for Enterprise Retailers","Web Development","headless commerce",2900,"shopify vs headless seo comparison","enterprise ecommerce platform seo",
    "Shopify vs Headless Commerce: SEO Trade-Offs for Enterprise | Growpha",
    "Enterprise retailers evaluating headless commerce face real SEO trade-offs against Shopify's more turnkey approach. Here's an honest comparison.",
    "shopify-vs-headless-commerce-seo-tradeoffs",
    "Give a balanced comparison for enterprise retailers specifically weighing standard Shopify (or Shopify Plus) against a headless commerce architecture: the performance and customisation ceiling headless can offer, against the implementation complexity and SEO risk if the frontend team doesn't prioritise technical SEO fundamentals. Cover realistic scenarios where headless's benefits justify the added complexity versus when a well-optimised standard Shopify Plus setup is the more pragmatic choice. Give guidance on what to require from a headless implementation to protect SEO fundamentals. Close with how Growpha advises enterprise clients evaluating this decision.")

# ---- Missing rows (backfilled) ----
add(9,1,"Building a Content Calendar Around Search Intent, Not Just Keywords","Content Marketing","content calendar",12100,"search intent content planning","editorial calendar search intent",
    "Building a Content Calendar Around Search Intent | Growpha",
    "Most content calendars are organised around publishing frequency, not search intent. Here's how to build one around what searchers actually need.",
    "content-calendar-search-intent",
    "Challenge the common practice of building a content calendar purely around a publishing cadence (e.g. two posts a week) rather than around genuine search intent and topical coverage. Give a practical framework for planning content around intent clusters — informational, commercial, and transactional — mapped to the buyer journey. Cover how this produces a more coherent, authority-building calendar than frequency-driven planning alone. Close with a simple planning template combining keyword research and intent mapping.")

add(11,4,"The Difference Between Press Coverage and Wikipedia-Grade Sourcing","Wikipedia Creation","wikipedia reliable sources",170,"press coverage vs wikipedia sources","what counts as reliable source wikipedia",
    "Press Coverage vs Wikipedia-Grade Sourcing: The Real Difference | Growpha",
    "Being featured in the press doesn't automatically mean the coverage qualifies for Wikipedia. Here's the real difference between the two standards.",
    "press-coverage-vs-wikipedia-grade-sourcing",
    "Explain why general press coverage and Wikipedia-grade sourcing are not the same standard: Wikipedia requires independent, secondary, in-depth coverage, which excludes sponsored content, press releases republished as articles, and brief mentions. Give concrete examples distinguishing sufficient coverage from insufficient coverage using realistic scenarios. Cover why businesses are often surprised their existing press coverage doesn't clear the bar. Close with practical guidance for building coverage that genuinely meets the higher standard.")

add(14,5,"E-E-A-T Signals: What They Actually Look Like on a Page","On-Page SEO","eeat seo",1000,"eeat signals examples","experience expertise authoritativeness trust",
    "E-E-A-T Signals: What They Actually Look Like on a Page | Growpha",
    "E-E-A-T isn't a direct ranking factor you can tick off, but it shapes quality signals Google evaluates. Here's what it concretely looks like on a real page.",
    "eeat-signals-what-they-look-like",
    "Clarify that E-E-A-T (Experience, Expertise, Authoritativeness, Trust) is a quality framework from Google's rater guidelines, not a direct algorithmic ranking factor to optimise in isolation. Give concrete, visible examples of what strong E-E-A-T looks like on a page: detailed author bios, first-hand experience demonstrated in the content itself, citations to credible sources, and clear business transparency. Cover the sectors where E-E-A-T scrutiny is highest (YMYL topics like finance and health). Close with a practical page-level E-E-A-T checklist.")

add(16,1,"Notability for Executives and Founders: A Different Standard Than Companies","Wikipedia Creation","personal wikipedia page",20,"executive wikipedia notability","founder wikipedia page requirements",
    "Notability for Executives and Founders: A Different Standard | Growpha",
    "Wikipedia's notability bar for individuals differs meaningfully from the bar for companies. Here's what executives and founders specifically need.",
    "notability-executives-founders-different-standard",
    "Explain that Wikipedia's notability guidelines for people (WP:BIO) differ from those for organisations, often requiring coverage of the individual specifically, not just their company. Cover the common mistake of assuming a well-covered company automatically qualifies its founder for a personal page. Give practical guidance on what kind of individual-focused coverage actually helps meet this bar. Close with when it makes more sense to pursue a company page only versus attempting both.")

add(19,4,"Video Engagement Signals: What YouTube's Algorithm Actually Measures","YouTube SEO","youtube audience retention",70,"youtube engagement metrics algorithm","audience retention youtube ranking",
    "Video Engagement Signals: What YouTube's Algorithm Measures | Growpha",
    "Views alone don't drive YouTube's recommendation system. Here's what engagement signals the algorithm actually weighs most heavily.",
    "video-engagement-signals-youtube-algorithm",
    "Explain which engagement signals YouTube's algorithm weighs most heavily beyond raw view count: audience retention curves, session duration after watching, and interaction signals like comments and shares. Cover how retention graphs specifically reveal where viewers drop off, and why that data should directly inform future content and editing decisions. Give practical guidance for improving retention through pacing and structure. Close with why chasing views alone without retention is a losing long-term strategy on the platform.")

add(26,3,"AI Citation Tracking: The Tools That Actually Measure LLM Visibility","AI/LLM SEO","ai citation tracking tools",70,"track ai citations tools","llm visibility monitoring",
    "AI Citation Tracking: Tools That Measure LLM Visibility | Growpha",
    "Measuring whether AI tools cite your content is still an emerging discipline. Here's the current landscape of tools and methods that actually work.",
    "ai-citation-tracking-tools-llm-visibility",
    "Give an honest, current overview of the emerging AI citation tracking tool landscape, acknowledging this space is still maturing compared to established rank tracking. Cover practical manual monitoring methods businesses can use in the meantime: running consistent test queries across major AI tools and logging citation patterns over time. Give guidance on what to prioritise tracking given limited tooling maturity. Close with how this monitoring should evolve as dedicated tools become more reliable.")

with open('/tmp/blog_calendar_full.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Day','Order','Title','Pillar','Main Keyword','Search Volume (US)','Secondary Keyword 1','Secondary Keyword 2','Meta Title','Meta Description','URL Slug','Content Brief'])
    rows_sorted = sorted(rows, key=lambda r: (r[0], r[1]))
    for r in rows_sorted:
        writer.writerow(r)

print(f"Wrote {len(rows)} rows")
