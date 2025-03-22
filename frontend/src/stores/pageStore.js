import { defineStore } from 'pinia'

export const usePageStore = defineStore('page', {
	state: () => ({
		appBarTitle: 'Home',
	}),
	getters: {
		getPageTitle() {
			return this.pageTitle;
		},
		getPageDescription() {
			return this.pageDescription;
		}
	},
	actions: {
		setPageTitle(title) {
			this.pageTitle = title;
		},
	}
})

export default usePageStore;
