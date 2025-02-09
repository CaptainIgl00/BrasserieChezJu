<template>
  <div>
    <NavbarComponent />
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<style>
/* Scrollbar personnalisée pour les navigateurs Webkit (Chrome, Safari, etc.) */
::-webkit-scrollbar {
  width: 10px;
}

::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.9);
}

::-webkit-scrollbar-thumb {
  background: rgb(249, 115, 22);
  border-radius: 5px;
}

::-webkit-scrollbar-thumb:hover {
  background: rgb(251, 146, 60);
}

/* Scrollbar personnalisée pour Firefox */
* {
  scrollbar-width: thin;
  scrollbar-color: rgb(249, 115, 22) rgba(0, 0, 0, 0.9);
}
</style>