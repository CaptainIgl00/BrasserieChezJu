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
                  <h4 class="text-lg text-gray-400 font-medium transition-colors duration-300 group-hover:text-orange-500">{{ dish.name }}</h4>
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
    </div>

    <!-- Version Mobile et Fallback -->
    <div v-else class="dishes-grid fade-in">
      <div v-for="dish in dishes" :key="dish.name" 
           class="p-4 rounded-lg transition-all duration-300 relative backdrop-blur-sm hover:-translate-y-0.5 group"
           :style="{ background: 'rgba(0, 0, 0, 0.9)' }">
        <div class="space-y-2">
          <div class="flex justify-between items-start gap-4">
            <h4 class="text-lg text-gray-400 font-medium transition-colors duration-300 group-hover:text-orange-500">{{ dish.name }}</h4>
            <span class="text-orange-500 font-semibold whitespace-nowrap">{{ dish.price }} €</span>
          </div>
          <p v-if="dish.description" class="text-sm text-gray-500 italic leading-relaxed">{{ dish.description }}</p>
          <p v-if="dish.portion" class="text-xs text-gray-600 italic">{{ dish.portion }}</p>
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
    loadingStates.value.set(dishName, true)
    const newImage = props.dishImages[dishName]
    
    // Mettre un timeout de sécurité
    if (loadTimeout.value) clearTimeout(loadTimeout.value)
    loadTimeout.value = setTimeout(() => {
      isLoading.value = false
      loadingStates.value.set(dishName, false)
    }, 10000)
    
    try {
      if (!preloadedImages.value.has(newImage)) {
        await preloadImage(newImage)
      }
      currentImage.value = newImage
      activeCard.value = dishName
    } catch (error) {
      console.error(error)
      isLoading.value = false
      loadingStates.value.set(dishName, false)
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
  gap: 2rem;
  padding: 2rem;
}

@media (min-width: 1024px) {
  .dishes-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

/* Ajout d'une bordure transparente par défaut sur toutes les cartes */
[class*="flex-1"] {
  border: 1px solid rgba(234, 92, 11, 0.2);
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
}

[class*="flex-1"]:hover {
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.5);
}

.active-card {
  border-color: rgb(249, 115, 22, 0.6);
  box-shadow: 0 0 15px rgba(249, 115, 22, 0.3);
}

/* Loading Spinner */
.loading-spinner {
  width: 40px;
  height: 40px;
  border: 3px solid rgba(249, 115, 22, 0.3);
  border-radius: 50%;
  border-top-color: rgb(249, 115, 22);
  animation: spin 1s ease-in-out infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
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
</style>
