<template>
	<div class="bg-gray-100 dark:bg-gray-900">
		<!-- Navigation Bar -->
		<nav class="bg-white dark:bg-gray-800 shadow-md py-4 px-6 sticky top-0 z-50">
			<div class="container mx-auto flex justify-between items-center">
				<div class="text-xl font-bold text-gray-800 dark:text-white flex items-center justify-center gap-2">
					<img
							src="/web-app-manifest-192x192.png"
							alt="AetherClock"
							width="40"
							height="40"
							class="rounded-xl shadow-lg"
						/>
					Service Management AI
				</div>
				<div class="flex items-center space-x-4">
					<ThemeSwitcher />
					<div class="hidden md:flex space-x-4">
						<router-link
							:to="{ name: 'login' }"
						>
							<Button
								label="Login"
								text
							/>
						</router-link>
						<router-link
							:to="{ name: 'register' }"
							>
							<Button
								label="Sign Up"
							/>
							</router-link
						>
					</div>
					<Button
						icon="pi pi-bars"
						text
						rounded
						class="md:hidden"
						@click="toggleMobileMenu"
					/>
				</div>
			</div>
			<!-- Mobile Menu -->
			<div
				v-if="mobileMenuOpen"
				class="md:hidden absolute top-16 left-0 right-0 bg-white dark:bg-gray-800 shadow-md py-4 px-6 z-50"
			>
				<div class="flex flex-col space-y-4">
					<router-link
						:to="{ name: 'login' }"
						class="text-gray-600 hover:text-blue-600 dark:text-gray-300 dark:hover:text-blue-400 transition-colors"
						>Login</router-link
					>
					<router-link
						:to="{ name: 'register' }"
						class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md transition-colors text-center"
						>Sign Up</router-link
					>
				</div>
			</div>
		</nav>
		<div class="landing-page">
			<!-- Hero Section -->
			<section
				class="hero-section bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-800 dark:to-purple-900 text-white py-20"
			>
				<div class="container mx-auto px-4 sm:px-8 md:px-12">
					<div class="flex flex-col md:flex-row items-center justify-between">
						<div class="md:w-1/2 mb-8 md:mb-0">
							<h1 class="text-4xl md:text-5xl font-bold mb-6">
								Smart Service Management
							</h1>
							<p class="text-xl mb-8">
								AI-powered service booking and management platform that connects
								service providers with customers.
							</p>
							<div
								class="flex flex-col sm:flex-row space-y-3 sm:space-y-0 sm:space-x-4"
							>
								<Button
									label="Sign Up"
									icon="pi pi-user-plus"
									severity="success"
									class="px-6 py-3"
									@click="navigateToRegister"
								/>
								<Button
									label="Login"
									icon="pi pi-sign-in"
									outlined
									class="px-6 py-3 border-white text-white hover:bg-primary-600 dark:hover:bg-purple-950"
									@click="navigateToLogin"
								/>
							</div>
						</div>
						<div class="md:w-1/2">

						</div>
					</div>
				</div>
			</section>

			<!-- Features Section -->
			<section class="py-20 bg-gray-50 dark:bg-gray-800">
				<div class="container mx-auto px-4 sm:px-8 md:px-12">
					<h2 class="text-3xl font-bold text-center mb-12 text-gray-800 dark:text-white">
						Key Features
					</h2>
					<div class="grid grid-cols-1 md:grid-cols-3 gap-8">
						<!-- Feature 1 -->
						<div
							class="bg-white dark:bg-gray-700 p-8 rounded-lg shadow-md hover:shadow-lg transition-shadow"
						>
							<div class="text-center mb-6">
								<i
									class="pi pi-calendar text-4xl text-blue-600 dark:text-blue-400"
								></i>
							</div>
							<h3
								class="text-xl font-semibold mb-4 text-center text-gray-800 dark:text-white"
							>
								Service Booking
							</h3>
							<p class="text-gray-600 dark:text-gray-300 text-center">
								Browse and book services with ease. Schedule appointments that fit
								your calendar.
							</p>
						</div>
						<!-- Feature 2 -->
						<div
							class="bg-white dark:bg-gray-700 p-8 rounded-lg shadow-md hover:shadow-lg transition-shadow"
						>
							<div class="text-center mb-6">
								<i class="pi pi-cog text-4xl text-blue-600 dark:text-blue-400"></i>
							</div>
							<h3
								class="text-xl font-semibold mb-4 text-center text-gray-800 dark:text-white"
							>
								Service Management
							</h3>
							<p class="text-gray-600 dark:text-gray-300 text-center">
								Service providers can manage their offerings, availability, and
								bookings in one place.
							</p>
						</div>
						<!-- Feature 3 -->
						<div
							class="bg-white dark:bg-gray-700 p-8 rounded-lg shadow-md hover:shadow-lg transition-shadow"
						>
							<div class="text-center mb-6">
								<i class="pi pi-bolt text-4xl text-blue-600 dark:text-blue-400"></i>
							</div>
							<h3
								class="text-xl font-semibold mb-4 text-center text-gray-800 dark:text-white"
							>
								AI Recommendations
							</h3>
							<p class="text-gray-600 dark:text-gray-300 text-center">
								Get smart service reminders and suggestions powered by DeepSeek AI
								technology.
							</p>
						</div>
					</div>
				</div>
			</section>

			<!-- User Roles Section -->
			<section class="py-20 bg-white dark:bg-gray-900">
				<div class="container mx-auto px-4 sm:px-8 md:px-12">
					<h2 class="text-3xl font-bold text-center mb-12 text-gray-800 dark:text-white">
						User Roles
					</h2>
					<div class="grid grid-cols-1 md:grid-cols-3 gap-8">
						<!-- Admin Role -->
						<div
							class="border border-gray-200 dark:border-gray-700 rounded-lg p-8 hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors"
						>
							<div class="text-center mb-6">
								<i
									class="pi pi-shield text-4xl text-indigo-600 dark:text-indigo-400"
								></i>
							</div>
							<h3
								class="text-xl font-semibold mb-4 text-center text-gray-800 dark:text-white"
							>
								Admin
							</h3>
							<ul class="list-disc pl-5 text-gray-600 dark:text-gray-300 space-y-2">
								<li>Review and approve services</li>
								<li>Manage users and system configurations</li>
								<li>Monitor platform performance</li>
							</ul>
						</div>
						<!-- Service Provider Role -->
						<div
							class="border border-gray-200 dark:border-gray-700 rounded-lg p-8 hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors"
						>
							<div class="text-center mb-6">
								<i
									class="pi pi-briefcase text-4xl text-indigo-600 dark:text-indigo-400"
								></i>
							</div>
							<h3
								class="text-xl font-semibold mb-4 text-center text-gray-800 dark:text-white"
							>
								Service Provider
							</h3>
							<ul class="list-disc pl-5 text-gray-600 dark:text-gray-300 space-y-2">
								<li>Register services in the system</li>
								<li>Manage availability and service details</li>
								<li>Receive and process bookings</li>
							</ul>
						</div>
						<!-- End User Role -->
						<div
							class="border border-gray-200 dark:border-gray-700 rounded-lg p-8 hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors"
						>
							<div class="text-center mb-6">
								<i
									class="pi pi-user text-4xl text-indigo-600 dark:text-indigo-400"
								></i>
							</div>
							<h3
								class="text-xl font-semibold mb-4 text-center text-gray-800 dark:text-white"
							>
								End User
							</h3>
							<ul class="list-disc pl-5 text-gray-600 dark:text-gray-300 space-y-2">
								<li>Browse and book available services</li>
								<li>Receive AI-powered reminders</li>
								<li>Book services via AI chat or manually</li>
							</ul>
						</div>
					</div>
				</div>
			</section>

			<!-- Workflow Section -->
			<section class="py-20 bg-gray-50 dark:bg-gray-800">
				<div class="container mx-auto px-4">
					<h2 class="text-3xl font-bold text-center mb-12 text-gray-800 dark:text-white">
						How It Works
					</h2>
					<div
						class="flex flex-col md:flex-row items-center justify-center space-y-8 md:space-y-0 md:space-x-12"
					>
						<!-- Step 1 -->
						<div class="flex flex-col items-center max-w-xs text-center">
							<div
								class="w-16 h-16 rounded-full bg-blue-600 flex items-center justify-center text-white text-xl font-bold mb-4"
							>
								1
							</div>
							<h3 class="text-xl font-semibold mb-2 text-gray-800 dark:text-white">
								Service Registration
							</h3>
							<p class="text-gray-600 dark:text-gray-300">
								Service providers register their services for admin approval
							</p>
						</div>
						<!-- Arrow -->
						<div class="hidden md:block text-gray-400 dark:text-gray-500">
							<i class="pi pi-arrow-right text-3xl"></i>
						</div>
						<div class="block md:hidden text-gray-400 dark:text-gray-500">
							<i class="pi pi-arrow-down text-3xl"></i>
						</div>
						<!-- Step 2 -->
						<div class="flex flex-col items-center max-w-xs text-center">
							<div
								class="w-16 h-16 rounded-full bg-blue-600 flex items-center justify-center text-white text-xl font-bold mb-4"
							>
								2
							</div>
							<h3 class="text-xl font-semibold mb-2 text-gray-800 dark:text-white">
								Service Booking
							</h3>
							<p class="text-gray-600 dark:text-gray-300">
								Users browse and book available services
							</p>
						</div>
						<!-- Arrow -->
						<div class="hidden md:block text-gray-400 dark:text-gray-500">
							<i class="pi pi-arrow-right text-3xl"></i>
						</div>
						<div class="block md:hidden text-gray-400 dark:text-gray-500">
							<i class="pi pi-arrow-down text-3xl"></i>
						</div>
						<!-- Step 3 -->
						<div class="flex flex-col items-center max-w-xs text-center">
							<div
								class="w-16 h-16 rounded-full bg-blue-600 flex items-center justify-center text-white text-xl font-bold mb-4"
							>
								3
							</div>
							<h3 class="text-xl font-semibold mb-2 text-gray-800 dark:text-white">
								AI Recommendations
							</h3>
							<p class="text-gray-600 dark:text-gray-300">
								Receive smart reminders and suggestions for future services
							</p>
						</div>
					</div>
				</div>
			</section>

			<!-- CTA Section -->
			<section class="py-20 bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-800 dark:to-purple-900 text-white">
				<div class="container mx-auto px-4 text-center">
					<h2 class="text-3xl font-bold mb-6">Ready to Get Started?</h2>
					<p class="text-xl mb-8 max-w-2xl mx-auto">
						Join our platform today and experience the future of service management with
						AI-powered recommendations.
					</p>
					<div
						class="flex flex-col sm:flex-row justify-center space-y-4 sm:space-y-0 sm:space-x-4"
					>
						<Button
							label="Sign Up Now"
							icon="pi pi-user-plus"
							severity="success"
							size="large"
							@click="navigateToRegister"
						/>
						<Button
							label="Learn More"
							icon="pi pi-info-circle"
							outlined
							class="border-white text-white"
							size="large"
						/>
					</div>
				</div>
			</section>

			<!-- Footer -->
			<footer class="bg-gray-800 text-white py-12">
				<div class="mx-auto px-4">
					<div class="flex flex-col md:flex-row justify-between items-center">
						<div class="mb-4 md:mb-0">
							<h3 class="text-xl font-bold">Service Management AI</h3>
							<p class="text-gray-400">Connecting service providers with customers</p>
						</div>
						<div class="flex space-x-4">
							<a href="#" class="hover:text-blue-400 transition-colors"
								><i class="pi pi-facebook"></i
							></a>
							<a href="#" class="hover:text-blue-400 transition-colors"
								><i class="pi pi-twitter"></i
							></a>
							<a href="#" class="hover:text-blue-400 transition-colors"
								><i class="pi pi-linkedin"></i
							></a>
							<a href="#" class="hover:text-blue-400 transition-colors"
								><i class="pi pi-instagram"></i
							></a>
						</div>
					</div>
					<div class="mt-8 pt-8 border-t border-gray-700 text-center text-gray-400">
						<p>
							&copy; {{ new Date().getFullYear() }} Service Management AI. All rights
							reserved.
						</p>
					</div>
				</div>
			</footer>
		</div>
	</div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ref } from 'vue'

const router = useRouter()

const mobileMenuOpen = ref(false)

const toggleMobileMenu = () => {
	mobileMenuOpen.value = !mobileMenuOpen.value
}

const navigateToLogin = () => {
	router.push({ name: 'login' })
}

const navigateToRegister = () => {
	router.push({ name: 'register' })
}
</script>

<style scoped>
/* Add responsive adjustments */
@media (max-width: 768px) {
	.hero-section {
		text-align: center;
	}
}
</style>
