<script setup>
useHead({
  title: 'Brasserie Chez Ju - Restaurant traditionnel à Carcassonne',
  meta: [
    { name: 'description', content: 'Restaurant traditionnel à Carcassonne proposant une cuisine généreuse avec des produits locaux de qualité. Menu du jour, carte et formules.' },
    { name: 'keywords', content: 'restaurant carcassonne, brasserie, cuisine traditionnelle, produits locaux, menu du jour' },
    { property: 'og:title', content: 'Brasserie Chez Ju - Restaurant traditionnel à Carcassonne' },
    { property: 'og:description', content: 'Restaurant traditionnel à Carcassonne proposant une cuisine généreuse avec des produits locaux de qualité.' },
    { property: 'og:image', content: '/images/display/restaurant-interieur.jpg' },
    { property: 'og:url', content: 'https://brasseriechezu.fr' },
    { name: 'twitter:card', content: 'summary_large_image' },
    { name: 'twitter:title', content: 'Brasserie Chez Ju - Restaurant traditionnel à Carcassonne' },
    { name: 'twitter:description', content: 'Restaurant traditionnel à Carcassonne proposant une cuisine généreuse avec des produits locaux de qualité.' },
    { name: 'twitter:image', content: '/images/display/restaurant-interieur.jpg' }
  ],
  link: [
    { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
    { rel: 'canonical', href: 'https://brasseriechezu.fr' },
    { 
      rel: 'preload', 
      as: 'font',
      href: '/fonts/DancingScript-Bold.ttf',
      type: 'font/ttf',
      crossorigin: 'anonymous'
    }
  ]
})
</script>

<template>
  <div>
    <NavbarComponent />
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<style>
html {
  scroll-behavior: smooth;
}

body {
  @apply bg-gray-500 text-white font-sans antialiased;
}

/* Optimisation du FCP (First Contentful Paint) */
@font-face {
  font-family: 'Dancing Script';
  font-display: swap;
  src: url('/fonts/DancingScript-Bold.ttf') format('ttf');
  font-weight: 700;
  font-style: normal;
}

/* Préchargement des images critiques */
@media (prefers-reduced-motion: no-preference) {
  .preload-animation {
    animation-duration: 0.3s;
    animation-fill-mode: both;
  }
}
</style>
