<template>
  <section class="w-full max-w-7xl mx-auto mb-16">
    <div class="text-center mb-12">
      <h3 class="text-2xl md:text-3xl font-playfair text-orange-500 italic" style="font-family: 'Dancing Script', cursive; text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);">{{ title }}</h3>
      <p v-if="subtitle" class="text-gray-500 italic mt-2">{{ subtitle }}</p>
    </div>

    <!-- Version Desktop -->
    <div class="relative hidden lg:block" v-if="dishImages">
      <div class="flex flex-col lg:flex-row gap-8">
        <!-- Left Side Cards -->
        <div class="flex flex-wrap lg:flex-col gap-4 lg:w-[40%]">
          <div v-for="dish in leftSideCards" :key="dish.name" 
               @click="setActiveImage(dish.name)"
               class="flex-1 lg:flex-none p-4 rounded-lg transition-all duration-300 relative backdrop-blur-sm hover:-translate-y-0.5 group min-w-[280px] lg:min-w-0 cursor-pointer"
               :class="{ 'active-card': activeCard === dish.name }"
               :style="{ background: 'rgba(0, 0, 0, 0.9)' }">
            <div class="space-y-2">
              <div class="flex justify-between items-start gap-4">
                <div class="flex items-center gap-2 flex-1">
                  <h4 class="dish-title">{{ dish.name }}</h4>
                  <span v-if="dishImages && dishImages[dish.name]" class="text-orange-500">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                    </svg>
                  </span>
                </div>
                <span class="text-orange-500 font-semibold whitespace-nowrap">{{ dish.price }} €</span>
              </div>
              <p v-if="dish.description" class="text-sm text-gray-500 italic leading-relaxed">{{ dish.description }}</p>
              <p v-if="dish.portion" class="text-xs text-gray-600 italic">{{ dish.portion }}</p>
            </div>
          </div>
        </div>

        <!-- Right Side Image -->
        <div class="lg:w-[60%] relative rounded-lg overflow-hidden h-[400px] bg-black/80 backdrop-blur-sm">
          <div v-if="isLoading" class="absolute inset-0 flex items-center justify-center z-10">
            <div class="loading-spinner"></div>
          </div>
          <div v-else-if="loadError" class="absolute inset-0 flex flex-col items-center justify-center z-10 bg-black/90 p-6 text-center">
            <p class="text-gray-400 mb-4">Impossible de charger l'image</p>
            <button @click="retryLoading" class="px-4 py-2 bg-orange-500 text-white rounded-lg hover:bg-orange-600 transition-colors">
              Réessayer
            </button>
          </div>
          <nuxt-img 
            v-else-if="currentImage" 
            :src="currentImage" 
            class="w-full h-full object-cover transition-opacity duration-300"
            loading="lazy"
            format="webp"
            quality="90"
            placeholder
          />
          <div v-else class="absolute inset-0 flex items-center justify-center bg-black/80 text-gray-500">
            Aucune image disponible
          </div>
        </div>
      </div>
      
      <!-- Bottom Cards -->
      <div v-if="bottomCards.length > 0" class="mt-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div v-for="(dish, index) in bottomCards" :key="dish.name" 
             @click="setActiveImage(dish.name)"
             class="p-4 rounded-lg transition-all duration-300 relative backdrop-blur-sm hover:-translate-y-0.5 group cursor-pointer bottom-card"
             :class="{ 'active-card': activeCard === dish.name }"
             :style="{ background: 'rgba(0, 0, 0, 0.9)', '--index': index }"
             >
          <div class="space-y-2">
            <div class="flex justify-between items-start gap-4">
              <div class="flex items-center gap-2 flex-1">
                <h4 class="dish-title">{{ dish.name }}</h4>
                <span v-if="dishImages && dishImages[dish.name]" class="text-orange-500">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                  </svg>
                </span>
              </div>
              <span class="text-orange-500 font-semibold whitespace-nowrap">{{ dish.price }} €</span>
            </div>
            <p v-if="dish.description" class="text-sm text-gray-500 italic leading-relaxed">{{ dish.description }}</p>
            <p v-if="dish.portion" class="text-xs text-gray-600 italic">{{ dish.portion }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Version Mobile -->
    <div class="block lg:hidden">
      <!-- Image mobile si disponible -->
      <div v-if="dishImages && currentImage" class="mb-6 rounded-lg overflow-hidden h-[200px] bg-black/80 backdrop-blur-sm relative mx-auto max-w-full">
        <div v-if="isLoading" class="absolute inset-0 flex items-center justify-center z-10">
          <div class="loading-spinner"></div>
        </div>
        <div v-else-if="loadError" class="absolute inset-0 flex flex-col items-center justify-center z-10 bg-black/90 p-6 text-center">
          <p class="text-gray-400 mb-4">Impossible de charger l'image</p>
          <button @click="retryLoading" class="px-4 py-2 bg-orange-500 text-white rounded-lg hover:bg-orange-600 transition-colors">
            Réessayer
          </button>
        </div>
        <nuxt-img 
          v-else
          :src="currentImage" 
          class="w-full h-full object-cover transition-opacity duration-300"
          loading="lazy"
          format="webp"
          quality="90"
          placeholder
        />
      </div>

      <!-- Cartes mobiles -->
      <div class="dishes-grid fade-in px-2 sm:px-4">
        <div v-for="(dish, index) in dishes" :key="dish.name" 
             @click="dishImages && dishImages[dish.name] ? setActiveImage(dish.name) : null"
             class="p-3 sm:p-4 rounded-lg transition-all duration-300 relative backdrop-blur-sm hover:-translate-y-0.5 group bottom-card w-full"
             :class="{ 'active-card': activeCard === dish.name, 'cursor-pointer': dishImages && dishImages[dish.name] }"
             :style="{ background: 'rgba(0, 0, 0, 0.9)', '--index': index }">
          <div class="space-y-2">
            <div class="flex justify-between items-start gap-2 sm:gap-4">
              <div class="flex items-center gap-2 flex-1">
                <h4 class="dish-title text-base sm:text-lg">{{ dish.name }}</h4>
                <span v-if="dishImages && dishImages[dish.name]" class="text-orange-500 flex-shrink-0">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 sm:h-5 sm:w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                  </svg>
                </span>
              </div>
              <span class="text-orange-500 font-semibold whitespace-nowrap text-sm sm:text-base">{{ dish.price }} €</span>
            </div>
            <p v-if="dish.description" class="text-xs sm:text-sm text-gray-500 italic leading-relaxed">{{ dish.description }}</p>
            <p v-if="dish.portion" class="text-xs text-gray-600 italic">{{ dish.portion }}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, onMounted, watch, onUnmounted } from 'vue'

const props = defineProps({
  title: {
    type: String,
    required: true
  },
  subtitle: {
    type: String,
    default: ''
  },
  dishes: {
    type: Array,
    required: true,
    default: () => []
  },
  dishImages: {
    type: Object,
    default: null
  }
})

const isLoading = ref(false)
const loadingStates = ref(new Map())
const errorStates = ref(new Map())
const preloadedImages = ref(new Set())
const imageCache = ref(new Map())
const isHovered = ref(false)
const currentImage = ref(null)
const activeCard = ref(null)
const loadTimeout = ref(null)
const imageKey = ref(0) // Pour forcer le rechargement de l'image
const loadError = ref(false)

// Fonction pour réessayer de charger l'image actuelle
const retryLoading = () => {
  if (activeCard.value && props.dishImages && props.dishImages[activeCard.value]) {
    loadError.value = false
    isLoading.value = true
    imageKey.value++ // Forcer le rechargement de l'image
    
    const img = new Image()
    img.onload = () => {
      isLoading.value = false
      currentImage.value = props.dishImages[activeCard.value]
    }
    
    img.onerror = () => {
      isLoading.value = false
      loadError.value = true
    }
    
    img.src = props.dishImages[activeCard.value]
  }
}

// Simplifier la fonction de préchargement
const preloadImage = (src) => {
  if (process.server || !src) {
    return Promise.resolve()
  }

  return new Promise((resolve, reject) => {
    const img = new Image()
    const timeout = setTimeout(() => {
      img.src = ''
      reject(new Error('Image loading timeout'))
    }, 10000)

    img.onload = () => {
      clearTimeout(timeout)
      resolve()
    }

    img.onerror = () => {
      clearTimeout(timeout)
      reject(new Error(`Failed to load image: ${src}`))
    }

    img.src = src
  })
}

// Simplifier la fonction toggleMobileCard
const toggleMobileCard = async (dishName) => {
  // Si on ferme la carte
  if (activeCard.value === dishName) {
    activeCard.value = null
    loadingStates.value.set(dishName, false)
    errorStates.value.set(dishName, false)
    return
  }

  // Si on ouvre une nouvelle carte
  if (props.dishImages && props.dishImages[dishName]) {
    loadingStates.value.set(dishName, true)
    errorStates.value.set(dishName, false)
    activeCard.value = dishName

    try {
      await preloadImage(props.dishImages[dishName])
      onImageLoaded(dishName)
    } catch (error) {
      console.error('Error loading image:', error)
      onImageError(dishName)
    }
  }
}

// Simplifier la gestion du chargement
const onImageLoaded = (dishName) => {
  loadingStates.value.set(dishName, false)
  errorStates.value.set(dishName, false)
}

const onImageError = (dishName) => {
  loadingStates.value.set(dishName, false)
  errorStates.value.set(dishName, true)
  console.error(`Failed to load image for ${dishName}`)
}

// Fonction pour réessayer de charger une image
const retryLoadImage = async (dishName) => {
  if (!props.dishImages || !props.dishImages[dishName]) return
  
  errorStates.value.set(dishName, false)
  loadingStates.value.set(dishName, true)
  imageKey.value++ // Forcer le rechargement de l'image
  
  try {
    await preloadImage(props.dishImages[dishName])
    onImageLoaded(dishName)
  } catch (error) {
    onImageError(dishName)
  }
}

// Fixed distribution: 4 cards on the left, rest at the bottom
const leftSideCards = computed(() => {
  return props.dishes.slice(0, 4)
})

const bottomCards = computed(() => {
  return props.dishes.slice(4)
})

const setActiveImage = async (dishName) => {
  if (props.dishImages && props.dishImages[dishName]) {
    // Ne pas recharger si l'image est déjà active
    if (activeCard.value === dishName) return
    
    isLoading.value = true
    loadError.value = false
    loadingStates.value.set(dishName, true)
    const newImage = props.dishImages[dishName]
    
    // Mettre un timeout de sécurité
    if (loadTimeout.value) clearTimeout(loadTimeout.value)
    loadTimeout.value = setTimeout(() => {
      isLoading.value = false
      loadingStates.value.set(dishName, false)
      loadError.value = true
    }, 10000)
    
    try {
      if (!preloadedImages.value.has(newImage)) {
        await preloadImage(newImage)
        preloadedImages.value.add(newImage)
      }
      
      currentImage.value = newImage
      activeCard.value = dishName
      isLoading.value = false
      loadingStates.value.set(dishName, false)
      
      if (loadTimeout.value) {
        clearTimeout(loadTimeout.value)
        loadTimeout.value = null
      }
    } catch (error) {
      console.error(error)
      isLoading.value = false
      loadingStates.value.set(dishName, false)
      loadError.value = true
      
      if (loadTimeout.value) {
        clearTimeout(loadTimeout.value)
        loadTimeout.value = null
      }
    }
  }
}

// Nettoyer les timeouts au démontage du composant
onUnmounted(() => {
  if (loadTimeout.value) {
    clearTimeout(loadTimeout.value)
    loadTimeout.value = null
  }
})

// Initialiser l'état au montage du composant
onMounted(() => {
  if (props.dishes.length > 0 && props.dishImages) {
    const firstDishWithImage = props.dishes.find(dish => props.dishImages[dish.name])
    if (firstDishWithImage) {
      currentImage.value = props.dishImages[firstDishWithImage.name]
    }
  }
})
</script>

<style scoped>
.dishes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  padding: 1rem;
  justify-content: center;
}

@media (min-width: 1024px) {
  .dishes-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

/* Styles pour les titres des plats */
.dish-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.25rem;
  font-weight: 600;
  color: #e2e2e2;
  letter-spacing: 0.02em;
  line-height: 1.3;
  position: relative;
  transition: all 0.3s ease;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.group:hover .dish-title {
  color: #f97316;
  transform: translateX(2px);
}

.active-card .dish-title {
  color: #f97316;
}

/* Ajout d'une bordure subtile sous le titre au survol */
.dish-title::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 0;
  height: 1px;
  background: linear-gradient(90deg, #f97316, transparent);
  transition: width 0.3s ease;
  opacity: 0;
}

.group:hover .dish-title::after {
  width: 100%;
  opacity: 0.7;
}

.active-card .dish-title::after {
  width: 100%;
  opacity: 0.7;
}

/* Style des cartes sans bordure orange */
[class*="flex-1"], .bottom-card {
  border: 1px solid rgba(255, 255, 255, 0.05);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
}

[class*="flex-1"]:hover, .bottom-card:hover {
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.5);
  transform: translateY(-2px);
}

.active-card {
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.6);
  background: rgba(10, 10, 10, 0.95) !important;
}

/* Bottom cards animation */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.mt-8 > div {
  animation: fadeInUp 0.5s ease-out forwards;
  animation-delay: calc(0.1s * var(--index, 0));
  opacity: 0;
}

.dishes-grid > div {
  animation: fadeInUp 0.5s ease-out forwards;
  animation-delay: calc(0.05s * var(--index, 0));
  opacity: 0;
}

/* Assurer que les cartes sont visibles */
.mt-8 {
  width: 100%;
  margin-top: 2rem !important;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
}

@media (min-width: 768px) {
  .mt-8 {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .mt-8 {
    grid-template-columns: repeat(3, 1fr);
  }
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

/* Image transition */
.nuxt-img {
  opacity: 0;
  animation: fadeIn 0.3s ease-in-out forwards;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Ajout d'un style pour le bouton de retry */
button {
  transition: all 0.3s ease;
}

button:hover {
  transform: scale(1.05);
}

button:active {
  transform: scale(0.95);
}

/* Styles pour les cartes mobiles */
@media (max-width: 1023px) {
  .dishes-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1rem;
    justify-content: center;
    margin: 0 auto;
    max-width: 100%;
  }
  
  .bottom-card {
    animation: fadeInUp 0.5s ease forwards;
    animation-delay: calc(var(--index) * 0.1s);
    opacity: 0;
    transform: translateY(20px);
  }
  
  .active-card {
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.6);
    background: rgba(10, 10, 10, 0.95) !important;
  }
}

/* Ajustements pour les très petits écrans */
@media (max-width: 480px) {
  .dishes-grid {
    grid-template-columns: minmax(0, 1fr);
    padding-left: 0.5rem;
    padding-right: 0.5rem;
    width: 100%;
  }
  
  .bottom-card {
    width: 100%;
    min-width: 0;
  }
}
</style>
