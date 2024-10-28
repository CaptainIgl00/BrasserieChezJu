<template>
  <div class="footer-content">
    <div class="contact-info">
      <h3 class="title">Contacts</h3>
      <div class="contact-item">
        <span class="icon-location">&#x1F4CD;</span>
        <p>42-54 Route de Limoux, 11000 Carcassonne</p>
      </div>
      <div class="contact-item">
        <span class="icon-phone">&#x1F4DE;</span>
        <p>04 30 34 41 90</p>
      </div>
      <div class="contact-item">
        <span class="icon-email">&#x2709;&#xFE0F;</span>
        <p>brasseriechezju@gmail.com</p>
      </div>
    </div>
    
    <div class="logo">
      <div class="logo-wrapper">
        <div class="logo-border">
          <span class="logo-text">Chez Ju</span>
        </div>
      </div>
      <p>BRASSERIE - BAR - TAPAS</p>
      <div class="social-icons">
        <a href="#" class="icon-facebook">
          <span>&#x1F4F7;</span>
        </a>
        <a href="#" class="icon-instagram">
          <span>&#x1F4F7;</span>
        </a>
      </div>
    </div>

    <div class="hours-info">
      <h3 class="title">Horaires</h3>
      <p>
        <span class="font-bold">Lun.</span> 8h00 – 22h30
      </p>
      <p>
        <span class="font-bold">Mar. – Sam.</span> 5h00 – 14h30 | 18h30 – 22h30
      </p>
      <p>Fermeture Mercredi à 22h30, Ouverture samedi à 09h00</p>
      <p>
        <span class="font-bold">Dim.</span> 10h00 – 15h00
      </p>
      <h3 class="title">Petit-déjeuner</h3>
      <p>
        <span class="font-bold">Lun. – Sam.</span> 05h00 – 11h30
      </p>
    </div>
  </div>
</template>

<style scoped>
.footer-content {
  @apply flex justify-between items-center bg-gray-900 p-16;
}

.contact-info, .hours-info {
  @apply text-white;
}

.title {
  @apply text-lg mb-6;
}

.contact-item {
  @apply flex items-center mb-4;
}

.icon-location, .icon-phone, .icon-email {
  @apply text-orange-500 mr-4;
}

.logo {
  @apply text-white flex flex-col items-center;
}

.logo-wrapper {
  @apply mb-4 relative;
}

.logo-border {
  @apply border-orange-500 rounded-full p-6 border-4;
}

.logo-text {
  @apply text-4xl;
}

.social-icons {
  @apply flex gap-4 mt-4;
}

.icon-facebook, .icon-instagram {
  @apply text-white border rounded-full p-2 border-white;
}

.hours-info p {
  @apply mb-2;
}

.font-bold {
  font-weight: bold;
  color: #EA5C0B;
}
</style>
