import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const blog = defineCollection({
	// Load Markdown and MDX files in the `src/content/blog/` directory.
	loader: glob({ base: './src/content/blog', pattern: '**/*.{md,mdx}' }),
	// Type-check frontmatter using a schema
	schema: ({ image }) =>
		z.object({
			title: z.string(),
			description: z.string(),
			// Transform string to Date object
			pubDate: z.coerce.date(),
			updatedDate: z.coerce.date().optional(),
			heroImage: z.optional(image()),
			// SEO: [main keyword, secondary keyword 1, secondary keyword 2, ...]
			keywords: z.array(z.string()).optional(),
			// Badge shown on the blog detail page (e.g. 'SEO', 'AI Automations')
			category: z.string().optional(),
			// "AI Summary" tab content
			aiSummary: z
				.object({
					tldr: z.string(),
					keyTakeaways: z.array(z.string()),
					readingLevel: z.string().optional(),
				})
				.optional(),
			// "Definitions" tab content
			definitions: z
				.array(
					z.object({
						term: z.string(),
						definition: z.string(),
					}),
				)
				.optional(),
			// "AI + SEO Data" tab: AI content quality assessment cards (metrics are computed automatically)
			qualityAssessment: z
				.array(
					z.object({
						label: z.string(),
						score: z.number(),
						description: z.string(),
					}),
				)
				.optional(),
		}),
});

export const collections = { blog };
