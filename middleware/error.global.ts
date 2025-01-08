export default defineNuxtRouteMiddleware((to, from) => {
  // Liste des extensions de fichiers à bloquer
  const blockedExtensions = ['.php', '.html', '.asp', '.aspx']
  
  // Liste des chemins à bloquer
  const blockedPaths = [
    '/vendor',
    '/wp-',
    '/wordpress',
    '/wp-admin',
    '/admin',
    '/systembc',
    '/geoip',
    '/cdn.js'
  ]

  // Vérifier si le chemin contient une extension bloquée
  if (blockedExtensions.some(ext => to.path.toLowerCase().endsWith(ext))) {
    return navigateTo('/')
  }

  // Vérifier si le chemin commence par un préfixe bloqué
  if (blockedPaths.some(path => to.path.toLowerCase().startsWith(path))) {
    return navigateTo('/')
  }

  // Si la route n'existe pas, rediriger vers la page d'accueil
  if (!to.matched.length) {
    return navigateTo('/')
  }
}) 