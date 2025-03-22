<template>
	<div
		class="min-h-screen flex items-center justify-center bg-gray-100 dark:bg-gray-900 py-12 px-4 sm:px-6 lg:px-8"
	>
		<div
			class="w-full max-w-xl space-y-8 bg-white dark:bg-gray-800 py-5 px-4 sm:px-6 md:px-8 rounded-lg shadow dark:shadow-gray-700 overflow-auto"
		>
			<div class="flex flex-col items-center w-full">
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
