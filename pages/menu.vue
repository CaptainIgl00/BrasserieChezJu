<template>
  <div class="menu-page">
    <!-- Hero Section avec Tabs -->
    <div class="hero-section">
      <h1 class="text-4xl md:text-5xl font-playfair text-orange-500 text-center font-bold mb-4 mt-10">
        Notre Carte
      </h1>
      <p class="text-gray-300 text-center text-lg italic mb-4">
        Une cuisine authentique et raffinée
      </p>

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
      </div>
    </div>

    <!-- Suggestion Component -->
    <div class="suggestion-section">
      <MenuSuggestion 
        :hideInFormulaTab="activeTab === 'formulas'"
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
            <div class="loading-placeholder">
              <p class="text-orange-500 text-center">Chargement de la carte...</p>
            </div>
          </template>
        </Suspense>
      </div>

      <!-- Formules -->
      <div v-show="activeTab === 'formulas'" class="tab-content">
        <Suspense>
          <MenuComponent />
          <template #fallback>
            <div class="loading-placeholder">
              <p class="text-orange-500 text-center">Chargement des formules...</p>
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
import MenuSuggestion from '../components/MenuSuggestion.vue'

// Lazy load heavy components
const RestaurantMenu = defineAsyncComponent(() => import('../components/RestaurantMenu.vue'))
const MenuComponent = defineAsyncComponent(() => import('../components/FormuleComponent.vue'))

const route = useRoute()
const activeTab = ref('menu')

// Gérer les changements de hash
const handleHash = () => {
  if (route.hash === '#formules') {
    activeTab.value = 'formulas'
  } else {
    activeTab.value = 'menu'
  }
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

// Surveiller les changements de hash
watch(() => route.hash, handleHash)

// Initialiser l'onglet en fonction du hash au chargement
onMounted(() => {
  handleHash()
})

const scrollToFormula = async (formulaId) => {
  // D'abord on change l'onglet
  activeTab.value = 'formulas'
  
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
  @apply min-h-screen bg-black/95;
}

.hero-section {
  @apply py-16 px-4 bg-black/80 border-b border-orange-500/20;
}

.suggestion-section {
  @apply max-w-4xl mx-auto py-8 px-4;
}

.tabs-navigation {
  @apply flex justify-center gap-8;
}

.tab-button {
  @apply px-6 py-3 text-lg font-medium text-gray-400 transition-all duration-300
         hover:text-orange-500 relative;
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
  @apply py-12;
}

.tab-content {
  @apply transition-opacity duration-300;
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
</style> 