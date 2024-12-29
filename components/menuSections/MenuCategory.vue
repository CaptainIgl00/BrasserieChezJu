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
               @mouseenter="updateImage(dish.name)"
               @mouseleave="resetImage"
               class="flex-1 lg:flex-none p-4 rounded-lg transition-all duration-300 relative backdrop-blur-sm hover:-translate-y-0.5 group min-w-[280px] lg:min-w-0"
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
            <img 
              :src="currentImage" 
              :alt="title"
              class="w-full h-full object-cover transition-all duration-700"
              :class="{'scale-105': isHovered}"
            />
          </div>

          <!-- Bottom Cards -->
          <div class="flex flex-wrap gap-4">
            <div v-for="dish in bottomCards" :key="dish.name" 
                 @mouseenter="updateImage(dish.name)"
                 @mouseleave="resetImage"
                 class="flex-1 p-4 rounded-lg transition-all duration-300 relative backdrop-blur-sm hover:-translate-y-0.5 group min-w-[280px]"
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
import { ref, computed } from 'vue'

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
const lastHoveredImage = ref(defaultImage.value)

const updateImage = (dishName) => {
  if (props.dishImages && props.dishImages[dishName]) {
    currentImage.value = props.dishImages[dishName]
    lastHoveredImage.value = props.dishImages[dishName]
    isHovered.value = true
  }
}

const resetImage = () => {
  currentImage.value = lastHoveredImage.value
  isHovered.value = false
}
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
</style>
