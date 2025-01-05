<template>
  <div class="restaurant-display">
    <div class="content-wrapper">
      <!-- Images de gauche -->
      <div class="side-images left-images">
        <div class="image-container tall fade-in" style="--delay: 0s">
          <img src="/images/display/plat-principal.jpg" alt="Plat principal" />
        </div>
        <div class="image-container fade-in" style="--delay: 0.3s; margin-top: -100px; margin-left: 50px;">
          <img src="/images/display/vin.jpg" alt="Vin" />
        </div>
      </div>

      <!-- Contenu central -->
      <div class="content">
        <h1 class="title fade-in" style="--delay: 0.2s">Brasserie Chez Ju</h1>
        <div class="subtitle fade-in" style="--delay: 0.4s">MAÎTRE RESTAURATEUR</div>
        <div class="separator-wrapper fade-in" style="--delay: 0.6s">
          <SeparatorComponent />
        </div>
        <div class="category fade-in" style="--delay: 0.8s">
          BRASSERIE · BAR · TAPAS
        </div>
        <p class="description fade-in" style="--delay: 1s">
          Notre brasserie traditionnelle vous propose une cuisine généreuse mettant
          en valeur les produits locaux et de qualité de notre beau terroir.
        </p>
      </div>

      <!-- Images de droite -->
      <div class="side-images right-images">
        <div class="image-container fade-in" style="--delay: 0.3s; margin-left: -50px;">
          <img src="/images/display/restaurant-interieur.jpg" alt="Intérieur du restaurant" />
        </div>
        <div class="image-container tall fade-in" style="--delay: 0s; margin-top: -100px;">
          <img src="/images/display/entrecote.jpg" alt="Entrecôte" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import SeparatorComponent from './SeparatorComponent.vue'
</script>

<style scoped>
.restaurant-display {
  @apply bg-black/95 relative overflow-hidden px-4;
  min-height: 100vh;
  display: flex;
  align-items: center;
}

/* Background SVG pattern */
.restaurant-display::before {
  content: '';
  @apply absolute inset-0 opacity-10;
  background-image: url("/images/display/background.svg");
  background-size: cover;
  background-position: center;
  z-index: 0;
}

.content-wrapper {
  @apply container mx-auto flex flex-col lg:flex-row items-center justify-between gap-6 lg:gap-16 relative py-6;
  max-width: 1600px;
  z-index: 1;
}

/* Images latérales */
.side-images {
  @apply flex flex-row lg:flex-col gap-4 lg:gap-8 w-full lg:w-1/3 justify-center;
}

.image-container {
  @apply relative overflow-hidden rounded-xl shadow-xl w-1/2 lg:w-full;
  height: 120px;
  z-index: 1;
}

/* Styles spécifiques desktop */
@media (min-width: 1024px) {
  .restaurant-display {
    height: 100vh;
  }

  .content-wrapper {
    height: 100%;
    @apply py-16;
  }

  .side-images {
    height: 100%;
    @apply justify-center;
  }

  .image-container {
    height: 35vh;
  }

  .image-container.tall {
    height: 45vh;
  }

  .left-images .image-container:last-child {
    margin-top: -10vh;
    margin-left: 5vw;
  }

  .right-images .image-container:first-child {
    margin-left: -5vw;
  }

  .right-images .image-container:last-child {
    margin-top: -10vh;
  }

  .title {
    @apply text-7xl mb-4;
  }

  .subtitle {
    @apply text-2xl mb-4;
  }

  .category {
    @apply text-xl mb-6;
  }

  .description {
    @apply text-lg;
    max-width: 90%;
  }
}

/* Version tablette */
@media (min-width: 768px) and (max-width: 1023px) {
  .image-container {
    height: 180px;
  }

  .image-container.tall {
    height: 180px;
  }

  .content-wrapper {
    @apply py-8;
  }
}

/* Mobile */
@media (max-width: 767px) {
  .image-container {
    height: 120px;
  }

  .image-container.tall {
    height: 120px;
  }

  .content-wrapper {
    @apply py-6;
  }
}

/* Très petits écrans */
@media (max-width: 480px) {
  .image-container {
    height: 100px;
  }

  .image-container.tall {
    height: 100px;
  }

  .content-wrapper {
    @apply py-4 gap-4;
  }
}

.side-images img {
  @apply w-full h-full object-cover transition-all duration-500;
  filter: grayscale(20%) brightness(90%);
}

.image-container:hover img {
  @apply scale-105;
  filter: grayscale(0%) brightness(100%);
}

/* Contenu central */
.content {
  @apply flex flex-col items-center text-center w-full lg:w-1/3 relative order-first lg:order-none;
}

.title {
  @apply text-3xl sm:text-4xl md:text-5xl lg:text-6xl text-orange-500 mb-2 md:mb-3;
  font-family: 'Dancing Script', cursive;
}

.subtitle {
  @apply text-base sm:text-lg md:text-xl text-gray-200 tracking-wide mb-2 md:mb-3;
  font-family: 'Montserrat', sans-serif;
}

.separator-wrapper {
  @apply w-full max-w-sm mb-3 md:mb-4;
}

.category {
  @apply text-sm sm:text-base md:text-lg text-orange-500 tracking-widest mb-2 md:mb-4;
  font-family: 'Montserrat', sans-serif;
}

.description {
  @apply text-sm sm:text-base text-gray-300 leading-relaxed max-w-lg md:max-w-xl;
  font-family: 'Montserrat', sans-serif;
}

/* Animation de chargement */
.fade-in {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInAnimation 0.8s ease-out forwards;
  animation-delay: var(--delay, 0s);
}

@keyframes fadeInAnimation {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Responsive */
@media (max-width: 1024px) {
  .content {
    @apply w-full max-w-2xl mx-auto;
  }
}

@media (max-width: 640px) {
  .title {
    @apply text-4xl;
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
}

/* Ajustements responsive pour la superposition */
@media (max-width: 1023px) {
  .image-container {
    margin: 0 !important;
  }

  .side-images {
    @apply px-4;
  }
}
</style>
