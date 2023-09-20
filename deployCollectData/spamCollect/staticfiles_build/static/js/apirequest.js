const form = document.querySelector("#formQuestionnaire");
const urlsite = "http://127.0.0.1:8000/api/";
console.log("okay");
form.addEventListener("submit", (event) => {
  event.preventDefault();

  const formData = new FormData(event.target);

  console.log(formData);
  fetch(`${urlsite}/message/`, {
    method: "POST",
    body: formData,
  })
    .then((response) => {
      console.log(response);
    })
    .catch((error) => {
      console.error(error);
    });
});
