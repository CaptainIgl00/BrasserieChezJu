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
const API_ENDPOINT = 'wines'

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
      
      // Simuler des données pour le développement si l'API n'est pas disponible
      if (process.env.NODE_ENV === 'development') {
        console.log('Mode développement: simulation de données')
        
        // Attendre un peu pour simuler une requête réseau
        await new Promise(resolve => setTimeout(resolve, 1000))
        
        // Données simulées
        const mockWines: Wine[] = [
          {
            id: '1',
            name: 'Cuvée Archibald',
            domain: 'Domaine La Sapinière',
            region: 'AOP Malepère',
            description: 'Cabernet Franc et Merlot aux arômes de fruits mûrs, vanille et menthol. Bouche concentrée, tanins soyeux, finale cacao.',
            bottlePrice: 29,
            category: 'Rouge'
          },
          {
            id: '2',
            name: 'Le rouge de L\'Azérolle',
            domain: 'Raymond Julien - Domaine Mirausse',
            region: 'AOP Minervois',
            description: 'Cinsault, Grenache et Syrah aux notes de violette et cassis. Frais, fruité et souple en bouche.',
            glassPrice: 4,
            bottlePrice: 19,
            category: 'Rouge'
          },
          {
            id: '3',
            name: 'Uby n°4',
            domain: 'Domaine Uby',
            region: 'IGP Côtes de Gascogne',
            description: 'Blanc moelleux issu de Gros et Petit Manseng. Nez exotique, bouche veloutée et crémeuse, finale sur le coing et le citron confit.',
            glassPrice: 4,
            bottlePrice: 20,
            category: 'Blanc'
          },
          {
            id: '4',
            name: 'Tom et Lilly',
            domain: 'Raymond Julien – Domaine Mirausse',
            region: 'AOP Minervois',
            description: 'Rosé frais et fruité à base de Grenache et Cinsault. Léger, équilibré et rafraîchissant, parfait pour les journées ensoleillées.',
            glassPrice: 3.5,
            bottlePrice: 18,
            category: 'Rosé'
          },
          {
            id: '5',
            name: 'Première Bulles',
            domain: 'Sieur d\'Arques',
            region: 'AOC Limoux',
            description: 'Élaboré selon la méthode traditionnelle, cet assemblage de Chardonnay, Chenin et Mauzac offre des bulles fines, une bouche onctueuse et une finale toastée.',
            glassPrice: 5,
            bottlePrice: 26,
            category: 'Champagne'
          }
        ]
        
        wines.value = mockWines
        console.log('Données simulées chargées:', wines.value)
        isLoading.value = false
        return
      }
      
      // Appel API réel
      const response = await fetch(url)
      
      if (!response.ok) {
        throw new Error(`Erreur HTTP: ${response.status}`)
      }
      
      const data = await response.json()
      console.log('Données reçues de l\'API:', data)
      
      wines.value = data
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
      const response = await fetch(`${apiBaseUrl}/${API_ENDPOINT}/${id}`)
      
      if (!response.ok) {
        throw new Error(`Erreur HTTP: ${response.status}`)
      }
      
      const data = await response.json()
      
      // Mettre à jour le vin dans la liste si déjà chargé
      const index = wines.value.findIndex(wine => wine.id === id)
      if (index !== -1) {
        wines.value[index] = data
      } else {
        wines.value.push(data)
      }
      
      return data
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
    resetState
  }
} 