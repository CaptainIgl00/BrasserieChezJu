<template>
  <div class="showcase-container">
    <div class="showcase-content">
      <div class="showcase">
        <div 
          class="showcase-item fade-in"
          v-for="(item, index) in showcaseItems" 
          :key="item.title"
          :style="{ animationDelay: `${index * 100}ms` }"
        >
          <div class="icon-container">
            <div class="icon-wrapper">
              <div class="circle-border"></div>
              <img :src="`/images/showcase/${item.image}`" alt="icon" class="icon" />
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
  name: "ShowcaseComponent",
  data() {
    return {
      showcaseItems: [
        {
          image: "produits_frais.png",
          title: "Produits frais",
          description: "Des produits locaux, frais, de saison, sélectionnés par notre chef"
        },
        {
          image: "cuisine_passionnee.png",
          title: "Cuisine passionnée",
          description: "Un chef et une brigade passionnés par la belle cuisine française"
        },
        {
          image: "vins_de_region.png",
          title: "Vins de région",
          description: "Des vins d'exceptions triés sur le volet pour offrir le meilleur de notre région"
        },
        {
          image: "bar_a_cocktail.png",
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
.showcase-container {
  @apply bg-gray-900 py-32;
}

.showcase-content {
  @apply mx-auto px-4 sm:px-6 lg:px-8;
}

.showcase {
  @apply flex flex-wrap justify-center gap-8;
}

.showcase-item {
  @apply text-center text-white w-full md:w-1/2 lg:w-1/4 xl:w-1/6 p-6 rounded-3xl shadow-lg transition-all duration-300 ease-in-out;
  background-image: url("/images/showcase/background.svg");
  background-size: cover;
  background-position: center;
}

.showcase-item:hover {
  @apply transform -translate-y-2 shadow-xl;
}

.icon-container {
  @apply flex justify-center items-center mb-6;
}

.icon-wrapper {
  @apply relative flex justify-center items-center bg-black rounded-full w-48 h-48;
}

.circle-border {
  @apply absolute inset-0 border-4 border-transparent;
  border-radius: 9999px;
  transition: border-color 0.3s ease-in-out, transform 0.6s ease-in-out;
  width: 100%;
  height: 100%;
}

.showcase-item:hover .circle-border {
  border-color: #EA5C0B;
  transform: rotate(360deg);
}

.icon {
  @apply transition-transform duration-300 ease-in-out z-10;
  width: 90%;
  height: 90%;
  object-fit: contain;
}

.showcase-item:hover .icon {
  @apply transform scale-110;
}

.title {
  @apply text-2xl mb-4 font-bold;
}

.description {
  @apply text-lg;
}

@media (max-width: 768px) {
  .showcase {
    @apply p-4 gap-4;
  }
  
  .showcase-item {
    @apply w-full;
  }

  .icon-wrapper {
    width: 100px;
    height: 100px;
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
</style>