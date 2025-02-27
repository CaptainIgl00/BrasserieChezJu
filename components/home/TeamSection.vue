<template>
  <div class="team-section">
    <div class="team-particles"></div>
    <div class="team-container">
      <h1 class="title fade-in" style="--delay: 0.1s">L'Équipe</h1>
      <h2 class="subtitle fade-in" style="--delay: 0.2s">
        Une équipe passionnée, à votre service
      </h2>
      
      <BaseDivider class="fade-in" style="--delay: 0.3s" />

      <div class="staff-grid">
        <div class="staff-member fade-in" style="--delay: 0.4s">
          <div class="staff-image-container">
            <div class="image-glow"></div>
            <nuxt-img 
              src="/images/staff/fred.jpg" 
              alt="Frédéric Becq" 
              class="staff-image"
              preset="showcase"
            />
            <div class="staff-overlay">
              <span>Chef Cuisinier</span>
            </div>
          </div>
          <div class="staff-text">
            <h3 class="staff-name">Frédéric Becq</h3>
            <p class="staff-role">Chef</p>
            <p class="staff-description fade-in" style="--delay: 0.5s">Passionné par la cuisine traditionnelle française, Fred apporte son expertise et sa créativité à chaque plat.</p>
          </div>
        </div>

        <div class="staff-member fade-in" style="--delay: 0.6s">
          <div class="staff-image-container">
            <div class="image-glow"></div>
            <nuxt-img 
              src="/images/staff/jb_romain.jpg" 
              alt="Jean-Baptiste & Romain" 
              class="staff-image"
              preset="showcase"
            />
            <div class="staff-overlay">
              <span>Équipe Cuisine</span>
            </div>
          </div>
          <div class="staff-text">
            <h3 class="staff-name">Jean-Baptiste & Romain</h3>
            <p class="staff-role">En cuisine</p>
            <p class="staff-description fade-in" style="--delay: 0.7s">Le duo dynamique qui assure la préparation des plats avec précision et enthousiasme.</p>
          </div>
        </div>

        <div class="staff-member fade-in" style="--delay: 0.8s">
          <div class="staff-image-container">
            <div class="image-glow"></div>
            <nuxt-img 
              src="/images/staff/tino_oceane.jpg" 
              alt="Océane & Valentino" 
              class="staff-image"
              preset="showcase"
              :modifiers="{ rotate: 90 }"
            />
            <div class="staff-overlay">
              <span>Service en Salle</span>
            </div>
          </div>
          <div class="staff-text">
            <h3 class="staff-name">Océane & Valentino</h3>
            <p class="staff-role">En salle</p>
            <p class="staff-description fade-in" style="--delay: 0.9s">Attentifs et chaleureux, ils veillent à ce que votre expérience soit parfaite du début à la fin.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, onUnmounted } from 'vue';
import BaseDivider from '../layout/BaseDivider.vue'

onMounted(() => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('fade-in-visible')
      }
    })
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -10% 0px'
  })

  document.querySelectorAll('.fade-in').forEach(el => observer.observe(el))
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Montserrat:wght@300;400;500;600&family=Playfair+Display:ital@0;1&family=Cormorant+Garamond:ital@0;1&family=Lora:ital@0;1&display=swap');

.team-section {
  @apply relative overflow-hidden py-24 px-4 bg-black/90;
}

.team-particles {
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

.team-container {
  @apply flex flex-col items-center justify-center max-w-7xl mx-auto relative z-10;
}

.title {
  @apply text-4xl md:text-5xl mb-2 text-orange-500;
  font-family: 'Dancing Script', cursive;
  text-shadow: 0 2px 10px rgba(234, 92, 11, 0.3);
}

.subtitle {
  @apply text-2xl md:text-3xl text-white mb-8 italic;
  font-family: 'Cormorant Garamond', serif;
  letter-spacing: 0.02em;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

.staff-grid {
  @apply grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-12 mt-12 w-full;
}

.staff-member {
  @apply flex flex-col items-center transition-all duration-500;
}

.staff-image-container {
  @apply relative overflow-hidden rounded-lg mb-4;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3), 0 0 15px rgba(234, 92, 11, 0.1);
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.staff-image {
  @apply w-[300px] h-[300px] object-cover transition-all duration-500;
  filter: grayscale(80%) brightness(0.9) contrast(1.1);
}

.staff-member:hover .staff-image-container {
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5), 0 0 25px rgba(234, 92, 11, 0.3);
  transform: translateY(-5px);
}

.staff-member:hover .staff-image {
  filter: grayscale(0%) brightness(1) contrast(1.15);
  transform: scale(1.05);
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

.staff-member:hover .image-glow {
  opacity: 1;
  animation: pulse-glow 2s ease-in-out infinite;
}

@keyframes pulse-glow {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 0.6; }
}

/* Overlay des images */
.staff-overlay {
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

.staff-overlay span {
  color: white;
  font-size: 1.25rem;
  font-weight: 500;
  letter-spacing: 1px;
  transform: translateY(10px);
  transition: transform 0.3s ease;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

.staff-member:hover .staff-overlay {
  opacity: 1;
}

.staff-member:hover .staff-overlay span {
  transform: translateY(0);
}

.staff-text {
  @apply text-center mt-4 px-4 max-w-xs;
}

.staff-name {
  @apply text-2xl text-white mb-1;
  font-family: 'Dancing Script', cursive;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
}

.staff-role {
  @apply text-orange-500 text-lg italic mb-3;
  font-family: 'Cormorant Garamond', serif;
}

.staff-description {
  @apply text-gray-300 text-sm leading-relaxed;
  font-family: 'Montserrat', sans-serif;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
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

/* Responsive adjustments */
@media (max-width: 480px) {
  .staff-image {
    @apply w-[250px] h-[250px];
  }
  
  .staff-name {
    @apply text-xl;
  }
  
  .staff-role {
    @apply text-base;
  }
  
  .staff-description {
    @apply text-xs;
  }
}

@media (max-width: 320px) {
  .team-section {
    @apply py-16;
  }
  
  .staff-image {
    @apply w-[200px] h-[200px];
  }
  
  .title {
    @apply text-3xl;
  }
  
  .subtitle {
    @apply text-xl;
  }
}
</style> 