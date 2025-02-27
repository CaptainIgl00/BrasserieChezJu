<template>
  <div class="restaurant-display">
    <!-- Overlay de particules pour effet ambiance -->
    <div class="particles-overlay"></div>
    
    <!-- Background avec effet parallaxe -->
    <div class="parallax-background"></div>
    
    <div class="content-wrapper">
      <!-- Effet de lumière spotlight -->
      <div class="spotlight"></div>
      
      <!-- Logo animé -->
      <div class="logo-animation">
        <div class="logo-container">
          <h1 class="title reveal-text">Brasserie Chez Ju</h1>
          <div class="logo-underline"></div>
        </div>
      </div>
      
      <!-- Contenu principal avec effet de révélation -->
      <div class="main-content">
        <div class="text-content">
          <div class="subtitle reveal-item" style="--delay: 0.4s">MAÎTRE RESTAURATEUR</div>
          <div class="separator-wrapper reveal-item" style="--delay: 0.6s">
            <BaseDivider />
          </div>
          <div class="category reveal-item" style="--delay: 0.8s">
            BRASSERIE · BAR · TAPAS
          </div>
          <p class="description reveal-item" style="--delay: 1s">
            Notre brasserie traditionnelle vous propose une cuisine généreuse mettant
            en valeur les produits locaux et de qualité de notre beau terroir.
          </p>
        </div>
        
        <!-- Galerie d'images avec effet 3D -->
        <div class="image-gallery">
          <!-- Image principale -->
          <div class="gallery-main reveal-item" style="--delay: 0.3s">
            <nuxt-img 
              src="/images/display/plat_principal.jpg" 
              alt="Plat principal" 
              class="gallery-image"
              loading="eager"
              preset="showcase"
              fetchpriority="high"
              placeholder
            />
            <div class="image-overlay">
              <span>Cuisine Authentique</span>
            </div>
          </div>
          
          <!-- Images secondaires -->
          <div class="gallery-secondary">
            <div class="gallery-item reveal-item" style="--delay: 0.5s">
              <nuxt-img 
                src="/images/display/vin.jpg" 
                alt="Vin"   
                class="gallery-image"
                loading="eager"
                preset="showcase"
                fetchpriority="high"
                placeholder
              />
              <div class="image-overlay">
                <span>Carte des Vins</span>
              </div>
            </div>
            
            <div class="gallery-item reveal-item" style="--delay: 0.7s">
              <nuxt-img 
                src="/images/display/restaurant_interieur.jpg" 
                alt="Intérieur du restaurant" 
                class="gallery-image"
                loading="eager"
                fetchpriority="high"
                preset="showcase"
                placeholder
              />
              <div class="image-overlay">
                <span>Ambiance Chaleureuse</span>
              </div>
            </div>
            
            <div class="gallery-item reveal-item" style="--delay: 0.9s">
              <nuxt-img 
                src="/images/display/entrecote.jpg" 
                alt="Entrecôte" 
                class="gallery-image"
                loading="eager"
                fetchpriority="high"
                preset="showcase"
                placeholder
              />
              <div class="image-overlay">
                <span>Spécialités</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Bouton d'action -->
      <div class="cta-container reveal-item" style="--delay: 1.2s">
        <NuxtLink to="/menu" class="cta-button">
          Découvrir notre carte
          <span class="btn-arrow">→</span>
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, onUnmounted, ref } from 'vue'
import BaseDivider from '../layout/BaseDivider.vue'

// Effet de parallaxe au scroll
const handleParallax = () => {
  const scrollPosition = window.scrollY
  const parallaxElements = document.querySelectorAll('.parallax-background')
  const spotlight = document.querySelector('.spotlight')
  
  parallaxElements.forEach(element => {
    element.style.transform = `translateY(${scrollPosition * 0.4}px)`
  })
  
  if (spotlight) {
    spotlight.style.opacity = Math.max(0, 1 - scrollPosition * 0.003)
  }
}

// Animation des éléments au chargement
onMounted(() => {
  // Observer pour les animations au scroll
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed')
      }
    })
  }, { threshold: 0.1 })
  
  // Observer tous les éléments avec animation
  document.querySelectorAll('.reveal-item, .reveal-text').forEach(el => {
    observer.observe(el)
  })
  
  // Effet de parallaxe
  window.addEventListener('scroll', handleParallax)
  
  // Initialiser les animations
  setTimeout(() => {
    document.querySelectorAll('.reveal-item, .reveal-text').forEach(el => {
      el.classList.add('revealed')
    })
  }, 100)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleParallax)
})
</script>

<style scoped>
/* Base */
.restaurant-display {
  @apply relative w-full min-h-screen overflow-hidden flex items-center justify-center;
  padding-bottom: 2rem;
  background-color: #000;
}

/* Effet de particules */
.particles-overlay {
  @apply absolute inset-0 z-10 opacity-30;
  background-image: radial-gradient(circle at 50% 50%, rgba(234, 92, 11, 0.1) 0%, transparent 8%),
                    radial-gradient(circle at 80% 20%, rgba(234, 92, 11, 0.05) 0%, transparent 10%),
                    radial-gradient(circle at 20% 80%, rgba(234, 92, 11, 0.05) 0%, transparent 10%);
  background-size: 60px 60px, 100px 100px, 80px 80px;
  background-position: 0 0, 0 0, 0 0;
  pointer-events: none;
}

/* Fond avec effet parallaxe */
.parallax-background {
  @apply absolute inset-0 z-0;
  background-image: url("/images/display/background.svg");
  background-size: cover;
  background-position: center;
  transform: translateY(0);
  transition: transform 0.1s ease-out;
  will-change: transform;
}

/* Effet de spotlight */
.spotlight {
  @apply absolute z-20 opacity-70 pointer-events-none;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(
    circle at center,
    rgba(234, 92, 11, 0.05) 0%,
    transparent 50%
  );
  transition: opacity 0.5s ease;
}

/* Conteneur principal */
.content-wrapper {
  @apply relative z-30 container mx-auto flex flex-col items-center justify-center px-4 py-16 md:py-24;
  max-width: 1600px;
}

/* Animation du logo */
.logo-animation {
  @apply mb-12 md:mb-16 w-full;
}

.logo-container {
  @apply flex flex-col items-center;
}

.logo-underline {
  @apply bg-orange-500 h-0.5 mt-2 transform scale-x-0 transition-transform duration-1000;
  width: 120px;
  animation: expandLine 1.5s cubic-bezier(0.25, 1, 0.5, 1) forwards 0.8s;
}

@keyframes expandLine {
  0% { transform: scaleX(0); }
  100% { transform: scaleX(1); }
}

/* Contenu principal */
.main-content {
  @apply w-full flex flex-col lg:flex-row items-center justify-between gap-12 lg:gap-16;
}

/* Contenu texte */
.text-content {
  @apply flex flex-col items-center lg:items-start text-center lg:text-left w-full lg:w-2/5;
}

/* Galerie d'images */
.image-gallery {
  @apply w-full lg:w-3/5 flex flex-col gap-4;
}

.gallery-main {
  @apply w-full h-64 md:h-80 lg:h-96 relative overflow-hidden rounded-xl shadow-2xl;
  transform-style: preserve-3d;
  transform: perspective(1000px) rotateX(0deg) rotateY(0deg);
  transition: transform 0.5s ease;
}

.gallery-secondary {
  @apply grid grid-cols-3 gap-4 mt-4;
}

.gallery-item {
  @apply relative overflow-hidden rounded-xl shadow-xl h-32 md:h-40;
  transform-style: preserve-3d;
  transform: perspective(1000px) rotateX(0deg) rotateY(0deg);
  transition: transform 0.5s ease;
}

.gallery-image {
  @apply w-full h-full object-cover transition-all duration-700;
  filter: grayscale(20%) brightness(90%);
}

.image-overlay {
  @apply absolute inset-0 bg-black/40 opacity-0 flex items-center justify-center transition-opacity duration-300;
}

.image-overlay span {
  @apply text-white text-sm md:text-base font-medium tracking-wider transform translate-y-4 transition-transform duration-300;
}

.gallery-main:hover, .gallery-item:hover {
  transform: perspective(1000px) rotateX(2deg) rotateY(-2deg);
}

.gallery-main:hover .gallery-image, .gallery-item:hover .gallery-image {
  @apply scale-105;
  filter: grayscale(0%) brightness(110%);
}

.gallery-main:hover .image-overlay, .gallery-item:hover .image-overlay {
  @apply opacity-100;
}

.gallery-main:hover .image-overlay span, .gallery-item:hover .image-overlay span {
  @apply translate-y-0;
}

/* Bouton d'action */
.cta-container {
  @apply mt-12 md:mt-16;
}

.cta-button {
  @apply bg-orange-500 text-white px-8 py-3 rounded-full font-medium tracking-wide inline-flex items-center gap-2 transition-all duration-300 relative overflow-hidden;
  box-shadow: 0 4px 20px rgba(234, 92, 11, 0.3);
}

.cta-button::before {
  content: '';
  @apply absolute inset-0 bg-orange-600 transform scale-x-0 origin-left transition-transform duration-300;
  z-index: -1;
}

.cta-button:hover {
  @apply transform -translate-y-1;
  box-shadow: 0 6px 25px rgba(234, 92, 11, 0.4);
}

.cta-button:hover::before {
  @apply scale-x-100;
}

.btn-arrow {
  @apply transition-transform duration-300;
}

.cta-button:hover .btn-arrow {
  @apply transform translate-x-1;
}

/* Typographie */
.title {
  @apply text-4xl sm:text-5xl md:text-6xl lg:text-7xl text-orange-500 font-bold;
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

/* Animations de révélation */
.reveal-text {
  @apply opacity-0;
  animation: revealText 1.2s cubic-bezier(0.25, 1, 0.5, 1) forwards;
  animation-delay: 0.2s;
}

.reveal-item {
  @apply opacity-0 transform translate-y-8;
  transition: opacity 0.8s ease, transform 0.8s cubic-bezier(0.25, 1, 0.5, 1);
  transition-delay: var(--delay, 0s);
}

.reveal-item.revealed {
  @apply opacity-100 transform translate-y-0;
}

@keyframes revealText {
  0% {
    opacity: 0;
    transform: translateY(20px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Responsive */
@media (max-width: 1023px) {
  .main-content {
    @apply flex-col-reverse;
  }
  
  .text-content {
    @apply w-full items-center text-center mt-8;
  }
  
  .gallery-secondary {
    @apply grid-cols-3;
  }
}

@media (max-width: 767px) {
  .gallery-item {
    @apply h-24;
  }
  
  .gallery-main {
    @apply h-56;
  }
}

@media (max-width: 640px) {
  .title {
    @apply text-4xl;
  }
  
  .gallery-secondary {
    @apply gap-2;
  }
  
  .gallery-item {
    @apply h-20;
  }
}

/* Très petits écrans */
@media (max-width: 480px) {
  .gallery-item {
    @apply h-16;
  }
  
  .gallery-main {
    @apply h-48;
  }
  
  .image-overlay span {
    @apply text-xs;
  }
}

/* Ajustement pour les très petits écrans */
@media (max-width: 320px) {
  .gallery-secondary {
    @apply gap-1;
  }
  
  .gallery-item {
    @apply h-14;
  }
  
  .gallery-main {
    @apply h-40;
  }
  
  .title {
    @apply text-3xl;
  }
  
  .subtitle {
    @apply text-sm;
  }
  
  .category {
    @apply text-xs;
  }
  
  .description {
    @apply text-xs;
  }
  
  .cta-button {
    @apply px-5 py-2 text-sm;
  }
}
</style>
