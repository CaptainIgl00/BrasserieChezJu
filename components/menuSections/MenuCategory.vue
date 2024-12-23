<template>
  <section class="w-full max-w-5xl mx-auto mb-16">
    <div class="text-center mb-12">
      <h3 class="text-2xl md:text-3xl font-playfair text-orange-500 italic" style="font-family: 'Playfair Display', serif;">{{ title }}</h3>
      <p v-if="subtitle" class="text-gray-400 italic mt-2">{{ subtitle }}</p>
    </div>

    <div class="grid gap-8 dishes-grid">
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
defineProps({
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
  }
})
</script>

<style scoped>
.dishes-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 350px));
  justify-content: center;
  gap: 2rem;
}

@media (max-width: 1200px) {
  .dishes-grid {
    grid-template-columns: repeat(2, minmax(0, 350px));
  }
}

@media (max-width: 768px) {
  .dishes-grid {
    grid-template-columns: minmax(0, 400px);
  }
}
</style>
