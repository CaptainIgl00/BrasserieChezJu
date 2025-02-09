// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: {
    enabled: true,
    timeline: {
      enabled: true,
    },
  },
  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxt/image',
    '@nuxt/content',
    'vuetify-nuxt-module',
    '@vueuse/nuxt',
    '@nuxtjs/sitemap',
    '@vite-pwa/nuxt'
  ],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
      'postcss-preset-env': {
        stage: 1
      }
    }
  },
  image: {
    provider: 'ipx',
    dir: 'public',
    screens: {
      xs: 320,
      sm: 640,
      md: 768,
      lg: 1024,
      xl: 1280,
      xxl: 1536,
    },
    presets: {
      showcase: {
        modifiers: {
          format: 'webp',
          quality: '80',
          loading: 'lazy'
        }
      }
    }
  },
  app: {
    head: {
      htmlAttrs: {
        lang: 'fr'
      },
      charset: 'utf-8',
      viewport: 'width=device-width, initial-scale=1',
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
        { rel: 'icon', type: 'image/png', sizes: '16x16', href: '/favicon-16x16.png' },
        { rel: 'icon', type: 'image/png', sizes: '32x32', href: '/favicon-32x32.png' },
        { rel: 'icon', type: 'image/png', sizes: '192x192', href: '/favicon-192x192.png' },
        { rel: 'icon', type: 'image/png', sizes: '512x512', href: '/favicon-512x512.png' },
        { rel: 'apple-touch-icon', sizes: '180x180', href: '/apple-touch-icon.png' },
      ],
      meta: [
        { name: 'theme-color', content: '#000000' },
      ]
    },
    pageTransition: { name: 'page', mode: 'out-in' }
  },
  sitemap: {
    urls: ['/', '/menu']
  },
  pwa: {
    manifest: {
      name: 'Chez Ju',
      short_name: 'Chez Ju',
      description: 'Brasserie - Bar - Tapas',
      theme_color: '#000000',
      background_color: '#000000',
      display: 'standalone',
      orientation: 'portrait',
      icons: [
        {
          src: '/favicon-192x192.png',
          sizes: '192x192',
          type: 'image/png'
        },
        {
          src: '/favicon-512x512.png',
          sizes: '512x512',
          type: 'image/png'
        }
      ]
    },
    workbox: {
      navigateFallback: '/',
      globPatterns: [
        '**/*.{js,css}',
        'images/**/*.{png,jpg,jpeg,svg,gif,webp}'
      ],
      runtimeCaching: [
        {
          urlPattern: /^\/$/,
          handler: 'NetworkFirst',
          options: {
            cacheName: 'pages'
          }
        },
        {
          urlPattern: /^\/menu$/,
          handler: 'NetworkFirst',
          options: {
            cacheName: 'pages'
          }
        },
        {
          urlPattern: /\/_nuxt\//,
          handler: 'CacheFirst',
          options: {
            cacheName: 'nuxt-assets'
          }
        },
        {
          urlPattern: /\/images\//,
          handler: 'CacheFirst',
          options: {
            cacheName: 'images',
            expiration: {
              maxEntries: 50,
              maxAgeSeconds: 7 * 24 * 60 * 60 // 7 jours
            }
          }
        }
      ]
    },
    devOptions: {
      enabled: true,
      type: 'module',
      suppressWarnings: true
    }
  },
  experimental: {
    treeshakeClientOnly: true,
    viewTransition: true,
    renderJsonPayloads: true
  },
  routeRules: {
    '/**': { 
      prerender: true 
    }
  },
  vite: {
    build: {
      cssMinify: true,
      cssCodeSplit: true,
      rollupOptions: {
        output: {
          manualChunks: {
            'vendor-group': ['@vueuse/core']
          }
        }
      },
      chunkSizeWarningLimit: 1000
    },
    css: {
      devSourcemap: false
    },
    optimizeDeps: {
      include: ['@vueuse/core'],
      exclude: ['vuetify']
    }
  }
})