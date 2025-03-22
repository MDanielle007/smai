<template>
	<!-- Company Branding -->
	<div class="text-center">
		<h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900 dark:text-gray-100">
			Create Your Account
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

	<!-- Registration Form -->
	<form class=" space-y-6 w-full mb-8" @submit.prevent="handleSubmit">

		<div>
			<label class="block text-gray-700 dark:text-gray-400">Full Name</label>
			<IconField fluid>
				<InputIcon>
					<i class="pi pi-user" />
				</InputIcon>
				<InputText type="text" v-model="name" fluid placeholder="Juan Dela Cruz" />
			</IconField>
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
				<Password :feedback="true" v-model="password" fluid toggleMask placeholder="Create a password" />
			</IconField>
		</div>
		<div>
			<label class="block mt-4 text-gray-700 dark:text-gray-400">Role</label>
			<Select
				v-model="role"
				:options="roleOptions"
				optionLabel="label"
				optionValue="value"
				placeholder="Select your role"
				class="w-full"
			/>
		</div>
		<div class="flex items-center justify-between mt-4">
			<div class="text-sm">
				<router-link :to="{name: 'login'}" class="text-blue-600 hover:text-blue-800 dark:text-blue-400 dark:hover:text-blue-300">
					Already have an account? Sign in
				</router-link>
			</div>
		</div>
		<button
			type="submit"
			class="w-full mt-4 bg-gray-900 text-white dark:bg-gray-100 dark:text-gray-900 py-2 rounded-lg"
		>
			Create Account
		</button>
	</form>
</template>
<script>
import { register } from '@/services/apiClient.js';

export default {
	data() {
		return {
			email: '',
			name: '',
			password: '',
			role: 'end_user',
			error: null,
			roleOptions: [
				{ label: 'Requestor', value: 'end_user' },
				{ label: 'Service Provider', value: 'service_provider' },
			]
		};
	},
	methods: {
		async handleSubmit() {
			// Validate form
			if (!this.email || !this.name || !this.password) {
				this.error = 'Please fill in all required fields';
				return;
			}

			// Perform registration logic
			console.log('Email:', this.email);
			console.log('Name:', this.name);
			console.log('Password:', this.password);
			console.log('Role:', this.role);

			 const res = await register(this.email, this.name, this.password, this.role)
			 if (res) {
				 this.$router.push('/app');
			 } else {
			 	this.error = 'Registration failed. Please try again.';
			 }
		},
		signInWithMicrosoft() {
			// Implement Microsoft sign-up logic here
			console.log('Signing up with Microsoft...');
		}
	}
}
</script>