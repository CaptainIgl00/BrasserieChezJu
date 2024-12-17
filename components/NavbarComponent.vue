<script setup>
const isScrolled = ref(false)

onMounted(() => {
  window.addEventListener('scroll', () => {
    isScrolled.value = window.scrollY > 0
  })
})

onUnmounted(() => {
  window.removeEventListener('scroll', () => {})
})

</script>

<template>
  <nav :class="['navbar', { 'navbar-fixed': isScrolled }]">
    <NuxtLink to="/menu" class="nav-link">
      Menu
    </NuxtLink>
    
    <NuxtLink to="/" class="logo-link">
      <img src="/images/display/logo.png" alt="Brasserie Chez Ju" class="h-20 w-auto" />
    </NuxtLink>


    <NuxtLink to="https://www.google.com/maps/reserve/v/dine/c/o0LDliLAXCA"
      class="text-white text-lg font-semibold
        px-4 py-2 rounded-lg mx-8
        transition-all duration-300
        hover:bg-orange-500 hover:scale-105">
      Réserver
    </NuxtLink>
  </nav>
</template>

<style scoped>
.navbar {
  @apply flex justify-between items-center
         px-8 py-6 fixed top-0 left-0 right-0 z-50
         transition-all duration-300 ease-in-out;
  background-color: transparent;
}

.navbar-fixed {
  @apply shadow-lg;
  background-color: rgba(9, 12, 15, 0.85);
  backdrop-filter: blur(8px);
}

.logo-link {
  @apply absolute left-1/2 transform -translate-x-1/2
         transition-transform duration-300 hover:scale-105;
}

.nav-links {
  @apply flex gap-6;
}

.nav-link {
  @apply text-white text-lg font-semibold
         px-4 py-2 rounded-lg mx-8
         transition-all duration-300
         hover:bg-orange-500 hover:scale-105;
}
</style> 