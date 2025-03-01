<template>
  <div class="wine-list-container">
    <div class="wine-intro">
      <h2 class="wine-title">Notre Sélection de Vins</h2>
      <p class="wine-description">Une sélection soigneusement élaborée pour accompagner vos plats</p>
    </div>

    <!-- Vins Rouges -->
    <div class="wine-category fade-in">
      <h3 class="category-title">Vins Rouges</h3>
      <div class="wines-grid">
        <div v-for="(wine, index) in redWines" :key="index" class="wine-card">
          <div class="wine-header">
            <h4 class="wine-name">{{ wine.name }}</h4>
            <div class="region-domain-container">
              <div class="wine-region">{{ wine.region }}</div>
              <div class="wine-domain">{{ wine.domain }}</div>
            </div>
          </div>
          <div class="wine-details">
            <p v-if="wine.description" class="wine-description-text">{{ wine.description }}</p>
            <div class="wine-prices">
              <div v-if="wine.glassPrice" class="price-item">
                <span class="price-label">Verre</span>
                <span class="price-value">{{ wine.glassPrice }}€</span>
              </div>
              <div class="price-item">
                <span class="price-label">Bouteille</span>
                <span class="price-value">{{ wine.bottlePrice }}€</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Vins Blancs -->
    <div class="wine-category fade-in">
      <h3 class="category-title">Vins Blancs</h3>
      <div class="wines-grid">
        <div v-for="(wine, index) in whiteWines" :key="index" class="wine-card">
          <div class="wine-header">
            <h4 class="wine-name">{{ wine.name }}</h4>
            <div class="region-domain-container">
              <div class="wine-region">{{ wine.region }}</div>
              <div class="wine-domain">{{ wine.domain }}</div>
            </div>
          </div>
          <div class="wine-details">
            <p v-if="wine.description" class="wine-description-text">{{ wine.description }}</p>
            <div class="wine-prices">
              <div v-if="wine.glassPrice" class="price-item">
                <span class="price-label">Verre</span>
                <span class="price-value">{{ wine.glassPrice }}€</span>
              </div>
              <div class="price-item">
                <span class="price-label">Bouteille</span>
                <span class="price-value">{{ wine.bottlePrice }}€</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Vins Rosés -->
    <div class="wine-category fade-in">
      <h3 class="category-title">Vins Rosés</h3>
      <div class="wines-grid">
        <div v-for="(wine, index) in roseWines" :key="index" class="wine-card">
          <div class="wine-header">
            <h4 class="wine-name">{{ wine.name }}</h4>
            <div class="region-domain-container">
              <div class="wine-region">{{ wine.region }}</div>
              <div class="wine-domain">{{ wine.domain }}</div>
            </div>
          </div>
          <div class="wine-details">
            <p v-if="wine.description" class="wine-description-text">{{ wine.description }}</p>
            <div class="wine-prices">
              <div v-if="wine.glassPrice" class="price-item">
                <span class="price-label">Verre</span>
                <span class="price-value">{{ wine.glassPrice }}€</span>
              </div>
              <div class="price-item">
                <span class="price-label">Bouteille</span>
                <span class="price-value">{{ wine.bottlePrice }}€</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Champagnes -->
    <div class="wine-category fade-in">
      <h3 class="category-title">Champagnes</h3>
      <div class="wines-grid">
        <div v-for="(wine, index) in champagnes" :key="index" class="wine-card">
          <div class="wine-header">
            <h4 class="wine-name">{{ wine.name }}</h4>
            <div class="region-domain-container">
              <div class="wine-region">{{ wine.region }}</div>
              <div class="wine-domain">{{ wine.domain }}</div>
            </div>
          </div>
          <div class="wine-details">
            <p v-if="wine.description" class="wine-description-text">{{ wine.description }}</p>
            <div class="wine-prices">
              <div v-if="wine.glassPrice" class="price-item">
                <span class="price-label">Verre</span>
                <span class="price-value">{{ wine.glassPrice }}€</span>
              </div>
              <div class="price-item">
                <span class="price-label">Bouteille</span>
                <span class="price-value">{{ wine.bottlePrice }}€</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

// Données des vins rouges
const redWines = [
  {
    name: "Cuvée Archibald",
    domain: "Domaine La Sapinière",
    region: "AOP Malepère",
    description: "Cabernet Franc et Merlot aux arômes de fruits mûrs, vanille et menthol. Bouche concentrée, tanins soyeux, finale cacao.",
    bottlePrice: "29"
  },
  {
    name: "Le rouge de L'Azérolle",
    domain: "Raymond Julien - Domaine Mirausse",
    region: "AOP Minervois",
    description: "Cinsault, Grenache et Syrah aux notes de violette et cassis. Frais, fruité et souple en bouche.",
    glassPrice: "4",
    bottlePrice: "19"
  },
  {
    name: "Le Grand Penchant",
    domain: "Raymond Julien - Domaine Mirausse",
    region: "AOC Minervois",
    description: "Syrah et Grenache aux arômes de fruits rouges et épices. Frais, long et tannins fins.",
    bottlePrice: "23"
  },
  {
    name: "Les Nourritures Terrestres",
    domain: "Damien Baudouy - Domaine Pautard",
    region: "Vin de France (VDF)",
    description: "Assemblage typique du Minervois, ce vin dévoile des arômes de fruits rouges mûrs et d’épices. Sa bouche est souple et équilibrée, avec des tanins fins et une belle fraîcheur.",
    glassPrice: "3.5",
    bottlePrice: "17"
  },
  {
    name: "Cuvée Pinot noir",
    domain: "Domaine Py",
    region: "IGP Pays d'Oc",
    description: "Pinot Noir bio aux arômes de cerise et framboise. Bouche lisse, tanins fins, finale persistante.",
    bottlePrice: "24"
  },
  {
    name: "La Pompadour",
    domain: "Cave de Castelmaure",
    region: "AOP Corbières",
    description: "Carignan, Syrah et Grenache noir aux arômes de fruits mûrs et épices. Bouche soyeuse, notes de vanille, belle longueur.",
    bottlePrice: "24"
  },
  {
    name: "Clos des Natices",
    domain: "Domaine Galy",
    region: "AOP Cabardès",
    description: "Syrah et Cabernet Franc aux arômes de fruits frais et vanille. Bouche volumineuse, tanins fins, finale réglisse.",
    glassPrice: "4",
    bottlePrice: "21"
  },
  {
    name: "Cuvée Joseph Mazard",
    domain: "Domaine Serres-Mazard",
    region: "AOC Corbières",
    description: "Syrah, Carignan, Grenache et Mourvèdre aux arômes de fruits noirs, thym et café. Bouche riche et soyeuse, finale réglisse.",
    bottlePrice: "28"
  },
  {
    name: "Château de Villemajou",
    domain: "Domaine Gérard Bertrand",
    region: "AOP Corbières Boutenac",
    description: "Robe grenat profond, arômes de fruits confits, épices et cuir. Bouche ronde, tanins fondus, finale longue.",
    bottlePrice: "39"
  }
];


// Données des vins rosés
const roseWines = [
  {
    name: "Tom et Lilly",
    domain: "Raymond Julien – Domaine Mirausse",
    region: "AOP Minervois",
    description: "Rosé frais et fruité à base de Grenache et Cinsault. Léger, équilibré et rafraîchissant, parfait pour les journées ensoleillées.",
    glassPrice: "3.5",
    bottlePrice: "18"
  },
  {
    name: "Le Rosé",
    domain: "Domaine La Sapinière",
    region: "AOP Malepère",
    description: "Assemblage de Merlot, Grenache et Cabernet Franc. Robe rose-pêche, bouche fruitée et structurée, idéale en apéritif ou avec un repas.",
    bottlePrice: "20"
  },
  {
    name: "Gris Blanc",
    domain: "Domaine Gérard Bertrand",
    region: "IGP Pays d'Oc",
    description: "Rosé très pâle aux notes délicates de petits fruits rouges. Frais, léger et vif, avec une finale subtilement minérale.",
    bottlePrice: "24"
  }
];

// Données des vins blancs
const whiteWines = [
  {
    name: "Uby n°4",
    domain: "Domaine Uby",
    region: "IGP Côtes de Gascogne",
    description: "Blanc moelleux issu de Gros et Petit Manseng. Nez exotique, bouche veloutée et crémeuse, finale sur le coing et le citron confit.",
    glassPrice: "4",
    bottlePrice: "20"
  },
  {
    name: "Cuvée Antoine",
    domain: "Domaine Py",
    region: "AOC Corbières",
    description: "Blanc bio alliant Vermentino et Grenache blanc. Nez d’agrumes, bouche vive et subtile, parfait avec poissons et crustacés.",
    bottlePrice: "24"
  },
  {
    name: "Chardonnay",
    domain: "Domaine Antech",
    region: "IGP Pays d'Oc",
    description: "Chardonnay frais et croquant aux arômes floraux et exotiques. Équilibré et minéral, idéal avec poissons et fruits de mer.",
    glassPrice: "3.5",
    bottlePrice: "17"
  },
  {
    name: "Cuvée Marie-Pierre",
    domain: "Domaine Serres-Mazard",
    region: "AOC Corbières",
    description: "Blanc demi-doux aux notes d’agrumes et de fleurs. Frais et léger, il accompagne parfaitement fruits de mer et poissons grillés.",
    bottlePrice: "21"
  }
];

// Données des champagnes
const champagnes = [
  {
    name: "Première Bulles",
    domain: "Sieur d'Arques",
    region: "AOC Limoux",
    description: "Élaboré selon la méthode traditionnelle, cet assemblage de Chardonnay, Chenin et Mauzac offre des bulles fines, une bouche onctueuse et une finale toastée.",
    glassPrice: "5",
    bottlePrice: "26"
  },
  {
    name: "Blanquette L'Ancestrale",
    domain: "Domaine Antech",
    region: "AOP Limoux",
    description: "Blanquette douce et pétillante à base de Mauzac, aux arômes de miel, d’acacia et de poire mûre. Finale fruitée et vive sur la pomme et le raisin.",
    glassPrice: "4.5",
    bottlePrice: "22"
  },
  {
    name: "Blanquette Brut nature",
    domain: "Domaine Antech",
    region: "AOP Blanquette Limoux",
    description: "Brut nature frais et léger, dominé par le Mauzac avec une touche de Chenin et Chardonnay. Notes de pomme verte, citron et camomille, avec une finale vive et minérale.",
    glassPrice: "4.5",
    bottlePrice: "23"
  },
  {
    name: "Champagne Taittinger",
    region: "Champagne",
    description: "Assemblage raffiné de Chardonnay, Pinot Noir et Pinot Meunier. Fines bulles, arômes de fruits frais et brioche, bouche vive et élégante avec une touche miellée.",
    bottlePrice: "70"
  }
];

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
.wine-list-container {
  @apply space-y-16 max-w-7xl mx-auto;
  animation: fadeIn 0.6s ease-out;
}

.wine-intro {
  @apply text-center mb-12;
}

.wine-title {
  @apply text-3xl md:text-4xl text-orange-500 mb-4;
  font-family: 'Dancing Script', cursive;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.wine-description {
  @apply text-gray-400 italic text-lg;
  font-family: 'Cormorant Garamond', serif;
}

.wine-category {
  @apply bg-black/95 backdrop-blur-sm rounded-xl p-6 md:p-8 mb-12;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.6);
  border: 1px solid rgba(234, 92, 11, 0.2);
}

.category-title {
  @apply text-2xl text-orange-500 mb-8 text-center;
  font-family: 'Dancing Script', cursive;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.wines-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.wine-card {
  @apply bg-black/95 p-5 rounded-lg transition-all duration-300 hover:-translate-y-1;
  border: 1px solid rgba(234, 92, 11, 0.2);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
}

.wine-card:hover {
  border-color: rgba(234, 92, 11, 0.4);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4), 0 0 15px rgba(234, 92, 11, 0.1);
}

.wine-header {
  @apply border-b border-orange-500/20 pb-3 mb-3;
}

.region-domain-container {
  @apply flex justify-between items-center mt-1;
}

.wine-name {
  @apply text-xl text-orange-500 font-medium;
  font-family: 'Cormorant Garamond', serif;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.wine-region {
  @apply text-sm text-gray-500 italic;
  font-family: 'Cormorant Garamond', serif;
}

.wine-domain {
  @apply text-sm text-gray-500 italic text-right;
  font-family: 'Cormorant Garamond', serif;
}

.wine-details {
  @apply space-y-3;
}

.wine-description-text {
  @apply text-gray-400 text-sm italic;
  font-family: 'Cormorant Garamond', serif;
}

.wine-prices {
  @apply flex flex-wrap justify-between mt-4 gap-2;
}

.price-item {
  @apply flex flex-col;
}

.price-label {
  @apply text-xs text-gray-500;
  font-family: 'Montserrat', sans-serif;
}

.price-value {
  @apply text-lg text-orange-500 font-semibold;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
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

@media (max-width: 768px) {
  .wines-grid {
    grid-template-columns: 1fr;
  }
  
  .wine-card {
    @apply p-4;
  }
  
  .wine-prices {
    @apply flex-col gap-1;
  }
  
  .price-item {
    @apply flex-row justify-between;
  }
}
</style> 