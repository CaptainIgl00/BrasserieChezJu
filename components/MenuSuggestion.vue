<template>
  <div v-if="suggestion" class="suggestion-container">
    <div class="suggestion-content" @click="selectFormula">
      <div class="time-badge">
        {{ suggestion.timeRange }}
      </div>
      <div class="suggestion-text">
        <h3 class="suggestion-title">{{ suggestion.title }}</h3>
        <p class="suggestion-description">{{ suggestion.description }}</p>
      </div>
      <div class="suggestion-price">
        {{ suggestion.price }}€
      </div>
      <div class="suggestion-action">
        <span class="action-text">Voir la formule</span>
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
        </svg>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const suggestion = ref(null)
const emit = defineEmits(['select-formula'])

const formulas = {
  breakfast: {
    id: 'petit-dej',
    timeRange: '7h - 11h',
    title: 'Formule Petit déj\'',
    description: '1 boisson chaude au choix + 1 jus de fruit + 1 viennoiserie',
    price: '6',
    available: {
      days: [2, 3, 4, 5], // Mardi à Vendredi
      startHour: 7,
      endHour: 11
    }
  },
  lunch: {
    id: 'dejeuner',
    timeRange: '12h - 14h30',
    title: 'Formule Déjeuner',
    description: 'Entrée + Plat ou Plat + Dessert',
    price: '19',
    available: {
      days: [1, 2, 3, 4, 5], // Lundi à Vendredi
      startHour: 12,
      endHour: 14.5
    }
  },
  routier: {
    id: 'routier',
    timeRange: '11h - 15h',
    title: 'Formule Routier',
    description: 'Entrée + Plat + Dessert + 1 boisson',
    price: '20',
    available: {
      days: [1, 2, 3, 4, 5], // Lundi à Vendredi
      startHour: 11,
      endHour: 15
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
.suggestion-container {
  @apply bg-black/40 rounded-xl p-1;
}

.suggestion-content {
  @apply flex items-center gap-6 p-4 rounded-lg cursor-pointer
         transition-all duration-300 hover:bg-orange-500/5;
}

.time-badge {
  @apply px-4 py-2 rounded-lg bg-orange-500/10 text-orange-500 font-medium text-sm
         border border-orange-500/20;
}

.suggestion-text {
  @apply flex-1;
}

.suggestion-title {
  @apply text-xl font-medium text-orange-500 mb-1;
}

.suggestion-description {
  @apply text-sm text-gray-400 italic;
}

.suggestion-price {
  @apply text-2xl font-bold text-orange-500;
}

.suggestion-action {
  @apply flex items-center gap-2 text-orange-500;
}

.action-text {
  @apply text-sm font-medium;
}

@media (max-width: 640px) {
  .suggestion-content {
    @apply flex-col text-center gap-4 p-6;
  }

  .suggestion-action {
    @apply justify-center;
  }
}
</style>
