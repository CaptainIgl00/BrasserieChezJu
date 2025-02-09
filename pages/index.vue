<script setup lang="ts">
import { useHead, useSeoMeta } from '#imports'

const route = useRoute()

// Lazy load components that are not immediately visible
const ShowcaseComponent = defineAsyncComponent(() => import('../components/ShowcaseComponent.vue'))
const StaffComponent = defineAsyncComponent(() => import('../components/StaffComponent.vue'))
const InstagramFeedComponent = defineAsyncComponent(() => import('../components/InstagramFeedComponent.vue'))
const ContactComponent = defineAsyncComponent(() => import('../components/ContactComponent.vue'))

// SEO
useSeoMeta({
  title: 'Brasserie Chez Ju - Restaurant traditionnel à Carcassonne',
  ogTitle: 'Brasserie Chez Ju - Restaurant traditionnel à Carcassonne',
  description: 'Bienvenue à la Brasserie Chez Ju, votre restaurant traditionnel à Carcassonne. Cuisine authentique, produits frais et locaux, ambiance chaleureuse.',
  ogDescription: 'Bienvenue à la Brasserie Chez Ju, votre restaurant traditionnel à Carcassonne. Cuisine authentique et produits locaux.',
  ogImage: 'https://brasseriechezju.com/images/display/plat-principal.jpg'
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