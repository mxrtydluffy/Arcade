/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['/blog/templates/base.html'],
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
