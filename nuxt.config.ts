const isProduction = process.env.NODE_ENV !== 'development'

export default defineNuxtConfig({
  ssr: true,
  compatibilityDate: '2024-04-03',
  devtools: {
    enabled: isProduction,
    timeline: {
      enabled: isProduction,
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
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' },
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
      name: 'Brasserie Chez Ju',
      short_name: 'Chez Ju',
      description: 'Restaurant traditionnel à Carcassonne',
      theme_color: '#EA5C0B',
      background_color: '#000000',
      icons: [
        {
          src: 'android-chrome-192x192.png',
          sizes: '192x192',
          type: 'image/png'
        },
        {
          src: 'android-chrome-512x512.png',
          sizes: '512x512',
          type: 'image/png'
        }
      ]
    },
    workbox: {
      globPatterns: ['**/*.{js,css,html,ico,png,svg}'],
      globIgnores: ['**/images/**/*.{jpg,jpeg,png,gif}'],
      runtimeCaching: [{
        urlPattern: '/_ipx/**',
        handler: 'CacheFirst',
        options: {
          cacheName: 'ipx-images',
          expiration: {
            maxEntries: 100,
            maxAgeSeconds: 60 * 60 * 24 * 30 // 30 jours
          }
        }
      }]
    },
    devOptions: {
      enabled: isProduction,
      type: 'module',
      suppressWarnings: true
    }
  },
  experimental: {
    treeshakeClientOnly: true,
    viewTransition: true,
    renderJsonPayloads: true,
    payloadExtraction: true
  },
  routeRules: {
    '/**': { 
      prerender: true,
      cache: {
        maxAge: 60 * 60 * 24 * 7 // 7 jours
      }
    },
    '/': { 
      prerender: true,
      cache: {
        maxAge: 60 * 60 * 24 // 1 jour
      }
    }
  },
  vite: {
    build: {
      cssMinify: true,
      cssCodeSplit: true,
      minify: 'terser',
      terserOptions: {
        compress: {
          drop_console: true,
          drop_debugger: true
        }
      },
      rollupOptions: {
        output: {
          manualChunks: {
            'vendor': ['@vueuse/core', 'vuetify']
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
  },
  devServer: {
    port: 3300
  }
})
