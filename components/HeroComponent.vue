<template>
  <div class="hero-section">
    <div class="hero-container">
      <!-- Colonne des images -->
      <div class="image-column">
        <!-- Image du plat -->
        <div class="plat-image-wrapper">
          <img 
            src="/images/hero/plat-principal.jpg" 
            alt="Plat gastronomique" 
            class="hero-image"
          />
        </div>
        <!-- Image du restaurant -->
        <div class="restaurant-image-wrapper">
          <img 
            src="/images/hero/restaurant-interieur.png" 
            alt="Intérieur du restaurant" 
            class="hero-image"
          />
        </div>
      </div>

      <!-- Colonne du texte -->
      <div class="text-column">
        <h2 
          class="hero-title"
          :style="{ fontFamily: 'Dancing Script, cursive' }"
        >
          {{ brasserie.title }}
        </h2>
        
        <h3 class="hero-subtitle">
          {{ brasserie.subtitle }}
        </h3>
        
        <SeparatorComponent :showLeftLine="false" />
        
        <p class="hero-description">
          {{ brasserie.description }}
        </p>
        
        <p class="hero-call-to-action">
          {{ brasserie.callToAction }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BrasserieHero',
  components: {
    SeparatorComponent: () => import('./SeparatorComponent.vue')
  },
  data() {
    return {
      brasserie: {
        title: 'Brasserie traditionnelle',
        subtitle: 'Restaurant chaleureux et convivial qui prône la bonne humeur !',
        description: `Plongez dans l'atmosphère chaleureuse de notre salle, où le charme du 
          bois se marie à une ambiance traditionnelle et épurée. Les tons 
          chaleureux des couleurs invitent à la détente, créant un espace convivial 
          pour savourer notre cuisine généreuse. La simplicité et l'authenticité se 
          rencontrent dans une décoration soigneusement pensée, mettant en valeur 
          la tradition tout en créant un cadre apaisant. Découvrez le mariage subtil 
          de l'élégance et du rustique, où chaque détail contribue à l'expérience 
          unique de notre brasserie routière à Carcassonne.`,
        callToAction: `Venez vous imprégner de cette atmosphère accueillante et profitez de 
          moments délicieux dans un cadre qui respire la tradition.`
      }
    };
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&display=swap');

.hero-section {
  @apply bg-gray-900 min-h-screen p-8;
}

.hero-container {
  @apply max-w-7xl mx-auto grid md:grid-cols-2 gap-8 items-center;
}

.image-column {
  @apply relative w-full h-[400px] flex items-center justify-center;
}

.plat-image-wrapper {
  @apply w-[100%] h-[100%] relative z-10;
}

.restaurant-image-wrapper {
  @apply w-1/2 h-1/2 absolute z-20 bottom-0 left-0 transform -translate-x-1/2 translate-y-1/2;
}

.hero-image {
  @apply w-full h-full object-cover rounded-lg shadow-lg transition-transform duration-300 ease-in-out;
}

.hero-image:hover {
  @apply transform scale-105;
}

.text-column {
  @apply space-y-6 px-4 md:px-8;
}

.hero-title {
  @apply text-orange-500 text-4xl md:text-5xl;
  font-family: 'Dancing Script', cursive;
}

.hero-subtitle {
  @apply text-3xl md:text-5xl text-white font-light leading-tight;
}

.hero-description {
  @apply text-gray-300 text-lg leading-relaxed;
}

.hero-call-to-action {
  @apply text-gray-300 text-xl italic font-light mt-8;
}
</style>
