document.addEventListener("DOMContentLoaded", function () {
  const select = $(".select-country-with-flag");
  const flag = document.getElementById("country-flag");

  function formatCountry(country) {
    if (!country.id) return country.text;
    const code = country.id.toLowerCase();
    const img = $('<img>', {
      src: `/static/img/flags/${code}.svg`
    });
    const span = $('<span>').text(` ${country.text}`);
    return $('<span>').append(img).append(span);
  }

  select.select2({
    placeholder: "Select your country",
    width: '100%',
    templateResult: formatCountry,
    templateSelection: formatCountry,
    escapeMarkup: function (markup) {
      return markup;
    }
  });

  function updateFlag() {
    const countryCode = select.val()?.toLowerCase();
    if (countryCode) {
      flag.src = `/static/img/flags/${countryCode}.svg`;
    } else {
      flag.src = `/static/img/flags/default.jpeg`;
    }
  }

  select.on("change", updateFlag);
  updateFlag();
});
