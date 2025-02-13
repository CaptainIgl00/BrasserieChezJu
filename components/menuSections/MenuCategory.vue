<template>
  <section class="w-full max-w-7xl mx-auto mb-16">
    <div class="text-center mb-12">
      <h3 class="text-2xl md:text-3xl font-playfair text-orange-500 italic" style="font-family: 'Playfair Display', serif;">{{ title }}</h3>
      <p v-if="subtitle" class="text-gray-400 italic mt-2">{{ subtitle }}</p>
    </div>

    <div class="relative" v-if="dishImages">
      <div class="flex flex-col lg:flex-row gap-8">
        <!-- Left Side Cards -->
        <div class="flex flex-wrap lg:flex-col gap-4 lg:w-[40%]">
          <div v-for="dish in leftSideCards" :key="dish.name" 
               @click="setActiveImage(dish.name)"
               class="flex-1 lg:flex-none p-4 rounded-lg transition-all duration-300 relative backdrop-blur-sm hover:-translate-y-0.5 group min-w-[280px] lg:min-w-0 cursor-pointer"
               :class="{ 'active-card': activeCard === dish.name }"
               :style="{ background: 'rgba(0, 0, 0, 0.4)' }">
            <div class="space-y-2">
              <div class="flex justify-between items-start gap-4">
                <div class="flex items-center gap-2 flex-1">
                  <h4 class="text-lg text-gray-200 font-medium transition-colors duration-300 group-hover:text-orange-500">{{ dish.name }}</h4>
                  <span v-if="dishImages && dishImages[dish.name]" class="text-orange-500">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                    </svg>
                  </span>
                </div>
                <span class="text-orange-500 font-semibold whitespace-nowrap">{{ dish.price }} €</span>
              </div>
              <p v-if="dish.description" class="text-sm text-gray-400 italic leading-relaxed">{{ dish.description }}</p>
              <p v-if="dish.portion" class="text-sm text-orange-500/80 italic mt-1">{{ dish.portion }}</p>
            </div>
          </div>
        </div>

        <!-- Right Side Container -->
        <div class="lg:w-[60%] flex flex-col gap-4">
          <!-- Image Container with Loading State -->
          <div class="w-full h-[400px] lg:h-[500px] rounded-xl overflow-hidden relative">
            <div v-if="isLoading" class="absolute inset-0 flex items-center justify-center bg-black/40 z-10">
              <div class="loading-spinner"></div>
            </div>
            <ClientOnly>
              <nuxt-img 
                :src="currentImage" 
                :alt="title"
                class="w-full h-full object-cover transition-all duration-700"
                :class="{'scale-105': isHovered}"
                preset="showcase"
                loading="eager"
                fetchpriority="high"
                @load="onImageLoaded"
              />
            </ClientOnly>
          </div>

          <!-- Bottom Cards -->
          <div class="flex flex-wrap gap-4">
            <div v-for="dish in bottomCards" :key="dish.name" 
                 @click="setActiveImage(dish.name)"
                 class="flex-1 p-4 rounded-lg transition-all duration-300 relative backdrop-blur-sm hover:-translate-y-0.5 group min-w-[280px] cursor-pointer"
                 :class="{ 'active-card': activeCard === dish.name }"
                 :style="{ background: 'rgba(0, 0, 0, 0.4)' }">
              <div class="space-y-2">
                <div class="flex justify-between items-start gap-4">
                  <div class="flex items-center gap-2 flex-1">
                    <h4 class="text-lg text-gray-200 font-medium transition-colors duration-300 group-hover:text-orange-500">{{ dish.name }}</h4>
                    <span v-if="dishImages && dishImages[dish.name]" class="text-orange-500">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                      </svg>
                    </span>
                  </div>
                  <span class="text-orange-500 font-semibold whitespace-nowrap">{{ dish.price }} €</span>
                </div>
                <p v-if="dish.description" class="text-sm text-gray-400 italic leading-relaxed">{{ dish.description }}</p>
                <p v-if="dish.portion" class="text-sm text-orange-500/80 italic mt-1">{{ dish.portion }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Original grid for sections without images -->
    <div class="grid gap-8 dishes-grid" v-else>
      <div v-for="dish in dishes" :key="dish.name" 
           class="p-4 rounded-lg transition-all duration-300 relative w-full backdrop-blur-sm hover:-translate-y-0.5 group"
           :style="{ background: 'rgba(0, 0, 0, 0.4)' }">
        <div class="space-y-2">
          <div class="flex justify-between items-start gap-4">
            <h4 class="text-lg text-gray-200 font-medium flex-1 transition-colors duration-300 group-hover:text-orange-500">{{ dish.name }}</h4>
            <span class="text-orange-500 font-semibold whitespace-nowrap">{{ dish.price }} €</span>
          </div>
          <p v-if="dish.description" class="text-sm text-gray-400 italic leading-relaxed">{{ dish.description }}</p>
          <p v-if="dish.portion" class="text-sm text-orange-500/80 italic mt-1">{{ dish.portion }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'

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
const preloadedImages = ref(new Set())
const imageCache = ref(new Map())

// Précharger une image spécifique avec Promise
const preloadImage = (src) => {
  if (process.server || !src || preloadedImages.value.has(src)) {
    return Promise.resolve()
  }

  return new Promise((resolve, reject) => {
    const img = new Image()
    
    img.onload = () => {
      preloadedImages.value.add(src)
      imageCache.value.set(src, img)
      resolve()
    }
    
    img.onerror = () => {
      reject(new Error(`Failed to load image: ${src}`))
    }
    
    img.src = src
  })
}

// Précharger les images restantes en arrière-plan
const preloadRemainingImages = async () => {
  if (process.server || !props.dishImages) return
  
  const remainingImages = Object.entries(props.dishImages)
    .filter(([_, src]) => !preloadedImages.value.has(src))
  
  for (const [_, src] of remainingImages) {
    try {
      await preloadImage(src)
    } catch (error) {
      console.error(error)
    }
  }
}

// Gérer le chargement d'une image
const onImageLoaded = () => {
  isLoading.value = false
}

// Get the first available image as default
const defaultImage = computed(() => {
  if (!props.dishImages) return null
  const firstImage = Object.values(props.dishImages)[0] || null
  if (firstImage) {
    preloadImage(firstImage) // Précharger la première image immédiatement
  }
  return firstImage
})

// Fixed distribution: 5 cards on the left, 2 at the bottom
const leftSideCards = computed(() => {
  return props.dishes.slice(0, 4)
})

const bottomCards = computed(() => {
  return props.dishes.slice(4)
})

const isHovered = ref(false)
const currentImage = ref(defaultImage.value)
const activeCard = ref(null)

const setActiveImage = async (dishName) => {
  if (props.dishImages && props.dishImages[dishName]) {
    isLoading.value = true
    const newImage = props.dishImages[dishName]
    
    // Si l'image n'est pas dans le cache, la précharger
    if (!preloadedImages.value.has(newImage)) {
      try {
        await preloadImage(newImage)
      } catch (error) {
        console.error(error)
      }
    }
    
    currentImage.value = newImage
    activeCard.value = dishName
    
    // Lancer le préchargement des autres images en arrière-plan
    preloadRemainingImages()
  }
}

// Initialiser l'état au montage du composant
onMounted(() => {
  if (props.dishes.length > 0 && props.dishImages) {
    const firstDishWithImage = props.dishes.find(dish => props.dishImages[dish.name])
    if (firstDishWithImage) {
      setActiveImage(firstDishWithImage.name)
    }
    // Commencer le préchargement des autres images après un court délai
    setTimeout(preloadRemainingImages, 1000)
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
  border: 1px solid transparent;
  transition: border-color 0.3s ease;
}

.active-card {
  border-color: rgb(249, 115, 22);
}

/* Loading Spinner */
.loading-spinner {
  width: 50px;
  height: 50px;
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
</style>
