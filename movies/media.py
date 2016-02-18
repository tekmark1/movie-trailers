# import webbrowser from the python library
import webbrowser

# create a movie class with instance variables which
# include title, storyline, poster image, and youtube url.
# this class also contains an open webbrowser function
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
