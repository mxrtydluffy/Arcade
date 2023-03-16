/** @type {import('tailwindcss').Config} */
module.exports = {
  content:
    ["./templates/**/*.{html,js}"],
  theme: {
    screens: {
      sm: '480px',
      md: '750px',
      lg: '970px'
    },
    extend: {},
  },
  plugins: [],
}
