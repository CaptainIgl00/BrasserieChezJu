/**
 * Template de composable pour interagir avec le backend.
 * Ce composable peut être utilisé comme base pour créer de nouveaux composables.
 * 
 * Utilisation:
 * 1. Copiez ce fichier et renommez-le selon votre besoin (ex: useEvents.ts)
 * 2. Modifiez les interfaces et les fonctions selon vos besoins
 * 3. Importez le composable dans vos composants Vue
 */

import { ref, computed } from 'vue'

// Types pour les données
interface TemplateItem {
  id: string
  name: string
  description?: string
  // Ajoutez d'autres propriétés selon vos besoins
}

// État réactif
const items = ref<TemplateItem[]>([])
const isLoading = ref(false)
const error = ref<string | null>(null)

// URL de l'API backend
const apiBaseUrl = process.env.NODE_ENV === 'production' 
  ? '/api/v1' 
  : 'http://localhost:8000/api/v1'

// Endpoint API
const API_ENDPOINT = 'template-items'

/**
 * Composable pour gérer les données template
 */
export function useTemplate() {
  /**
   * Récupère tous les items
   */
  const fetchItems = async () => {
    // Éviter de recharger si déjà chargé
    if (items.value.length > 0) return
    
    isLoading.value = true
    error.value = null
    
    try {
      const response = await fetch(`${apiBaseUrl}/${API_ENDPOINT}`)
      
      if (!response.ok) {
        throw new Error(`Erreur HTTP: ${response.status}`)
      }
      
      const data = await response.json()
      items.value = data.items || data // Adapter selon la structure de réponse de votre API
    } catch (err) {
      console.error('Erreur lors de la récupération des données:', err)
      error.value = err instanceof Error ? err.message : 'Erreur inconnue'
    } finally {
      isLoading.value = false
    }
  }

  /**
   * Récupère un item par son ID
   */
  const fetchItemById = async (id: string) => {
    isLoading.value = true
    error.value = null
    
    try {
      const response = await fetch(`${apiBaseUrl}/${API_ENDPOINT}/${id}`)
      
      if (!response.ok) {
        throw new Error(`Erreur HTTP: ${response.status}`)
      }
      
      const data = await response.json()
      // Mettre à jour l'item dans la liste si déjà chargé
      const index = items.value.findIndex(item => item.id === id)
      if (index !== -1) {
        items.value[index] = data
      } else {
        items.value.push(data)
      }
      
      return data
    } catch (err) {
      console.error(`Erreur lors de la récupération de l'item ${id}:`, err)
      error.value = err instanceof Error ? err.message : 'Erreur inconnue'
      return null
    } finally {
      isLoading.value = false
    }
  }

  /**
   * Crée un nouvel item
   */
  const createItem = async (item: Omit<TemplateItem, 'id'>) => {
    isLoading.value = true
    error.value = null
    
    try {
      const response = await fetch(`${apiBaseUrl}/${API_ENDPOINT}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(item)
      })
      
      if (!response.ok) {
        throw new Error(`Erreur HTTP: ${response.status}`)
      }
      
      const data = await response.json()
      items.value.push(data)
      return data
    } catch (err) {
      console.error('Erreur lors de la création de l\'item:', err)
      error.value = err instanceof Error ? err.message : 'Erreur inconnue'
      return null
    } finally {
      isLoading.value = false
    }
  }

  /**
   * Met à jour un item existant
   */
  const updateItem = async (id: string, item: Partial<TemplateItem>) => {
    isLoading.value = true
    error.value = null
    
    try {
      const response = await fetch(`${apiBaseUrl}/${API_ENDPOINT}/${id}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(item)
      })
      
      if (!response.ok) {
        throw new Error(`Erreur HTTP: ${response.status}`)
      }
      
      const data = await response.json()
      
      // Mettre à jour l'item dans la liste
      const index = items.value.findIndex(item => item.id === id)
      if (index !== -1) {
        items.value[index] = { ...items.value[index], ...data }
      }
      
      return data
    } catch (err) {
      console.error(`Erreur lors de la mise à jour de l'item ${id}:`, err)
      error.value = err instanceof Error ? err.message : 'Erreur inconnue'
      return null
    } finally {
      isLoading.value = false
    }
  }

  /**
   * Supprime un item
   */
  const deleteItem = async (id: string) => {
    isLoading.value = true
    error.value = null
    
    try {
      const response = await fetch(`${apiBaseUrl}/${API_ENDPOINT}/${id}`, {
        method: 'DELETE'
      })
      
      if (!response.ok) {
        throw new Error(`Erreur HTTP: ${response.status}`)
      }
      
      // Supprimer l'item de la liste
      items.value = items.value.filter(item => item.id !== id)
      return true
    } catch (err) {
      console.error(`Erreur lors de la suppression de l'item ${id}:`, err)
      error.value = err instanceof Error ? err.message : 'Erreur inconnue'
      return false
    } finally {
      isLoading.value = false
    }
  }

  /**
   * Réinitialise l'état
   */
  const resetState = () => {
    items.value = []
    isLoading.value = false
    error.value = null
  }

  // Computed properties
  const hasItems = computed(() => items.value.length > 0)
  const itemCount = computed(() => items.value.length)

  // Exposer les fonctions et propriétés
  return {
    // État
    items,
    isLoading,
    error,
    
    // Computed
    hasItems,
    itemCount,
    
    // Actions
    fetchItems,
    fetchItemById,
    createItem,
    updateItem,
    deleteItem,
    resetState
  }
} 