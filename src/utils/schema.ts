// Sitewide schema.org nodes. Every page that outputs JSON-LD imports these so the
// Organization, Person and WebSite nodes (and their @id values) stay identical everywhere.
// Link direction is one way on purpose: ProfessionalService.founder -> Person. Person has no
// worksFor back to the organisation, which would create a reference loop.

export const SITE_URL = 'https://growpha.com';
export const ORG_ID = `${SITE_URL}/#organization`;
export const WEBSITE_ID = `${SITE_URL}/#website`;
export const PERSON_ID = `${SITE_URL}/who-am-i/#person`;

export const areaServed = [
	{ '@type': 'City', name: 'Dubai' },
	{ '@type': 'Country', name: 'United Arab Emirates' },
];

export const organization = {
	'@type': 'ProfessionalService',
	'@id': ORG_ID,
	name: 'Growpha',
	url: `${SITE_URL}/`,
	logo: { '@type': 'ImageObject', url: `${SITE_URL}/logo.png` },
	description: 'Technical SEO, AI search optimisation and digital growth consultancy based in Dubai.',
	telephone: '+971522418594',
	founder: { '@id': PERSON_ID },
	areaServed,
};

export const person = {
	'@type': 'Person',
	'@id': PERSON_ID,
	name: 'Fadil İleri',
	jobTitle: 'Founder, Technical SEO & Digital Growth Strategist',
	url: `${SITE_URL}/who-am-i/`,
	sameAs: ['https://www.linkedin.com/in/fadilileri34/'],
	knowsAbout: [
		'Generative engine optimisation',
		'AI search visibility',
		'ChatGPT visibility',
		'AI visibility',
	],
};

export const website = {
	'@type': 'WebSite',
	'@id': WEBSITE_ID,
	url: `${SITE_URL}/`,
	name: 'Growpha',
	publisher: { '@id': ORG_ID },
};
