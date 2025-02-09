<script setup lang="ts">
import { useHead } from '#imports'

const route = useRoute()

// Lazy load components that are not immediately visible
const ShowcaseComponent = defineAsyncComponent(() => import('../components/ShowcaseComponent.vue'))
const StaffComponent = defineAsyncComponent(() => import('../components/StaffComponent.vue'))
const InstagramFeedComponent = defineAsyncComponent(() => import('../components/InstagramFeedComponent.vue'))
const ContactComponent = defineAsyncComponent(() => import('../components/ContactComponent.vue'))

// SEO
definePageMeta({
  title: 'Brasserie Chez Ju - Restaurant traditionnel à Carcassonne',
  meta: [
    { name: 'description', content: 'Bienvenue à la Brasserie Chez Ju, votre restaurant traditionnel à Carcassonne. Cuisine authentique, produits frais et locaux, ambiance chaleureuse.' },
    { property: 'og:title', content: 'Brasserie Chez Ju - Restaurant traditionnel à Carcassonne' },
    { property: 'og:description', content: 'Bienvenue à la Brasserie Chez Ju, votre restaurant traditionnel à Carcassonne. Cuisine authentique et produits locaux.' }
  ]
})
</script>

<template>
  <div class="home-page">
    <DisplayComponent />
    <ShowcaseComponent />
    <HeroComponent />
    <StaffComponent />
    <InstagramFeedComponent />
    <ContactComponent />
  </div>
</template>