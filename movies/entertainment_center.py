# import relevant files from movies directory
import media
import fresh_tomatoes

# instantiate seven Movie objects using the Movie()
# from the media file
the_fast_and_the_furious = media.Movie("The Fast and the Furious",
                        "A young cop attempts to take down a speed-racing\
                        criminal gang",
                        "http://ia.media-imdb.com/images/M/MV5BMjAwNTQ0Nzc2M15BMl5BanBnXkFtZTcwNTk1MDIwNA@@._V1_SX640_SY720_.jpg",
                        "https://www.youtube.com/watch?v=2TAOizOnNPo")

two_fast_two_furious = media.Movie("2 Fast 2 Furious",
                     "A young cop and his friend go after a drug dealer with\
                     fast cars",
                     "https://upload.wikimedia.org/wikipedia/en/9/9d/Two_fast_two_furious_ver5.jpg",
                     "https://www.youtube.com/watch?v=F_VIM03DXWI")

fast_and_furious = media.Movie("Fast and Furious",
                             "A former crime family goes after a\
                             Mexican cartel",
                             "https://upload.wikimedia.org/wikipedia/en/8/8f/Fast_and_Furious_Poster.jpg",
                             "https://www.youtube.com/watch?v=k98tBkRsGl4")

fast_and_furious_five = media.Movie("Fast and Furious 5",
                          "A former crime family goes after a\
                          Colombian drug lord",
                          "https://s-media-cache-ak0.pinimg.com/736x/e5/f7/e7/e5f7e7645aa51751e12d74830f1c2c35.jpg",
                          "https://www.youtube.com/watch?v=tPZfa7bZzF4")

fast_and_furious_six = media.Movie("Fast and Furious 6",
                                "A former crime gang teams up with the\
                                police to fight against a British terrorist",
                                "https://upload.wikimedia.org/wikipedia/en/f/fd/FastandFurious6-teaserposter.jpg",
                                "https://www.youtube.com/watch?v=PP7pH4pqC5A")

fast_and_furious_seven = media.Movie("Fast and Furious 7",
                           "A former crime gang teams up with the\
                           police to fight against a British terrorist's brother",
                           "http://tiffanyyong.com/wp-content/uploads/2015/04/fast7-poster.jpg",
                           "https://www.youtube.com/watch?v=Skpu5HaVkOc")

# create a movies array with the Movie() objects in it
movies = [the_fast_and_the_furious, two_fast_two_furious, fast_and_furious, fast_and_furious_five, fast_and_furious_six, fast_and_furious_seven]

# implement the open_movies_page function from the
# fresh_tomatoes file. This will create a HTML page
# with our titles, poster and movie trailers
fresh_tomatoes.open_movies_page(movies)


