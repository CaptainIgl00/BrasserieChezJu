<template>
  <div class="menu-card">
    <div class="menu-header">
      <h2 class="text-3xl font-bold text-orange-500 font-playfair">Menu Gourmand</h2>
      <div class="price-tag">41 €</div>
    </div>

    <!-- Entrées -->
    <div class="section-container">
      <h3 class="section-title">Entrées</h3>
      <div class="dishes-container">
        <div class="dish-item-with-desc group">
          <span class="dish-name">Soupe de lentilles</span>
          <div class="dish-description">
            Lardons, croûtons et œuf fermier mollet
          </div>
        </div>
        <div class="dish-item-with-desc group">
          <span class="dish-name">Escalope de saumon</span>
          <div class="dish-description">
            Marinée à l'aneth
          </div>
        </div>
        <div class="dish-item-with-desc group">
          <span class="dish-name">Tranche de foie gras mi-cuit</span>
          <div class="dish-description">
            Du périgord
          </div>
        </div>
      </div>
    </div>

    <SeparatorComponent />

    <!-- Plats -->
    <div class="section-container">
      <h3 class="section-title">Plats</h3>
      <div class="dishes-container">
        <div class="dish-item-with-desc group">
          <span class="dish-name">Filet de bar</span>
          <div class="dish-description">
            À la plancha, sauce vierge à la ricotta et son toast de tapenade
          </div>
        </div>
        <div class="dish-item-with-desc group">
          <span class="dish-name">Cassoulet du chef Becq</span>
          <div class="dish-description">
            Élaboré par le chef Becq dans le respect des traditions
          </div>
        </div>
        <div class="dish-item-with-desc group">
          <span class="dish-name">Magret de canard grillé</span>
          <div class="dish-description">
            Du Périgord grillé à la fleur de sel à la plancha
          </div>
        </div>
      </div>
    </div>

    <SeparatorComponent />

    <!-- Desserts -->
    <div class="section-container">
      <h3 class="section-title">Desserts</h3>
      <div class="dishes-container">
        <div class="dish-item-with-desc group">
          <span class="dish-name">Crème brûlée</span>
          <div class="dish-description">
            Et son caramel au beurre salé
          </div>
        </div>
        <div class="dish-item-with-desc group">
          <span class="dish-name">Moelleux au chocolat</span>
          <div class="dish-description">
            Avec sa crème anglaise
          </div>
        </div>
        <div class="dish-item">Café ou chocolat liégeois</div>
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
  @apply p-8 bg-black/60 border-2 border-orange-500 rounded-xl relative overflow-hidden 
         transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_6px_15px_rgba(249,115,22,0.3)];
}

/* Header du menu */
.menu-header {
  @apply flex justify-between items-center mb-8 pb-4 border-b border-orange-500/30;
}

.price-tag {
  @apply text-2xl font-semibold text-orange-500 px-4 py-2 border-2 border-orange-500 
         rounded-lg bg-orange-500/10;
}

/* Sections */
.section-container {
  @apply my-8;
}

.section-title {
  @apply text-2xl font-semibold text-orange-500 text-center mb-6;
  font-family: 'Playfair Display', serif;
}

.dishes-container {
  @apply flex flex-col;
}

/* Plats */
.dish-item {
  @apply p-3 text-center text-gray-200 text-lg 
         hover:text-orange-500 transition-colors duration-300;
}

.dish-item-with-desc {
  @apply relative p-3 cursor-pointer overflow-hidden
         h-[60px] hover:h-[100px] transition-all duration-300;
}

.dish-name {
  @apply block text-gray-200 text-center text-lg 
         transition-all duration-300 group-hover:-translate-y-2 
         group-hover:text-orange-500;
}

.dish-description {
  @apply absolute w-full left-0 bg-orange-500/10 text-orange-500 
         p-3 text-sm italic text-center transition-all duration-300 
         transform translate-y-full group-hover:translate-y-0
         backdrop-blur-sm rounded-b-lg;
}

/* Effet de brillance */
.menu-card::after {
  @apply content-[''] absolute -top-1/2 -left-1/2 w-[200%] h-[200%] 
         pointer-events-none opacity-0 transition-opacity duration-300;
  background: radial-gradient(circle, rgba(249, 115, 22, 0.1) 0%, transparent 70%);
}

.menu-card:hover::after {
  @apply opacity-100;
}
</style>
