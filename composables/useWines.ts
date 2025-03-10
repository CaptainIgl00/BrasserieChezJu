/**
 * Composable pour interagir avec l'API des vins.
 * Ce composable permet de récupérer, filtrer et trier les vins.
 */

import { ref, computed } from 'vue'

// Types pour les données des vins
export interface Wine {
  id: string
  name: string
  description?: string
  category: string // Rouge, Blanc, Rosé, Champagne
  region?: string
  domain?: string
  year?: number
  glassPrice?: number
  bottlePrice: number
  type?: string
}

// État réactif
const wines = ref<Wine[]>([])
const isLoading = ref(false)
const error = ref<string | null>(null)

// URL de l'API backend
const apiBaseUrl = process.env.NODE_ENV === 'production' 
  ? '/api/v1' 
  : 'http://localhost:8000/api/v1'

// Endpoint API
const API_ENDPOINT = 'menu/wines'

/**
 * Composable pour gérer les données des vins
 */
export function useWines() {
  /**
   * Récupère tous les vins
   * @param category Catégorie de vin (optionnel)
   * @param sort Tri (optionnel)
   */
  const fetchWines = async (category?: string, sort?: string) => {
    isLoading.value = true
    error.value = null
    
    try {
      let url = `${apiBaseUrl}/${API_ENDPOINT}`
      const params = new URLSearchParams()
      
      if (category) {
        params.append('category', category)
      }
      
      if (sort) {
        params.append('sort', sort)
      }
      
      const queryString = params.toString()
      if (queryString) {
        url += `?${queryString}`
      }
      
      console.log('Fetching wines from:', url)
      
      // Appel API réel
      const response = await fetch(url)
      
      if (!response.ok) {
        throw new Error(`Erreur HTTP: ${response.status}`)
      }
      
      const data = await response.json()
      console.log('Données reçues de l\'API:', data)
      
      // Transformer les données pour correspondre à notre structure
      const allWines: Wine[] = []
      
      // Parcourir chaque catégorie et ajouter les vins à notre tableau
      data.forEach((categoryData: { name: string, wines: any[] }) => {
        const categoryName = categoryData.name
        
        // Transformer chaque vin pour correspondre à notre interface Wine
        const categoryWines = categoryData.wines.map(wine => ({
          id: wine.id,
          name: wine.name,
          description: wine.description,
          category: categoryName,
          region: wine.region,
          domain: wine.domain,
          year: wine.year,
          glassPrice: undefined, // L'API ne semble pas fournir de prix au verre
          bottlePrice: parseFloat(wine.price),
          type: wine.type
        }))
        
        // Ajouter les vins de cette catégorie à notre tableau
        allWines.push(...categoryWines)
      })
      
      wines.value = allWines
    } catch (err) {
      console.error('Erreur lors de la récupération des vins:', err)
      error.value = err instanceof Error ? err.message : 'Erreur inconnue'
    } finally {
      isLoading.value = false
    }
  }

  /**
   * Récupère un vin par son ID
   */
  const fetchWineById = async (id: string) => {
    isLoading.value = true
    error.value = null
    
    try {
      // Vérifier si le vin est déjà dans notre liste
      const existingWine = wines.value.find(wine => wine.id === id)
      if (existingWine) {
        return existingWine
      }
      
      // Si nous n'avons pas encore chargé les vins, charger tous les vins
      if (wines.value.length === 0) {
        await fetchWines()
        const wine = wines.value.find(wine => wine.id === id)
        if (wine) {
          return wine
        }
      }
      
      // Si nous n'avons toujours pas trouvé le vin, c'est qu'il n'existe pas
      throw new Error(`Vin avec l'ID ${id} non trouvé`)
    } catch (err) {
      console.error(`Erreur lors de la récupération du vin ${id}:`, err)
      error.value = err instanceof Error ? err.message : 'Erreur inconnue'
      return null
    } finally {
      isLoading.value = false
    }
  }

  /**
   * Réinitialise l'état
   */
  const resetState = () => {
    wines.value = []
    isLoading.value = false
    error.value = null
  }

  /**
   * Charge toutes les données des vins
   */
  const loadWineData = async (category?: string, sort?: string) => {
    await fetchWines(category, sort)
  }

  // Computed properties
  const hasWines = computed(() => wines.value.length > 0)
  const wineCount = computed(() => wines.value.length)
  
  // Filtres par catégorie
  const redWines = computed(() => wines.value.filter(wine => wine.category.toLowerCase() === 'rouge'))
  const whiteWines = computed(() => wines.value.filter(wine => wine.category.toLowerCase() === 'blanc'))
  const roseWines = computed(() => wines.value.filter(wine => wine.category.toLowerCase() === 'rosé'))
  const champagnes = computed(() => wines.value.filter(wine => wine.category.toLowerCase() === 'champagne'))

  // Exposer les fonctions et propriétés
  return {
    // État
    wines,
    isLoading,
    error,
    
    // Computed
    hasWines,
    wineCount,
    redWines,
    whiteWines,
    roseWines,
    champagnes,
    
    // Actions
    fetchWines,
    fetchWineById,
    resetState,
    loadWineData
  }
} 