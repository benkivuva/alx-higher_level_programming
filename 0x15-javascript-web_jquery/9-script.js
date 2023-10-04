$.ajax(
  {
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    type: 'GET',
    dataType: 'json',
    success: function (response) { $('#hello').text(response.hello); }
  }
);
