// axios.js
import axios from 'axios';

const backendUrl = import.meta.env.VITE_API_BACKEND_URL || 'http://127.0.0.1:8000/api/';

const api = axios.create({
    baseURL: backendUrl,
    withCredentials: true, // Send cookies with requests
	timeout: 10000, // 10 seconds
});

// Add auth token to all requests
api.interceptors.request.use((config) => {
    const csrfToken = document.cookie.split('; ').find(row => row.startsWith('csrftoken='))?.split('=')[1];
    if (csrfToken) {
        config.headers['X-CSRFToken'] = csrfToken;
    }
    return config;
});

api.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config;

        if (error.response?.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;

            try {
                // Send request to refresh the token (cookie-based)
                await axios.post(`${backendUrl}/api/token/refresh/`, {}, { withCredentials: true });

                // Retry the original request
                return api(originalRequest);
            } catch (refreshError) {
				console.log(refreshError);

                // Redirect to login if refresh fails
                // window.location.href = '/';
                return Promise.reject(refreshError);
            }
        }

        return Promise.reject(error);
    }
);


// Login using email and password
export const login = async (email, password) => {
	try {
        const response = await axios.post(`${backendUrl}login/`, { email, password }, {
            withCredentials: true
        });
        console.log('Login response:', response);
        return true;
    } catch (error) {
        console.error('Login failed:', error.response?.data || error.message);
        return false;
    }
};

// Logout by clearing cookies
export const logout = async () => {
    try {
        const response = await api.post('logout/', {}, {
            withCredentials: true,
            headers: {
                'X-CSRFToken': document.cookie.split('; ')
                    .find(row => row.startsWith('csrftoken='))
                    ?.split('=')[1]
            }
        });
        console.log('Logout successful:', response);
        return true;
    } catch (error) {
        console.error('Logout failed:', error.response?.data || error.message);
        return false;
    }
};

export default api;