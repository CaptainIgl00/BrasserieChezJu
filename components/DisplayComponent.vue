<template>
    <div class="restaurant-display">
      <!-- Nouvelle structure pour la grille -->
      <div class="image-grid">
        <!-- Colonne de gauche -->
        <div class="left-images">
          <img src="/images/display/vin.jpg" alt="Wine" class="wine-image" />
          <img src="/images/display/plat-principal.jpg" alt="Restaurant dish" class="dish-image" />
          <img src="/images/display/logo.png" alt="Logo" class="logo-image" />
          <img src="/images/display/slider-img-4.jpg" alt="Slider image" class="slider-image" />
          <img src="/images/display/plumes.png" alt="Plume" class="plume-image" />
        </div>

        <!-- Contenu central -->
        <div class="content">
          <h1 class="title">Brasserie Chez Ju</h1>
          <div class="subtitle">MAÎTRE RESTAURATEUR</div>
          <div class="separator-wrapper">
            <SeparatorComponent show-left-line />
          </div>
          <div class="category">
            BRASSERIE · BAR · TAPAS
          </div>
          
          <p class="description">
            Notre brasserie traditionnelle vous propose une cuisine généreuse mettant<br />
            en valeur les produits locaux et de qualité de notre beau terroir.
          </p>
        </div>

        <!-- Colonne de droite -->
        <div class="right-images">
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
          wine: -2,
          dish: 2,
          interior: -2,
          entrecote: 2,
          logo: 3,
          plume: -2
        }
      }
    },

    mounted() {
      window.addEventListener('mousemove', this.handleParallax);
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
          
          const offsetX = moveX * level * 10;
          const offsetY = moveY * level * 10;
          
          container.style.setProperty('--parallax-offset', `${offsetY}px`);
          img.style.transform = `translateX(${offsetX}px)`;
        });
      }
    }
  }
  </script>
  
  <style scoped>
  .restaurant-display {
    @apply bg-gray-900 text-white min-h-screen p-8 relative;
  }
  
  .image-grid {
    @apply grid grid-cols-3 gap-8 mb-8 relative;
    min-height: 920px;
  }
  
  .left-images, .right-images {
    @apply relative h-full;
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
    @apply flex flex-col items-center justify-center text-center px-8;
  }
  
  .title {
    @apply text-7xl mb-4;
    font-family: 'Dancing Script', cursive;
  }
  
  .subtitle {
    @apply text-sm tracking-widest mb-8 font-semibold;
  }
  
  .category {
    @apply text-orange-500 text-lg tracking-wider mb-8 font-bold;
  }
  
  .description {
    @apply text-gray-300 leading-relaxed;
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
  </style>
