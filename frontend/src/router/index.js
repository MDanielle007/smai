import { createRouter, createWebHistory } from 'vue-router'
import GuestLayout from '@/layouts/guest/GuestLayout.vue'
import LoginPage from '@/views/auth/LoginPage.vue'
import AuthenticatedUserLayout from '@/layouts/authenticated/AuthenticatedUserLayout.vue'
import HomeView from '@/views/users/HomeView.vue'

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: [
		{
			path: '/',
			component: GuestLayout,
			children: [
				{
					path: '',
					name: 'login',
					component: LoginPage,
				},
			]
		},
		{
			path: '/app',
			component: AuthenticatedUserLayout,
			children:[
				{
					path: '',
					name: 'home',
					component: HomeView
				}
			]
		}
	],
})

export default router
