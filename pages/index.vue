<script setup lang="ts">
const route = useRoute()

// Lazy load components that are not immediately visible
const ShowcaseComponent = defineAsyncComponent(() => import('../components/ShowcaseComponent.vue'))
const StaffComponent = defineAsyncComponent(() => import('../components/StaffComponent.vue'))
const InstagramFeedComponent = defineAsyncComponent(() => import('../components/InstagramFeedComponent.vue'))
const ContactComponent = defineAsyncComponent(() => import('../components/ContactComponent.vue'))
</script>

<template>
  <div class="home-page">
    <DisplayComponent />
    <ShowcaseComponent />
    <HeroComponent />
    <StaffComponent />
    <InstagramFeedComponent />
    <ContactComponent />
  </div>
</template>