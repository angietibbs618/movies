import fresh_tomatoes
import movie

fifty_shades_of_grey = movie.Movie("Fifty Shades of Grey",
                                   "An unconventional Love story",
                                   "https://en.wikipedia.org/wiki/Fifty_Shades_of_Grey#/media/File:50ShadesofGreyCoverArt.jpg",
                                   "https://www.youtube.com/watch?v=SfZWFDs0LxA")
#print(fifty_shades_of_grey.storyline)
#fifty_shades_of_grey.show_trailer()

fifty_shades_darker = movie.Movie("Fifty Shades Darker",
                                  "part two of the Love story",
                                  "http://t0.gstatic.com/images?q=tbn:ANd9GcTm7vaHWXiIkfKAWAwrxRGyfZFCLQ1tVPIVnyQYVUfV74fwws5P",
                                  "https://www.youtube.com/watch?v=qAxK-SYF1eQ")

fifty_shades_freed = movie.Movie("Fifty Shades Freed",
                                 "part three and conclusion of the Love story",
                                 "https://en.wikipedia.org/wiki/Fifty_Shades_Freed#/media/File:Fifty_Shades_Freed_book_cover.png",
                                 "https://www.youtube.com/watch?v=G6iSUyEcbNA")

passangers = movie.Movie("Passangers",
                         "futuristic love story",
                         "https://www.google.com/imgres?imgurl=http://t3.gstatic.com/images%3Fq%3Dtbn:ANd9GcQvqid_rbEby5j_XkVnSdwWgvSTiX9Np1I6iTJPJWYZFCBOPe4w&imgrefurl=http://t3.gstatic.com/images%3Fq%3Dtbn:ANd9GcQvqid_rbEby5j_XkVnSdwWgvSTiX9Np1I6iTJPJWYZFCBOPe4w&h=1080&w=720&tbnid=x3aQMqMYRVywAM:&tbnh=160&tbnw=106&usg=__5g69vhjE-PtzlErW1NttG2LAUqs=&vet=10ahUKEwiS4uqTgpvTAhXKOSYKHWBYDH0Q_B0IsgEwHQ..i&docid=CDoCwoKQ5cNsqM&itg=1&sa=X&sqi=2&ved=0ahUKEwiS4uqTgpvTAhXKOSYKHWBYDH0Q_B0IsgEwHQ#spf=1",
                         "https://www.youtube.com/watch?v=32DGC0dyWRY")

hunger_games = movie.Movie("Hunger Games",
                           "real life survival game",
                           "https://www.bing.com/images/search?view=detailV2&ccid=XwmOd7VD&id=031D890A735028FA10A7BF725823716F9E7AAD4A&q=movie+posters+hunger+games&simid=608028643107604053&selectedIndex=11&qft=+filterui%3aimagesize-small&ajaxhist=0",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

step_brothers = movie.Movie("Step Brothers",
                            "40 year old men still living at home become step brothers",
                            "https://en.wikipedia.org/wiki/Step_Brothers_(film)#/media/File:StepbrothersMP08.jpg",
                            "https://www.youtube.com/watch?v=_0TWeOrIYVI")

                          
movies = [fifty_shades_of_grey, fifty_shades_darker, fifty_shades_freed, passangers, hunger_games, step_brothers]
fresh_tomatoes.open_movies_page(movies)
#print (movie.Movie.valid_ratings)
#print(movie.Movie.__doc__)
