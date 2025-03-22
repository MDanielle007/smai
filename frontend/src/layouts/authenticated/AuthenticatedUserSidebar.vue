<template>
	<div
		:class="[
			'bg-white dark:bg-slate-800 fixed top-14 left-0 h-screen z-20 transition-all duration-300 ease-in-out drop-shadow-lg lg:drop-shadow-none pt-4',
			isSidebarVisible ? 'w-80 px-4' : 'w-16 px-2 hover:w-80 hover:px-6',
		]"
		@mouseenter="handleMouseEnter"
		@mouseleave="handleMouseLeave"
	>
		<div>
			<ScrollPanel
				style="width: 100%; height: 100%"
				:dt="{
					bar: {
						background: '{blue.600}',
					},
				}"
				pt:barX:class="hidden"
			>
				<div :class="[isSidebarVisible || isHovered ? 'pr-3' : 'pr-0']">
					<AuthenticatedUserMenuItem
						:menuItems="menuItems"
						:collapsed="!isSidebarVisible && !isHovered"
					/>
				</div>
			</ScrollPanel>
		</div>

		<AuthenticatedUserMenuItem
			:menuItems="userMenuItems"
			:collapsed="!isSidebarVisible && !isHovered"
		/>
	</div>
	<div
		v-if="(isSidebarVisible || isHovered) && isSmallScreen"
		class="fixed inset-0 bg-black bg-opacity-50 dark:opacity-80 z-10 transition-opacity"
		@click="closeSidebar"
	></div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import AuthenticatedUserMenuItem from './AuthenticatedUserMenuItem.vue'
import { useLayoutStore } from '@/stores/layoutStore'


// const authStore = useAuthStore()
const layoutStore = useLayoutStore()
const isSidebarVisible = computed(() => layoutStore.sideBar)

const isSmallScreen = computed(() => window.innerWidth < 1280)

if (window.innerWidth >= 1280) {
	layoutStore.sideBar = false
}

const updateScreenSize = () => {
	if (window.innerWidth >= 1280) {
		layoutStore.sideBar = true
	}
}

const closeSidebar = () => {
	layoutStore.sideBar = false
}

const menuItems = ref([
	{
		label: 'Home',
		route: { name: 'home' },
		icon: 'pi pi-home',
	},
])

const userMenuItems = ref([])

const isHovered = ref(false)

const handleMouseEnter = () => {
	if (!isSidebarVisible.value) {
		isHovered.value = true
	}
}

const handleMouseLeave = () => {
	isHovered.value = false
}

onMounted(() => {
	window.addEventListener('resize', updateScreenSize)
})

onUnmounted(() => {
	window.removeEventListener('resize', updateScreenSize)
})
</script>

<style scoped>
/* Optional: Add this if you want to prevent text selection during hover transitions */
.hover\:w-80 {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}
</style>
