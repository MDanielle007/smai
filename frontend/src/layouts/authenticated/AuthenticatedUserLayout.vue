<template>
	<div class="flex relative bg-slate-100 dark:bg-slate-950 h-screen overflow-hidden">
		<AunthenticatedUserAppBar />
		<AuthenticatedUserSidebar />

		<!-- Main Content -->
		<main
			:class="[
				'flex-1 pt-16 pr-2 h-full w-full transition-all duration-300 ease-in-out pl-14',
				isSidebarVisible ? 'xl:pl-80' : 'xl:pl-16',
			]"
		>
			<ScrollPanel
				class="w-full"
				:style="{ height: `${scrollHeight}px` }"
				:dt="{ bar: { background: '{surface.700}' } }"
			>
				<div class="p-2 sm:p-4 md:p-6">
					<router-view></router-view>
				</div>
			</ScrollPanel>
		</main>
	</div>
</template>

<script>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import AunthenticatedUserAppBar from './AunthenticatedUserAppBar.vue'
import AuthenticatedUserSidebar from './AuthenticatedUserSidebar.vue'
import { useLayoutStore } from '@/stores/layoutStore'

export default {
	components: {
		AunthenticatedUserAppBar,
		AuthenticatedUserSidebar,
	},
	setup() {
		const layoutStore = useLayoutStore()
		const isSidebarVisible = computed(() => layoutStore.sideBar)

		const scrollHeight = ref(window.innerHeight - 64) // Adjust based on your layout

		const updateScrollHeight = () => {
			scrollHeight.value = window.innerHeight - 64 // Adjust for navbar height if needed
		}

		onMounted(() => {
			layoutStore.initResizeListener()
			window.addEventListener('resize', updateScrollHeight)
		})

		onUnmounted(() => {
			layoutStore.cleanupResizeListener()
			window.removeEventListener('resize', updateScrollHeight)
		})

		return { isSidebarVisible, scrollHeight }
	},
}
</script>
