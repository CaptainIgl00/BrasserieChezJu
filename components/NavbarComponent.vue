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
    <div class="nav-container">
      <!-- Section gauche -->
      <div class="nav-side">
        <NuxtLink to="/menu" class="nav-link">
          Menu
        </NuxtLink>
      </div>
      
      <!-- Logo central -->
      <div class="nav-center">
        <NuxtLink to="/" class="logo-link">
          <img src="/images/display/logo.png" alt="Brasserie Chez Ju" class="h-20 w-auto" />
        </NuxtLink>
      </div>

      <!-- Section droite -->
      <div class="nav-side">
        <NuxtLink to="https://www.google.com/maps/reserve/v/dine/c/o0LDliLAXCA"
          class="nav-link">
          Réserver
        </NuxtLink>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  @apply fixed top-0 left-0 right-0 z-50
         transition-all duration-300 ease-in-out;
  background-color: transparent;
}

.navbar-fixed {
  @apply shadow-lg;
  background-color: rgba(9, 12, 15, 0.85);
  backdrop-filter: blur(8px);
}

.nav-container {
  @apply container mx-auto flex items-center justify-between relative px-4 py-6;
  max-width: 1920px;
}

.nav-side {
  @apply w-[200px] flex;
}

.nav-side:first-child {
  @apply justify-start;
}

.nav-side:last-child {
  @apply justify-end;
}

.nav-center {
  @apply absolute left-1/2 transform -translate-x-1/2;
}

.logo-link {
  @apply transition-transform duration-300 hover:scale-105 block;
}

.nav-link {
  @apply text-white text-lg font-semibold
         rounded-lg
         transition-all duration-300
         hover:bg-orange-500 hover:scale-105
         flex items-center justify-center;
  width: 110px;
  height: 40px;
}

/* Responsive */
@media (max-width: 768px) {
  .nav-side {
    @apply w-[120px];
  }

  .nav-link {
    width: 90px;
    height: 36px;
    @apply text-base;
  }

  .logo-link img {
    @apply h-16;
  }
}

@media (max-width: 360px) {
  .nav-side {
    @apply w-[100px];
  }

  .nav-link {
    width: 80px;
    @apply text-sm;
  }

  .logo-link img {
    @apply h-14;
  }
}
</style> 