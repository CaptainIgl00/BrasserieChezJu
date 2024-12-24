<template>
    <div class="restaurant-display">
      <!-- Nouvelle structure pour la grille -->
      <div class="image-grid">
        <!-- Colonne de gauche -->
        <div class="left-images fade-in">
          <img src="/images/display/vin.jpg" alt="Wine" class="wine-image" />
          <img src="/images/display/plat-principal.jpg" alt="Restaurant dish" class="dish-image" />
          <img src="/images/display/logo.png" alt="Logo" class="logo-image" />
          <img src="/images/display/slider-img-4.jpg" alt="Slider image" class="slider-image" />
          <img src="/images/display/plumes.png" alt="Plume" class="plume-image" />
        </div>

        <!-- Contenu central -->
        <div class="content">
          <h1 class="title fade-in">Brasserie Chez Ju</h1>
          <div class="subtitle fade-in">MAÎTRE RESTAURATEUR</div>
          <div class="separator-wrapper fade-in">
            <SeparatorComponent show-left-line />
          </div>
          <div class="category fade-in">
            BRASSERIE · BAR · TAPAS
          </div>
          
          <p class="description fade-in">
            Notre brasserie traditionnelle vous propose une cuisine généreuse mettant<br />
            en valeur les produits locaux et de qualité de notre beau terroir.
          </p>
        </div>

        <!-- Colonne de droite -->
        <div class="right-images fade-in">
          <img src="/images/display/restaurant-interieur.jpg" alt="Restaurant interior" class="interior-image" />
          <img src="/images/display/entrecote.jpg" alt="Entrecote" class="entrecote-image" />
          <img src="/images/display/slider-img-8.jpg" alt="Slider image" class="slider-image" />
          <img src="/images/display/plume.png" alt="Plume" class="plume-image" />
        </div>
      </div>
      
    </div>
  </template>
  
  <script>
  export default {
    name: 'DisplayComponent',
    data() {
      return {
        parallaxLevels: {
          wine: -0.5,
          dish: 0.5,
          interior: -0.5,
          entrecote: 0.5,
          logo: 0.8,
          plume: -0.3
        }
      }
    },

    mounted() {
      window.addEventListener('mousemove', this.handleParallax);
      
      // Ajout de l'Intersection Observer pour le fade-in
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
    },

    beforeDestroy() {
      window.removeEventListener('mousemove', this.handleParallax);
    },

    methods: {
      handleParallax(e) {
        const { clientX, clientY } = e;
        const { innerWidth, innerHeight } = window;
        
        const moveX = (clientX - innerWidth / 2) / innerWidth;
        const moveY = (clientY - innerHeight / 2) / innerHeight;
        
        const images = document.querySelectorAll('.left-images img, .right-images img');
        
        images.forEach(img => {
          const container = img.closest('.left-images, .right-images');
          const level = this.parallaxLevels[img.className.split('-')[0]] || 0;
          
          const offsetX = moveX * level * 5;
          const offsetY = moveY * level * 5;
          
          container.style.setProperty('--parallax-offset', `${offsetY}px`);
          img.style.transform = `translateX(${offsetX}px)`;
        });
      }
    }
  }
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Montserrat:wght@300;400;500;600&display=swap');

  .restaurant-display {
    @apply bg-gray-900 text-white min-h-screen p-4 md:p-8 relative;
  }
  
  .image-grid {
    @apply grid grid-cols-1 md:grid-cols-3 gap-4 md:gap-8 relative;
    min-height: 600px;
    @apply md:min-h-[920px];
  }
  
  .left-images, .right-images {
    @apply hidden md:block relative h-full;
  }
  
  .wine-image {
    @apply absolute top-0 left-0 w-[200px] h-[250px] object-cover rounded-lg z-10;
  }
  
  .dish-image {
    @apply absolute top-[100px] left-[100px] w-[300px] h-[400px] object-cover rounded-lg z-20;
  }
  
  .interior-image {
    @apply absolute top-0 left-0 w-[300px] h-[350px] object-cover rounded-lg z-10;
  }
  
  .entrecote-image {
    @apply absolute bottom-0 right-0 w-[250px] h-[300px] object-cover rounded-lg z-20;
  }
  
  .content {
    @apply flex flex-col items-center justify-center text-center px-4 md:px-8 py-8 md:py-0;
  }
  
  .title {
    @apply text-4xl md:text-7xl mb-4;
    font-family: 'Dancing Script', cursive;
  }
  
  .subtitle {
    @apply text-xl md:text-2xl tracking-wide mb-4 md:mb-6;
    font-family: 'Montserrat', sans-serif;
    font-weight: 500;
  }
  
  .category {
    @apply text-orange-500 text-lg md:text-xl tracking-widest mb-6 md:mb-8;
    font-family: 'Montserrat', sans-serif;
    font-weight: 600;
  }
  
  .description {
    @apply text-gray-300 text-sm md:text-base leading-relaxed max-w-xl md:max-w-2xl mx-auto;
    font-family: 'Montserrat', sans-serif;
    font-weight: 300;
  }
  
  .logo-image {
    @apply w-full h-full object-cover;
  }
  
  /* Add wave pattern background */
  .restaurant-display::before {
    content: '';
    @apply absolute inset-0 opacity-10;
    background-image: url("/images/display/background.svg");
  }
  
  /* Styles de base pour toutes les images */
  .wine-image, .dish-image, .interior-image, .entrecote-image {
    @apply transition-all duration-500 ease-in-out;
    filter: grayscale(20%) brightness(90%);
  }
  
  /* Effets au survol pour les conteneurs d'images */
  .left-images:hover .wine-image {
    @apply -translate-y-2 -translate-x-2;
    filter: grayscale(0%) brightness(100%);
    box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.4);
  }

  
  .left-images:hover .dish-image {
    @apply translate-y-2 translate-x-2;
    filter: grayscale(0%) brightness(100%);
    box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.4);
  }
  
  .right-images:hover .interior-image {
    @apply -translate-y-2 -translate-x-2;
    filter: grayscale(0%) brightness(100%);
    box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.4);
  }
  
  .right-images:hover .entrecote-image {
    @apply translate-y-2 translate-x-2;
    filter: grayscale(0%) brightness(100%);
    box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.4);
  }
  
  /* Styles individuels pour chaque image */
  .wine-image {
    @apply absolute top-0 left-0 w-[300px] h-[350px] object-cover rounded-lg z-10;
  }
  
  .dish-image {
    @apply absolute top-[300px] left-[100px] w-[400px] h-[500px] object-cover rounded-lg z-20;
  }
  
  .logo-image {
    @apply absolute top-[750px] left-[450px] w-[100px] h-[100px] object-cover rounded-lg z-20;
  }

  .left-images .slider-image {
    @apply absolute top-[100px] left-[400px]  object-cover rounded-lg z-20;
  }

  .right-images .slider-image {
    @apply absolute top-[100px] left-[400px] rotate-180 object-cover rounded-lg z-20;
  }

  .left-images .plume-image {
    @apply absolute top-[300px] right-[30px];
  }

  .right-images .plume-image {
    @apply absolute bottom-[800px] left-[250px] h-32 rotate-180;
  }

  .interior-image {
    @apply absolute top-0 left-0 w-[400px] h-[450px] object-cover rounded-lg z-10;
  }
  
  .entrecote-image {
    @apply absolute top-[350px] right-0 w-[350px] h-[600px] object-cover rounded-lg z-20;
  }
  /* Animation des conteneurs */
  .left-images, .right-images {
    @apply relative h-full transition-transform duration-500;
  }

  /* Opacité des images */
  .wine-image, .dish-image, .interior-image, .entrecote-image {
    @apply opacity-90;
  }
  
  .separator-wrapper {
    @apply w-full px-12;
  }

  /* Animations d'entrée */
  @keyframes slideFromLeft {
    from { transform: translateX(-100px); opacity: 0; }
    to { transform: translateX(0); opacity: 1; }
  }

  @keyframes slideFromRight {
    from { transform: translateX(100px); opacity: 0; }
    to { transform: translateX(0); opacity: 1; }
  }

  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }

  /* Application des animations */
  .wine-image {
    animation: slideFromLeft 1.5s ease-in-out;
  }

  .dish-image {
    animation: slideFromLeft 1.5s ease-in-out 0.5s backwards;
  }

  .interior-image {
    animation: slideFromRight 1.5s ease-in-out;
  }

  .entrecote-image {
    animation: slideFromRight 1.5s ease-in-out 0.5s backwards;
  }

  .title {
    animation: fadeIn 1s ease-in-out 0.3s backwards;
  }

  .subtitle {
    animation: fadeIn 1s ease-in-out 0.6s backwards;
  }

  .category {
    animation: fadeIn 1s ease-in-out 0.9s backwards;
  }

  .description {
    animation: fadeIn 1s ease-in-out 1.2s backwards;
  }

  /* Effet parallax */
  .left-images, .right-images {
    transform: translateY(var(--parallax-offset, 0));
    transition: transform 0.1s ease-out;
  }

  /* Ajustement des dimensions */
  .image-grid {
    min-height: 920px; /* Même hauteur que l'exemple */
  }

  /* Ajout d'un filtre mayfair comme dans l'exemple */
  .restaurant-display::after {
    content: '';
    position: absolute;
    inset: 0;
    background:rgba(0,0,0,0.2);
    pointer-events: none;
  }

  /* Ajustement des opacités */
  .wine-image, .dish-image, .interior-image, .entrecote-image {
    opacity: 0.9;
    transition: opacity 0.3s ease;
  }

  .left-images:hover img, .right-images:hover img {
    opacity: 1;
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

  /* Version mobile des images */
  @media (max-width: 768px) {
    .image-grid {
      @apply grid-cols-1;
    }

    .content {
      @apply order-first;
    }

    .left-images, .right-images {
      @apply relative h-[300px] mx-auto max-w-md;
    }

    .wine-image {
      @apply absolute top-0 left-0 w-[150px] h-[200px] md:w-[200px] md:h-[250px];
    }

    .dish-image {
      @apply absolute top-[50px] right-0 w-[200px] h-[250px] md:w-[300px] md:h-[400px];
    }

    .interior-image {
      @apply absolute top-0 left-0 w-[200px] h-[250px] md:w-[300px] md:h-[350px];
    }

    .entrecote-image {
      @apply absolute top-[50px] right-0 w-[150px] h-[200px] md:w-[250px] md:h-[300px];
    }

    .logo-image, .slider-image, .plume-image {
      @apply hidden;
    }
  }

  /* Ajustements pour petits écrans */
  @media (max-width: 480px) {
    .title {
      @apply text-3xl;
    }

    .subtitle {
      @apply text-lg;
    }

    .category {
      @apply text-base;
    }

    .description {
      @apply text-sm;
    }

    .wine-image, .interior-image {
      @apply w-[120px] h-[160px];
    }

    .dish-image, .entrecote-image {
      @apply w-[160px] h-[200px];
    }
  }
  </style>
