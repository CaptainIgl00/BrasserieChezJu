<template>
  <div class="instagram-section">
    <div class="instagram-container">
      <h1 class="title fade-in" style="--delay: 0.1s">Actualité</h1>
      <h2 class="subtitle fade-in" style="--delay: 0.2s">
        Menus du moment
      </h2>
      
      <BaseDivider class="fade-in" style="--delay: 0.3s" />

      <!-- Carousel pour les posts Instagram -->
      <div class="carousel-container fade-in" style="--delay: 0.4s">
        <button @click="prevSlide" class="carousel-button prev-button">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-6 h-6">
            <polyline points="15 18 9 12 15 6"></polyline>
          </svg>
        </button>
        
        <div class="carousel-track" ref="carouselTrack">
          <div 
            v-for="(post, index) in instagramPosts" 
            :key="post.id" 
            class="carousel-slide"
            :class="{ 
              'active': currentSlide === index,
              'prev': (currentSlide === index + 1) || (currentSlide === 0 && index === instagramPosts.length - 1),
              'next': (currentSlide === index - 1) || (currentSlide === instagramPosts.length - 1 && index === 0)
            }"
          >
            <div class="post-image-container">
              <div class="image-glow"></div>
              <a :href="post.postUrl" target="_blank" class="block relative overflow-hidden">
                <nuxt-img 
                  :src="post.imageUrl" 
                  :alt="post.title" 
                  class="post-image"
                  preset="showcase"
                  @load="onImageLoad(post.id)"
                />
                <div class="post-overlay">
                  <span>Voir sur Instagram</span>
                </div>
              </a>
            </div>
            <div class="post-content">
              <h3 class="post-title">{{ post.title }}</h3>
              <p class="post-description">{{ post.description }}</p>
            </div>
          </div>
        </div>
        
        <button @click="nextSlide" class="carousel-button next-button">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-6 h-6">
            <polyline points="9 18 15 12 9 6"></polyline>
          </svg>
        </button>
      </div>
      
      <!-- Indicateurs de slide -->
      <div class="carousel-indicators fade-in" style="--delay: 0.5s">
        <button 
          v-for="(post, index) in instagramPosts" 
          :key="`indicator-${post.id}`"
          class="indicator-dot"
          :class="{ 'active': currentSlide === index }"
          @click="goToSlide(index)"
        ></button>
      </div>

      <div class="instagram-cta fade-in" style="--delay: 0.6s">
        <a 
          href="https://www.instagram.com/brasserie_chez_ju/" 
          target="_blank" 
          class="cta-link"
        >
          <svg class="cta-icon" viewBox="0 0 448 512" xmlns="http://www.w3.org/2000/svg">
            <path d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z"/>
          </svg>
          <span class="cta-text">Suivez-nous sur Instagram !</span>
        </a>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import BaseDivider from '../layout/BaseDivider.vue'

const isMounted = ref(false)
const imagesLoaded = ref(new Set())
const currentSlide = ref(0)
const carouselTrack = ref(null)
const autoplayInterval = ref<NodeJS.Timeout | null>(null)

interface InstagramPost {
  id: string
  imageUrl: string
  postUrl: string
  title: string
  description: string
}

const instagramPosts = ref<InstagramPost[]>([
  {
    id: '1',
    imageUrl: '/images/instagram/mere.jpg',
    postUrl: 'https://www.instagram.com/p/DJuNhWwika5/',
    title: 'Menu fête des mères',
    description: 'Dimanche 25 mai'
  },
  {
    id: '2',
    imageUrl: '/images/instagram/menu_semaine.jpg',
    postUrl: 'https://www.instagram.com/p/DKpfON_CYBo/',
    title: 'Menu de la semaine',
    description: 'Du lundi 09 juin au vendredi 13 juin'
  },
  {
    id: '3',
    imageUrl: '/images/instagram/soiree_ete.webp',
    postUrl: 'https://www.instagram.com/p/DKsFnQJoUa3/',
    title: "Première soirée de l'été ☀️",
    description: 'Animation musicale avec le DJ Bob Dassin, tapas, brasero, cocktails' 
  }
])

const onImageLoad = (id: string) => {
  imagesLoaded.value.add(id)
}

const nextSlide = () => {
  currentSlide.value = (currentSlide.value + 1) % instagramPosts.value.length
  resetAutoplay()
}

const prevSlide = () => {
  currentSlide.value = (currentSlide.value - 1 + instagramPosts.value.length) % instagramPosts.value.length
  resetAutoplay()
}

const goToSlide = (index: number) => {
  currentSlide.value = index
  resetAutoplay()
}

const startAutoplay = () => {
  autoplayInterval.value = setInterval(() => {
    nextSlide()
  }, 5000) // Change slide every 5 seconds
}

const resetAutoplay = () => {
  if (autoplayInterval.value) {
    clearInterval(autoplayInterval.value)
    startAutoplay()
  }
}

onMounted(() => {
  isMounted.value = true
  startAutoplay()

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

onUnmounted(() => {
  if (autoplayInterval.value) {
    clearInterval(autoplayInterval.value)
  }
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Montserrat:wght@300;400;500;600&family=Playfair+Display:ital@0;1&family=Cormorant+Garamond:ital@0;1&family=Lora:ital@0;1&display=swap');

.instagram-section {
  @apply relative overflow-hidden py-24 px-4;
  background-image: url("/images/showcase/background.svg");
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  position: relative;
}

.instagram-section::before {
  content: '';
  @apply absolute inset-0 z-0;
  background: radial-gradient(circle at 50% 30%, rgba(234, 92, 11, 0.05) 0%, transparent 70%);
}

.instagram-container {
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

/* Styles du carrousel */
.carousel-container {
  @apply relative flex items-center justify-center w-full mt-12 mb-8;
  max-width: 1400px;
  overflow: visible;
}

.carousel-track {
  @apply relative overflow-visible w-full;
  height: 650px;
  perspective: 1000px;
}

.carousel-slide {
  @apply absolute flex flex-col items-center transition-all duration-500 opacity-0;
  width: 100%;
  max-width: 500px;
  left: 50%;
  transform: translateX(-50%) translateZ(-100px) scale(0.8);
  pointer-events: none;
  z-index: 1;
}

.carousel-slide.active {
  @apply opacity-100;
  transform: translateX(-50%) translateZ(0) scale(1);
  z-index: 3;
  pointer-events: auto;
}

.carousel-slide.prev {
  @apply opacity-70;
  transform: translateX(-120%) translateZ(-50px) scale(0.85);
  z-index: 2;
  pointer-events: auto;
}

.carousel-slide.next {
  @apply opacity-70;
  transform: translateX(20%) translateZ(-50px) scale(0.85);
  z-index: 2;
  pointer-events: auto;
}

.carousel-button {
  @apply absolute z-10 flex items-center justify-center w-12 h-12 text-white bg-black/50 rounded-full transition-all duration-300;
  backdrop-filter: blur(5px);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
}

.carousel-button:hover {
  @apply bg-orange-500/70 text-white;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.4), 0 0 10px rgba(234, 92, 11, 0.3);
}

.prev-button {
  @apply left-0 -ml-6;
  z-index: 4;
}

.next-button {
  @apply right-0 -mr-6;
  z-index: 4;
}

.carousel-indicators {
  @apply flex justify-center gap-3 mt-4;
}

.indicator-dot {
  @apply w-3 h-3 rounded-full bg-white/30 transition-all duration-300;
}

.indicator-dot.active {
  @apply bg-orange-500;
  box-shadow: 0 0 10px rgba(234, 92, 11, 0.5);
}

.post-image-container {
  @apply relative overflow-hidden rounded-xl mb-4 w-full;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3), 0 0 15px rgba(234, 92, 11, 0.1);
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  width: 450px;
  height: 450px;
}

.post-image {
  @apply w-full h-full object-contain transition-all duration-500;
  filter: brightness(0.9) contrast(1.1);
}

.carousel-slide.active .post-image-container {
  animation: slide-in 0.5s cubic-bezier(0.4, 0, 0.2, 1) forwards;
}

@keyframes slide-in {
  0% {
    transform: translateY(20px);
    opacity: 0;
  }
  100% {
    transform: translateY(0);
    opacity: 1;
  }
}

.carousel-slide.active:hover .post-image-container,
.carousel-slide.prev:hover .post-image-container,
.carousel-slide.next:hover .post-image-container {
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5), 0 0 25px rgba(234, 92, 11, 0.3);
  transform: translateY(-5px);
}

.carousel-slide.active:hover .post-image,
.carousel-slide.prev:hover .post-image,
.carousel-slide.next:hover .post-image {
  filter: brightness(1.05) contrast(1.15);
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

.carousel-slide.active:hover .image-glow {
  opacity: 1;
  animation: pulse-glow 2s ease-in-out infinite;
}

@keyframes pulse-glow {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 0.6; }
}

/* Overlay des images */
.post-overlay {
  position: absolute;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
  z-index: 2;
}

.post-overlay span {
  color: white;
  font-size: 1.25rem;
  font-weight: 500;
  letter-spacing: 1px;
  transform: translateY(10px);
  transition: transform 0.3s ease;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
  padding: 0.5rem 1rem;
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 4px;
  background-color: rgba(0, 0, 0, 0.3);
}

.carousel-slide.active:hover .post-overlay,
.carousel-slide.prev:hover .post-overlay,
.carousel-slide.next:hover .post-overlay {
  opacity: 1;
}

.carousel-slide.active:hover .post-overlay span,
.carousel-slide.prev:hover .post-overlay span,
.carousel-slide.next:hover .post-overlay span {
  transform: translateY(0);
}

.post-content {
  @apply text-center mt-4 px-4 w-full;
}

.post-title {
  @apply text-xl text-white mb-1;
  font-family: 'Playfair Display', serif;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
}

.post-description {
  @apply text-orange-500 text-base italic;
  font-family: 'Cormorant Garamond', serif;
}

.instagram-cta {
  @apply mt-16 flex justify-center;
}

.cta-link {
  @apply flex items-center gap-3 text-white px-6 py-3 rounded-full transition-all duration-300;
  background-color: rgba(234, 92, 11, 0.1);
  border: 1px solid rgba(234, 92, 11, 0.3);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.cta-link:hover {
  @apply transform scale-105;
  background-color: rgba(234, 92, 11, 0.2);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3), 0 0 15px rgba(234, 92, 11, 0.3);
}

.cta-icon {
  @apply w-5 h-5 fill-current transition-all duration-300;
}

.cta-link:hover .cta-icon {
  @apply text-orange-500;
}

.cta-text {
  @apply text-base transition-all duration-300;
  font-family: 'Montserrat', sans-serif;
}

.cta-link:hover .cta-text {
  @apply text-orange-500;
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
@media (max-width: 1200px) {
  .carousel-container {
    max-width: 95%;
  }
  
  .carousel-track {
    height: 600px;
  }
  
  .post-image-container {
    width: 400px;
    height: 400px;
  }
  
  .carousel-slide.prev {
    transform: translateX(-115%) translateZ(-50px) scale(0.8);
  }
  
  .carousel-slide.next {
    transform: translateX(15%) translateZ(-50px) scale(0.8);
  }
}

@media (max-width: 1024px) {
  .carousel-container {
    max-width: 90%;
  }
  
  .carousel-track {
    height: 550px;
  }
  
  .post-image-container {
    width: 350px;
    height: 350px;
  }
  
  .carousel-slide.prev {
    transform: translateX(-110%) translateZ(-50px) scale(0.8);
  }
  
  .carousel-slide.next {
    transform: translateX(10%) translateZ(-50px) scale(0.8);
  }
}

@media (max-width: 768px) {
  .carousel-container {
    max-width: 90%;
  }
  
  .carousel-track {
    height: 500px;
  }
  
  .carousel-button {
    @apply w-10 h-10;
  }
  
  .post-image-container {
    width: 320px;
    height: 320px;
  }
  
  .carousel-slide.prev {
    transform: translateX(-105%) translateZ(-50px) scale(0.75);
    opacity: 0.5;
  }
  
  .carousel-slide.next {
    transform: translateX(5%) translateZ(-50px) scale(0.75);
    opacity: 0.5;
  }
  
  .post-title {
    @apply text-lg;
  }
  
  .post-description {
    @apply text-sm;
  }
}

@media (max-width: 480px) {
  .instagram-section {
    @apply py-16;
  }
  
  .title {
    @apply text-3xl;
  }
  
  .subtitle {
    @apply text-xl;
  }
  
  .carousel-track {
    height: 450px;
  }
  
  .carousel-button {
    @apply w-8 h-8;
  }
  
  .post-image-container {
    width: 250px;
    height: 250px;
  }
  
  .carousel-slide.prev,
  .carousel-slide.next {
    opacity: 0.4;
  }
  
  .post-title {
    @apply text-base;
  }
  
  .post-description {
    @apply text-xs;
  }
  
  .cta-link {
    @apply px-4 py-2;
  }
  
  .cta-text {
    @apply text-sm;
  }
}

@media (max-width: 320px) {
  .instagram-section {
    @apply py-12;
  }
  
  .title {
    @apply text-2xl;
  }
  
  .subtitle {
    @apply text-lg;
  }
  
  .carousel-track {
    height: 400px;
  }
  
  .post-image-container {
    width: 200px;
    height: 200px;
  }
  
  .carousel-slide.prev,
  .carousel-slide.next {
    display: none;
  }
}
</style> 