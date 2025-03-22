<template>
	<button
		type="button"
		class="inline-flex w-8 h-8 p-0 items-center justify-center surface-0 dark:surface-800 rounded"
		@click="themeChange"
	>
		<i :class="`dark:text-white text-slate-900 pi ${iconClass}`" style="font-size: 1.5rem;" />
	</button>
</template>

<script>
import { useThemeStore } from '@/stores/themeStore'
import { mapActions, mapState } from 'pinia'

export default {
	methods: {
		...mapActions(useThemeStore, ['themeChange']),
	},
	computed: {
		rippleActive() {
			return this.$primevue.config.ripple
		},
		...mapState(useThemeStore, ['iconClass']),
	},
}
</script>
