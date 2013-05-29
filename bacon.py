import cPickle

import bacon_functions


if __name__ == "__main__":
    # Loading the pickled data structure of actors to movies
    print 'Loading the pickled data structure of actors to movies ...'
    with open('actors_to_movies') as pickled_actors_to_movies:
        actors_to_movies = cPickle.load(pickled_actors_to_movies)
    # Loading the pickled data structure of actors to movies
    print 'Loading the pickled data structure of movies to actors' \
          ' ...'
    with open('movies_to_actors') as pickled_movies_to_actors:
        movies_to_actors = cPickle.load(pickled_movies_to_actors)

    largest = 0
    bacon_number = 0
    while bacon_number != - 1:
        actor_name = raw_input("Please enter an actor (or press return to exit): ")
        actor_name = bacon_functions.capitalize_name(actor_name)
        if actor_name == "Kevin Bacon":
            print "Kevin Bacon has a Bacon Number of 0."
        elif actor_name == "":
            print "Thank you for playing! The largest Bacon Number you found was %d."%(largest)
            bacon_number = -1
        else:
            full_link = bacon_functions.find_connection(actor_name,actors_to_movies,movies_to_actors)
            # The length of the full link represents the distance for any
            # natural number except 0. For the case of 0, either the actor is
            # either 'Kevin Bacon' (already checked above) or the actor has
            # no connection with 'Kevin Bacon'.
            bacon_number = len(full_link)
            if not bacon_number:
                print "%s has a Bacon Number of Infinity." %(actor_name)
            else:
                print "%s has a Bacon Number of %d." %(actor_name,bacon_number)
                previous_actor = actor_name
                for sublink in full_link:
                    movie,actor = sublink
                    print "%s was in %s with %s."%(previous_actor,movie,actor)
                    previous_actor = actor
        # If the bacon number found for the actor is larger than any bacon
        # number found in the game so far, then assign variable largest
        # to the bacon number.
        if bacon_number > largest:
            largest = bacon_number
        print "\n",
