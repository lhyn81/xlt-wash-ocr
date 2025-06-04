<template>
  <div class="task-detail-page">
    <h1>{{ taskID }}</h1>
    <div class="carrage-buttons-container">
      <button v-for="detail in taskData.details" :key="detail['carrage-id']" @click="selectCarrage(detail)" class="carrage-button">
        {{ detail['carrage-id'] }}
      </button>
    </div>
    <div class="image-display">
      <img :src="currentImageA" alt="Image A" @click="showImageModal(currentImageA)" class="displayed-image" />
      <img :src="currentImageB" alt="Image B" @click="showImageModal(currentImageB)" class="displayed-image" />
    </div>
    <div class="score-display">
      <textarea :value="currentScore" rows="3" class="score-textarea" readonly></textarea>
    </div>

    <!-- Image Modal -->
    <div v-if="showModal" class="modal" @click.self="closeImageModal"> <!-- .self ensures click on backdrop closes modal -->
      <span class="close" @click="closeImageModal">&times;</span>
      <img class="modal-content" :src="modalImageSrc">
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const taskID = ref(route.params.taskid);
const taskData = ref({ details: [] });
const currentImageA = ref('');
const currentImageB = ref('');
const currentScore = ref('');
const showModal = ref(false);
const modalImageSrc = ref('');

onMounted(async () => {
  try {
    const response = await fetch(\`http://localhost:5000/\${taskID.value}\`);
    if (!response.ok) {
      throw new Error(\`HTTP error! status: \${response.status}\`);
    }
    const data = await response.json();
    taskData.value = data;
    if (data.details && data.details.length > 0) {
      selectCarrage(data.details[0]);
    }
  } catch (error) {
    console.error("Failed to fetch task details:", error);
    taskData.value = { details: [{ "carrage-id": "Error", image: ["",""], score: ["Failed to load data"] }] };
    selectCarrage(taskData.value.details[0]);
  }
});

function selectCarrage(detail) {
  // Using a placeholder image if actual images are not found or path is incorrect.
  // The public/images directory should contain these images.
  // The path should be relative to the public directory.
  currentImageA.value = detail.image && detail.image[0] ? \`/images/\${detail.image[0]}\` : '/images/placeholder.jpg';
  currentImageB.value = detail.image && detail.image[1] ? \`/images/\${detail.image[1]}\` : '/images/placeholder.jpg';
  currentScore.value = detail.score.join(', ');
}

function showImageModal(imageSrc) {
  modalImageSrc.value = imageSrc;
  showModal.value = true;
}

function closeImageModal() {
  showModal.value = false;
}
</script>

<style scoped>
.task-detail-page {
  width: 800px;
  /* Height is removed to allow content to define it, or set to min-height if 500px is a minimum */
  /* height: 500px; */
  min-height: 480px; /* Adjusted to prevent scrollbars if padding/borders add up */
  margin: 20px auto; /* Added some top/bottom margin for better page appearance */
  padding: 20px;
  border: 1px solid #ccc;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  text-align: center; /* Centers inline content like text and buttons in their containers */
  display: flex;
  flex-direction: column;
  justify-content: space-between; /* Distributes space between elements */
}

h1 {
  margin-top: 0;
  margin-bottom: 15px; /* Reduced margin */
}

.carrage-buttons-container {
  margin-bottom: 15px; /* Reduced margin */
  /* text-align: center; is inherited */
}

.carrage-button {
  margin: 0 5px; /* Horizontal margin only */
  padding: 8px 15px; /* Adjusted padding */
  cursor: pointer;
  border: 1px solid #007bff;
  background-color: #007bff;
  color: white;
  border-radius: 4px;
  transition: background-color 0.2s ease;
}

.carrage-button:hover {
  background-color: #0056b3;
}

.image-display {
  display: flex;
  justify-content: space-around; /* Distributes images with space around them */
  align-items: center; /* Vertically align images if they have different heights */
  margin-bottom: 15px; /* Reduced margin */
}

.displayed-image {
  width: 300px;
  height: 200px;
  border: 1px solid #ddd;
  background-color: #f8f8f8; /* Light background for image placeholder */
  object-fit: cover; /* Ensures image covers the area, might crop */
  cursor: pointer;
  border-radius: 4px;
}

.score-display {
  /* text-align: center; is inherited */
  margin-bottom: 10px; /* Adjusted margin */
}

.score-textarea {
  width: calc(100% - 40px); /* Make textarea responsive within padding */
  max-width: 620px; /* As specified before, but now relative to container */
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  resize: vertical; /* Allow vertical resize only */
  font-family: inherit;
}

.modal {
  display: block;
  position: fixed;
  z-index: 1000; /* Ensure modal is on top */
  padding-top: 60px; /* Adjusted padding */
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0,0,0,0.85); /* Darkened backdrop */
}

.modal-content {
  margin: auto;
  display: block;
  width: auto; /* Adjust width automatically */
  max-width: 80%; /* Max width relative to viewport */
  max-height: 80vh; /* Max height relative to viewport height */
}

.close {
  position: absolute;
  top: 20px; /* Adjusted position */
  right: 30px; /* Adjusted position */
  color: #fff; /* White close button for better contrast */
  font-size: 35px; /* Adjusted size */
  font-weight: bold;
  transition: 0.3s;
}

.close:hover,
.close:focus {
  color: #bbb;
  text-decoration: none;
  cursor: pointer;
}
</style>
