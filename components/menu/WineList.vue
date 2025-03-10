<template>
  <div class="wine-list-container">
    <div class="wine-intro">
      <h2 class="wine-title">Notre Sélection de Vins</h2>
      <p class="wine-description">Une sélection soigneusement élaborée pour accompagner vos plats</p>
    </div>

    <div v-if="isLoading" class="loading-container">
      <div class="loading-spinner"></div>
      <p class="loading-text">Chargement de notre carte des vins...</p>
    </div>

    <div v-else-if="error" class="error-container">
      <p class="error-message">{{ error }}</p>
      <button @click="loadWineData" class="retry-button">Réessayer</button>
    </div>

    <template v-else>
      <!-- Vins Rouges -->
      <div v-if="redWines.length > 0" class="wine-category fade-in">
        <h3 class="category-title">Vins Rouges</h3>
        <div class="wines-grid">
          <div v-for="wine in redWines" :key="wine.id" class="wine-card">
            <div class="wine-header">
              <h4 class="wine-name">{{ wine.name }}</h4>
              <div class="region-domain-container">
                <div v-if="wine.region" class="wine-region">{{ wine.region }}</div>
                <div v-if="wine.domain" class="wine-domain">{{ wine.domain }}</div>
              </div>
            </div>
            <div class="wine-details">
              <p v-if="wine.description" class="wine-description-text">{{ wine.description }}</p>
              <div class="wine-prices">
                <div v-if="wine.glassPrice" class="price-item">
                  <span class="price-label">Verre</span>
                  <span class="price-value">{{ wine.glassPrice }}€</span>
                </div>
                <div class="price-item">
                  <span class="price-label">Bouteille</span>
                  <span class="price-value">{{ wine.bottlePrice }}€</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Vins Blancs -->
      <div v-if="whiteWines.length > 0" class="wine-category fade-in">
        <h3 class="category-title">Vins Blancs</h3>
        <div class="wines-grid">
          <div v-for="wine in whiteWines" :key="wine.id" class="wine-card">
            <div class="wine-header">
              <h4 class="wine-name">{{ wine.name }}</h4>
              <div class="region-domain-container">
                <div v-if="wine.region" class="wine-region">{{ wine.region }}</div>
                <div v-if="wine.domain" class="wine-domain">{{ wine.domain }}</div>
              </div>
            </div>
            <div class="wine-details">
              <p v-if="wine.description" class="wine-description-text">{{ wine.description }}</p>
              <div class="wine-prices">
                <div v-if="wine.glassPrice" class="price-item">
                  <span class="price-label">Verre</span>
                  <span class="price-value">{{ wine.glassPrice }}€</span>
                </div>
                <div class="price-item">
                  <span class="price-label">Bouteille</span>
                  <span class="price-value">{{ wine.bottlePrice }}€</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Vins Rosés -->
      <div v-if="roseWines.length > 0" class="wine-category fade-in">
        <h3 class="category-title">Vins Rosés</h3>
        <div class="wines-grid">
          <div v-for="wine in roseWines" :key="wine.id" class="wine-card">
            <div class="wine-header">
              <h4 class="wine-name">{{ wine.name }}</h4>
              <div class="region-domain-container">
                <div v-if="wine.region" class="wine-region">{{ wine.region }}</div>
                <div v-if="wine.domain" class="wine-domain">{{ wine.domain }}</div>
              </div>
            </div>
            <div class="wine-details">
              <p v-if="wine.description" class="wine-description-text">{{ wine.description }}</p>
              <div class="wine-prices">
                <div v-if="wine.glassPrice" class="price-item">
                  <span class="price-label">Verre</span>
                  <span class="price-value">{{ wine.glassPrice }}€</span>
                </div>
                <div class="price-item">
                  <span class="price-label">Bouteille</span>
                  <span class="price-value">{{ wine.bottlePrice }}€</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Champagnes -->
      <div v-if="champagnes.length > 0" class="wine-category fade-in">
        <h3 class="category-title">Champagnes</h3>
        <div class="wines-grid">
          <div v-for="wine in champagnes" :key="wine.id" class="wine-card">
            <div class="wine-header">
              <h4 class="wine-name">{{ wine.name }}</h4>
              <div class="region-domain-container">
                <div v-if="wine.region" class="wine-region">{{ wine.region }}</div>
                <div v-if="wine.domain" class="wine-domain">{{ wine.domain }}</div>
              </div>
            </div>
            <div class="wine-details">
              <p v-if="wine.description" class="wine-description-text">{{ wine.description }}</p>
              <div class="wine-prices">
                <div v-if="wine.glassPrice" class="price-item">
                  <span class="price-label">Verre</span>
                  <span class="price-value">{{ wine.glassPrice }}€</span>
                </div>
                <div class="price-item">
                  <span class="price-label">Bouteille</span>
                  <span class="price-value">{{ wine.bottlePrice }}€</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </template>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useWines } from '~/composables/useWines'

// Utiliser le composable useWines
const { 
  wines, 
  isLoading, 
  error, 
  redWines, 
  whiteWines, 
  roseWines, 
  champagnes, 
  fetchWines,
  loadWineData
} = useWines()

onMounted(async () => {
  // Charger les vins au montage du composant
  await loadWineData()
  
  // Configuration de l'animation au scroll
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('fade-in-visible')
      }
    })
  }, {
    threshold: 0.1,
    rootMargin: '50px'
  })

  document.querySelectorAll('.fade-in').forEach(el => {
    observer.observe(el)
  })
})
</script>

<style scoped>
.wine-list-container {
  @apply space-y-16 max-w-7xl mx-auto;
  animation: fadeIn 0.6s ease-out;
}

.wine-intro {
  @apply text-center mb-12;
}

.wine-title {
  @apply text-3xl md:text-4xl text-orange-500 mb-4;
  font-family: 'Dancing Script', cursive;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.wine-description {
  @apply text-gray-400 italic text-lg;
  font-family: 'Cormorant Garamond', serif;
}

.loading-container {
  @apply flex flex-col items-center justify-center py-16 space-y-4;
}

.loading-spinner {
  @apply w-12 h-12 border-4 border-orange-500/30 border-t-orange-500 rounded-full;
  animation: spin 1s linear infinite;
}

.loading-text {
  @apply text-gray-400 italic;
}

.error-container {
  @apply bg-red-500/10 border border-red-500/30 rounded-lg p-6 my-8 text-center;
}

.error-message {
  @apply text-red-500 mb-4;
}

.retry-button {
  @apply px-4 py-2 bg-orange-500 text-white rounded-md hover:bg-orange-600 transition-colors;
}

.wine-category {
  @apply bg-black/95 backdrop-blur-sm rounded-xl p-6 md:p-8 mb-12;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.6);
  border: 1px solid rgba(234, 92, 11, 0.2);
}

.category-title {
  @apply text-2xl text-orange-500 mb-8 text-center;
  font-family: 'Dancing Script', cursive;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.wines-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.wine-card {
  @apply bg-black/95 p-5 rounded-lg transition-all duration-300 hover:-translate-y-1;
  border: 1px solid rgba(234, 92, 11, 0.2);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
}

.wine-card:hover {
  border-color: rgba(234, 92, 11, 0.4);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4), 0 0 15px rgba(234, 92, 11, 0.1);
}

.wine-header {
  @apply border-b border-orange-500/20 pb-3 mb-3;
}

.region-domain-container {
  @apply flex justify-between items-center mt-1;
}

.wine-name {
  @apply text-xl text-orange-500 font-medium;
  font-family: 'Cormorant Garamond', serif;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.wine-region {
  @apply text-sm text-gray-500 italic;
  font-family: 'Cormorant Garamond', serif;
}

.wine-domain {
  @apply text-sm text-gray-500 italic text-right;
  font-family: 'Cormorant Garamond', serif;
}

.wine-details {
  @apply space-y-3;
}

.wine-description-text {
  @apply text-gray-400 text-sm italic;
  font-family: 'Cormorant Garamond', serif;
}

.wine-prices {
  @apply flex flex-wrap justify-between mt-4 gap-2;
}

.price-item {
  @apply flex flex-col;
}

.price-label {
  @apply text-xs text-gray-500;
  font-family: 'Montserrat', sans-serif;
}

.price-value {
  @apply text-lg text-orange-500 font-semibold;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
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

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@media (max-width: 768px) {
  .wines-grid {
    grid-template-columns: 1fr;
  }
  
  .wine-card {
    @apply p-4;
  }
  
  .wine-prices {
    @apply flex-col gap-1;
  }
  
  .price-item {
    @apply flex-row justify-between;
  }
}
</style> 