import { getCollection } from 'astro:content';

// Blog index plus every published post, with lastmod dates where we have them.
function toLastmod(date) {
	if (!date) return null;
	const d = new Date(date);
	if (Number.isNaN(d.getTime())) return null;
	return d.toISOString().split('T')[0];
}

export async function GET(context) {
	const site = context.site;
	const posts = await getCollection('blog');

	const postEntries = posts.map((post) => {
		const lastmod = toLastmod(post.data.updatedDate ?? post.data.pubDate);
		const loc = new URL(`/blog/${post.id}/`, site).href;
		return `<url><loc>${loc}</loc>${lastmod ? `<lastmod>${lastmod}</lastmod>` : ''}</url>`;
	});

	const urls = [`<url><loc>${new URL('/blog/', site).href}</loc></url>`, ...postEntries].join('');

	const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${urls}</urlset>`;

	return new Response(xml, {
		headers: { 'Content-Type': 'application/xml' },
	});
}
