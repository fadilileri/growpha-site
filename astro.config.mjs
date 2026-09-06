// @ts-check

import mdx from '@astrojs/mdx';
import { defineConfig, fontProviders } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
// Sitemaps are hand-rolled as endpoints (src/pages/sitemap-*.xml.js), split by
// section (pages/services/blog) with a sitemap-index.xml pointing at all three,
// so @astrojs/sitemap's single auto-generated file isn't used.
export default defineConfig({
  site: 'https://growpha.com',
  integrations: [mdx()],

  redirects: {
    '/about': '/who-am-i',
  },

  fonts: [
      {
          provider: fontProviders.google(),
          name: 'Space Grotesk',
          cssVariable: '--font-heading',
          fallbacks: ['sans-serif'],
          weights: [400, 500, 600, 700, 800],
      },
      {
          provider: fontProviders.google(),
          name: 'DM Sans',
          cssVariable: '--font-body',
          fallbacks: ['sans-serif'],
          weights: [300, 400, 500, 600, 700],
      },
	],

  vite: {
    plugins: [tailwindcss()],
  },
});