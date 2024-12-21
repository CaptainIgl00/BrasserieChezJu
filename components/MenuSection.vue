<template>
  <div :class="['menu-section', `menu-section--${type}`]">
    <div class="menu-header">
      <h2 class="title">{{ title }}</h2>
      <p v-if="subtitle" class="subtitle">{{ subtitle }}</p>
    </div>

    <div class="menu-content">
      <div v-if="items" class="dishes-list">
        <div v-for="(item, index) in items" :key="index" class="dish-item">
          <div class="dish-info">
            <h3 class="dish-name">{{ item.name }}</h3>
            <p v-if="item.description" class="dish-description">{{ item.description }}</p>
          </div>
          <span class="dish-price">{{ item.price }}€</span>
        </div>
      </div>

      <template v-else>
        <p class="items">{{ formule }}</p>
        <p class="items">{{ description }}</p>
        <p class="price">{{ price }} €</p>
      </template>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MenuSection',
  props: {
    title: String,
    subtitle: {
      type: String,
      default: null,
    },
    type: {
      type: String,
      default: 'default',
      validator: (value) => ['starter', 'main', 'dessert', 'default', 'formule'].includes(value)
    },
    formule: String,
    description: String,
    price: String,
    items: {
      type: Array,
      default: null,
    }
  },
};
</script>

<style scoped>
.menu-section {
  @apply p-6 border-2 border-orange-500 rounded-xl relative overflow-hidden h-full;
  background: rgba(249, 115, 22, 0.05);
  transition: all 0.3s ease;
}

.menu-section:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(249, 115, 22, 0.2);
}

.menu-header {
  @apply mb-4;
}

.title {
  @apply text-2xl font-bold text-orange-500 mb-2;
  font-family: 'Playfair Display', serif;
}

.subtitle {
  @apply text-gray-400 italic text-sm mb-3;
}

.items {
  @apply text-gray-300 text-base leading-relaxed mb-4;
}

.price {
  @apply text-xl font-bold text-orange-500 mt-auto inline-block px-3 py-1;
  background: rgba(249, 115, 22, 0.1);
  border-radius: 6px;
}

.menu-content {
  @apply flex flex-col h-full;
}

/* Animation au hover */
.menu-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    45deg,
    rgba(249, 115, 22, 0.1) 0%,
    transparent 100%
  );
  opacity: 0;
  transition: opacity 0.3s ease;
}

.menu-section:hover::before {
  opacity: 1;
}
</style>
  