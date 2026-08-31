// @ts-check

import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import { defineConfig, fontProviders } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://example.com',
  integrations: [mdx(), sitemap()],

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