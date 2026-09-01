export interface ContentMetrics {
	wordCount: number;
	readingTimeMinutes: number;
	headings: number;
	paragraphs: number;
	links: number;
	images: number;
	sentences: number;
	fleschScore: number;
	fleschLabel: string;
}

function countSyllables(word: string): number {
	const w = word.toLowerCase().replace(/[^a-z]/g, '');
	if (!w) return 0;
	const groups = w.match(/[aeiouy]+/g);
	let count = groups ? groups.length : 1;
	if (w.endsWith('e') && count > 1) count -= 1;
	return Math.max(count, 1);
}

function fleschLabel(score: number): string {
	if (score >= 90) return 'Very Easy';
	if (score >= 80) return 'Easy';
	if (score >= 70) return 'Fairly Easy';
	if (score >= 60) return 'Standard';
	if (score >= 50) return 'Fairly Difficult';
	if (score >= 30) return 'Difficult';
	return 'Very Confusing';
}

/** Computes reading/SEO metrics from raw markdown body text. */
export function computeMetrics(markdown: string): ContentMetrics {
	const headings = (markdown.match(/^#{1,6}\s+.+$/gm) || []).length;
	const images = (markdown.match(/!\[[^\]]*\]\([^)]*\)/g) || []).length;
	// Links, excluding images (images also match the link pattern minus the leading !)
	const allLinks = markdown.match(/(?<!!)\[[^\]]*\]\([^)]*\)/g) || [];
	const links = allLinks.length;

	// Strip markdown syntax to get plain text for word/sentence/paragraph counts.
	const plain = markdown
		.replace(/^---[\s\S]*?---/, '') // frontmatter
		.replace(/!\[[^\]]*\]\([^)]*\)/g, '') // images
		.replace(/\[([^\]]*)\]\([^)]*\)/g, '$1') // links -> keep text
		.replace(/^#{1,6}\s+/gm, '') // headings markers
		.replace(/[*_`]/g, '') // emphasis/code markers
		.replace(/^>\s?/gm, '') // blockquote markers
		.replace(/^[-*+]\s+/gm, '') // bullet markers
		.replace(/^\d+\.\s+/gm, '') // numbered list markers
		.trim();

	const words = plain.split(/\s+/).filter(Boolean);
	const wordCount = words.length;

	const sentenceMatches = plain.match(/[^.!?]+[.!?]+/g);
	const sentences = sentenceMatches ? sentenceMatches.length : Math.max(1, Math.round(wordCount / 20));

	const paragraphs = markdown
		.replace(/^---[\s\S]*?---/, '')
		.split(/\n\s*\n/)
		.map((b) => b.trim())
		.filter((b) => b.length > 0 && !/^#{1,6}\s/.test(b) && !/^[-*+]\s/.test(b) && !/^\d+\.\s/.test(b)).length;

	const totalSyllables = words.reduce((sum, w) => sum + countSyllables(w), 0);
	const rawScore =
		206.835 - 1.015 * (wordCount / Math.max(sentences, 1)) - 84.6 * (totalSyllables / Math.max(wordCount, 1));
	const fleschScore = Math.max(0, Math.min(100, Math.round(rawScore)));

	const readingTimeMinutes = Math.max(1, Math.round(wordCount / 200));

	return {
		wordCount,
		readingTimeMinutes,
		headings,
		paragraphs,
		links,
		images,
		sentences,
		fleschScore,
		fleschLabel: fleschLabel(fleschScore),
	};
}
