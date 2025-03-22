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
		<button
			type="button"
			@click="signInWithMicrosoft"
			class="w-full bg-gray-900 dark:bg-gray-100 dark:text-gray-900 text-white py-2 rounded-lg flex items-center justify-center"
		>
			<span class="mr-2"
				><svg width="32" height="32" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
					<path fill="#f24f21" d="M4 4h10.7v10.7H4z"></path>
					<path fill="#7fb900" d="M17.3 4H28v10.7H17.3z"></path>
					<path fill="#00a3ee" d="M4 17.3h10.7V28H4z"></path>
					<path fill="#ffb900" d="M17.3 17.3H28V28H17.3z"></path></svg
			></span>
			Sign in with Microsoft
		</button>
		<div class="flex items-center my-4">
			<hr class="flex-grow border-gray-300" />
			<span class="px-2 text-gray-500 dark:text-gray-300">or</span>
			<hr class="flex-grow border-gray-300" />
		</div>
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