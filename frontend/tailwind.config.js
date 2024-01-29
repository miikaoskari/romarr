/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'primary-dark': '#151515',
        'secondary-dark': '#202020',
        'primary-light': '#f5f5f5',
      }
    },
  },
  plugins: [],
}

