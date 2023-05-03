//script that fetches and prints how to say “Hello”

$(document).ready(function() {
  $('#btn_translate').click(function() {
    let langCode = $('#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/?lang=' + langCode, function(data) {
      $('#hello').html(data.hello);
    });
  });
});

