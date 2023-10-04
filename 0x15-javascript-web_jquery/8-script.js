$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
  let films = data.results;
  films.forEach(film => {
    $('<li>' + film.title + '</li>').appendTo('#list_movies');
  });
});
