<template>
  <div class="space-y-16 mx-auto max-w-7xl">
    <!-- Formules Section -->
    <section class="formules-section">
      <h2 class="text-3xl font-playfair text-orange-500 text-center font-bold mb-8">Nos Formules</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 px-4">
        <v-card
          v-for="(menu, index) in menus"
          :key="index"
          class="animate-fadeIn backdrop-blur-sm bg-black/60 h-full"
          theme="dark"
          :style="{ animationDelay: `${index * 100}ms` }"
        >
          <MenuSection
            :title="menu.title"
            :formule="menu.formule"
            :description="menu.description"
            :price="menu.price"
            :subtitle="menu.subtitle"
          />
        </v-card>
      </div>
    </section>

    <!-- Menu Gourmand Section -->
    <section class="menu-gourmand-section">
      <h2 class="text-3xl font-playfair text-orange-500 text-center font-bold mb-8">Menu Signature</h2>
      <div class="max-w-3xl mx-auto px-4">
        <MenuGourmand />
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
    formule: "1 boisson chaude au choix + 1 jus de fruit + 1 viennoiserie",
    description: "du mardi au vendredi",
    price: "6",
    subtitle: "du mardi au vendredi"
  },
  {
    title: "Formule Déjeuner",
    formule: "Entrée + Plat ou Plat + Dessert / Entrée + Plat + Dessert",
    description: "du lundi au vendredi",
    price: "19 / 23",
    subtitle: "du lundi au vendredi"
  },
  {
    title: "Formule Routiers",
    formule: "Entrée + Plat + Dessert + 1 boisson",
    description: "du lundi au vendredi",
    price: "20"
  },
  {
    title: "Formule Côte de Boeuf",
    formule: "Planche de jambon Serrano et jambon blanc truffé, Côte de boeuf à volonté, Planche de mignardises",
    description: "55/personne (2 minimum)",
    price: "55"
  },
  {
    title: "Formule des Loulous",
    formule: "Steak haché frais ou poulet pané, Frites maison, Moelleux au chocolat ou glace",
    description: "pour les moins de 12 ans",
    price: "12",
    subtitle: "pour les moins de 12 ans"
  }
]
</script>

<style scoped>
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
