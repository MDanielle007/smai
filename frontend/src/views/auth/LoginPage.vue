<template>
	<!-- Company Branding -->
	<div class="text-center">
		<h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900 dark:text-gray-100">
			Sign in to Your Account
		</h2>
	</div>

	<!-- Error Alert -->
	<div
		v-if="error"
		class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative"
		role="alert"
	>
		<span class="block sm:inline">{{ error }}</span>
	</div>

	<!-- Login Form -->
	<form class="my-8 space-y-6 w-full" @submit.prevent="handleSubmit">
		<div>
			<label class="block text-gray-700 dark:text-gray-400">Email address</label>
			<IconField fluid>
				<InputIcon>
					<i class="pi pi-envelope" />
				</InputIcon>
				<InputText type="text" v-model="email" fluid placeholder="name@company.com" />
			</IconField>
		</div>
		<div>
			<label class="block mt-4 text-gray-700 dark:text-gray-400">Password</label>
			<IconField fluid>
				<InputIcon>
					<i class="pi pi-lock" />
				</InputIcon>
				<Password :feedback="false" v-model="password" fluid toggleMask placeholder="Enter your password"/>
			</IconField>
		</div>
		<button
			type="submit"
			class="w-full mt-4 bg-gray-900 text-white dark:bg-gray-100 dark:text-gray-900 py-2 rounded-lg"
		>
			Sign in
		</button>
		<div class="flex items-center justify-between mt-4">
			<div class="text-sm">
				<router-link :to="{name: 'register'}" class="text-blue-600 hover:text-blue-800 dark:text-blue-400 dark:hover:text-blue-300">
				Don't have an account yet? Sign up
				</router-link>
			</div>
		</div>
	</form>
</template>
<script>
import { login } from '@/services/apiClient.js';

export default {
	data() {
		return {
			email: '',
			password: '',
			error: null,
		};
	},
	methods: {
		async handleSubmit() {
			// Perform login logic here
			console.log('Email:', this.email);
			console.log('Password:', this.password);
			const res = await login(this.email, this.password);

			if (res) {
				this.$router.push('/app');
			} else {
				this.error = 'Invalid login credentials';
			}
		},
		signInWithMicrosoft() {
			// Implement Microsoft sign-in logic here
			console.log('Signing in with Microsoft...');
		}
	}
}

</script>