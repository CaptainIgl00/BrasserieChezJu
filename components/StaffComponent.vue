<template>
  <div class="staff-container">
    <h1 class="title font-marcellus fade-in">L'Équipe</h1>
    <h2 class="subtitle font-marcellus fade-in" style="--delay: 0.2s">En Cuisine</h2>
    
    <div class="separator-container fade-in" style="--delay: 0.4s">
      <SeparatorComponent />
    </div>

    <div class="staff-grid">
      <div class="staff-member fade-in" style="--delay: 0.6s">
        <img src="/images/staff/fred.jpg" alt="Frédéric Becq" class="staff-image" />
        <h3 class="staff-name">Frédéric Becq</h3>
        <p class="staff-role">Chef</p>
      </div>

      <div class="staff-member fade-in" style="--delay: 0.8s">
        <img src="/images/staff/jb.jpg" alt="Jean-Baptiste" class="staff-image" />
        <h3 class="staff-name">Jean-Baptiste</h3>
        <p class="staff-role">Second de cuisine</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import SeparatorComponent from './SeparatorComponent.vue';

onMounted(() => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('fade-in-visible')
      }
    })
  }, {
    threshold: 0.1
  })

  document.querySelectorAll('.fade-in').forEach(el => observer.observe(el))
})
</script>

<style scoped>
.staff-container {
  @apply flex flex-col items-center justify-center py-24 px-4 bg-gray-900;
}

.title {
  @apply text-4xl mb-2 text-orange-500;
  font-family: 'Dancing Script', serif;
}

.subtitle {
  @apply text-2xl text-white mb-8;
}

.staff-grid {
  @apply grid grid-cols-1 md:grid-cols-2 gap-12 mt-12 max-w-6xl mx-auto;
}

.staff-member {
  @apply flex flex-col items-center;
}

.staff-image {
  @apply w-[300px] h-[300px] object-cover mb-4 transition-all duration-300;
  filter: grayscale(100%);
}

.staff-member:hover .staff-image {
  filter: grayscale(0%);
  @apply scale-105;
}

.staff-name {
  @apply text-xl text-white mb-1;
  font-family: 'Dancing Script', serif;
}

.staff-role {
  @apply text-[#EA5C0B] italic;
}

.separator-container {
  @apply w-56
}

/* Animation de fade-in au scroll */
.fade-in {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.6s ease-out, transform 0.6s ease-out;
  transition-delay: var(--delay, 0s);
}

.fade-in-visible {
  opacity: 1;
  transform: translateY(0);
}
</style> 