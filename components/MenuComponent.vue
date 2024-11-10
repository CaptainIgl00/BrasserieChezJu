<template>
  <div class="py-6 px-8 border border-orange-400 rounded-lg bg-black text-white shadow-lg">
    <div class="mb-4">
      <h1 class="text-2xl font-bold text-orange-500">Avec Riz et Légumes de Saison</h1>
    </div>
    <div>
      <h2 class="text-xl text-orange-500 mb-4">Poissons</h2>
      <div class="menu-list">
        <div 
          v-for="(dish, index) in dishes" 
          :key="index" 
          class="menu-item flex justify-between items-center border-b border-orange-400 py-2"
        >
          <div>
            <span class="uppercase font-medium">{{ dish.name }}</span>
            <span v-if="dish.description" class="block text-gray-300 text-sm mt-1">{{ dish.description }}</span>
          </div>
          <span class="text-orange-500 text-lg">{{ dish.price }} €</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MenuComponent',
  data() {
    return {
      dishes: [
        { name: "Queue de Lofe à l'Armoricain", price: 28 },
        { name: "Seiche Entière 500 G", price: 25 },
        { name: "Bar Planché à l'Huile d'Olive", price: 26, description: "& tapenade" },
      ],
    };
  },
};
</script>

<style scoped>
.border-orange-400 {
  border-color: #F1A67B;
}

.bg-black {
  background-color: #000;
}

.text-orange-500 {
  color: #F1A67B;
}

.menu-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.menu-item:last-child {
  border-bottom: none;
}
</style>
  