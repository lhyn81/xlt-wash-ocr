import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import TaskDetail from '../views/TaskDetail.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    // Path for task details, e.g., /taskid123
    path: '/:taskid',
    name: 'TaskDetail',
    component: TaskDetail,
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
