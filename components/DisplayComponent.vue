<template>
    <div class="restaurant-display">
      <!-- Image Grid -->
      <div class="image-grid">
        <div class="left-images">
          <img src="/images/display/plat-principal.jpg" alt="Restaurant dish" class="dish-image" />
        </div>
        <div class="content">
          <h1 class="title">Brasserie Chez Ju</h1>
          <div class="subtitle">MAÎTRE RESTAURATEUR</div>
          
          <div class="category">
            BRASSERIE · BAR · TAPAS
          </div>
          
          <p class="description">
            Notre brasserie traditionnelle vous propose une cuisine généreuse mettant<br />
            en valeur les produits locaux et de qualité de notre beau terroir.
          </p>
        </div>
        <div class="right-images">
          <img src="/images/display/restaurant-interieur.jpg" alt="Restaurant interior" class="interior-image" />
        </div>
      </div>
      
      <!-- Logo and Reservation -->
      <div class="footer">
        <div class="logo">
          <img src="/images/display/logo.png" alt="Restaurant logo" class="logo-image" />
        </div>
        <button class="reservation-btn">
          Réserver une table
        </button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'DisplayComponent'
  }
  </script>
  
  <style scoped>
  .restaurant-display {
    @apply bg-gray-900 text-white min-h-screen p-8 relative;
  }
  
  .image-grid {
    @apply grid grid-cols-3 gap-8 mb-8;
  }
  
  .left-images, .right-images {
    @apply space-y-4;
  }
  
  .dish-image, .interior-image {
    @apply rounded-lg w-full h-64 object-cover;
  }
  
  .content {
    @apply flex flex-col items-center justify-center text-center px-8;
  }
  
  .title {
    @apply text-5xl mb-4;
    font-family: 'Dancing Script', cursive;
  }
  
  .subtitle {
    @apply text-sm tracking-widest mb-8;
  }
  
  .category {
    @apply text-orange-500 tracking-wider mb-8;
  }
  
  .description {
    @apply text-gray-300 leading-relaxed;
  }
  
  .footer {
    @apply flex justify-between items-center mt-auto;
  }
  
  .logo {
    @apply w-20 h-20 rounded-full overflow-hidden border-2 border-orange-500;
  }
  
  .logo-image {
    @apply w-full h-full object-cover;
  }
  
  .reservation-btn {
    @apply bg-orange-500 text-white px-6 py-3 rounded-lg hover:bg-orange-600 transition-colors;
  }
  
  /* Add wave pattern background */
  .restaurant-display::before {
    content: '';
    @apply absolute inset-0 opacity-10;
    background-image: url("data:image/svg+xml,%3Csvg width='100' height='100' viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M11 18c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm48 25c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm-43-7c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zm63 31c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zM34 90c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zm56-76c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zM12 86c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm28-65c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm23-11c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm-6 60c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm29 22c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zM32 63c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm57-13c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm-9-21c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM60 91c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM35 41c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM12 60c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2z' fill='%23ffffff' fill-opacity='0.1' fill-rule='evenodd'/%3E%3C/svg%3E");
  }
  </style>
