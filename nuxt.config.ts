// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: {
    enabled: true,

    timeline: {
      enabled: true,
    },
  },
  image: {
    format: ['webp'],
    quality: 80,
    screens: {
      'xs': 320,
      'sm': 640,
      'md': 768,
      'lg': 1024,
      'xl': 1280,
      '2xl': 1536
    }
  },
  nitro: {
    compressPublicAssets: true,
    minify: true
  },
  app: {
    head: {
      htmlAttrs: {
        lang: 'fr'
      },
      charset: 'utf-8',
      viewport: 'width=device-width, initial-scale=1',
      link: [
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: true }
      ]
    },
    pageTransition: { name: 'page', mode: 'out-in' }
  },
  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxt/image',
    '@nuxt/content',
    'vuetify-nuxt-module',
    '@vueuse/nuxt',
    '@nuxtjs/sitemap'
  ],
  build: {
    transpile: ['vue'],
    extractCSS: true,
    optimizeCSS: true
  },
  experimental: {
    payloadExtraction: true,
    renderJsonPayloads: true
  },
  performance: {
    gzip: true
  },
  sitemap: {
    hostname: 'https://brasseriechezu.fr',
    gzip: true,
    exclude: [
      '/assets/**'
    ],
    routes: [
      {
        url: '/',
        changefreq: 'weekly',
        priority: 1
      },
      {
        url: '/menu',
        changefreq: 'weekly',
        priority: 0.9
      }
    ]
  }
})