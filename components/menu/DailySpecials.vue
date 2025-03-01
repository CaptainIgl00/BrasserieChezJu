<template>
  <div v-if="suggestion && !hideInFormulaTab" class="suggestion-wrapper">
    <div class="suggestion-container" @click="selectFormula">
      <div class="time-badge">
        {{ suggestion.timeRange }}
      </div>
      <div class="content">
        <h3 class="title">{{ suggestion.title }}</h3>
        <p class="description">{{ suggestion.description }}</p>
      </div>
      <div class="price">
        {{ suggestion.price }}€
      </div>
      <div class="action">
        <span>Voir la formule</span>
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
        </svg>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const props = defineProps({
  hideInFormulaTab: {
    type: Boolean,
    default: false
  }
})

const suggestion = ref(null)
const emit = defineEmits(['select-formula'])

const formulas = {
  breakfast: {
    id: 'petit-dej',
    timeRange: '5h - 10h',
    title: 'Formule Petit déj\'',
    description: '1 boisson chaude au choix + 1 jus de fruit + 1 viennoiserie',
    price: '6',
    available: {
      days: [2, 3, 4, 5], // Mardi à Vendredi
      startHour: 5,
      endHour: 10
    }
  },
  lunch: {
    id: 'dejeuner',
    timeRange: '12h - 14h',
    title: 'Formule Déjeuner',
    description: 'Entrée + Plat ou Plat + Dessert',
    price: '19',
    available: {
      days: [1, 2, 3, 4, 5], // Du lundi au vendredi
      startHour: 10,
      endHour: 14.5
    }
  },
  menuGourmand: {
    id: 'menu-gourmand',
    timeRange: '18h30 - 22h',
    title: 'Menu Gourmand',
    description: 'Entrée + Plat + Dessert',
    price: '41',
    available: {
      days: [1, 2, 3, 4, 5, 6], // Toute la semaine
      startHour: 14.5,
      endHour: 23
    }
  }
}

const getCurrentSuggestion = () => {
  const now = new Date()
  const currentDay = now.getDay()
  const currentHour = now.getHours() + now.getMinutes() / 60

  // Trouver la formule appropriée selon l'heure et le jour
  for (const [key, formula] of Object.entries(formulas)) {
    const { days, startHour, endHour } = formula.available
    if (days.includes(currentDay) && currentHour >= startHour && currentHour < endHour) {
      return formula
    }
  }

  return null
}

onMounted(() => {
  suggestion.value = getCurrentSuggestion()
  // Mettre à jour la suggestion toutes les minutes
  setInterval(() => {
    suggestion.value = getCurrentSuggestion()
  }, 60000)
})

const selectFormula = () => {
  if (suggestion.value) {
    emit('select-formula', suggestion.value.id)
  }
}
</script>

<style scoped>
.suggestion-wrapper {
  @apply bg-black/90 backdrop-blur-sm rounded-xl p-1 transition-all duration-300 hover:bg-black/95;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(234, 92, 11, 0.2);
}

.suggestion-container {
  @apply flex items-center gap-6 p-4 rounded-lg cursor-pointer;
}

.time-badge {
  @apply px-4 py-2 rounded-lg bg-black/90 text-orange-500 font-medium text-sm border border-orange-500/30 whitespace-nowrap;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}

.content {
  @apply flex-1 min-w-0;
}

.title {
  @apply text-xl font-medium text-orange-500 mb-1 truncate;
  font-family: 'Dancing Script', cursive;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
}

.description {
  @apply text-sm text-gray-500 italic truncate;
  font-family: 'Cormorant Garamond', serif;
}

.price {
  @apply text-2xl font-bold text-orange-500 whitespace-nowrap;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
}

.action {
  @apply flex items-center gap-2 text-orange-500 whitespace-nowrap transition-all duration-300;
}

.action span {
  @apply text-sm font-medium;
  font-family: 'Montserrat', sans-serif;
}

.suggestion-container:hover .action {
  @apply translate-x-1;
}

@media (max-width: 768px) {
  .suggestion-container {
    @apply flex-col text-center gap-4 p-6;
  }

  .content {
    @apply w-full;
  }

  .action {
    @apply w-full justify-center;
  }
  
  .suggestion-container:hover .action {
    @apply translate-x-0 translate-y-1;
  }
}
</style>
