<template>
  <div class="flex flex-col items-center justify-center py-24 px-4 bg-black/95">
    <h1 class="text-4xl md:text-5xl text-orange-500 mb-2" :class="{ 'fade-in': isMounted }" style="font-family: 'Dancing Script', serif;">
      Actualité
    </h1>
    <h2 class="text-xl md:text-2xl text-white mb-8" :class="{ 'fade-in-2': isMounted }">
      Menus du moment
    </h2>
    
    <div class="separator-container w-96 md:w-[32rem] mb-12" :class="{ 'fade-in-3': isMounted }">
      <SeparatorComponent />
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 md:gap-8 max-w-6xl mx-auto">
      <div v-for="(post, index) in instagramPosts" 
           :key="post.id" 
           class="instagram-post group"
           :class="[{ 'fade-in': isMounted }, `fade-delay-${index + 1}`]"
      >
        <div class="relative overflow-hidden rounded-xl shadow-lg">
          <a :href="post.postUrl" target="_blank" class="block">
            <div class="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-end justify-center pb-4">
              <span class="text-white text-sm">Voir sur Instagram</span>
            </div>
            <nuxt-img 
              :src="post.imageUrl" 
              :alt="post.title" 
              class="w-full h-[300px] md:h-[400px] object-cover transition-transform duration-500 group-hover:scale-105"
              preset="showcase"
            />
          </a>
        </div>
        <div class="mt-4 text-center px-2">
          <p class="text-white text-sm md:text-base">{{ post.title }}</p>
          <p class="text-orange-500 text-xs md:text-sm mt-1">{{ post.description }}</p>
        </div>
      </div>
    </div>

    <div class="mt-12 flex justify-center" :class="{ 'fade-in-last': isMounted }">
      <a 
        href="https://www.instagram.com/brasserie_chez_ju/" 
        target="_blank" 
        class="flex items-center gap-3 text-white group transition-all duration-300 hover:scale-105"
      >
        <svg class="w-5 h-5 fill-current transition-all duration-300 group-hover:text-orange-500" viewBox="0 0 448 512" xmlns="http://www.w3.org/2000/svg">
          <path d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z"/>
        </svg>
        <span class="text-sm md:text-base transition-all duration-300 group-hover:text-orange-500">Suivez-nous sur Instagram !</span>
      </a>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import SeparatorComponent from './SeparatorComponent.vue'

const isMounted = ref(false)

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
    imageUrl: '/images/instagram/truffe.jpg',
    postUrl: 'https://www.instagram.com/p/DE5OHkVIKSz/',
    title: 'Menu spécial truffe',
    description: 'Vendredi 7 février'
  },
  {
    id: '2',
    imageUrl: '/images/instagram/menu_de_la_semaine.jpg',
    postUrl: 'https://www.instagram.com/p/DFhqvoQsUpk/',
    title: 'Menu de la semaine',
    description: 'Du lundi 10 au vendredi 14 février'
  },
  {
    id: '3',
    imageUrl: '/images/instagram/saint_valentin.jpg',
    postUrl: 'https://www.instagram.com/p/DExcRqEBDZj/',
    title: 'Menu spéciale Saint Valentin ✨️',
    description: 'Animation au piano par Gabriel'
  }
])

onMounted(() => {
  isMounted.value = true
})
</script>

<style scoped>
.fade-in {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeIn 0.6s ease-out forwards;
}

.fade-in-2 {
  composes: fade-in;
  animation-delay: 0.2s;
}

.fade-in-3 {
  composes: fade-in;
  animation-delay: 0.4s;
}

.fade-delay-1 {
  animation-delay: 0.6s;
}

.fade-delay-2 {
  animation-delay: 0.8s;
}

.fade-delay-3 {
  animation-delay: 1s;
}

.fade-in-last {
  composes: fade-in;
  animation-delay: 1.2s;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 768px) {
  .instagram-post {
    max-width: 500px;
    margin: 0 auto;
  }
}

@media (max-width: 480px) {
  .instagram-post {
    max-width: 100%;
  }
}
</style> 