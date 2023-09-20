var app = new Vue({
  el: "#app",
  delimiters: ["[[", "]]"],
  data: {
    message: "Bonjour",
    name: "nn",
    email: "",
    lastName: "",
    gender: "",
    numCountries: 0,
  },
  methods: {
    addTod() {
      aler("hey");
    },
  },
});
