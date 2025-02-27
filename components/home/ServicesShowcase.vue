<template>
  <div class="showcase-container">
    <div class="showcase-header">
      <h2 class="section-title fade-in">Nos Services</h2>
      <div class="section-divider fade-in"></div>
    </div>
    <div class="showcase-content">
      <div class="showcase">
        <div 
          class="showcase-item fade-in"
          v-for="(item, index) in showcaseItems" 
          :key="item.title"
          :style="{ '--delay': `${0.2 + index * 0.2}s` }"
        >
          <div class="icon-container">
            <div class="icon-wrapper">
              <div class="circle-border"></div>
              <div class="icon-glow"></div>
              <nuxt-img 
                :src="`/images/showcase/${item.image}`" 
                :alt="item.title" 
                class="icon"
                preset="showcase"
                placeholder
              />
            </div>
          </div>
          <h3 class="title">{{ item.title }}</h3>
          <p class="description">{{ item.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ServicesShowcase",
  data() {
    return {
      showcaseItems: [
        {
          image: "entrecote.png",
          title: "Produits frais",
          description: "Des produits locaux, frais, de saison, sélectionnés par notre chef"
        },
        {
          image: "chef.png",
          title: "Cuisine passionnée",
          description: "Un chef et une brigade passionnés par la belle cuisine française"
        },
        {
          image: "vin.png",
          title: "Vins de région",
          description: "Des vins d'exceptions triés sur le volet pour offrir le meilleur de notre région"
        },
        {
          image: "cocktail.png",
          title: "Bar à Cocktail",
          description: "Des cocktails maison et une multitude de digestifs de qualité supérieure de tous les instants"
        },
        {
          image: "routier.png",
          title: "Routier",
          description: "Un axe stratégique, une formule repas avantageuse et un parking gratuit 7/7 jours"
        }
      ]
    };
  },
  mounted() {
    // Observer pour les animations au scroll
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('fade-in-visible');
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -10% 0px'
    });

    document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
    
    // Animation subtile des éléments
    this.animateItems();
  },
  methods: {
    animateItems() {
      // Animation subtile des icônes
      const iconWrappers = document.querySelectorAll('.icon-wrapper');
      iconWrappers.forEach((wrapper, index) => {
        const delay = 0.2 + index * 0.1;
        wrapper.style.animationDelay = `${delay}s`;
      });
    }
  }
};
</script>

<style scoped>
.showcase-container {
  @apply bg-gray-900 py-16 md:py-32 relative;
  background-image: url("/images/showcase/background.svg");
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  position: relative;
}

.showcase-container::before {
  content: '';
  @apply absolute inset-0 z-0;
  background: radial-gradient(circle at 50% 30%, rgba(234, 92, 11, 0.05) 0%, transparent 70%);
}

.showcase-header {
  @apply flex flex-col items-center justify-center mb-12 md:mb-16 relative z-10;
}

.section-title {
  @apply text-3xl md:text-4xl lg:text-5xl font-bold text-orange-500 mb-4;
  font-family: 'Dancing Script', cursive;
  text-shadow: 0 2px 10px rgba(234, 92, 11, 0.3);
}

.section-divider {
  @apply w-24 h-1 bg-orange-500 rounded-full;
  box-shadow: 0 0 10px rgba(234, 92, 11, 0.5);
}

.showcase-content {
  @apply mx-auto px-4 sm:px-6 lg:px-8 relative z-10;
  max-width: 1920px;
}

.showcase {
  @apply grid gap-6 md:gap-8;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
}

.showcase-item {
  @apply text-center text-white p-6 lg:p-8 rounded-3xl;
  background-color: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(5px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3), 0 0 15px rgba(234, 92, 11, 0.1);
  min-height: 400px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  transform: translateY(0);
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  border: 1px solid rgba(234, 92, 11, 0.1);
  position: relative;
  overflow: hidden;
}

.showcase-item::after {
  content: '';
  @apply absolute inset-0 opacity-0;
  background: radial-gradient(circle at center, rgba(234, 92, 11, 0.05) 0%, transparent 70%);
  transition: opacity 0.5s ease;
}

.showcase-item:hover {
  transform: translateY(-8px);
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4), 0 0 20px rgba(234, 92, 11, 0.2);
  border-color: rgba(234, 92, 11, 0.3);
}

.showcase-item:hover::after {
  @apply opacity-100;
}

.icon-container {
  @apply flex justify-center items-center mb-8;
}

.icon-wrapper {
  @apply relative flex justify-center items-center bg-black rounded-full mx-auto;
  width: 160px;
  height: 160px;
  @apply lg:w-[200px] lg:h-[200px];
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.5), inset 0 0 20px rgba(234, 92, 11, 0.1);
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  animation: subtle-float 6s ease-in-out infinite;
  will-change: transform;
}

.circle-border {
  @apply absolute inset-0 border-2 border-orange-500;
  border-radius: 9999px;
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  width: 100%;
  height: 100%;
  opacity: 0.3;
}

.icon-glow {
  @apply absolute rounded-full;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle at center, rgba(234, 92, 11, 0.1) 0%, transparent 70%);
  opacity: 0;
  transition: opacity 0.5s ease;
}

.showcase-item:hover .circle-border {
  border-color: #EA5C0B;
  transform: rotate(180deg) scale(1.05);
  opacity: 0.8;
}

.showcase-item:hover .icon-glow {
  opacity: 1;
  animation: pulse-glow 2s ease-in-out infinite;
}

@keyframes pulse-glow {
  0%, 100% { opacity: 0.3; transform: scale(1); }
  50% { opacity: 0.6; transform: scale(1.05); }
}

.showcase-item:hover .icon-wrapper {
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.6), inset 0 0 30px rgba(234, 92, 11, 0.2);
}

.icon {
  @apply z-10;
  width: 75%;
  height: 75%;
  object-fit: contain;
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.3));
}

.showcase-item:hover .icon {
  transform: scale(1.1) rotate(-5deg);
  filter: drop-shadow(0 6px 8px rgba(0, 0, 0, 0.4));
}

.title {
  @apply text-2xl lg:text-3xl mb-4 lg:mb-6 font-bold text-orange-400;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
  transition: color 0.3s ease;
}

.showcase-item:hover .title {
  @apply text-orange-300;
  text-shadow: 0 2px 8px rgba(234, 92, 11, 0.4);
}

.description {
  @apply text-base lg:text-lg leading-relaxed text-gray-300;
  max-width: 90%;
  margin: 0 auto;
  transition: color 0.3s ease;
}

.showcase-item:hover .description {
  @apply text-gray-200;
}

/* Ajustements pour très petits écrans */
@media (max-width: 480px) {
  .showcase-container {
    @apply py-12;
  }

  .showcase {
    @apply gap-4;
  }

  .showcase-item {
    @apply p-4;
    min-height: 320px;
  }

  .icon-wrapper {
    width: 120px;
    height: 120px;
  }

  .title {
    @apply text-xl mb-3;
  }

  .description {
    @apply text-sm;
  }
}

/* Animation de fade-in au scroll */
.fade-in {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.8s ease-out, transform 0.8s cubic-bezier(0.25, 1, 0.5, 1);
  transition-delay: var(--delay, 0s);
}

.fade-in-visible {
  opacity: 1;
  transform: translateY(0);
}
</style>