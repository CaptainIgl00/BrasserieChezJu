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
    background-image: url("data:image/svg+xml,<svg id='patternId' width='100%' height='100%' xmlns='http://www.w3.org/2000/svg'><defs><pattern id='a' patternUnits='userSpaceOnUse' width='56.915' height='30' patternTransform='scale(2) rotate(90)'><rect x='0' y='0' width='100%' height='100%' fill='hsla(240,6.7%,17.6%,1)'/><path d='M10.023 0c1.263 1.051 2.418 2.246 3.592 3.462 1.874 1.944 3.808 3.938 6.287 5.404-.94.552-1.8 1.18-2.606 1.856-.844-.785-1.66-1.625-2.452-2.444C11.22 4.525 7.476.646 0 .645v1.71c6.752.001 10.089 3.451 13.615 7.107.771.8 1.568 1.619 2.397 2.401a62.36 62.36 0 0 0-1.785 1.776C10.785 10.099 7.056 6.646 0 6.645v1.708c6.38.002 9.706 3.085 13.038 6.513a50.715 50.715 0 0 1-1.878 1.86C8.773 14.73 5.373 12.646 0 12.646v1.707c4.679.001 7.63 1.687 9.86 3.514-.97.793-2.009 1.5-3.173 2.066C4.652 19.07 2.46 18.646 0 18.646v1.706c1.494 0 2.872.171 4.17.512-1.24.332-2.61.517-4.17.517v1.71c7.477-.001 11.22-3.881 14.842-7.63 3.527-3.654 6.864-7.106 13.615-7.106s10.084 3.452 13.612 7.106c3.622 3.75 7.363 7.63 14.842 7.63h.004v-1.71h-.006c-1.56 0-2.932-.186-4.171-.517 1.294-.34 2.675-.512 4.17-.512h.007v-1.706h-.004c-2.466 0-4.654.427-6.686 1.287-1.164-.567-2.206-1.273-3.175-2.066 2.23-1.827 5.182-3.514 9.86-3.514h.005v-1.708h-.004c-5.375 0-8.777 2.084-11.16 4.081a50.04 50.04 0 0 1-1.88-1.86c3.33-3.425 6.657-6.513 13.04-6.513h.004V6.647h-.004c-7.052 0-10.785 3.449-14.23 6.99a53.881 53.881 0 0 0-1.786-1.774 73 73 0 0 0 2.397-2.4c3.528-3.658 6.864-7.108 13.619-7.108h.004V.645c-7.479 0-11.225 3.88-14.848 7.633-.793.819-1.606 1.66-2.45 2.444a19.368 19.368 0 0 0-2.612-1.86c2.482-1.461 4.415-3.46 6.293-5.404C44.472 2.243 45.628 1.051 46.89 0h-2.564a56.28 56.28 0 0 0-1.644 1.638A57.394 57.394 0 0 0 41.04 0h-2.563c1.058.878 2.037 1.854 3.017 2.865a56.484 56.484 0 0 1-1.877 1.864C37.23 2.732 33.83.647 28.457.647c-5.375 0-8.776 2.085-11.163 4.082a57.454 57.454 0 0 1-1.879-1.864c.98-1.01 1.957-1.988 3.016-2.865H15.87a56.212 56.212 0 0 0-1.642 1.638A57.473 57.473 0 0 0 12.583 0zm18.432 2.355c4.678 0 7.63 1.684 9.86 3.511-.967.79-2.003 1.49-3.167 2.061-1.871-.796-4.05-1.281-6.693-1.282-2.65 0-4.825.486-6.696 1.282-1.164-.567-2.198-1.272-3.165-2.057 2.23-1.83 5.18-3.515 9.861-3.515zm.002 10.29c-7.479 0-11.224 3.879-14.847 7.628-2.134 2.213-4.16 4.306-6.916 5.651a15.806 15.806 0 0 0-3.792-1.063l-.134-.022c-.27-.041-.547-.074-.827-.101l-.143-.011c-.232-.02-.465-.037-.703-.052l-.234-.009A17.34 17.34 0 0 0 0 24.644v1.708c.262 0 .52.008.775.019l.211.01c.212.011.424.028.636.045.041.004.089.005.13.009.25.024.494.054.737.088.047.01.095.017.143.024.222.034.44.072.655.116l.083.014c.247.052.492.11.735.171.017.007.036.01.053.017.502.13.99.291 1.466.475h.007a13.434 13.434 0 0 1 1.789.847h.004c.864.484 1.71 1.079 2.591 1.813h2.568c-.048-.044-.095-.092-.141-.136.833-.782 1.624-1.603 2.396-2.402 3.531-3.657 6.868-7.108 13.62-7.108 6.75 0 10.083 3.453 13.61 7.106a69.76 69.76 0 0 0 2.401 2.408c-.048.045-.097.088-.141.132h2.562c2.534-2.11 5.516-3.646 10.02-3.646h.005v-1.71h-.002c-2.646 0-4.825.489-6.697 1.28-2.756-1.349-4.781-3.438-6.918-5.651-3.62-3.752-7.366-7.628-14.84-7.628zm-.002 1.708c6.751 0 10.084 3.453 13.616 7.107 1.875 1.942 3.806 3.94 6.288 5.405-.938.554-1.8 1.182-2.608 1.86-.847-.788-1.664-1.632-2.455-2.452-3.62-3.749-7.366-7.63-14.84-7.63-7.478 0-11.225 3.881-14.845 7.63-.792.823-1.609 1.663-2.455 2.449a19.312 19.312 0 0 0-2.606-1.857c2.478-1.465 4.411-3.46 6.287-5.404 3.53-3.657 6.864-7.108 13.618-7.108zm-.001 10.291c-5.953 0-9.538 2.46-12.581 5.356h2.556c2.534-2.11 5.52-3.648 10.027-3.648 4.504 0 7.485 1.538 10.018 3.648h2.56c-3.038-2.895-6.628-5.356-12.58-5.356z'  stroke-width='1' stroke='none' fill='%2320222aff'/></pattern></defs><rect width='800%' height='800%' transform='translate(0,0)' fill='url(%23a)'/></svg>");
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
    @apply absolute top-[400px] right-[30px];
  }

  .right-images .plume-image {
    @apply absolute bottom-[700px] left-[350px] h-32 rotate-180;
  }

  .interior-image {
    @apply absolute top-0 left-0 w-[400px] h-[450px] object-cover rounded-lg z-10;
  }
  
  .entrecote-image {
    @apply absolute top-[400px] right-0 w-[350px] h-[600px] object-cover rounded-lg z-20;
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
    background: linear-gradient(
      to bottom,
      rgba(0,0,0,0.4) 0%,
      rgba(0,0,0,0.2) 100%
    );
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
