The "movies" directory contains four files:

 - fresh_tomatoes.py creates the and populates the fresh_tomatoes.html page which displays the finished product. fresh_tomatoes.py requires an input of a movie or movies object/s which will then be used to populate the page

 - media.py contains a class which can be instantiated to make movies

 - entertainment_center.py contains the instantiated movies from the media.py class. These movies are then placed into an array called movies

 - fresh_tomatoes.html is a file that is created when the open_movies_page within fresh_tomatoes.py is called with an input (in this case the movies array in entertainment_center.py)

Running the app:

 - The fresh_tomatoes.html has been created and, thus, to open the app all you need to do is open this file. 
 - You may also open the entertainment_center.py file in python idle and click run. This is possible because the open_movies_page from fresh_tomatoes.py is being called within entertainment_center.py and thus the fresh_tomatoes.html file is created and populated.