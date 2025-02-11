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
               @mouseenter="setActiveImage(dish.name)"
               class="flex-1 lg:flex-none p-4 rounded-lg transition-all duration-300 relative backdrop-blur-sm hover:-translate-y-0.5 group min-w-[280px] lg:min-w-0"
               :class="{ 'active-card': activeCard === dish.name }"
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

        <!-- Right Side Container -->
        <div class="lg:w-[60%] flex flex-col gap-4">
          <!-- Image -->
          <div class="w-full h-[400px] lg:h-[500px] rounded-xl overflow-hidden">
            <nuxt-img 
              :src="currentImage" 
              :alt="title"
              class="w-full h-full object-cover transition-all duration-700"
              :class="{'scale-105': isHovered}"
              preset="showcase"
            />
          </div>

          <!-- Bottom Cards -->
          <div class="flex flex-wrap gap-4">
            <div v-for="dish in bottomCards" :key="dish.name" 
                 @mouseenter="setActiveImage(dish.name)"
                 class="flex-1 p-4 rounded-lg transition-all duration-300 relative backdrop-blur-sm hover:-translate-y-0.5 group min-w-[280px]"
                 :class="{ 'active-card': activeCard === dish.name }"
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
import { ref, computed, onMounted } from 'vue'

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

// Get the first available image as default
const defaultImage = computed(() => {
  if (!props.dishImages) return null
  return Object.values(props.dishImages)[0] || null
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

const updateImage = (dishName) => {
  if (props.dishImages && props.dishImages[dishName]) {
    currentImage.value = props.dishImages[dishName]
    isHovered.value = true
    activeCard.value = dishName
  }
}

const resetImage = () => {
  isHovered.value = false
}

const setActiveImage = (dishName) => {
  if (props.dishImages && props.dishImages[dishName]) {
    currentImage.value = props.dishImages[dishName]
    activeCard.value = dishName
  }
}

// Initialiser l'état au montage du composant
onMounted(() => {
  if (props.dishes.length > 0 && props.dishImages) {
    // Trouver le premier plat qui a une image associée
    const firstDishWithImage = props.dishes.find(dish => props.dishImages[dish.name])
    if (firstDishWithImage) {
      setActiveImage(firstDishWithImage.name)
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
  border: 1px solid transparent;
  transition: border-color 0.3s ease;
}

.active-card {
  border-color: rgb(249, 115, 22);
}

</style>
