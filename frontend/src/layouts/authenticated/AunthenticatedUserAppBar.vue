<template>
	<div
		class="fixed top-0 left-0 right-0 z-50 w-screen h-14 bg-blue-800 text-white flex justify-between items-center px-4 gap-4 drop-shadow-md"
	>
		<div class="flex gap-4 justify-center items-center">
			<i
				class="pi pi-bars hover:cursor-pointer"
				style="font-size: 2rem"
				@click="layoutStore.toggleSideBar"
			></i>
		</div>

		<!-- Notification Bell & User Controls -->
		<div class="flex gap-4 items-center">
			<!-- Notification Bell -->
			<div class="relative notification-menu">
				<button
					class="relative p-1 mt-2 ml-3"
					data-notification
					@click="toggleNotificationMenu"
				>
					<i class="pi pi-bell text-2xl"></i>
					<!-- Unread Badge -->
					<span
						v-if="unreadNotifications.length > 0"
						class="absolute -top-1 -right-1 bg-red-600 text-white text-xs font-bold rounded-full w-5 h-5 flex items-center justify-center"
					>
						{{ unreadNotifications.length }}
					</span>
				</button>

				<div
					v-if="showNotifications"
					class="absolute right-0 mt-2 w-80 bg-white dark:bg-slate-800 text-slate-800 shadow-lg rounded-lg overflow-hidden z-10"
				>
					<div
						class="p-4 border-b dark:border-slate-700 flex justify-between items-center bg-blue-100 dark:bg-slate-800 dark:text-slate-50"
					>
						<h3 class="font-semibold text-blue-900 dark:text-slate-50">
							Notifications
						</h3>
						<button
							@click="markAllAsRead"
							class="text-sm text-blue-700 hover:underline dark:text-slate-50"
						>
							Mark all as read
						</button>
					</div>

					<ul class="max-h-64 overflow-y-auto">
						<li
							v-for="notification in notifications"
							:key="notification.id"
							class="p-4 border-b dark:border-slate-700 flex flex-col space-y-1 cursor-pointer dark:bg-slate-800 dark:text-slate-50"
							@click="markAsRead(notification)"
						>
							<p class="text-sm">{{ notification.message }}</p>
							<p class="text-xs opacity-80">
								{{ formatDate(notification.timestamp) }}
							</p>
						</li>
					</ul>

					<!-- No Notifications -->
					<div v-if="notifications.length === 0" class="p-4 text-center opacity-80">
						No new notifications
					</div>
				</div>
			</div>

			<ThemeSwitcher />

			<!-- User Profile with Dropdown -->
			<div class="relative profile-menu">
				<button @click="toggleProfileMenu" class="flex items-center focus:outline-none">
					<Avatar
						label="V"
						class="mr-2 cursor-pointer"
						size="medium"
						style="background-color: #ece9fc; color: #2a1261"
						shape="circle"
					/>
				</button>

				<!-- Profile Dropdown Menu -->
				<div
					v-show="showProfileMenu"
					class="absolute right-0 mt-2 w-40 bg-white text-gray-800 shadow-lg rounded-lg overflow-hidden z-50 border border-gray-200 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-50"
				>
					<ul>
						<li class="hover:bg-blue-50 dark:hover:bg-slate-700 transition-colors">
							<button
								@click="goToEditProfile"
								class="w-full text-left p-3 flex items-center gap-2"
							>
								<i class="pi pi-user text-blue-600"></i>
								<span>User Profile</span>
							</button>
						</li>
						<li
							class="hover:bg-blue-50 dark:hover:bg-slate-700 transition-colors border-t dark:border-gray-700"
						>
							<button
								class="w-full text-left p-3 flex items-center gap-2"
								@click="handleLogout"
							>
								<i class="pi pi-sign-out text-blue-600"></i>
								<span>Log out</span>
							</button>
						</li>
					</ul>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'
import ThemeSwitcher from '@/components/ThemeSwitcher.vue'
import { useLayoutStore } from '@/stores/layoutStore'
import { logout } from '@/services/apiClient.js'

const router = useRouter()
const layoutStore = useLayoutStore()

const showNotifications = ref(false)
const showProfileMenu = ref(false)

const notifications = ref([
	{
		id: 1,
		ticketId: 'TKT-INC-USR123-20250227-0001',
		message: 'Your ticket has been updated',
		read: false,
		timestamp: '2025-03-10T14:30:00',
	},
	{
		id: 2,
		ticketId: 'TKT-REQ-USR456-20250301-0002',
		message: 'You have a new response regarding your ticket.',
		read: true,
		timestamp: '2025-03-09T09:15:00',
	},
])

const unreadNotifications = computed(() => notifications.value.filter((n) => !n.read))

const toggleNotificationMenu = () => {
	showNotifications.value = !showNotifications.value
	if (showNotifications.value) showProfileMenu.value = false
}

const toggleProfileMenu = () => {
	showProfileMenu.value = !showProfileMenu.value
}

const goToEditProfile = () => {
	router.push({ name: 'profile' })
	showProfileMenu.value = false
}

const markAsRead = (notification) => {
	notification.read = true
	showNotifications.value = false
	router.push(`/app/tickets/${notification.ticketId}`)
}

const markAllAsRead = () => {
	notifications.value.forEach((n) => (n.read = true))
}

const formatDate = (timestamp) => {
	const date = new Date(timestamp)
	return date.toLocaleString('en-US', {
		weekday: 'short',
		month: 'short',
		day: '2-digit',
		hour: '2-digit',
		minute: '2-digit',
		hour12: true,
	})
}

const handleClickOutside = (event) => {
	// Check for clicks outside the profile menu
	if (!event.target.closest('.profile-menu')) {
		showProfileMenu.value = false
	}

	// Check for clicks outside the notification menu
	if (
		!event.target.closest('.notification-menu') &&
		!event.target.closest('[data-notification]')
	) {
		showNotifications.value = false
	}
}

const handleLogout = async () => {
	await logout();
	router.push({ name: 'login' })
}

onMounted(() => {
	document.addEventListener('mousedown', handleClickOutside)
})

onBeforeUnmount(() => {
	document.removeEventListener('mousedown', handleClickOutside)
})
</script>
