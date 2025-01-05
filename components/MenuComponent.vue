<template>
  <div class="space-y-16 mx-auto max-w-7xl">
    <!-- Formules Section -->
    <section class="formules-section">
      
      <div class="flex flex-col lg:flex-row gap-8 lg:gap-12 px-4">
        <!-- Left Column -->
        <div class="lg:w-1/4 space-y-8">
          <div v-for="menu in menus.slice(0, 3)" :key="menu.title" class="formula-card">
            <h3 class="formula-title">{{ menu.title }}</h3>
            <div class="formula-content">
              <p v-for="(item, index) in menu.formule" :key="index" class="formula-item">
                {{ item }}
              </p>
            </div>
            <p v-if="menu.description" class="formula-subtitle">{{ menu.description }}</p>
            <div class="formula-price">{{ menu.price }} €</div>
          </div>
        </div>

        <!-- Center Column - Menu Gourmand -->
        <div class="lg:w-1/2">
          <MenuGourmand />
        </div>

        <!-- Right Column -->
        <div class="lg:w-1/4 space-y-8">
          <div v-for="menu in menus.slice(3)" :key="menu.title" class="formula-card">
            <h3 class="formula-title">{{ menu.title }}</h3>
            <div class="formula-content">
              <p v-for="(item, index) in menu.formule" :key="index" class="formula-item">
                {{ item }}
              </p>
            </div>
            <p v-if="menu.description" class="formula-subtitle">{{ menu.description }}</p>
            <div class="formula-price">{{ menu.price }} €</div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import MenuGourmand from './menuSections/MenuGourmand.vue'

const menus = [
  {
    title: "Formule Petit déj'",
    formule: ["1 boisson chaude au choix", "1 jus de fruit", "1 viennoiserie"],
    description: "du mardi au vendredi",
    price: "6",
    subtitle: "du mardi au vendredi"
  },
  {
    title: "Formule Déjeuner",
    formule: ["Entrée + Plat", "ou", "Plat + Dessert"],
    description: "du lundi au vendredi",
    price: "19 / 23",
    subtitle: "du lundi au vendredi"
  },
  {
    title: "Formule Routiers",
    formule: ["Entrée + Plat + Dessert + 1 boisson"],
    description: "du lundi au vendredi",
    price: "20"
  },
  {
    title: "Formule Côte de Boeuf",
    formule: [
      "Planche de jambon Serrano et jambon blanc truffé",
      "Côte de boeuf à volonté",
      "Planche de mignardises"
    ],
    description: "55/personne (2 minimum)",
    price: "55"
  },
  {
    title: "Formule des Loulous",
    formule: [
      "Steak haché frais ou poulet pané",
      "Frites maison",
      "Moelleux au chocolat ou glace"
    ],
    description: "pour les moins de 12 ans",
    price: "12",
    subtitle: "pour les moins de 12 ans"
  }
]
</script>

<style scoped>
.formula-card {
  @apply p-6 bg-black/60 border border-orange-500/50 rounded-xl relative overflow-hidden;
  font-family: 'Playfair Display', serif;
}

.formula-title {
  @apply text-xl text-orange-500 font-medium text-center mb-4;
  letter-spacing: 0.02em;
}

.formula-content {
  @apply text-gray-200 text-center mb-3 space-y-1;
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.05rem;
}

.formula-item {
  @apply leading-relaxed transition-colors duration-300;
}

.formula-card:hover .formula-item {
  @apply text-orange-500/90;
}

.formula-subtitle {
  @apply text-gray-400 text-sm italic text-center mb-4 transition-colors duration-300;
  font-family: 'Cormorant Garamond', serif;
  letter-spacing: 0.02em;
}

.formula-card:hover .formula-subtitle {
  @apply text-orange-500/70;
}

.formula-price {
  @apply text-orange-500 font-semibold text-lg text-center mt-4 pt-3 border-t border-orange-500/30 transition-all duration-300;
}

.formula-card:hover .formula-price {
  @apply border-orange-500;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fadeIn {
  animation: fadeIn 0.5s ease-out forwards;
}
</style>
