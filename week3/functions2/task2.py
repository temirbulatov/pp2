def good_movies_list(movies):
    return [movie.get('name') for movie in movies if movie.get('imdb', 0) > 5.5]


movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
}]

good_movies = good_movies_list(movies)
print("Good movies:", good_movies)