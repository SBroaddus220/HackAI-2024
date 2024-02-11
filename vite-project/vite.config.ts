import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  base: './',
  plugins: [react()],
  build: {
    assetsDir: 'static',
  },
  server: {
    port: 3000,
    cors: true,
    proxy: {
      // Proxy /api requests to the Flask server. Remove /api from the request path for the server
      "/api": {
        target: "http://127.0.0.1:5000/",
        changeOrigin: true,
        secure: false,
        rewrite: (path) => path.replace(/^\/api/, ""),
      },
    },
  },
})
