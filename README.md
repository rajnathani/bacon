bacon
=====

Python implementation of the game 'Oracle of Bacon' using the IMDB repository of actors and actresses.

##What is 'Oracle of Bacon'?

Oracle of Bacon is a game where the goal is to find an actor/actress with the furthest movie distance
from the renowned actor Kevin Bacon. The game was created quite sometime ago and is available at
[www.oracleofbacon.org](http://www.oracleofbacon.org).

##Can you elaborate please?
The movie distance between any two actors is calculated by searching
for a connection between the actors with movies as the medium. For instance if Kevin Bacon acted in a movie A
with actor X, and actor X acted in movie B with actor Y, and assuming that are no actors besides Kevin Bacon,
actor X, and actor Y,  and also no other movies besides movie A and movie B (ofcourse this would be a highly
entertaining parallel universe), then Kevin Bacon has a movie distance of 1 from actor X, as they acted together
in the same movie (movie A) and Kevin Bacon has a movie distance of 2 from actor Y, in this case because the
connection which they share is 2 movies apart. This movie distance is also known as the given actor's 'bacon number'.
Now you might ask, what if there exists an actor (a really isolated one)
who bears no movie connection with the great and almighty Kevin Bacon? Well in that case the bacon number would be
infinite.

##So relfor what you trying to show us here?

Good question. One of the reasons I open sourced this work of mine is because I feel its exemplary for the concept of
*Breadth First Search* which is a part of *The Graph Theory*, a concept which is of great importance, its used highly in
many different fields like road planning, airline routing, and even game development. Therefore I thought I'd share this
great example of it to find distances between actors in the industry.

##The implementation

The language used: python
Actors and Movies data: thanks to the generosity of the IMDB corporation I've been able to use and parse the entire actors and movies database.
The data structures used: 2 pickled python dictionaries
- Actor to Movies relationship (one to many mapping)
- Movie to Actors relationship (one to many mapping)
The above 2 pickled dictionaries have already been created and are loaded in the repository.

##About the parsing and creation of the pickled data structures
To improve efficiency, and not have the program parse the actors and movies files everytime on loading
I've created a separate program called *make_bacon.py* which on running parses the following two files
- actors.list (male actors to their respective movies)
- actresses.list (female actors to their respective movies)
and created a common merged data structure for actors (both male and female) to movies, alongwith an inverted
data structure which is movies to actors. After the creation of these two vital data structures I've pickled (using cPickle)
them into two separate files which in turn can be loaded back into python dictionaries as those were before, from bacon.py, and used for the game.

##Can I run make_bacon.py?
In order to give you a better picture of the parsing of the IMDB files (in case you would also give a go at it) I've included
make_bacon.py
But now that brings us to an important question : 'Can I run it?'
My original intent was to let you able to run it straight away. However I decided against including the original IMDB files which
make_bacon.py parses as due to their not so surprisingly super massive size (around 0.6 gb for the male file, and 0.3 gb
for the actresses file) I wouldn't want to super load my repository which as been kindly provided to me by GitHub free of cost.
Instead if you would like to run make_bacon.py you can download the files from the IMDB website and place it in the main
directory of the cloned version of this repository and run it (make_bacon.py) Please be aware that you would need a bucket
of popcorn or a supercomputer to get through the processing time of this program in a breeze.


##Its not my data, please don't sue me!
I dedicate this section to explicitly let everyone know that the data which represents the entire recorded history of actors
and movies with their relationship DOES NOT belong to me. The rightful owner is the IMDB Corporation. They have aggregated
this amazing and useful amount of data and have ownership of the data. Once again I am not the rightful owner of the original source data.
