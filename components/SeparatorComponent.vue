<template>
    <div class="separator-container">

      <div v-if="showLeftLine" class="separator-line"></div>

      <div class="diamond-container">
        <div class="diamond-outer">
          <div class="diamond-inner"></div>
        </div>
      </div>
      <div class="separator-line"></div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SeparatorComponent',
    props: {
      showLeftLine: {
        type: Boolean,
        default: true
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
  
  .diamond-outer {
    @apply w-8 h-8 border-2 border-orange-500 flex items-center justify-center;
    transform: rotate(45deg);
  }
  
  .diamond-inner {
    @apply w-4 h-4 bg-orange-500;
  }
  .separator-line {
    @apply h-1 bg-orange-500 flex-1 ml-[-1rem] mr-[-1rem];
  }

  .diamond-outer, .diamond-inner {
    @apply transition-all duration-300;
  }
  
  .separator-container:hover .diamond-outer {
    @apply transform rotate-90 scale-125;
  }
  
  .separator-container:hover .diamond-inner {
    @apply transform rotate-90 scale-125;
  }
  </style>