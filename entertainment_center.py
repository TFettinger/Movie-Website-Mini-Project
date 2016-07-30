import fresh_tomatoes
import media
star_wars = media.Movie("Star Wars the Force Awakens",
                        "A science fiction story of a war a long time ago in a galaxy far away",
                        "https://upload.wikimedia.org/wikipedia/commons/2/20/Star_Wars_The_Force_Awakens_Norwegian_poster.jpg",
                        "https://www.youtube.com/watch?v=sGbxmsDFVnE")
Guardians_of_The_Galaxy = media.Movie("Guardians of the Galaxy", "A group of disfunctional people becoming heros",
                          "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
                          "https://www.youtube.com/watch?v=B16Bo47KS2g")

mad_max = media.Movie("Mad Max", "A really good car chase",
                           "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg",
                           "https://www.youtube.com/watch?v=jOZQZOVToDI")

movies = [star_wars,mad_max, Guardians_of_The_Galaxy]
fresh_tomatoes.open_movies_page(movies)
