<template>
  <div class="template-component">
    <!-- Section de chargement -->
    <div v-if="isLoading" class="loading-container">
      <div class="loading-spinner"></div>
      <p class="loading-text">Chargement en cours...</p>
    </div>
    
    <!-- Section d'erreur -->
    <div v-else-if="error" class="error-container">
      <p class="error-message">{{ error }}</p>
      <button @click="fetchItems" class="retry-button">
        Réessayer
      </button>
    </div>
    
    <!-- Section vide -->
    <div v-else-if="!hasItems" class="empty-container">
      <p class="empty-message">Aucun élément à afficher</p>
    </div>
    
    <!-- Section principale avec les données -->
    <div v-else class="items-grid">
      <div v-for="item in items" :key="item.id" class="item-card">
        <h3 class="item-title">{{ item.name }}</h3>
        <p v-if="item.description" class="item-description">{{ item.description }}</p>
        
        <!-- Boutons d'action -->
        <div class="item-actions">
          <button @click="editItem(item)" class="action-button edit-button">
            Modifier
          </button>
          <button @click="confirmDelete(item)" class="action-button delete-button">
            Supprimer
          </button>
        </div>
      </div>
    </div>
    
    <!-- Bouton d'ajout -->
    <div class="add-button-container">
      <button @click="showAddForm = true" class="add-button">
        Ajouter un élément
      </button>
    </div>
    
    <!-- Modal de formulaire d'ajout -->
    <div v-if="showAddForm" class="modal-overlay" @click.self="showAddForm = false">
      <div class="modal-container">
        <h2 class="modal-title">Ajouter un élément</h2>
        
        <form @submit.prevent="addItem" class="item-form">
          <div class="form-group">
            <label for="name" class="form-label">Nom</label>
            <input 
              id="name" 
              v-model="newItem.name" 
              type="text" 
              class="form-input"
              required
            />
          </div>
          
          <div class="form-group">
            <label for="description" class="form-label">Description</label>
            <textarea 
              id="description" 
              v-model="newItem.description" 
              class="form-textarea"
            ></textarea>
          </div>
          
          <div class="form-actions">
            <button type="button" @click="showAddForm = false" class="cancel-button">
              Annuler
            </button>
            <button type="submit" class="submit-button">
              Ajouter
            </button>
          </div>
        </form>
      </div>
    </div>
    
    <!-- Modal de formulaire d'édition -->
    <div v-if="showEditForm" class="modal-overlay" @click.self="showEditForm = false">
      <div class="modal-container">
        <h2 class="modal-title">Modifier un élément</h2>
        
        <form @submit.prevent="updateItem" class="item-form">
          <div class="form-group">
            <label for="edit-name" class="form-label">Nom</label>
            <input 
              id="edit-name" 
              v-model="editingItem.name" 
              type="text" 
              class="form-input"
              required
            />
          </div>
          
          <div class="form-group">
            <label for="edit-description" class="form-label">Description</label>
            <textarea 
              id="edit-description" 
              v-model="editingItem.description" 
              class="form-textarea"
            ></textarea>
          </div>
          
          <div class="form-actions">
            <button type="button" @click="showEditForm = false" class="cancel-button">
              Annuler
            </button>
            <button type="submit" class="submit-button">
              Mettre à jour
            </button>
          </div>
        </form>
      </div>
    </div>
    
    <!-- Modal de confirmation de suppression -->
    <div v-if="showDeleteConfirm" class="modal-overlay" @click.self="showDeleteConfirm = false">
      <div class="modal-container">
        <h2 class="modal-title">Confirmer la suppression</h2>
        
        <p class="confirm-message">
          Êtes-vous sûr de vouloir supprimer l'élément "{{ deletingItem?.name }}" ?
          Cette action est irréversible.
        </p>
        
        <div class="form-actions">
          <button @click="showDeleteConfirm = false" class="cancel-button">
            Annuler
          </button>
          <button @click="deleteItem" class="delete-button">
            Supprimer
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useTemplate } from '~/composables/useTemplate'

// Récupérer les fonctions et propriétés du composable
const { 
  items, 
  isLoading, 
  error, 
  hasItems,
  fetchItems, 
  fetchItemById, 
  createItem, 
  updateItem: updateItemApi, 
  deleteItem: deleteItemApi 
} = useTemplate()

// État local pour les formulaires
const showAddForm = ref(false)
const showEditForm = ref(false)
const showDeleteConfirm = ref(false)
const newItem = ref({ name: '', description: '' })
const editingItem = ref({ id: '', name: '', description: '' })
const deletingItem = ref(null)

// Charger les données au montage du composant
onMounted(() => {
  fetchItems()
})

// Méthodes pour gérer les actions utilisateur
const editItem = (item) => {
  editingItem.value = { ...item }
  showEditForm.value = true
}

const confirmDelete = (item) => {
  deletingItem.value = item
  showDeleteConfirm.value = true
}

const addItem = async () => {
  try {
    await createItem(newItem.value)
    showAddForm.value = false
    newItem.value = { name: '', description: '' }
  } catch (err) {
    console.error('Erreur lors de l\'ajout:', err)
  }
}

const updateItem = async () => {
  try {
    await updateItemApi(editingItem.value.id, {
      name: editingItem.value.name,
      description: editingItem.value.description
    })
    showEditForm.value = false
  } catch (err) {
    console.error('Erreur lors de la mise à jour:', err)
  }
}

const deleteItem = async () => {
  if (!deletingItem.value) return
  
  try {
    await deleteItemApi(deletingItem.value.id)
    showDeleteConfirm.value = false
    deletingItem.value = null
  } catch (err) {
    console.error('Erreur lors de la suppression:', err)
  }
}
</script>

<style scoped>
.template-component {
  @apply w-full max-w-4xl mx-auto py-8 px-4;
}

/* Conteneurs d'état */
.loading-container,
.error-container,
.empty-container {
  @apply flex flex-col items-center justify-center py-12 text-center;
}

.loading-spinner {
  @apply w-12 h-12 border-4 border-orange-500/30 border-t-orange-500 rounded-full;
  animation: spin 1s linear infinite;
}

.loading-text {
  @apply mt-4 text-orange-500 text-lg italic;
}

.error-message {
  @apply text-red-500 mb-4;
}

.retry-button {
  @apply px-4 py-2 bg-orange-500 text-white rounded-md hover:bg-orange-600 transition-colors;
}

.empty-message {
  @apply text-gray-400 italic;
}

/* Grille d'items */
.items-grid {
  @apply grid grid-cols-1 md:grid-cols-2 gap-6;
}

.item-card {
  @apply bg-black/50 backdrop-blur-sm border border-orange-500/20 rounded-lg p-6 transition-all duration-300 hover:border-orange-500/50;
}

.item-title {
  @apply text-xl font-bold text-orange-500 mb-2;
}

.item-description {
  @apply text-gray-300 mb-4;
}

.item-actions {
  @apply flex justify-end gap-2 mt-4;
}

.action-button {
  @apply px-3 py-1 rounded-md text-sm transition-colors;
}

.edit-button {
  @apply bg-blue-500/20 text-blue-400 border border-blue-500/30 hover:bg-blue-500/30;
}

.delete-button {
  @apply bg-red-500/20 text-red-400 border border-red-500/30 hover:bg-red-500/30;
}

/* Bouton d'ajout */
.add-button-container {
  @apply flex justify-center mt-8;
}

.add-button {
  @apply px-6 py-3 bg-orange-500 text-white rounded-md hover:bg-orange-600 transition-colors;
}

/* Modals */
.modal-overlay {
  @apply fixed inset-0 bg-black/80 backdrop-blur-sm flex items-center justify-center z-50;
}

.modal-container {
  @apply bg-gray-900 border border-orange-500/30 rounded-lg p-6 w-full max-w-md;
}

.modal-title {
  @apply text-xl font-bold text-orange-500 mb-4 pb-2 border-b border-orange-500/20;
}

.confirm-message {
  @apply text-gray-300 mb-6;
}

/* Formulaire */
.item-form {
  @apply space-y-4;
}

.form-group {
  @apply flex flex-col;
}

.form-label {
  @apply text-gray-300 mb-1;
}

.form-input,
.form-textarea {
  @apply bg-black/50 border border-gray-700 rounded-md px-3 py-2 text-white focus:border-orange-500 focus:outline-none;
}

.form-textarea {
  @apply h-24 resize-none;
}

.form-actions {
  @apply flex justify-end gap-3 mt-6;
}

.cancel-button {
  @apply px-4 py-2 bg-gray-800 text-gray-300 rounded-md hover:bg-gray-700 transition-colors;
}

.submit-button {
  @apply px-4 py-2 bg-orange-500 text-white rounded-md hover:bg-orange-600 transition-colors;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Responsive */
@media (max-width: 640px) {
  .items-grid {
    @apply grid-cols-1;
  }
  
  .modal-container {
    @apply mx-4;
  }
}
</style> 