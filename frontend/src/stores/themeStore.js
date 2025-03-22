import { defineStore } from "pinia";

const THEME_KEY = 'theme';

export const useThemeStore = defineStore('theme', {
	state: () => ({
		darkTheme: localStorage.getItem(THEME_KEY) === 'dark', // Load saved theme from localStorage
		iconClass: localStorage.getItem(THEME_KEY) === 'dark' ? 'pi-sun' : 'pi-moon',
	}),
	actions: {
		themeChange() {
			this.darkTheme = !this.darkTheme;
			const newTheme = this.darkTheme ? 'dark' : 'light';

			// Apply theme to document
			document.documentElement.classList.toggle('p-dark', this.darkTheme);

			// Store selected theme in localStorage
			localStorage.setItem(THEME_KEY, newTheme);

			// Toggle icon
			this.iconClass = this.darkTheme ? 'pi-sun' : 'pi-moon';
		},
		initializeTheme() {
			const storedTheme = localStorage.getItem(THEME_KEY) || 'auto';
			const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

			if (storedTheme === 'auto') {
				this.darkTheme = prefersDark;
			} else {
				this.darkTheme = storedTheme === 'dark';
			}

			// Apply theme on load
			document.documentElement.classList.toggle('p-dark', this.darkTheme);

			// Set correct icon
			this.iconClass = this.darkTheme ? 'pi-sun' : 'pi-moon';
		}
	},
});
