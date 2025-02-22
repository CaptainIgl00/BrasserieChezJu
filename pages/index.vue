<script setup lang="ts">
import { defineAsyncComponent } from 'vue'

const route = useRoute()

// Lazy load components that are not immediately visible
const ServicesShowcase = defineAsyncComponent(() => import('../components/home/ServicesShowcase.vue'))
const TeamSection = defineAsyncComponent(() => import('../components/home/TeamSection.vue'))
const InstagramFeed = defineAsyncComponent(() => import('../components/home/InstagramFeed.vue'))
const TheFooter = defineAsyncComponent(() => import('../components/layout/TheFooter.vue'))

</script>

<template>
  <div class="home-page">
    <Title>Brasserie Chez Ju - Restaurant traditionnel à Carcassonne</Title>
    <Meta name="description" content="Bienvenue à la Brasserie Chez Ju, votre restaurant traditionnel à Carcassonne. Cuisine authentique, produits frais et locaux, ambiance chaleureuse." />
    <Meta property="og:title" content="Brasserie Chez Ju - Restaurant traditionnel à Carcassonne" />
    <Meta property="og:description" content="Bienvenue à la Brasserie Chez Ju, votre restaurant traditionnel à Carcassonne. Cuisine authentique et produits locaux." />
    <Meta property="og:image" content="https://brasseriechezju.com/images/display/plat_principal.jpg" />
    
    <!-- Composants critiques chargés immédiatement -->
    <RestaurantDisplay />
    <HeroSection />
    
    <!-- Composants chargés de manière différée -->
    <Suspense>
      <template #default>
        <ServicesShowcase />
      </template>
      <template #fallback>
        <div class="loading-placeholder">Chargement...</div>
      </template>
    </Suspense>

    <Suspense>
      <template #default>
        <TeamSection />
      </template>
      <template #fallback>
        <div class="loading-placeholder">Chargement...</div>
      </template>
    </Suspense>

    <Suspense>
      <template #default>
        <InstagramFeed />
      </template>
      <template #fallback>
        <div class="loading-placeholder">Chargement...</div>
      </template>
    </Suspense>

    <Suspense>
      <template #default>
        <TheFooter />
      </template>
      <template #fallback>
        <div class="loading-placeholder">Chargement...</div>
      </template>
    </Suspense>
  </div>
</template>

<style scoped>
.loading-placeholder {
  @apply w-full h-32 flex items-center justify-center text-orange-500 bg-black/50;
}
</style>