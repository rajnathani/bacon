import cPickle

import bacon_functions


def pickle_dump(obj, file_name):
    f = open(file_name, 'w')
    cPickle.dump(obj, f)
    f.close()

if __name__ == "__main__":
    # Parsing file of actors (male)
    imdb_actors_file = open("actors.list")
    print 'Parsing file (actors.list) of actors (male) ...'
    actors_dict = bacon_functions.parse_actor_data(imdb_actors_file)
    imdb_actors_file.close()

    # Parsing file of actors (female)
    imdb_actresses_file = open("actresses.list")
    print 'Parsing file (actresses.list) of actresses (female) ...'
    actresses_dict = bacon_functions.parse_actor_data(imdb_actresses_file)
    imdb_actresses_file.close()

    # thanks for the quick reminder: http://stackoverflow.com/a/38990
    # Merging both the (actors to movies) data structures
    print 'Merging both the (actors to movies) data structures ...'
    actors_to_movies = dict(actors_dict.items() + actresses_dict.items())

    # Creating a movies to actors data structure
    print 'Creating a movies to actors data structure ...'
    movies_to_actors = bacon_functions.invert_actor_dict(actors_to_movies)

    # Pickling both the data structures
    # Pickling the actors to movies data structure
    print 'Pickling the actors to movies data structure ...'
    pickle_dump(actors_to_movies, 'actors_to_movies')
    # Pickling the actors to movies data structure
    print 'Pickling the actors to movies data structure ...'
    pickle_dump(movies_to_actors, 'movies_to_actors')

    print 'Done! Run bacon.py to begin playing!'