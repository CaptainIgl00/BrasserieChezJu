<script setup lang="ts">
import { defineAsyncComponent, onMounted } from 'vue'

const route = useRoute()

// Lazy load components that are not immediately visible
const ServicesShowcase = defineAsyncComponent(() => import('../components/home/ServicesShowcase.vue'))
const TeamSection = defineAsyncComponent(() => import('../components/home/TeamSection.vue'))
const InstagramFeed = defineAsyncComponent(() => import('../components/home/InstagramFeed.vue'))
const TheFooter = defineAsyncComponent(() => import('../components/layout/TheFooter.vue'))

// Animation de transition entre les sections
onMounted(() => {
  // Observer pour les animations au scroll
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('section-visible')
      }
    })
  }, { 
    threshold: 0.15,
    rootMargin: '0px 0px -10% 0px'
  })
  
  // Observer toutes les sections
  document.querySelectorAll('.animate-section').forEach(section => {
    observer.observe(section)
  })
})
</script>

<template>
  <div class="home-page">
    <Title>Brasserie Chez Ju - Restaurant traditionnel à Carcassonne</Title>
    <Meta name="description" content="Bienvenue à la Brasserie Chez Ju, votre restaurant traditionnel à Carcassonne. Cuisine authentique, produits frais et locaux, ambiance chaleureuse." />
    <Meta property="og:title" content="Brasserie Chez Ju - Restaurant traditionnel à Carcassonne" />
    <Meta property="og:description" content="Bienvenue à la Brasserie Chez Ju, votre restaurant traditionnel à Carcassonne. Cuisine authentique et produits locaux." />
    <Meta property="og:image" content="https://brasseriechezju.com/images/display/plat_principal.jpg" />
    
    <!-- Section d'accueil spectaculaire -->
    <section class="hero-container">
      <RestaurantDisplay />
    </section>
    
    <!-- Section Hero avec transition -->
    <section class="animate-section section-hero">
      <HeroSection />
    </section>
    
    <!-- Composants chargés de manière différée avec animations -->
    <section class="animate-section section-services">
      <Suspense>
        <template #default>
          <ServicesShowcase />
        </template>
        <template #fallback>
          <div class="loading-placeholder">
            <div class="loading-spinner"></div>
          </div>
        </template>
      </Suspense>
    </section>

    <section class="animate-section section-team">
      <Suspense>
        <template #default>
          <TeamSection />
        </template>
        <template #fallback>
          <div class="loading-placeholder">
            <div class="loading-spinner"></div>
          </div>
        </template>
      </Suspense>
    </section>

    <section class="animate-section section-instagram">
      <Suspense>
        <template #default>
          <InstagramFeed />
        </template>
        <template #fallback>
          <div class="loading-placeholder">
            <div class="loading-spinner"></div>
          </div>
        </template>
      </Suspense>
    </section>

    <section class="animate-section section-footer">
      <Suspense>
        <template #default>
          <TheFooter />
        </template>
        <template #fallback>
          <div class="loading-placeholder">
            <div class="loading-spinner"></div>
          </div>
        </template>
      </Suspense>
    </section>
  </div>
</template>

<style scoped>
.home-page {
  @apply bg-black;
}

.hero-container {
  @apply w-full min-h-screen;
}

.section-hero {
  @apply relative z-10;
  margin-top: 0;
}

.section-services,
.section-team,
.section-instagram,
.section-footer {
  @apply relative z-10;
}

/* Animation des sections */
.animate-section {
  @apply opacity-0 transform translate-y-8 transition-all duration-1000;
}

.section-visible {
  @apply opacity-100 transform translate-y-0;
}

/* Placeholder de chargement amélioré */
.loading-placeholder {
  @apply w-full h-32 flex items-center justify-center bg-black/50;
}

.loading-spinner {
  @apply w-10 h-10 border-4 border-orange-500/30 border-t-orange-500 rounded-full;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Responsive */
@media (max-width: 768px) {
  .section-hero {
    margin-top: 0;
  }
}

@media (max-width: 480px) {
  .section-hero {
    margin-top: 0;
  }
}
</style>