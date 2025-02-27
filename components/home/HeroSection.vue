<template>
  <div class="hero-section">
    <div class="hero-container">
      <!-- Effet de particules subtil -->
      <div class="hero-particles"></div>
      
      <!-- DESKTOP: Colonne des images (visible uniquement sur desktop) -->
      <div class="desktop-column">
        <div class="desktop-image-wrapper fade-in" style="--delay: 0.2s">
          <div class="image-glow"></div>
          <nuxt-img 
            src="/images/hero/plat_principal.jpg" 
            alt="Plat principal" 
            class="desktop-image"
            preset="showcase"
            placeholder
          />
          <div class="image-overlay">
            <span>Cuisine Authentique</span>
          </div>
        </div>
        <div class="desktop-small-image-wrapper fade-in" style="--delay: 0.4s">
          <div class="image-glow"></div>
          <nuxt-img 
            src="/images/hero/restaurant_interieur.png" 
            alt="Intérieur du restaurant" 
            class="desktop-image"
            preset="showcase"
            placeholder
          />
          <div class="image-overlay">
            <span>Ambiance Chaleureuse</span>
          </div>
        </div>
      </div>
      
      <!-- MOBILE: Image principale (visible uniquement sur mobile) -->
      <div class="mobile-top-image fade-in" style="--delay: 0.2s">
        <div class="image-glow"></div>
        <nuxt-img 
          src="/images/hero/plat_principal.jpg" 
          alt="Plat principal" 
          class="mobile-image"
          preset="showcase"
          placeholder
        />
        <div class="image-overlay">
          <span>Cuisine Authentique</span>
        </div>
      </div>
      
      <!-- Colonne du texte -->
      <div class="text-column">
        <h2 class="hero-title fade-in" style="--delay: 0.3s; font-family: 'Dancing Script', cursive;">
          {{ brasserie.title }}
        </h2>
        
        <h3 class="hero-subtitle fade-in" style="--delay: 0.4s">
          {{ brasserie.subtitle }}
        </h3>
        
        <BaseDivider :showLeftLine="false" class="fade-in" style="--delay: 0.5s" />
        
        <p class="hero-description fade-in" style="--delay: 0.6s">
          {{ brasserie.description }}
        </p>
        
        <p class="hero-call-to-action fade-in" style="--delay: 0.7s">
          {{ brasserie.callToAction }}
        </p>
      </div>
      
      <!-- MOBILE: Image secondaire (visible uniquement sur mobile) -->
      <div class="mobile-bottom-image fade-in" style="--delay: 0.8s">
        <div class="image-glow"></div>
        <nuxt-img 
          src="/images/hero/restaurant_interieur.png" 
          alt="Intérieur du restaurant" 
          class="mobile-image"
          preset="showcase"
          placeholder
        />
        <div class="image-overlay">
          <span>Ambiance Chaleureuse</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { onMounted, onUnmounted } from 'vue'
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
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Montserrat:wght@300;400;500;600&family=Playfair+Display:ital@0;1&family=Cormorant+Garamond:ital@0;1&family=Lora:ital@0;1&display=swap');

.hero-section {
  @apply bg-black/90 p-4 md:p-8 relative overflow-hidden;
  padding-top: 2rem;
}

.hero-container {
  @apply max-w-7xl mx-auto relative z-10;
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
}

@media (min-width: 768px) {
  .hero-container {
    grid-template-columns: 1fr 1fr;
    align-items: center;
  }
}

/* Effet de particules subtil */
.hero-particles {
  @apply absolute inset-0 z-0 opacity-30;
  background-image: radial-gradient(circle at 30% 40%, rgba(234, 92, 11, 0.05) 0%, transparent 8%),
                    radial-gradient(circle at 70% 60%, rgba(234, 92, 11, 0.03) 0%, transparent 10%);
  background-size: 80px 80px, 120px 120px;
  animation: float-particles 40s linear infinite;
}

@keyframes float-particles {
  0% { background-position: 0 0, 0 0; }
  100% { background-position: 80px 80px, 120px 120px; }
}

/* DESKTOP IMAGES */
.desktop-column {
  position: relative;
  display: none;
}

@media (min-width: 768px) {
  .desktop-column {
    display: block;
  }
}

.desktop-image-wrapper {
  width: 90%;
  height: 400px;
  overflow: hidden;
  border-radius: 0.5rem;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3), 0 0 15px rgba(234, 92, 11, 0.1);
  position: relative;
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.desktop-small-image-wrapper {
  position: absolute;
  width: 45%;
  height: 250px;
  left: -15%;
  bottom: -20%;
  overflow: hidden;
  border-radius: 0.5rem;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4), 0 0 20px rgba(234, 92, 11, 0.2);
  z-index: 10;
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.desktop-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  filter: brightness(0.9) contrast(1.1);
}

.desktop-image-wrapper:hover .desktop-image,
.desktop-small-image-wrapper:hover .desktop-image {
  transform: scale(1.05);
  filter: brightness(1) contrast(1.15);
}

.desktop-image-wrapper:hover,
.desktop-small-image-wrapper:hover {
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5), 0 0 25px rgba(234, 92, 11, 0.3);
}

/* Effet de lueur sur les images */
.image-glow {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: radial-gradient(circle at center, rgba(234, 92, 11, 0.1) 0%, transparent 70%);
  opacity: 0;
  transition: opacity 0.5s ease;
  z-index: 1;
  pointer-events: none;
}

.desktop-image-wrapper:hover .image-glow,
.desktop-small-image-wrapper:hover .image-glow,
.mobile-top-image:hover .image-glow,
.mobile-bottom-image:hover .image-glow {
  opacity: 1;
  animation: pulse-glow 2s ease-in-out infinite;
}

@keyframes pulse-glow {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 0.6; }
}

/* MOBILE IMAGES */
.mobile-top-image {
  width: 90%;
  height: 220px;
  margin: 0 auto;
  overflow: hidden;
  border-radius: 0.5rem;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3), 0 0 15px rgba(234, 92, 11, 0.1);
  order: 1;
  position: relative;
}

.mobile-bottom-image {
  width: 90%;
  height: 180px;
  margin: 0 auto;
  overflow: hidden;
  border-radius: 0.5rem;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3), 0 0 15px rgba(234, 92, 11, 0.1);
  order: 3;
  position: relative;
}

@media (min-width: 768px) {
  .mobile-top-image,
  .mobile-bottom-image {
    display: none;
  }
}

.mobile-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  filter: brightness(0.9) contrast(1.1);
}

.mobile-top-image:hover .mobile-image,
.mobile-bottom-image:hover .mobile-image {
  transform: scale(1.05);
  filter: brightness(1) contrast(1.15);
}

.mobile-top-image:hover,
.mobile-bottom-image:hover {
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4), 0 0 20px rgba(234, 92, 11, 0.2);
}

/* Overlay des images */
.image-overlay {
  position: absolute;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
  z-index: 2;
}

.image-overlay span {
  color: white;
  font-size: 1.25rem;
  font-weight: 500;
  letter-spacing: 1px;
  transform: translateY(10px);
  transition: transform 0.3s ease;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

.desktop-image-wrapper:hover .image-overlay,
.desktop-small-image-wrapper:hover .image-overlay,
.mobile-top-image:hover .image-overlay,
.mobile-bottom-image:hover .image-overlay {
  opacity: 1;
}

.desktop-image-wrapper:hover .image-overlay span,
.desktop-small-image-wrapper:hover .image-overlay span,
.mobile-top-image:hover .image-overlay span,
.mobile-bottom-image:hover .image-overlay span {
  transform: translateY(0);
}

/* TEXT CONTENT */
.text-column {
  @apply space-y-4 md:space-y-6 px-4 md:px-8;
  order: 2;
}

.hero-title {
  @apply text-orange-500 text-3xl md:text-4xl lg:text-5xl text-center md:text-left;
  text-shadow: 0 2px 10px rgba(234, 92, 11, 0.3);
}

.hero-subtitle {
  @apply text-lg md:text-2xl lg:text-3xl text-white leading-tight text-center md:text-left;
  font-family: 'Lora', serif;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

.hero-description {
  @apply text-gray-300 text-sm md:text-lg leading-relaxed max-w-2xl mx-auto md:mx-0;
  font-family: 'Montserrat', sans-serif;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.hero-call-to-action {
  @apply text-gray-300 mt-4 md:mt-8 text-lg md:text-2xl text-center md:text-left;
  font-family: 'Cormorant Garamond', serif;
  font-style: italic;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

/* ANIMATIONS */
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

/* RESPONSIVE ADJUSTMENTS */
@media (max-width: 480px) {
  .mobile-top-image {
    height: 200px;
    width: 95%;
  }
  
  .mobile-bottom-image {
    height: 160px;
    width: 95%;
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
  
  .image-overlay span {
    font-size: 1rem;
  }
}

@media (max-width: 320px) {
  .hero-section {
    @apply pt-6 pb-6;
  }
  
  .hero-container {
    gap: 1rem;
  }
  
  .mobile-top-image {
    height: 160px;
    width: 100%;
  }
  
  .mobile-bottom-image {
    height: 120px;
    width: 100%;
  }
  
  .text-column {
    @apply px-2 space-y-3;
  }
  
  .hero-title {
    @apply text-2xl;
  }
  
  .hero-subtitle {
    @apply text-sm;
  }
  
  .hero-description {
    @apply text-xs leading-relaxed;
  }
  
  .hero-call-to-action {
    @apply text-sm mt-2;
  }
  
  .image-overlay span {
    font-size: 0.875rem;
  }
}
</style>
