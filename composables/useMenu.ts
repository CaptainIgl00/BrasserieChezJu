import { ref, computed } from 'vue'

// Types pour les données du menu
interface Dish {
  id: string
  name: string
  description?: string
  price: number
  image?: string
  portion?: string
  category?: string
}

interface MenuCategory {
  id: string
  name: string
  description?: string
}

// État réactif pour stocker les données
const categories = ref<MenuCategory[]>([])
const dishes = ref<Dish[]>([])
const isLoading = ref(false)
const error = ref<string | null>(null)

// URL de l'API backend
const apiBaseUrl = process.env.NODE_ENV === 'production' 
  ? '/api/v1' 
  : 'http://localhost:8000/api/v1'

// Fonction pour normaliser les URLs d'images
const normalizeImageUrl = (imageUrl: string | undefined): string | undefined => {
  if (!imageUrl) return undefined
  
  // Si l'URL est déjà relative, la retourner telle quelle
  if (imageUrl.startsWith('/api/')) return imageUrl
  
  // Si nous sommes en développement et que l'URL contient localhost:8000, la convertir en URL relative
  if (process.env.NODE_ENV !== 'production' && imageUrl.includes('localhost:8000')) {
    return imageUrl.replace('http://localhost:8000', '')
  }
  
  return imageUrl
}

export function useMenu() {
  // Fonction pour récupérer les catégories de menu
  const fetchCategories = async () => {
    if (categories.value.length > 0) return // Éviter de recharger si déjà chargé
    
    isLoading.value = true
    error.value = null
    
    try {
      const response = await fetch(`${apiBaseUrl}/menu/categories`)
      if (!response.ok) {
        throw new Error(`Erreur lors de la récupération des catégories: ${response.status}`)
      }
      
      const data = await response.json()
      categories.value = data
    } catch (err) {
      console.error('Erreur lors du chargement des catégories:', err)
      error.value = err instanceof Error ? err.message : 'Erreur inconnue'
    } finally {
      isLoading.value = false
    }
  }
  
  // Fonction pour récupérer tous les plats
  const fetchDishes = async () => {
    if (dishes.value.length > 0) return // Éviter de recharger si déjà chargé
    
    isLoading.value = true
    error.value = null
    
    try {
      const response = await fetch(`${apiBaseUrl}/menu/dishes`)
      if (!response.ok) {
        throw new Error(`Erreur lors de la récupération des plats: ${response.status}`)
      }
      
      const data = await response.json()
      // Normaliser les URLs d'images
      dishes.value = data.map((dish: Dish) => ({
        ...dish,
        image: normalizeImageUrl(dish.image)
      }))
    } catch (err) {
      console.error('Erreur lors du chargement des plats:', err)
      error.value = err instanceof Error ? err.message : 'Erreur inconnue'
    } finally {
      isLoading.value = false
    }
  }
  
  // Fonction pour récupérer les plats par catégorie
  const fetchDishesByCategory = async (categoryName: string) => {
    isLoading.value = true
    error.value = null
    
    try {
      const response = await fetch(`${apiBaseUrl}/menu/dishes/category/${encodeURIComponent(categoryName)}`)
      if (!response.ok) {
        throw new Error(`Erreur lors de la récupération des plats par catégorie: ${response.status}`)
      }
      
      const data = await response.json()
      // Normaliser les URLs d'images
      return data.map((dish: Dish) => ({
        ...dish,
        image: normalizeImageUrl(dish.image)
      }))
    } catch (err) {
      console.error(`Erreur lors du chargement des plats pour la catégorie ${categoryName}:`, err)
      error.value = err instanceof Error ? err.message : 'Erreur inconnue'
      return []
    } finally {
      isLoading.value = false
    }
  }
  
  // Computed pour obtenir les plats par catégorie
  const getDishesByCategory = computed(() => {
    return (categoryName: string) => {
      return dishes.value.filter(dish => dish.category === categoryName)
    }
  })
  
  // Fonction pour charger toutes les données du menu
  const loadMenuData = async () => {
    await Promise.all([fetchCategories(), fetchDishes()])
  }
  
  return {
    categories,
    dishes,
    isLoading,
    error,
    fetchCategories,
    fetchDishes,
    fetchDishesByCategory,
    getDishesByCategory,
    loadMenuData
  }
} 