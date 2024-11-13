<template>
  <v-container class="py-8">
    <v-btn 
      color="primary" 
      @click="toggleMenu"
      :class="{ 'rotate-btn': showMenu }"
    >
      Formules et Menus
    </v-btn>
    
    <v-row v-if="showMenu" class="menu-transition">
      <v-container class="d-flex flex-wrap justify-space-around">
        <v-card
          v-for="(menu, index) in menus"
          :key="index"
          class="ma-2 pa-4 menu-card"
          width="350"
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
          <MenuGourmand/>
        </v-card>
      </v-container>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import MenuGourmand from './menuSections/MenuGourmand.vue'
const showMenu = ref(false)

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

const toggleMenu = () => {
  showMenu.value = !showMenu.value
}
</script>

<style scoped>
.bg-black {
  background-color: #000;
}
.text-orange-500 {
  color: #F1A67B;
}

/* Animation du bouton */
.rotate-btn {
  transform: scale(1.05);
  transition: transform 0.3s ease;
}

/* Animation d'apparition des cartes */
.menu-card {
  animation: fadeInUp 0.5s ease forwards;
  opacity: 0;
}

/* Animation de transition du menu */
.menu-transition {
  animation: slideDown 0.3s ease-out;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
