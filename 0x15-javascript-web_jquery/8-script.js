$.getJSON('https://swapi.co/api/films/?format=json', function(data){
  let result = data.results
  for (let i in result) {
    $('UL#list_movies').append('<li>' + result[i].title + '</li>');
  };
});
