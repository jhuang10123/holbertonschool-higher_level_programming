$(function()
{
    $.getJSON('https://swapi.co/api/films/?format=json', function(data){
      let result = data.results
      for (let i in result) {
	$('UL#list_movies').append('<li>' + result[i].title + '</li>');
	};


      // let result = data.results
      // alert(result);

      // let items = [];
      // $.each(data, function(key, val) {
      // 	items.push('<li>' + val + '</li>');
      // 	});
      // alert(items);

  });
});
