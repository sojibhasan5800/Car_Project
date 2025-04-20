
  document.addEventListener("DOMContentLoaded", function () {
    const select = $(".select-country-with-flag"); // jQuery is needed for Select2
    const flag = document.getElementById("country-flag");

    // Enable select2 with search bar
    select.select2({
      placeholder: "Select your country",
      width: '100%'
    });

    function updateFlag() {
      const countryCode = select.val()?.toLowerCase();
      if (countryCode) {
        flag.src = `/static/img/flags/${countryCode}.svg`;
      } else {
        flag.src = `/static/img/flags/default.png`;
      }
    }

    select.on("change", updateFlag);
    updateFlag();
  });

