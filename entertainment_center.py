import fresh_tomatoes
import media
# Code for Star Wars VII
star_wars = media.Movie("Star Wars the Force Awakens",
                        "A science fiction story of a war a long time ag\
                        o in a galaxy far away",
                        "https://upload.wikimedia.org/wikipedia/commons/2/20/Star_Wars_The_Force_Awakens_Norwegian_poster.jpg", # noqa
                        "https://www.youtube.com/watch?v=sGbxmsDFVnE")
# code for GOTG
Guardians_of_The_Galaxy = media.Movie("Guardians of the Galaxy", "A grou\
p of disfunctional people becoming heros",
                          "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg", # noqa
                          "https://www.youtube.com/watch?v=B16Bo47KS2g")
# code for mad max
mad_max = media.Movie("Mad Max", "A really good car chase",
                           "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg", # noqa
                           "https://www.youtube.com/watch?v=jOZQZOVToDI")
# code to organize and call the movies listed above
movies = [star_wars,mad_max, Guardians_of_The_Galaxy]
fresh_tomatoes.open_movies_page(movies)
