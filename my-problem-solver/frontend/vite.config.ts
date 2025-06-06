// frontend/vite.config.ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173, // You can specify the port for the frontend dev server
    host: '0.0.0.0', // Listen on all addresses
    proxy: {
      // String shorthand: '/foo' -> 'http://localhost:4567/foo'
      // '/api': 'http://localhost:3001', // If your backend API routes don't have /api prefix
      // With options:
      '/api': {
        target: 'http://localhost:5001', // Your backend server
        changeOrigin: true,
        // rewrite: (path) => path.replace(/^\/api/, '') // Uncomment if your backend API routes don't have /api prefix
      },
    },
  },
})