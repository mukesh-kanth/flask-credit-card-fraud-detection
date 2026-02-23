document.addEventListener("DOMContentLoaded", () => {
  const btn = document.querySelector("button[type='submit']");
  btn.addEventListener("click", () => {
    btn.classList.add("btn-loading");
  });
});
