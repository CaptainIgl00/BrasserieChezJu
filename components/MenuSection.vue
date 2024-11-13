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
  padding: 1.5rem;
  border: 2px solid #F1A67B;
  border-radius: 12px;
  margin-bottom: 1rem;
  background: rgba(241, 166, 123, 0.05);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.menu-section:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(241, 166, 123, 0.2);
}

.title {
  font-size: 1.5rem;
  font-weight: 600;
  color: #F1A67B;
  margin-bottom: 0.5rem;
  position: relative;
}

.subtitle {
  color: #9CA3AF;
  font-style: italic;
  margin-bottom: 0.75rem;
  font-size: 0.95rem;
}

.items {
  color: #9CA3AF;
  font-size: 0.95rem;
  line-height: 1.6;
  margin-bottom: 1rem;
}

.price {
  font-size: 1.25rem;
  font-weight: 700;
  color: #F1A67B;
  margin-top: 0.5rem;
  display: inline-block;
  padding: 0.25rem 0.75rem;
  background: rgba(241, 166, 123, 0.1);
  border-radius: 6px;
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
    rgba(241, 166, 123, 0.1) 0%,
    transparent 100%
  );
  opacity: 0;
  transition: opacity 0.3s ease;
}

.menu-section:hover::before {
  opacity: 1;
}
</style>
  