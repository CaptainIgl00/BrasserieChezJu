<template>
  <div class="menu-card" id="menu-gourmand">
    <div class="menu-header">
      <h2 class="text-3xl font-bold text-orange-500 font-playfair">Menu Gourmand</h2>
      <div class="price-tag">41 €</div>
    </div>

    <!-- Entrées -->
    <div class="section-container">
      <h3 class="section-title">Entrées</h3>
      <div class="dishes-container">
        <div class="dish-item">
          <h4 class="dish-name">Soupe de lentilles</h4>
          <p class="dish-description">Lardons, croûtons et œuf fermier mollet</p>
        </div>
        <div class="dish-item">
          <h4 class="dish-name">Escalope de saumon</h4>
          <p class="dish-description">Marinée à l'aneth</p>
        </div>
        <div class="dish-item">
          <h4 class="dish-name">Tranche de foie gras mi-cuit</h4>
          <p class="dish-description">Du périgord</p>
        </div>
      </div>
    </div>

    <SeparatorComponent />

    <!-- Plats -->
    <div class="section-container">
      <h3 class="section-title">Plats</h3>
      <div class="dishes-container">
        <div class="dish-item">
          <h4 class="dish-name">Filet de bar</h4>
          <p class="dish-description">À la plancha, sauce vierge à la ricotta et son toast de tapenade</p>
        </div>
        <div class="dish-item">
          <h4 class="dish-name">Cassoulet du chef Becq</h4>
          <p class="dish-description">Élaboré par le chef Becq dans le respect des traditions</p>
        </div>
        <div class="dish-item">
          <h4 class="dish-name">Magret de canard grillé</h4>
          <p class="dish-description">Du Périgord grillé à la fleur de sel à la plancha</p>
        </div>
      </div>
    </div>

    <SeparatorComponent />

    <!-- Desserts -->
    <div class="section-container">
      <h3 class="section-title">Desserts</h3>
      <div class="dishes-container">
        <div class="dish-item">
          <h4 class="dish-name">Crème brûlée</h4>
          <p class="dish-description">Et son caramel au beurre salé</p>
        </div>
        <div class="dish-item">
          <h4 class="dish-name">Moelleux au chocolat</h4>
          <p class="dish-description">Avec sa crème anglaise</p>
        </div>
        <div class="dish-item">
          <h4 class="dish-name">Café ou chocolat liégeois</h4>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import SeparatorComponent from '../SeparatorComponent.vue'
</script>

<style scoped>
/* Card principale */
.menu-card {
  @apply p-8 bg-black/60 border-2 border-orange-500 rounded-xl relative overflow-hidden;
  font-family: 'Playfair Display', serif;
}

/* Header du menu */
.menu-header {
  @apply flex justify-between items-center mb-12 pb-4 border-b border-orange-500/30;
}

.price-tag {
  @apply text-2xl font-semibold text-orange-500 px-4 py-2;
}

/* Sections */
.section-container {
  @apply my-12;
}

.section-title {
  @apply text-2xl font-semibold text-orange-500 text-center mb-8;
  letter-spacing: 0.05em;
}

.dishes-container {
  @apply flex flex-col gap-8;
}

/* Plats */
.dish-item {
  @apply text-center space-y-2 transition-all duration-300 p-2 rounded-lg;
}

.dish-name {
  @apply text-xl text-gray-200 font-medium transition-colors duration-300;
  font-family: 'Playfair Display', serif;
  letter-spacing: 0.02em;
}

.dish-description {
  @apply text-gray-400 text-sm italic transition-colors duration-300;
  font-family: 'Cormorant Garamond', serif;
  letter-spacing: 0.02em;
  line-height: 1.6;
}

.dish-item:hover .dish-name {
  @apply text-orange-500;
}

.dish-item:hover .dish-description {
  @apply text-orange-500/70;
}
</style>
