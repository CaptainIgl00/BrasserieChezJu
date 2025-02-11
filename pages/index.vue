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
    <Title>Brasserie Chez Ju - Restaurant traditionnel à Carcassonne</Title>
    <Meta name="description" content="Bienvenue à la Brasserie Chez Ju, votre restaurant traditionnel à Carcassonne. Cuisine authentique, produits frais et locaux, ambiance chaleureuse." />
    <Meta property="og:title" content="Brasserie Chez Ju - Restaurant traditionnel à Carcassonne" />
    <Meta property="og:description" content="Bienvenue à la Brasserie Chez Ju, votre restaurant traditionnel à Carcassonne. Cuisine authentique et produits locaux." />
    <Meta property="og:image" content="https://brasseriechezju.com/images/display/plat_principal.jpg" />
    <DisplayComponent />
    <ShowcaseComponent />
    <HeroComponent />
    <StaffComponent />
    <InstagramFeedComponent />
    <ContactComponent />
  </div>
</template>