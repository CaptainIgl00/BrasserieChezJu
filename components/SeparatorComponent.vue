<template>
    <div class="separator-container">

      <div v-if="showLeftLine" class="separator-line" :class="{ 'slim': slim }"></div>

      <div class="diamond-container" :class="{ 'slim': slim }">
        <div class="diamond-outer" :class="{ 'slim': slim }">
          <div class="diamond-inner" :class="{ 'slim': slim }"></div>
        </div>
      </div>
      <div class="separator-line" :class="{ 'slim': slim }"></div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SeparatorComponent',
    props: {
      showLeftLine: {
        type: Boolean,
        default: true
      },
      slim: {
        type: Boolean,
        default: false
      }
    }
  }
  </script>
  
  <style scoped>
  .separator-container {
    @apply my-8 flex items-center relative w-full gap-4;
  }
  
  .diamond-container {
    @apply relative w-10 h-10 flex items-center justify-center;
  }
  
  .diamond-container.slim {
    @apply w-6 h-6;
  }
  
  .diamond-outer {
    @apply w-8 h-8 border-2 border-orange-500 flex items-center justify-center;
    transform: rotate(45deg);
  }
  
  .diamond-outer.slim {
    @apply w-4 h-4 border border-orange-500/50;
  }
  
  .diamond-inner {
    @apply w-4 h-4 bg-orange-500;
  }

  .diamond-inner.slim {
    @apply w-2 h-2 bg-orange-500/50;
  }

  .separator-line {
    @apply h-1 bg-orange-500 flex-1 ml-[-1rem] mr-[-1rem];
  }

  .separator-line.slim {
    @apply h-px bg-orange-500/50;
  }

  .diamond-outer, .diamond-inner {
    @apply transition-all duration-300;
  }
  
  .separator-container:hover .diamond-outer {
    @apply transform rotate-90 scale-125;
  }
  
  .separator-container:hover .diamond-outer.slim {
    @apply border-orange-500;
  }
  
  .separator-container:hover .diamond-inner {
    @apply transform rotate-90 scale-125;
  }

  .separator-container:hover .diamond-inner.slim {
    @apply bg-orange-500;
  }

  .separator-container:hover .separator-line.slim {
    @apply bg-orange-500;
  }
  </style>