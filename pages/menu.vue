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
        <button 
          class="tab-button"
          :class="{ 'active': activeTab === 'menu' }"
          @click="activeTab = 'menu'"
        >
          La Carte
        </button>
        <button 
          class="tab-button"
          :class="{ 'active': activeTab === 'formulas' }"
          @click="activeTab = 'formulas'"
        >
          Nos Formules
        </button>
      </div>
    </div>

    <!-- Suggestion Component -->
    <div class="suggestion-section">
      <MenuSuggestion @select-formula="scrollToFormula" />
    </div>

    <!-- Menu Content -->
    <div class="menu-content">
      <!-- La Carte -->
      <div v-show="activeTab === 'menu'" class="tab-content">
        <RestaurantMenu />
      </div>

      <!-- Formules -->
      <div v-show="activeTab === 'formulas'" class="tab-content">
        <MenuComponent />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import RestaurantMenu from '../components/RestaurantMenu.vue'
import MenuComponent from '../components/MenuComponent.vue'
import MenuSuggestion from '../components/MenuSuggestion.vue'

const activeTab = ref('menu')

const scrollToFormula = (formulaId) => {
  activeTab.value = 'formulas'
  // On attend le prochain tick pour que le contenu soit rendu
  nextTick(() => {
    const element = document.getElementById(formulaId)
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' })
      // Ajouter une classe pour mettre en évidence la formule
      element.classList.add('highlighted')
      setTimeout(() => element.classList.remove('highlighted'), 2000)
    }
  })
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
  0%, 100% { background-color: transparent; }
  50% { background-color: rgba(249, 115, 22, 0.1); }
}

.highlighted {
  animation: highlight 2s ease-in-out;
}
</style> 