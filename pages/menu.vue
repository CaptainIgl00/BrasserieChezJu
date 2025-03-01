<template>
  <div class="menu-page">
    <Title>Menu - Brasserie Chez Ju</Title>
    <Meta name="description" content="Découvrez notre carte de brasserie traditionnelle, nos formules du jour et nos suggestions. Une cuisine authentique et raffinée mettant en valeur les produits locaux." />
    <Meta property="og:title" content="Menu - Brasserie Chez Ju" />
    <Meta property="og:description" content="Découvrez notre carte de brasserie traditionnelle, nos formules du jour et nos suggestions." />
    <Meta property="og:image" content="https://brasseriechezju.com/images/display/plat-principal.jpg" />
    
    <!-- Hero Section avec Tabs -->
    <div class="hero-section">
      <div class="hero-content">

        <!-- Tabs Navigation -->
        <div class="tabs-navigation">
          <NuxtLink 
            to="/menu#menu"
            class="tab-button"
            :class="{ 'active': activeTab === 'menu' }"
          >
            La Carte
          </NuxtLink>
          <NuxtLink 
            to="/menu#formules"
            class="tab-button"
            :class="{ 'active': activeTab === 'formulas' }"
          >
            Nos Formules
          </NuxtLink>
          <NuxtLink 
            to="/menu#vins"
            class="tab-button"
            :class="{ 'active': activeTab === 'wines' }"
          >
            Carte des Vins
          </NuxtLink>
        </div>
      </div>
    </div>

    <!-- Suggestion Component -->
    <div class="suggestion-section">
      <DailySpecials 
        :hideInFormulaTab="activeTab === 'formulas' || activeTab === 'wines'"
        @select-formula="scrollToFormula" 
      />
    </div>

    <!-- Menu Content -->
    <div class="menu-content">
      <!-- La Carte -->
      <div v-show="activeTab === 'menu'" class="tab-content">
        <Suspense>
          <RestaurantMenu />
          <template #fallback>
            <div class="loading-container">
              <div class="loading-spinner"></div>
              <p class="loading-text">Chargement de notre carte...</p>
            </div>
          </template>
        </Suspense>
      </div>

      <!-- Nos Formules -->
      <div v-show="activeTab === 'formulas'" class="tab-content">
        <Suspense>
          <MenuComponent />
          <template #fallback>
            <div class="loading-container">
              <div class="loading-spinner"></div>
              <p class="loading-text">Chargement de nos formules...</p>
            </div>
          </template>
        </Suspense>
      </div>

      <!-- Carte des Vins -->
      <div v-show="activeTab === 'wines'" class="tab-content">
        <Suspense>
          <WineList />
          <template #fallback>
            <div class="loading-container">
              <div class="loading-spinner"></div>
              <p class="loading-text">Chargement de notre carte des vins...</p>
            </div>
          </template>
        </Suspense>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick, watch, onMounted, defineAsyncComponent } from 'vue'
import { useRoute } from '#app'

// Lazy load heavy components avec des options de chargement plus robustes
const RestaurantMenu = defineAsyncComponent({
  loader: () => import('../components/menu/MenuGrid.vue'),
  delay: 0,
  timeout: 30000
})

const MenuComponent = defineAsyncComponent({
  loader: () => import('../components/menu/SetMenus.vue'),
  delay: 0,
  timeout: 30000
})

const WineList = defineAsyncComponent({
  loader: () => import('../components/menu/WineList.vue'),
  delay: 0,
  timeout: 30000
})

const route = useRoute()
const activeTab = ref('menu')
const isLoading = ref(true)

// Gérer les changements de hash
const handleHash = async () => {
  isLoading.value = true
  
  if (route.hash === '#formules') {
    activeTab.value = 'formulas'
  } else if (route.hash === '#vins') {
    activeTab.value = 'wines'
  } else if (route.hash === '#menu') {
    activeTab.value = 'menu'
  } else {
    activeTab.value = 'menu'
  }
  
  // Attendre le prochain tick pour s'assurer que le composant est monté
  await nextTick()
  isLoading.value = false
}

// Surveiller les changements de route complets
watch(() => route.fullPath, async () => {
  await handleHash()
}, { immediate: true })

// Initialiser l'onglet en fonction du hash au chargement
onMounted(async () => {
  await handleHash()
})

const scrollToFormula = async (formulaId) => {
  // D'abord on change l'onglet
  activeTab.value = 'formulas'
  
  // Mettre à jour le hashtag de l'URL
  window.location.hash = '#formules'
  
  try {
    // On attend que le DOM soit mis à jour
    await nextTick()
    
    // On attend un peu que l'animation de changement d'onglet soit terminée
    setTimeout(() => {
      const element = document.getElementById(formulaId)
      if (element) {
        // Calculer la position avec un offset
        const offset = 100 // offset en pixels
        const elementPosition = element.getBoundingClientRect().top
        const offsetPosition = elementPosition + window.pageYOffset - offset

        // Scroll avec une animation douce
        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        })

        // Ajouter la classe highlighted avec un délai pour correspondre à l'animation
        setTimeout(() => {
          element.classList.add('highlighted')
          setTimeout(() => element.classList.remove('highlighted'), 2000)
        }, 800) // Attendre que le scroll soit presque terminé
      }
    }, 300)
  } catch (error) {
    console.error('Erreur lors du scroll:', error)
  }
}

</script>

<style scoped>
.menu-page {
  @apply min-h-screen bg-black;
}

.hero-section {
  @apply pt-16 pb-6 px-4 bg-black/90 backdrop-blur-sm border-b border-orange-500/20 relative overflow-hidden;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
}

.hero-content {
  @apply max-w-4xl mx-auto relative z-10;
}

.menu-title {
  @apply text-4xl md:text-5xl font-playfair text-orange-500 text-center font-bold mb-4 mt-10;
  text-shadow: 0 2px 10px rgba(234, 92, 11, 0.3);
  font-family: 'Dancing Script', cursive;
}

.menu-subtitle {
  @apply text-gray-500 text-center text-lg italic mb-6;
  font-family: 'Cormorant Garamond', serif;
  letter-spacing: 0.02em;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

.suggestion-section {
  @apply max-w-4xl mx-auto py-10 px-4;
}

.tabs-navigation {
  @apply flex justify-center gap-6 mt-8 flex-wrap;
}

.tab-button {
  @apply px-5 py-3 text-lg font-medium text-gray-500 transition-all duration-300
         hover:text-orange-500 relative;
  font-family: 'Montserrat', sans-serif;
}

.tab-button::after {
  content: '';
  @apply absolute bottom-0 left-0 w-full h-0.5 bg-orange-500 transform scale-x-0
         transition-transform duration-300 -translate-y-1;
}

.tab-button:hover::after {
  @apply scale-x-100;
}

.tab-button.active {
  @apply text-orange-500;
}

.tab-button.active::after {
  @apply scale-x-100;
}

.menu-content {
  @apply py-12 max-w-7xl mx-auto bg-black;
}

.tab-content {
  @apply transition-opacity duration-300;
}

.loading-container {
  @apply flex flex-col items-center justify-center py-20 bg-black/90 backdrop-blur-sm rounded-xl;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
}

.loading-spinner {
  @apply w-12 h-12 border-4 border-orange-500/30 border-t-orange-500 rounded-full;
  animation: spin 1s linear infinite;
}

.loading-text {
  @apply mt-4 text-orange-500 text-lg italic;
  font-family: 'Cormorant Garamond', serif;
}

/* Animation pour la mise en évidence des formules */
@keyframes highlight {
  0% { background-color: transparent; }
  20% { background-color: rgba(249, 115, 22, 0.15); }
  80% { background-color: rgba(249, 115, 22, 0.15); }
  100% { background-color: transparent; }
}

.highlighted {
  animation: highlight 2s ease-in-out;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Ajout d'un breakpoint spécifique pour les très petits écrans */
@media (max-width: 320px) {
  .hero-section {
    @apply py-8;
  }
  
  .menu-title {
    @apply text-3xl mb-2;
  }
  
  .menu-subtitle {
    @apply text-sm mb-2;
  }
  
  .tabs-navigation {
    @apply gap-3;
  }
  
  .tab-button {
    @apply px-3 py-2 text-sm;
  }
  
  .suggestion-section {
    @apply py-4 px-2;
  }
  
  .menu-content {
    @apply py-6;
  }
}

/* Ajout d'un breakpoint pour les écrans moyens */
@media (max-width: 640px) {
  .tabs-navigation {
    @apply gap-4;
  }
  
  .tab-button {
    @apply px-3 py-2 text-base;
  }
}
</style> 