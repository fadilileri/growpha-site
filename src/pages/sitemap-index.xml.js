// Index referencing the three split sitemaps: pages, services, blog.
const CHILD_SITEMAPS = ['/sitemap-pages.xml', '/sitemap-services.xml', '/sitemap-blog.xml'];

export async function GET(context) {
	const site = context.site;
	const entries = CHILD_SITEMAPS.map((path) => `<sitemap><loc>${new URL(path, site).href}</loc></sitemap>`).join(
		''
	);

	const xml = `<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${entries}</sitemapindex>`;

	return new Response(xml, {
		headers: { 'Content-Type': 'application/xml' },
	});
}
