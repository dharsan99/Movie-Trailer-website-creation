import media
import fresh_tomatoes


# Instances of the class Movie with corresponding details.
transformers = media.Movie("Transformers",
                           "Alien robots accidentally crash landing on Earth.",
                           "https://s-media-cache-ak0.pinimg.com/736x/59/12/0f/59120f2a65fd05a78d9d450039a85a58--movies--movies-free.jpg",  # noqa
                           "https://www.youtube.com/watch?v=sgnO5fO46pE")

inception = media.Movie("Inception",
                        "Adventures within a dream.",
                        "http://cdn.collider.com/wp-content/uploads/Inception-movie-poster-3.jpg",  # noqa
                        "https://www.youtube.com/watch?v=M7O44CUIRYU")

pacific_rim = media.Movie("Pacific Rim",
                          "Clash beteween giant robots and Aliens",
                          "https://vignette1.wikia.nocookie.net/pacificrim/images/2/2f/Postery07h.jpg/revision/latest?cb=20140119115505",  # noqa
                          "https://www.youtube.com/watch?v=5guMumPFBag")

interstellar = media.Movie("Interstellar",
                           "4 Astronauts in search of an alternate planet",
                           "http://i.imgur.com/7Du30vM.jpg",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

john_wick = media.Movie("John Wick",
                        "John avenges the death of his dog and stolen car.",
                        "https://s-media-cache-ak0.pinimg.com/originals/d6/c5/f2/d6c5f268943bf8836a83d41df3cc7c6b.jpg",  # noqa
                        "https://www.youtube.com/watch?v=l1g0fn5Nm_g")

bat_vs_sup = media.Movie("Batman vs. Superman",
                         "Nail biting clash between batman nad Superman.",
                         "https://s-media-cache-ak0.pinimg.com/originals/37/93/ce/3793ceb2327983a8046b8977a5f46d0f.jpg",  # noqa
                         "https://www.youtube.com/watch?v=wAcbTd8Nd70")


hobbit = media.Movie("Hobbit: Battle of the five armies",
                     "Epic clash between Dwarves, Elves and Orcs.",
                     "https://s-media-cache-ak0.pinimg.com/originals/b0/1a/63/b01a63af5a78af52a0573fe492521708.jpg",  # noqa
                     "https://www.youtube.com/watch?v=MqsVr7Q3iug")

tomorrow = media.Movie("Edge of Tomorrow",
                       "Clever escape from an Alien invasion.",
                       "http://www.jhdierking.com/wp-content/uploads/2015/03/limanEdgeofTomorrow2014.jpg",  # noqa
                       "https://www.youtube.com/watch?v=MX1c1gJsXsE")

kong = media.Movie("Kong: Skull island",
                   "A group of poeple venture out into Kong island.",
                   "http://img02.deviantart.net/7818/i/2016/206/d/d/kong__skull_island__movie_poster__by_blantonl98-dabasb6.jpg",  # noqa
                   "https://www.youtube.com/watch?v=RAnc0uWLKyk")

# list of movies
movies = [transformers, pacific_rim, inception, interstellar, john_wick,
          bat_vs_sup, hobbit, tomorrow, kong]

# calling open_movies_page function from fresh_tomatoes.
fresh_tomatoes.open_movies_page(movies)
