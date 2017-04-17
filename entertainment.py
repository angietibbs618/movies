import fresh_tomatoes
import movie

#this is how i listed my fav movies including title trailer and synopsis 
fifty_shades_of_grey = movie.Movie("Fifty Shades of Grey",
                                   "An unconventional Love story",
                                   "http://www.tribute.ca/news/wp-content/uploads/2015/02/FiftyShadesofGrey.jpg",
                                   "https://www.youtube.com/watch?v=SfZWFDs0LxA")


fifty_shades_darker = movie.Movie("Fifty Shades Darker",
                                  "part two of the Love story",
                                  "http://t0.gstatic.com/images?q=tbn:ANd9GcTm7vaHWXiIkfKAWAwrxRGyfZFCLQ1tVPIVnyQYVUfV74fwws5P",
                                  "https://www.youtube.com/watch?v=qAxK-SYF1eQ")

fifty_shades_freed = movie.Movie("Fifty Shades Freed",
                                 "part three and conclusion of the Love story",
                                 "https://abeachbumslife.files.wordpress.com/2012/07/fiftyshadesfreed.jpg",
                                 "https://www.youtube.com/watch?v=G6iSUyEcbNA")

passangers = movie.Movie("Passangers",
                         "futuristic love story",
                         "http://www.sonypictures.com/movies/passengers/assets/images/onesheet.jpg",
                         "https://www.youtube.com/watch?v=32DGC0dyWRY")

hunger_games = movie.Movie("Hunger Games",
                           "real life survival game",
                           "http://ricmeyers.com/wp-content/ric-meyers-uploads/2012/03/the-hunger-games-movie-poster-24.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

step_brothers = movie.Movie("Step Brothers",
                            "40 year old men still living at home become step brothers",
                            "http://www.sonypictures.com/movies/stepbrothers/assets/images/onesheet.jpg",
                            "https://www.youtube.com/watch?v=_0TWeOrIYVI")
#below is an array of the movies and the fresh tomatoes info to run the page
                          
movies = [fifty_shades_of_grey, fifty_shades_darker, fifty_shades_freed,
passangers, hunger_games, step_brothers]
fresh_tomatoes.open_movies_page(movies)
#print (movie.Movie.valid_ratings)
#print(movie.Movie.__doc__)
