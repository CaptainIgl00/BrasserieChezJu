<template>
  <div class="w-full max-w-7xl mx-auto px-4 menu-container">
    <!-- En-tête décoratif -->
    <div class="flex items-center justify-center space-x-4 mb-16">
      <div class="flex-grow h-px bg-orange-500/50 max-w-[100px]"></div>
      <h2 class="text-xl md:text-2xl text-center font-playfair text-orange-500 italic px-4">Notre carte change au fil des saisons,<br/>notre bonne humeur jamais !</h2>
      <div class="flex-grow h-px bg-orange-500/50 max-w-[100px]"></div>
    </div>

    <!-- Message de chargement -->
    <div v-if="isLoading" class="flex flex-col items-center justify-center py-12">
      <div class="loading-spinner mb-4"></div>
      <p class="text-gray-400">Chargement du menu...</p>
    </div>

    <!-- Message d'erreur -->
    <div v-else-if="error" class="bg-red-900/30 text-red-200 p-6 rounded-lg text-center">
      <p class="mb-2">Une erreur est survenue lors du chargement du menu.</p>
      <p class="text-sm">{{ error }}</p>
      <button @click="loadMenuData" class="mt-4 px-4 py-2 bg-orange-500 text-white rounded-lg hover:bg-orange-600 transition-colors">
        Réessayer
      </button>
    </div>

    <!-- Sections du menu -->
    <div v-else class="space-y-16">
      <!-- Entrées -->
      <div v-if="getDishesByCategory('Toc toc toc... entrées').length > 0">
        <MenuCategory 
          title="Toc toc toc... entrées"
          :dishes="getDishesByCategory('Toc toc toc... entrées')"
        />
      </div>
      
      <!-- Séparateur -->
      <BaseDivider v-if="getDishesByCategory('Toc toc toc... entrées').length > 0 && getDishesByCategory('On se met au vert ?').length > 0" />

      <!-- Salades -->
      <div v-if="getDishesByCategory('On se met au vert ?').length > 0">
        <MenuCategory 
          title="On se met au vert ?"
          :dishes="getDishesByCategory('On se met au vert ?')"
        />
      </div>

      <!-- Séparateur -->
      <BaseDivider v-if="getDishesByCategory('On se met au vert ?').length > 0 && getDishesByCategory('T\'as faim de tradition ?').length > 0" />
      
      <!-- T'as faim de tradition ? -->
      <div v-if="getDishesByCategory('T\'as faim de tradition ?').length > 0">
        <MenuCategory 
        title="T'as faim de tradition ?"
        :dishes="getDishesByCategory('T\'as faim de tradition ?')"
        />
      </div>
      
      <!-- Séparateur -->
      <BaseDivider v-if="getDishesByCategory('T\'as faim de tradition ?').length > 0 && getDishesByCategory('Côté Mer').length > 0" />
      
      <!-- Côté Mer -->
      <div v-if="getDishesByCategory('Côté Mer').length > 0">
        <MenuCategory 
        title="Côté Mer"
        :dishes="getDishesByCategory('Côté Mer')"
        />
      </div>
      
      <!-- Séparateur -->
      <BaseDivider v-if="getDishesByCategory('Côté Mer').length > 0 && getDishesByCategory('Côté Terre').length > 0" />
      
      <!-- Côté Terre -->
      <div v-if="getDishesByCategory('Côté Terre').length > 0">
        <MenuCategory 
        title="Côté Terre"
        :dishes="getDishesByCategory('Côté Terre')"
        />
      </div>
      
      <!-- Séparateur -->
      <BaseDivider v-if="getDishesByCategory('Côté Terre').length > 0 && getDishesByCategory('Côté Flamme').length > 0" />
      
      <!-- Côté Flamme -->
      <div v-if="getDishesByCategory('Côté Flamme').length > 0">
        <MenuCategory 
        title="Côté Flamme"
        :dishes="getDishesByCategory('Côté Flamme')"
        />
      </div>

      <!-- Séparateur -->
      <BaseDivider v-if="getDishesByCategory('Côté Flamme').length > 0 && getDishesByCategory('Finir en douceur').length > 0" />

      <!-- Desserts -->
      <div v-if="getDishesByCategory('Finir en douceur').length > 0">
        <MenuCategory 
        title="Finir en douceur"
        :dishes="getDishesByCategory('Finir en douceur')"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue'
import MenuCategory from './MenuCategory.vue'
import BaseDivider from '../layout/BaseDivider.vue'
import { useMenu } from '~/composables/useMenu'

// Utiliser le composable pour récupérer les données du menu
const { dishes, isLoading, error, fetchDishes, loadMenuData } = useMenu()

// Fonction pour obtenir les plats par catégorie
const getDishesByCategory = (categoryName) => {
  return dishes.value.filter(dish => dish.category === categoryName)
}

// Charger les données du menu au montage du composant
onMounted(async () => {
  await loadMenuData()
})

// Données de secours au cas où l'API ne répond pas
const fallbackData = {
  starters: [
    {
      name: "Planche de jambon Serrano et jambon blanc truffé",
      price: "17",
      image: '/images/menu/planche_charcuterie.jpg'
    },
    {
      name: "Camembert entier rôti au piment d'Espelette",
      description: "Servi avec ses mouillettes",
      price: "14"
    },
    // ... autres entrées
  ],
  // ... autres catégories
}
</script>

<style scoped>
.menu-container {
  animation: fadeIn 0.6s ease-out;
  @apply bg-black/90 backdrop-blur-sm rounded-xl p-6 md:p-8;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(234, 92, 11, 0.2);
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Animation de fade-in au scroll */
.fade-in {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.6s ease-out, transform 0.6s ease-out;
  will-change: opacity, transform;
}

.fade-in-visible {
  opacity: 1;
  transform: translateY(0);
}

/* Loading Spinner */
.loading-spinner {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  border-top-color: #f97316;
  animation: spin 1s ease-in-out infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Responsive adjustments */
@media (max-width: 640px) {
  .menu-container {
    @apply p-4;
  }
  
  .w-full {
    @apply py-8;
  }

  .flex {
    @apply mb-12 px-2;
  }

  .flex-grow {
    @apply max-w-[60px];
  }

  .text-xl {
    @apply text-lg px-2;
  }

  .space-y-16 {
    @apply space-y-12;
  }
}
</style>
