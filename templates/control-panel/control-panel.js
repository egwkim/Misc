// Add an event listener to all input elements in control panel

const settingInputs = document.querySelectorAll('#control-panel input');

settingInputs.forEach((item) => {
  item.addEventListener("change", () => {
    // Do something
  });
});