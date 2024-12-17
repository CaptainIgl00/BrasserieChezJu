<template>
  <div class="staff-container">
    <h1 class="title font-marcellus">L'Équipe</h1>
    <h2 class="subtitle font-marcellus">En Cuisine</h2>
    
    <div class="separator-container">
      <SeparatorComponent />
    </div>

    <div class="staff-grid">
      <div class="staff-member">
        <img src="/images/staff/fred.jpg" alt="Frédéric Becq" class="staff-image" />
        <h3 class="staff-name">Frédéric Becq</h3>
        <p class="staff-role">Chef</p>
      </div>

      <div class="staff-member">
        <img src="/images/staff/jb.jpg" alt="Jean-Baptiste" class="staff-image" />
        <h3 class="staff-name">Jean-Baptiste</h3>
        <p class="staff-role">Second de cuisine</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import SeparatorComponent from './SeparatorComponent.vue';
</script>

<style scoped>
.staff-container {
  @apply flex flex-col items-center justify-center py-24 px-4 bg-[#090C0F];
}

.title {
  @apply text-4xl text-white mb-2 text-orange-500 ;
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

</style> 