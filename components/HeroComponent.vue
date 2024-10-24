<template>
  <div class="hero-section bg-gray-900 min-h-screen p-8">
    <div class="max-w-7xl mx-auto grid md:grid-cols-2 gap-8 items-center">
      <!-- Colonne des images -->
      <div class="relative w-full h-[400px]">
        <!-- Image du plat -->
        <div class="w-[80%] h-[250px] relative z-10">
          <img 
            src="/images/plat-principal.jpg" 
            alt="Plat gastronomique" 
            class="w-full h-full object-cover rounded-lg shadow-lg"
          />
        </div>
        <!-- Image du restaurant -->
        <div class="w-[60%] h-[200px] absolute bottom-0 left-8 z-20">
          <img 
            src="/images/restaurant-interieur.png" 
            alt="Intérieur du restaurant" 
            class="w-full h-full object-cover rounded-lg shadow-xl"
          />
        </div>
      </div>

      <!-- Colonne du texte -->
      <div class="space-y-6 px-4 md:px-8">
        <h2 
          class="text-orange-500 font-dancing-script text-4xl md:text-5xl"
          :style="{ fontFamily: 'Dancing Script, cursive' }"
        >
          {{ brasserie.title }}
        </h2>
        
        <h3 class="text-3xl md:text-5xl text-white font-light leading-tight">
          {{ brasserie.subtitle }}
        </h3>
        
        <!-- Séparateur décoratif -->
        <div class="separator-container my-8 flex items-center">
          <div class="diamond-container">
            <div class="diamond-outer">
              <div class="diamond-inner"></div>
            </div>
          </div>
          <div class="separator-line"></div>
        </div>
        
        <p class="text-gray-300 text-lg leading-relaxed">
          {{ brasserie.description }}
        </p>
        
        <p class="text-gray-300 text-xl italic font-light mt-8">
          {{ brasserie.callToAction }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BrasserieHero',
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

.hero-section img {
  @apply transition-transform duration-300 ease-in-out;
}

.hero-section img:hover {
  @apply transform scale-105;
}

/* Styles pour le séparateur décoratif */
.separator-container {
  @apply relative;
}

.diamond-container {
  @apply relative w-8 h-8;
}

.diamond-outer {
  @apply absolute w-6 h-6 border-2 border-orange-500;
  transform: rotate(45deg);
}

.diamond-inner {
  @apply absolute w-3 h-3 bg-orange-500;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.separator-line {
  @apply h-px bg-orange-500;
  width: 100px;
  margin-left: 8px;
}

/* Gestion des transitions et animations */
.diamond-outer, .diamond-inner {
  @apply transition-all duration-300;
}

.separator-container:hover .diamond-outer {
  @apply transform scale-110;
}

.separator-container:hover .diamond-inner {
  @apply transform scale-110;
}
</style>