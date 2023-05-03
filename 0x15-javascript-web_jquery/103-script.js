//script that fetches and prints how to say “Hello”

$(document).ready(() => {
  const url = 'https://www.fourtonfish.com/hellosalut/';
  const langInput = $('#language_code');
  const translateBtn = $('#btn_translate');
  const helloDiv = $('#hello');

  function getTranslation() {
    const langCode = langInput.val();
    $.get(`${url}?lang=${langCode}`, (data) => {
      helloDiv.text(data.hello);
    });
  }

  translateBtn.click(getTranslation);
  langInput.keypress((event) => {
    if (event.keyCode === 13) {
      getTranslation();
    }
  });
});

