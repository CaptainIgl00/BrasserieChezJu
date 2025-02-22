<template>
  <div class="p-6 border-2 border-orange-500 rounded-xl relative overflow-hidden h-full transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_6px_15px_rgba(249,115,22,0.3)]" style="background: rgba(249, 115, 22, 0.05);">
    <div class="mb-4">
      <h2 class="text-2xl font-bold text-orange-500 mb-2 font-playfair">{{ title }}</h2>
      <p v-if="subtitle" class="text-gray-400 italic text-sm mb-3">{{ subtitle }}</p>
    </div>

    <div class="flex flex-col h-full">
      <p class="text-gray-300 text-base leading-relaxed mb-4">{{ formule }}</p>
      <p class="text-gray-300 text-base leading-relaxed mb-4">{{ description }}</p>
      <p class="text-xl font-bold text-orange-500 mt-auto inline-block px-3 py-1 rounded-lg" style="background: rgba(249, 115, 22, 0.1);">{{ price }} €</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: String,
  subtitle: {
    type: String,
    default: null,
  },
  formule: String,
  description: String,
  price: String,
})
</script>
  