<template>
	<div
		class="min-h-screen flex items-center justify-center bg-gray-100 dark:bg-gray-900 py-12 px-4 sm:px-6 lg:px-8"
	>
		<div
			class="max-w-md w-full space-y-8 bg-white dark:bg-gray-800 py-5 px-8 rounded-lg shadow dark:shadow-gray-700"
		>
			<div class="flex flex-col items-center">
				<router-view></router-view>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'GuestLayout',
}
</script>
