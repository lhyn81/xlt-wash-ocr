import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import TaskDetail from '../views/TaskDetail.vue';
import TestPage from '../views/Test.vue';

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
  {
    // Path for task details, e.g., /taskid123
    path: '/test',
    name: 'TestPage',
    component: TestPage,
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
