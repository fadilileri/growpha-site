// Service pages: /services/ index plus every individual service page.
const SERVICE_SLUGS = [
	'ai-automations',
	'ai-llm-seo',
	'content-marketing',
	'international-seo',
	'local-seo',
	'off-page-seo',
	'on-page-seo',
	'seo',
	'shopify-development',
	'technical-seo',
	'web-development',
	'wikipedia-creation',
	'wordpress-development',
	'youtube-seo',
];

export async function GET(context) {
	const site = context.site;
	const paths = ['/services/', ...SERVICE_SLUGS.map((slug) => `/services/${slug}/`)];
	const urls = paths.map((path) => `<url><loc>${new URL(path, site).href}</loc></url>`).join('');

	const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${urls}</urlset>`;

	return new Response(xml, {
		headers: { 'Content-Type': 'application/xml' },
	});
}
