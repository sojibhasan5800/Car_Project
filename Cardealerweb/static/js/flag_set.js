
  // Country Flag Update Script

document.addEventListener("DOMContentLoaded", function () {
    const select = document.querySelector(".country-flag-select");
    console.log(100);

    function updateFlag() {
      const countryCode = select.value.toLowerCase();
      const flagUrl = `/static/img/flags/${countryCode}.svg`;
      const defaultFlag = `/static/img/flags/default.jpeg`;

      const img = new Image();
      img.onload = function () {
        select.style.backgroundImage = `url('${flagUrl}')`;
        
      };
      img.onerror = function () {
        select.style.backgroundImage = `url('${defaultFlag}')`;
      };
      img.src = flagUrl;
    }

    if (select) {
      select.addEventListener("change", updateFlag);
      updateFlag(); // initial load
    }
  });