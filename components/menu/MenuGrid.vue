<template>
  <div class="w-full max-w-7xl mx-auto px-4 menu-container">
    <!-- En-tête décoratif -->
    <div class="flex items-center justify-center space-x-4 mb-16">
      <div class="flex-grow h-px bg-orange-500/50 max-w-[100px]"></div>
      <h2 class="text-xl md:text-2xl text-center font-playfair text-orange-500 italic px-4">Notre carte change au fil des saisons,<br/>notre bonne humeur jamais !</h2>
      <div class="flex-grow h-px bg-orange-500/50 max-w-[100px]"></div>
    </div>

    <!-- Sections du menu -->
    <div class="space-y-16">
      <!-- Entrées -->
      <div>
        <MenuCategory 
          title="Toc toc toc... entrées"
          :dishes="starters"
        />
      </div>
      
      <!-- Séparateur -->
      <BaseDivider />

      <!-- Salades -->
      <div>
        <MenuCategory 
          title="On se met au vert ?"
          :dishes="salads"
        />
      </div>

      <!-- Séparateur -->
      <BaseDivider />
      
      <!-- T'as faim de tradition ? -->
      <div>
        <MenuCategory 
        title="T'as faim de tradition ?"
        :dishes="traditional"
        />
      </div>
      
      <!-- Séparateur -->
      <BaseDivider />
      
      <!-- Côté Mer -->
      <div>
        <MenuCategory 
        title="Côté Mer"
        :dishes="seafood"
        />
      </div>
      
      <!-- Séparateur -->
      <BaseDivider />
      
      <!-- Côté Terre -->
      <div>
        <MenuCategory 
        title="Côté Terre"
        :dishes="meat"
        />
      </div>
      
      <!-- Séparateur -->
      <BaseDivider />
      
      <!-- Côté Flamme -->
      <div>
        <MenuCategory 
        title="Côté Flamme"
        :dishes="grill"
        />
      </div>

      <!-- Séparateur -->
      <BaseDivider />

      <!-- Desserts -->
      <div>
        <MenuCategory 
        title="Finir en douceur"
        :dishes="desserts"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import MenuCategory from './MenuCategory.vue'
import BaseDivider from '../layout/BaseDivider.vue'

// Données du menu (à déplacer dans un store ou une API plus tard)
const starters = [
  {
    name: "Planche de jambon Serrano et jambon blanc truffé",
    price: "17",
    image: '/images/menu/planche_charcuterie.jpg'
  },
  {
    name: "Camembert entier rôti au piment d'Espelette",
    description: "Servi avec ses mouillettes",
    price: "14"
  },
  {
    name: "Tapenade maison et ses toasts grillés",
    price: "8",
    image: '/images/menu/tapenade.png'
  },
  {
    name: "Planche de foie gras mi-cuit du Périgord",
    portion: "1 tranche 15€ ou 2 tranches 24€",
    price: "15",
    image: '/images/menu/foie_gras.jpg'
  },
  {
    name: "Filets de sardines fraîches",
    description: "Marinés au cidre et aux agrumes",
    price: "14"
  },
  {
    name: "Soupe de lentilles du Pays d'Oc",
    description: "Avec ses lardons, croûtons et son œuf fermier mollet",
    price: "13"
  },
  {
    name: "La grande planche de Becq à partager",
    description: "Serrano, jambon truffé, foie gras, camembert rôti, saumon mariné, sardines, tapenade",
    price: "59"
  }
]

const salads = [
  {
    name: "Salade César",
    description: "Poulet pané, tomates, olives, croûtons, parmesan, œuf fermier mollet frit, sauce césar",
    price: "19"
  },
  {
    name: "Salade Gourmande",
    description: "Gésiers, toast de foie gras, œuf fermier mollet frit, tomates, olives",
    price: "21"
  },
  {
    name: "Escalopes de saumon mariné à l'aneth",
    description: "Frites maison et salade",
    price: "21",
    image: '/images/menu/saumon.png'
  }
]

const traditional = [
  {
    name: "Cassoulet du chef Becq",
    description: "Élaboré dans le respect de la tradition, servi avec sa salade",
    price: "24",
    image: '/images/menu/cassoulet.jpg'
  },
  {
    name: "Le fameux Welsh de Fred au Maroilles",
    description: "Œuf poché, frites maison et salade",
    price: "16",
    image: '/images/menu/welch.jpg'
  }
]

const seafood = [
  {
    name: "Filets de bar à la plancha",
    description: "Toast de tapenade, sauce vierge à la ricotta et roquette",
    price: "24",
    image: '/images/menu/filet_de_bar.jpg'
  },
  {
    name: "Seiches à la plancha",
    description: "En persillade (500g)",
    price: "20"
  }
]

const meat = [
  {
    name: "Le Burger de Ju",
    description: "Steak haché de 180g, oignons confits grenadine, sauce cheddar, tomate, cornichon et servi avec ses frites maison",
    price: "21",
    image: '/images/menu/burger.png'
  },
  {
    name: "Tartare de bœuf",
    description: "Ses condiments, ses frites maison et sa salade verte - Simple 180g",
    price: "20"
  },
  {
    name: "Tartare de bœuf double",
    description: "360g",
    price: "35"
  },
  {
    name: "Tagliatelles de Ju",
    description: "Magret de canard, sauce cèpes et parmesan",
    price: "23"
  },
  {
    name: "Tagliatelles fraîches",
    description: "Au pesto et parmesan",
    price: "14"
  }
]

const grill = [
  {
    name: "Entrecôte grillée",
    description: "Beurre maître d'hôtel (350 g)",
    price: "28",
    image: '/images/menu/entrecote.png'
  },
  {
    name: "Magret de canard du Périgord",
    description: "Grillé fleur de sel de Guérande",
    price: "26",
    image: '/images/menu/magret.jpg'
  },
  {
    name: "Côte de porc noir de Bigorre",
    description: "En deux cuissons (500 g)",
    price: "35",
    image: '/images/menu/cote_porc.png'
  },
  {
    name: "Le demi lapin du Lauragais",
    description: "Grillé et son aïoli (800 g)",
    price: "27"
  },
  {
    name: "Côte de bœuf à partager",
    description: "Demandez l'ardoise",
    portion: "Sauces aux choix: Poivre, cèpes ou roquefort 4€",
    price: "55/kg"
  }
]

const desserts = [
  {
    name: 'Plateau de fromage de l\'épicerie fine "Chez Julien"',
    price: "16"
  },
  {
    name: "Moelleux au chocolat",
    description: "Crème anglaise",
    price: "7",
    image: '/images/menu/moelleux.png'
  },
  {
    name: "Crème brûlée",
    description: "Au caramel beurre salé",
    price: "7",
    image: '/images/menu/creme_brulee.jpg'
  },
  {
    name: "Pavlova aux fruits rouges",
    description: "Et sa chantilly au pamplemousse",
    price: "9",
    image: '/images/menu/pavlova.jpg'
  },
  {
    name: "Profiterole XL",
    description: "Chocolat chaud",
    price: "9",
    image: '/images/menu/profiteroles.jpg'
  },
  {
    name: "Café ou chocolat liégeois",
    price: "9"
  },
  {
    name: "Café ou thé gourmand",
    price: "10",
    image: '/images/menu/cafe_gourmand.jpg'
  },
  {
    name: "Glaces",
    portion: "1 boule 3,50€, 2 boules 6€, 3 boules 8€, Supplément chantilly 1,50€",
    price: "3.50",
    image: '/images/menu/glace.png'
  },
  {
    name: "Irish coffee ou Colonel",
    price: "12"
  }
]

onMounted(() => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('fade-in-visible')
      }
    })
  }, {
    threshold: 0.1,
    rootMargin: '50px'
  })

  document.querySelectorAll('.fade-in').forEach(el => {
    observer.observe(el)
  })
})
</script>

<style scoped>
.menu-container {
  animation: fadeIn 0.6s ease-out;
  @apply bg-black/90 backdrop-blur-sm rounded-xl p-6 md:p-8;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(234, 92, 11, 0.2);
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

/* Animation de fade-in au scroll */
.fade-in {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.6s ease-out, transform 0.6s ease-out;
  will-change: opacity, transform;
}

.fade-in-visible {
  opacity: 1;
  transform: translateY(0);
}

/* Responsive adjustments */
@media (max-width: 640px) {
  .menu-container {
    @apply p-4;
  }
  
  .w-full {
    @apply py-8;
  }

  .flex {
    @apply mb-12 px-2;
  }

  .flex-grow {
    @apply max-w-[60px];
  }

  .text-xl {
    @apply text-lg px-2;
  }

  .space-y-16 {
    @apply space-y-12;
  }
}
</style>
