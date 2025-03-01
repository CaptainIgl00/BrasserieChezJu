<template>
  <div class="main-container">
    <div class="background-pattern"></div>
    <TheNavbar />
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<script setup>
import TheNavbar from './components/layout/TheNavbar.vue'
</script>

<style>
.main-container {
  @apply relative min-h-screen bg-black;
}

.background-pattern {
  @apply fixed inset-0 z-0;
  background-image: url('/images/pattern.svg');
  background-position: center;
  background-size: cover;
  background-repeat: repeat;
  opacity: 0.15;
}

/* Scrollbar personnalisée pour les navigateurs Webkit (Chrome, Safari, etc.) */
::-webkit-scrollbar {
  width: 10px;
}

::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.9);
}

::-webkit-scrollbar-thumb {
  background: rgb(249, 115, 22);
  border-radius: 5px;
}

::-webkit-scrollbar-thumb:hover {
  background: rgb(251, 146, 60);
}

/* Scrollbar personnalisée pour Firefox */
* {
  scrollbar-width: thin;
  scrollbar-color: rgb(249, 115, 22) rgba(0, 0, 0, 0.9);
}

/* Ajustements globaux pour les très petits écrans */
@media (max-width: 320px) {
  html, body {
    overflow-x: hidden;
    width: 100%;
  }
  
  /* Réduire les marges et paddings par défaut */
  .container {
    padding-left: 0.5rem !important;
    padding-right: 0.5rem !important;
  }
  
  /* Ajuster la taille des textes */
  h1 {
    font-size: 1.5rem !important;
  }
  
  h2 {
    font-size: 1.25rem !important;
  }
  
  h3 {
    font-size: 1rem !important;
  }
  
  p {
    font-size: 0.875rem !important;
  }
}
</style>