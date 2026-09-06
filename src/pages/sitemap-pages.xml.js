// Static top-level pages: home, who-am-i, contact, request-audit, news.
// Blog posts live in sitemap-blog.xml, service pages live in sitemap-services.xml.
const STATIC_PATHS = ['/', '/who-am-i/', '/contact/', '/request-audit/', '/news/'];

export async function GET(context) {
	const site = context.site;
	const urls = STATIC_PATHS.map((path) => `<url><loc>${new URL(path, site).href}</loc></url>`).join('');

	const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${urls}</urlset>`;

	return new Response(xml, {
		headers: { 'Content-Type': 'application/xml' },
	});
}
