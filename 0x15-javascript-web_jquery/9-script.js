$.ajax(
  {
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    type: 'GET',
    dataType: 'json',
    success: function (response) { $('#hello').text(response.hello); }
  }
);
