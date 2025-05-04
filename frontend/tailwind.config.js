// tailwind.config.js
import animate from 'tailwindcss-animate'
import { defineConfig } from 'tailwindcss/helpers'

export default defineConfig({
  darkMode: 'class',
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {},
  },
  plugins: [animate],
})
