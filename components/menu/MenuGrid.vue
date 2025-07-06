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
          title="Toc toc toc... entrées 'à partager (ou pas)''"
          :dishes="starters"
        />
      </div>
      
      <!-- Séparateur -->
      <BaseDivider />

      <!-- Salades -->
      <div>
        <MenuCategory 
          title="On se met au vert ? Grandes salades"
          :dishes="salads"
        />
      </div>

      <!-- Séparateur -->
      <BaseDivider />
      
      <!-- T'as faim de tradition ? -->
      <div>
        <MenuCategory 
        title="T'as faim de tradition ? Du Nord au Sud"
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
    name: "Gaspacho de tomates",
    description: "Burrata, pesto et copeaux de parmesan",
    price: "15"
  },
  {
    name: "Assiette de bulots et son aïoli",
    price: "12"
  },
  {
    name: "Camembert entier rôti au piment d'Espelette",
    description: "Servi avec ses mouillettes",
    price: "14"
  },
  {
    name: "Tataki de thon mariné",
    description: "Au soja, vinaigrette wasabi et sésame forestier",
    price: "17"
  }
]

const salads = [
  {
    name: "Salade César",
    description: "Poulet pané, tomates, olives, croûtons, parmesan, œuf fermier mollet frit, sauce césar",
    price: "20"
  },
  {
    name: "Salade du Sud-Ouest",
    description: "Gésiers de canard maison, toast de foie gras, magret de canard séché, tomates, olives et pignons torréfiés",
    price: "22"
  },
  {
    name: "Salade Pelardon",
    description: "'AOC Haute Corbières' Pelardon rôti, miel, romarin et jambon serrano",
    price: "19"
  },
  {
    name: "Éventail de melon",
    description: "Jambon serrano et son shooter de porto",
    price: "19"
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
    name: "Cassoulet de Fred",
    description: "Élaboré dans le respect de la tradition, servi avec sa salade",
    price: "24",
    image: '/images/menu/cassoulet.jpg'
  },
  {
    name: "Le fameux Welsh de Fred aux Maroilles",
    description: "Bière, cheddar, jambon truffé, œuf poché, frites maison et salade",
    price: "18",
    image: '/images/menu/welch.jpg'
  }
]

const seafood = [
  {
    name: "Daurade royale entière planchée",
    description: "(350g environ), sauce vierge",
    price: "24",
  },
  {
    name: "Steack de thon planché",
    description: "et huile au piment d'Espelette",
    price: "25",
  },
  {
    name: "Seiche à la plancha",
    description: "(300g environ) et persillade ",
    price: "22",
    image: '/images/menu/filet_de_bar.jpg'
  },
  {
    name: "Moules",
    description: "Selon arrivage à la marinière",
    price: "16"
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
    price: "21"
  },
  {
    name: "Tartare de bœuf double",
    description: "360g",
    price: "36"
  },
  {
    name: "Tagliatelles fraîches 'du petit Becq'",
    description: "Magret de canard, sauce cèpes et parmesan",
    price: "24"
  },
  {
    name: "Tagliatelles fraîches",
    description: "Au pesto et parmesan",
    price: "15"
  }
]

const grill = [
  {
    name: "L-Bone de boeuf grillé",
    description: "'Faux filet sur os', fleur de sel (350g environ)",
    price: "27",
  },
  {
    name: "Magret de canard du Périgord",
    description: "Grillé, fleur de sel de Guérande (350g environ)",
    price: "28",
    image: '/images/menu/magret.jpg'
  },
  {
    name: "Travers de porc grillé",
    description: "Huile au tandoori",
    price: "18"
  },
  {
    name: "Demi coquelet de chez 'Les Mexicots' grillé",
    description: "Et son aïoli (400g environ)",
    price: "22"
  },
  {
    name: "Côte de bœuf à partager",
    description: "Demandez l'ardoise",
    portion: "Sauces aux choix: Poivre, cèpes ou roquefort 4€",
    price: "65/kg"
  }
]

const desserts = [
  {
    name: 'Plateau de fromage de l\'épicerie fine "Chez Julien"',
    price: "16"
  },
  {
    name: "Pavlova aux fruits rouges",
    description: "Et sa chantilly au pamplemousse",
    price: "10",
    image: '/images/menu/pavlova.jpg'
  },
  {
    name: "Profiterole XL",
    description: "Chocolat chaud",
    price: "10",
    image: '/images/menu/profiteroles.jpg'
  },
  {
    name: "Café ou chocolat liégeois",
    price: "10"
  },
  {
    name: "Café ou thé gourmand",
    price: "11",
    image: '/images/menu/cafe_gourmand.jpg'
  },
  {
    name: "Moelleux au chocolat",
    description: "Crème anglaise",
    price: "7",
    image: '/images/menu/moelleux.png'
  },
  {
    name: "Salade de fruits frais",
    description: "Et sa boule de glace au yaourt",
    price: "8"
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
