bacon
=====

Python implementation of the game 'Oracle of Bacon' using the IMDB data of actors and movies.

###What is 'Oracle of Bacon'?

Oracle of Bacon (aka 6 degrees of Bacon) is a game where the goal is to find an actor/actress with the furthest movie distance
from the renowned actor Kevin Bacon. The game was created quite sometime ago and is available at
[www.oracleofbacon.org](http://www.oracleofbacon.org). Google recently integrated 6 degrees of Bacon into its
search results, to use it all you would have to do is type '< actor's name > bacon number' as a search query. 

###Can you elaborate please?
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

###So relfor what you trying to show us here?

Good question. One of the reasons I open sourced this work of mine is because I feel its exemplary for the concept of
*Breadth First Search* which is a part of *The Graph Theory*, a concept which is of great importance, its used highly in
many different fields like road planning, airline routing, and even game development. Therefore I thought I'd share this
great example of it to find distances between actors in the industry.

###Visualizing the problem with graphs
In order to solve the problem we are going to need a form of abstraction. The dataset of actors and movies alongwith their
relationship can be viewed as a graph, where the *nodes represent actors* and *movies represent edges*.
To find the closest connection between Kevin Bacon and the user inputted actor we can perform a *breadth first search*
beginning at the node representing Kevin Bacon, till we reach the node representing the user inputted actor. By performing
the search breadth first as opposed to depth first we are guarenteed to obtain the shortest path, and this is regardless
of whether the given path is unique. More about this at [http://ocw.mit.edu/courses/sloan-school-of-management/15-082j-network-optimization-fall-2010/lecture-notes/MIT15_082JF10_lec03.pdf](http://ocw.mit.edu/courses/sloan-school-of-management/15-082j-network-optimization-fall-2010/lecture-notes/MIT15_082JF10_lec03.pdf).

###About the Implementation

The language used: python  
Actors and Movies data: thanks to the generosity of the IMDB corporation I've been able to use and parse the entire actors and movies database.
The data structures used: 2 pickled python dictionaries
- Actor to Movies relationship (one to many mapping)
- Movie to Actors relationship (one to many mapping)
The above 2 pickled dictionaries have already been created and are loaded in the repository.

###About the parsing and creation of the pickled data structures
To improve efficiency, and not have the program parse the actors and movies files everytime on loading
I've created a separate program called *make_bacon.py* which on running parses the following two files
- actors.list (male actors to their respective movies)
- actresses.list (female actors to their respective movies)
and created a common merged data structure for actors (both male and female) to movies, alongwith an inverted
data structure which is movies to actors. After the creation of these two vital data structures I've pickled (using cPickle)
them into two separate files which in turn can be loaded back into python dictionaries as those were before, from bacon.py, and used for the game.

###How exactly do I get started?
The repository contains a python file name *bacon.py*, run this with python.  
If git & python are present in your path/environment variables, issue the following commands in your terminal:

    git clone https://github.com/relfor/bacon
    cd bacon
    python bacon.py
    
After which there will be a few second wait (while the program is unpickling the data structures from their respective files)
the following will be displayed:  

    Loading the pickled data structure of actors to movies ...
    Loading the pickled data structure of movies to actors ...
    Please enter an actor (or press return to exit): brad pitt
    Brad Pitt has a Bacon Number of 1.
    Brad Pitt was in Beyond All Boundaries (2009) with Kevin Bacon.
  
This program has been created in purpose of better explaining the graph theory, since that is the main priority
a couple of restrictions have been lifted from the parsing. The first is that if there exists multiple actors sharing
the same name, the actor is counted as one. Second is that parantheses will not occur within the movie names.

###TV Shows are included!
The almighty great IMDB data includes more than just movies, it includes tv  shows as well, this would include award
shows, reality shows and almost everything else you can watch on TV. Therefore the average bacon number found would
actually be lesser as TV shows serve as an additional medium for connection.

###Is my machine good enough to run this program?
This brings us to a really important aspect of the program. As the two data structures of actors to movies, and movies to actors
are loaded by the program in memory (as dictionaries), roughly around 1.9 GB of RAM is occupied by the program. Thus having
a machine with a memory of atleast 4 GB is highly recommended here.


###Can I run make_bacon.py?
In order to give you a better picture of the parsing of the IMDB files (in case you would also give a go at it) I've included
make_bacon.py
But now that brings us to an important question : 'Can I run it?'
My original intent was to let you able to run it straight away. However I decided against including the original IMDB files which
make_bacon.py parses as due to their not so surprisingly super massive size (around 0.6 gb for the male file, and 0.3 gb
for the actresses file) I wouldn't want to super load my repository which as been kindly provided to me by GitHub free of cost.
Instead if you would like to run make_bacon.py you can download the files from the IMDB website and place it in the main
directory of the cloned version of this repository and run it (make_bacon.py) Please be aware that you would need a bucket
of popcorn or a supercomputer to get through the processing time of this program in a breeze.


###Movie and Actors Data Source (please don't sue me!)
I dedicate this section to explicitly let everyone know that the data which represents the entire recorded history of actors
and movies with their relationship DOES NOT belong to me. The rightful owner is the IMDB Corporation. They have aggregated
this amazing and useful amount of data and have ownership of the data. Once again I am not the rightful owner of the original source data.
