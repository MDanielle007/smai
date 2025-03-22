import { defineStore } from 'pinia'

export const useLayoutStore = defineStore('layout', {
	state: () => ({
		sideBar: false,
	}),
	getters: {

	},
	actions: {
		toggleSideBar() {
			this.sideBar = !this.sideBar;
		},
		handleResize() {
			this.sideBar = window.innerWidth >= 1280;
		},
		initResizeListener() {
			this.handleResize(); // Initial setup
			window.addEventListener('resize', this.handleResize);
		},
		cleanupResizeListener() {
			window.removeEventListener('resize', this.handleResize);
		},
	}
})
