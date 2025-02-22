<template>
  <div class="hero-section">
    <div class="hero-container">
      <!-- Colonne des images -->
      <div class="image-column fade-in">
        <!-- Image du plat -->
        <div class="plat-image-wrapper">
          <nuxt-img 
            src="/images/hero/plat_principal.jpg" 
            alt="Plat principal" 
            class="w-full h-full object-cover"
            preset="showcase"
            placeholder
          />
        </div>
        <!-- Image du restaurant -->
        <div class="restaurant-image-wrapper">
          <nuxt-img 
            src="/images/hero/restaurant_interieur.png" 
            alt="Intérieur du restaurant" 
            class="hero-image"
            preset="showcase"
            placeholder
          />
        </div>
      </div>

      <!-- Colonne du texte -->
      <div class="text-column">
        <h2 
          class="hero-title fade-in"
          :style="{ fontFamily: 'Dancing Script, cursive' }"
        >
          {{ brasserie.title }}
        </h2>
        
        <h3 class="hero-subtitle fade-in">
          {{ brasserie.subtitle }}
        </h3>
        
        <BaseDivider :showLeftLine="false" class="fade-in" />
        
        <p class="hero-description fade-in">
          {{ brasserie.description }}
        </p>
        
        <p class="hero-call-to-action fade-in">
          {{ brasserie.callToAction }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import BaseDivider from '../layout/BaseDivider.vue'

export default {
  name: 'HeroSection',
  components: {
    BaseDivider
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
  },
  mounted() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('fade-in-visible');
        }
      });
    }, {
      threshold: 0.1
    });

    document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Montserrat:wght@300;400;500;600&family=Playfair+Display:ital@0;1&family=Cormorant+Garamond:ital@0;1&family=Lora:ital@0;1&display=swap');

.hero-section {
  @apply bg-black/90 p-4 md:p-8;
}

.hero-container {
  @apply max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12 items-center;
}

.image-column {
  @apply relative w-full flex items-center justify-center 
         order-1 md:order-none;
  height: auto;
  margin-bottom: 2rem;
}

.plat-image-wrapper {
  @apply w-[80%] md:w-[90%] relative z-10 overflow-hidden rounded-lg shadow-lg;
  height: 250px;
  @apply md:h-[400px];
}

.restaurant-image-wrapper {
  @apply absolute z-20 transform w-[40%] md:w-[45%] overflow-hidden rounded-lg shadow-lg;
  height: 180px;
  @apply md:h-[250px];
  left: 10%;
  bottom: 0;
  transform: translate(-50%, 50%);
}

.plat-image-wrapper img, .restaurant-image-wrapper img {
  @apply w-full h-full object-cover transition-transform duration-300 ease-in-out;
}

.plat-image-wrapper:hover img, .restaurant-image-wrapper:hover img {
  @apply transform scale-105;
}

.hero-image {
  @apply w-full h-full object-cover;
}

.hero-image:hover {
  @apply transform scale-105;
}

.text-column {
  @apply space-y-4 md:space-y-6 px-4 md:px-8 order-2 md:order-none;
}

.hero-title {
  @apply text-orange-500 text-3xl md:text-4xl lg:text-5xl text-center md:text-left;
  font-family: 'Dancing Script', cursive;
}

.hero-subtitle {
  @apply text-lg md:text-2xl lg:text-3xl text-white leading-tight text-center md:text-left;
  font-family: 'Lora', serif;
}

.hero-description {
  @apply text-gray-300 text-sm md:text-lg leading-relaxed max-w-2xl mx-auto md:mx-0;
  font-family: 'Montserrat', sans-serif;
}

.hero-call-to-action {
  @apply text-gray-300 mt-4 md:mt-8 text-lg md:text-2xl text-center md:text-left;
  font-family: 'Cormorant Garamond', serif;
  font-style: italic;
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

/* Version mobile spécifique */
@media (max-width: 768px) {
  .hero-section {
    @apply pt-8 pb-8;
    min-height: auto;
  }

  .hero-container {
    @apply gap-4;
  }

  .plat-image-wrapper {
    @apply w-[85%];
    height: 220px;
  }

  .restaurant-image-wrapper {
    height: 150px;
    width: 45%;
    left: 7.5%;
  }

  .text-column {
    @apply px-2 space-y-4 mt-20;
  }

  .hero-title {
    @apply text-3xl;
  }

  .hero-subtitle {
    @apply text-lg;
  }

  .hero-description {
    @apply text-sm leading-relaxed;
  }

  .hero-call-to-action {
    @apply text-base mt-4;
  }
}

/* Petits écrans */
@media (max-width: 360px) {
  .plat-image-wrapper {
    height: 180px;
  }

  .restaurant-image-wrapper {
    height: 120px;
    width: 50%;
  }
}
</style>
