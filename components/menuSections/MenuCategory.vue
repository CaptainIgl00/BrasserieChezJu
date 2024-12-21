<template>
  <section class="menu-category">
    <div class="category-header">
      <h3 class="category-title">{{ title }}</h3>
      <p v-if="subtitle" class="category-subtitle">{{ subtitle }}</p>
    </div>

    <div class="dishes-grid">
      <div v-for="dish in dishes" :key="dish.name" class="dish-item">
        <div class="dish-content">
          <div class="dish-header">
            <h4 class="dish-name">{{ dish.name }}</h4>
            <span class="dish-price">{{ dish.price }} €</span>
          </div>
          <p v-if="dish.description" class="dish-description">{{ dish.description }}</p>
          <p v-if="dish.portion" class="dish-portion">{{ dish.portion }}</p>
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
.menu-category {
  @apply w-full max-w-5xl mx-auto mb-16;
}

.category-header {
  @apply text-center mb-12;
}

.category-title {
  @apply text-2xl md:text-3xl font-playfair text-orange-500 italic;
  font-family: 'Playfair Display', serif;
}

.category-subtitle {
  @apply text-gray-400 italic mt-2;
}

.dishes-grid {
  @apply grid gap-8;
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 350px));
  justify-content: center;
}

.dishes-grid::after {
  content: '';
  grid-column: span 3;
}

/* Pour 1 élément */
.dishes-grid:has(> :only-child) {
  grid-template-columns: minmax(0, 350px);
}

/* Pour 2 éléments */
.dishes-grid:has(> :nth-last-child(2):first-child) {
  grid-template-columns: repeat(2, minmax(0, 350px));
}

/* Pour 4 éléments */
.dishes-grid:has(> :nth-child(4):last-child) {
  grid-template-columns: repeat(2, minmax(0, 350px));
}

/* Pour 5 éléments */
.dishes-grid:has(> :nth-child(5):last-child) {
  grid-template-columns: repeat(3, minmax(0, 350px));
}
.dishes-grid:has(> :nth-child(5):last-child)::before {
  content: '';
  grid-column: 2;
  grid-row: 2;
}

/* Pour 7 éléments */
.dishes-grid:has(> :nth-child(7):last-child) {
  grid-template-columns: repeat(3, minmax(0, 350px));
}
.dishes-grid:has(> :nth-child(7):last-child)::before {
  content: '';
  grid-column: 1;
  grid-row: 3;
}

.dish-item {
  @apply p-4 rounded-lg transition-all duration-300 relative w-full backdrop-blur-sm;
  background: rgba(0, 0, 0, 0.4);
}

.dish-item:hover {
  @apply transform -translate-y-0.5;
  background: rgba(249, 115, 22, 0.03);
}

.dish-content {
  @apply space-y-2;
}

.dish-header {
  @apply flex justify-between items-start gap-4;
}

.dish-name {
  @apply text-lg text-gray-200 font-medium flex-1
         transition-colors duration-300;
}

.dish-item:hover .dish-name {
  @apply text-orange-500;
}

.dish-price {
  @apply text-orange-500 font-semibold whitespace-nowrap;
}

.dish-description {
  @apply text-sm text-gray-400 italic leading-relaxed;
}

.dish-portion {
  @apply text-sm text-orange-500/80 italic mt-1;
}

/* Responsive adjustments */
@media (max-width: 1200px) {
  .dishes-grid,
  .dishes-grid:has(> :nth-child(n)) {
    grid-template-columns: repeat(2, minmax(0, 350px));
  }
  
  .dishes-grid::before,
  .dishes-grid::after {
    display: none;
  }
}

@media (max-width: 768px) {
  .dishes-grid,
  .dishes-grid:has(> :nth-child(n)) {
    grid-template-columns: minmax(0, 400px);
  }

  .dish-item {
    @apply p-3;
  }
}
</style>
