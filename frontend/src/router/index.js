import { createRouter, createWebHistory } from 'vue-router'
import GuestLayout from '@/layouts/guest/GuestLayout.vue'
import LoginPage from '@/views/auth/LoginPage.vue'
import AuthenticatedUserLayout from '@/layouts/authenticated/AuthenticatedUserLayout.vue'
import HomeView from '@/views/users/HomeView.vue'
import RegisterPage from '@/views/auth/RegisterPage.vue'
import LandingPage from '@/views/LandingPage.vue'

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: [
		{
			path: '',
			name: 'landing',
			component: LandingPage,
		},
		{
			path: '/',
			component: GuestLayout,
			children: [
				{
					path: 'login',
					name: 'login',
					component: LoginPage,
				},
				{
					path: 'register',
					name: 'register',
					component: RegisterPage,
				},
			]
		},
		{
			path: '/',
			component: AuthenticatedUserLayout,
			children:[
				{
					path: 'dashboard',
					name: 'dashboard',
					component: HomeView
				}
			]
		}
	],
})

export default router
