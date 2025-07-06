<template>
  <div class="space-y-16 mx-auto max-w-7xl">
    <!-- Formules Section -->
    <section class="formules-section">
      
      <div class="flex flex-col lg:flex-row gap-8 lg:gap-12 px-4">
        <!-- Left Column -->
        <div class="lg:w-1/4 space-y-8">
          <div v-for="menu in menus.slice(0, 3)" :key="menu.title" class="formula-card" :id="getFormulaId(menu.title)">
            <h3 class="formula-title">{{ menu.title }}</h3>
            <div v-if="menu.isLunchMenu" class="formula-content">
              <div v-for="(formule, index) in menu.formules" :key="index" class="formula-item lunch-item">
                <p>{{ formule.type }}</p>
                <p class="lunch-price">{{ formule.price }} €</p>
              </div>
              <p v-if="menu.note" class="formula-note">{{ menu.note }}</p>
            </div>
            <div v-else class="formula-content">
              <p v-for="(item, index) in menu.formule" :key="index" class="formula-item">
                {{ item }}
              </p>
            </div>
            <p v-if="menu.description" class="formula-subtitle">{{ menu.description }}</p>
            <div v-if="!menu.isLunchMenu" class="formula-price">{{ menu.price }} €</div>
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
import MenuGourmand from './MenuGourmand.vue'

const getFormulaId = (title) => {
  const mapping = {
    "Formule Petit déj'": 'petit-dej',
    "Formule Déjeuner": 'dejeuner',
    "Menu Gourmand": 'menu-gourmand',
    "Formule Routiers": 'routier'
  }
  return mapping[title] || title.toLowerCase().replace(/\s+/g, '-')
}

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
    isLunchMenu: true,
    formules: [
      { type: "Entrée + Plat ou Plat + Dessert", price: "19" },
      { type: "Entrée + Plat + Dessert", price: "23" },
      { type: "Plat du Jour", price: "15" }
    ],
    description: "du lundi au vendredi",
    note: "voir ardoise"
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
      "Côte de boeuf",
      "Planche de mignardises"
    ],
    description: "60/personne (2 minimum)",
    price: "60"
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
.formules-section {
  @apply bg-black/90 backdrop-blur-sm rounded-xl p-6 md:p-8;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(234, 92, 11, 0.2);
  animation: fadeIn 0.6s ease-out;
}

.formula-card {
  @apply p-6 bg-black/90 backdrop-blur-sm border border-orange-500/30 rounded-xl relative overflow-hidden transition-all duration-300;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}

.formula-card:hover {
  @apply border-orange-500/50 bg-black/90;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.25), 0 0 15px rgba(234, 92, 11, 0.1);
  transform: translateY(-3px);
}

.formula-title {
  @apply text-2xl text-orange-500 text-center mb-4 transition-colors duration-300;
  font-family: 'Dancing Script', cursive;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.formula-card:hover .formula-title {
  @apply text-orange-400;
}

.formula-content {
  @apply space-y-2 text-gray-400;
  font-family: 'Cormorant Garamond', serif;
}

.formula-item {
  @apply transition-colors duration-300;
  font-size: 1.05rem;
}

.formula-card:hover .formula-item {
  @apply text-gray-300;
}

.formula-subtitle {
  @apply text-gray-500 text-sm italic text-center mt-4 transition-colors duration-300;
  font-family: 'Cormorant Garamond', serif;
}

.formula-card:hover .formula-subtitle {
  @apply text-orange-500/70;
}

.formula-price {
  @apply text-2xl text-orange-500 text-center mt-4 font-bold transition-colors duration-300;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
}

.formula-card:hover .formula-price {
  @apply text-orange-400;
}

/* Prix avec divider pour toutes les formules sauf déjeuner */
.formula-card:not(:has(.formula-note)) .formula-price {
  @apply pt-3 border-t border-orange-500/30;
}

.formula-card:not(:has(.formula-note)):hover .formula-price {
  @apply border-orange-500;
}

.formula-note {
  @apply text-gray-500 text-sm italic text-center transition-colors duration-300;
  font-family: 'Cormorant Garamond', serif;
}

.formula-card:hover .formula-note {
  @apply text-orange-500/70;
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

.lunch-formula {
  @apply p-6 bg-black/90 backdrop-blur-sm border border-orange-500/50 rounded-xl relative overflow-hidden transition-all duration-300;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}

.lunch-formula:hover {
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.25), 0 0 15px rgba(234, 92, 11, 0.1);
  transform: translateY(-3px);
}

.lunch-options {
  @apply space-y-2 text-gray-400 mb-4;
  font-family: 'Cormorant Garamond', serif;
}

.lunch-option {
  @apply flex justify-between items-center transition-colors duration-300;
  font-size: 1.05rem;
}

.lunch-formula:hover .lunch-option {
  @apply text-orange-500/90;
}

.lunch-price {
  @apply font-medium text-orange-500;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}

.lunch-note {
  @apply text-gray-500 text-sm italic text-center mt-2 transition-colors duration-300;
  font-family: 'Cormorant Garamond', serif;
}

.lunch-formula:hover .lunch-note {
  @apply text-orange-500/70;
}

.lunch-divider {
  @apply w-full border-t border-orange-500/30 my-3 transition-colors duration-300;
}

.lunch-formula:hover .lunch-divider {
  @apply border-orange-500;
}

.lunch-note {
  @apply text-gray-500 text-sm italic text-center transition-colors duration-300;
  font-family: 'Cormorant Garamond', serif;
}

.lunch-item {
  @apply flex justify-between items-center gap-2;
}

.lunch-price {
  @apply text-orange-500 font-semibold whitespace-nowrap;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}
</style>
