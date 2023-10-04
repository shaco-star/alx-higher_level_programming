$.get('https://swapi-api.alx-tools.com/api/films/?format=json',
  function (data, textStatus, jqXHR) {
    const movies = data.results;
    $.map(movies, function (movie) {
      $('#list_movies').append(`<li>${movie.title}</li>`);
    });
  }
);
