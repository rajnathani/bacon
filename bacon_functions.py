def strip_roman_numeral(s):
    '''Return a new string containing all the substrings of string 's' from
    the beginning till the index of the occurence of '(*roman numeral*)'.
    If no roman numerals are present then return the original string.
    '''

    # Check for the first occurence of "("
    # If its present then return a new string
    # containing all the substrings till "("
    if s.find("(") != - 1:
        numeral_start = s.find("(")
        new_string = s[:numeral_start]
        return new_string
        # If no "(" is present then return the
    # original string.
    return s


def extract_actor_name(line):
    '''Return a string containing the actor's name from the string 'line'.
    '''

    comma = line.find(",")
    # If a comma is present then rearrange the first and last name.
    if comma == -1:
        # Distinguish between the end of the actor's name and
        # beginning of the movie's name by finding the tab
        actor_end = line.find("\t")
        full_name = line[:actor_end]
        full_name = strip_roman_numeral(full_name).strip()

    # If a comma is not present then don't reorder the name.
    else:
        last_name = line[:comma].strip()
        # Distinguish between the end of the actor's name and
        # beginning of the movie's name by finding the tab
        actor_end = line.find("\t")
        first_name = line[comma + 2:actor_end]
        first_name = strip_roman_numeral(first_name).strip()
        full_name = first_name + " " + last_name

    # Capitalize the full name of the actor and then return it.    
    actor_full_name = capitalize_name(full_name)
    return actor_full_name


def capitalize_name(s):
    '''Return a new string with all the substrings from string 's' followed
    by whitespace uppercased, and the rest of the substrings lowercased
    and with all leading and trailing whitespace removed.
    Note: First substring to be uppercased.
    '''

    s = s.strip()
    space_location = 0
    new_string = ""
    count = 0
    # Loop through each substring.
    for substring in s:
        if count < len(s):
            # Check if the previous substring is whitespace, or that
            # the we are dealing with the very first subsring. If it is
            # true then uppercase the substring that follows it and add
            # it to the new string.
            previous = s[count - 1]
            if previous == "\t" or previous == " " or count == 0:
                new_string += substring.upper()
            # If its not whitespace then lowercase the substring
            # and add it to the new string.
            else:
                new_string += substring.lower()
        count += 1
    return new_string.strip()


def find_movie_name(line):
    '''Return the contents of the string 'line' which contains the movie name.
    '''

    # Find the occurence of a tab and mark that as
    # the beginning of the movie name.
    # Find the occurence of a closing parentheses
    # and mark that as the end of the movie name.
    tab = line.find("\t")
    end = line.find(")", tab)
    movie = line[tab + 1: end + 1].strip()
    return movie


def parse_actor_data(actor_data):
    '''Return the actor & movie information in the open reader 'actor_data'.
    ('actor_data' contains movie and actor information in IMDB's format.)
    The returned dictionary contains the names of actors (string) as keys and
    lists of movies (string) the actor has been in as values.
    '''

    actor_dict = {}
    count = 0
    header_skipped = False
    passed_heading = False
    line_break = True
    line = actor_data.readline()
    # Iterate till the footer of the file.
    while not header_skipped or not (line_break and line.startswith("-------")):

        if not header_skipped:
            if line.startswith('THE ACTORS LIST') or line.startswith('THE ACTRESSES LIST'):
                passed_heading = True
            elif line.startswith('Name'):
                line_name = count
            # Check if 'Name' And the line with hyphens are
            # consecutive.
            elif line.count("-") == 10 and count == (line_name + 1):
                if passed_heading:
                    header_skipped = True
        elif line_break and not (line.isspace()):

            # Check if the previous line was a line break.
            # Note: For the first actor this condition is set to
            # be True.
            line_break = False
            actor_full_name = extract_actor_name(line)
            # Get the movie's name which is on the same line with the actor's
            # name. If the actor doesn't exist in the actor_dict then add
            # the actor's name to the dictionary with the first movie's name
            # as a list. If the actor already exists in the dictionary then
            # append the movie to the list of movies to which actor maps onto
            # in the dictionary.
            movie = find_movie_name(line)
            if not (actor_full_name) in actor_dict:
                actor_dict[actor_full_name] = [movie]
            else:
                actor_dict[actor_full_name].append(movie)
            line = actor_data.readline()
            # As long as there is no line break, keep appending the movies
            # found on each line to the actor's list of movies.
            while not (line.isspace()):
                if line.startswith("\t"):
                    movie = find_movie_name(line)
                    # Check if the movie is not present in the list
                    # of movies of the actor.
                    if not (movie in actor_dict[actor_full_name]):
                        actor_dict[actor_full_name].append(movie)
                line = actor_data.readline()
            line_break = True
        line = actor_data.readline()
        count += 1
    return actor_dict


def invert_actor_dict(actor_dict):
    '''Return a dictionary that is the inverse of dictionary 'actor_dict'.
    The original actor_dict maps actors (string) to lists of movies (string)
    in which they have appeared. The returned dictionary maps movies (string)
    to lists of actors (string) appearing in the movie.
    '''

    inverted = {}
    # Iterate through the dictionary 'actor_dict', check if
    # the movie in the list of movies of the actor has occured
    # in the dictionary 'movie_dict'. If it hasn't then add the
    # movie to 'movie_dict' (as a key) and the actor to it.
    # Else append the actor to the list of the already existing
    # movie key.
    for (actor, movies) in actor_dict.iteritems():
        for movie in movies:
            if not (movie in inverted):
                inverted[movie] = [actor]
            else:
                # Check if the actor is not the list.
                if not (actor in inverted[movie]):
                    inverted[movie].append(actor)
    return inverted


def directly_linked_movie(actor, goal_actor, actor_dict, movie_dict):
    '''Return the movie (a string) which directly links 'actor' (string to
    'goal_actor' (string), from dictionaries: 'actor_dict' and 'movie_dict'.
    Return None if no common movie is found.
    '''

    # Loop through the movies which 'actor' has acted in.
    # Check if 'goal_actor' occurs in the actor list of
    # any of the movies.
    for movie in actor_dict[actor]:
        if goal_actor in movie_dict[movie]:
            return movie


def shortest_link(actor_name, actor_dict, movie_dict):
    '''Return a list of actors (actors are strings)that represents the shortest
    connection between 'actor_name' and Kevin Bacon that can be found in the
    dictionaries: 'actor_dict' and 'movie_dict'.
    '''

    # Note about the algorithm:
    # Type: Breadth first

    # First, check if the actor's name is 'Kevin Bacon' or if the actor is
    # not present in the 'actor_dict'. If either of them if True
    # then return the empty list.
    if actor_name == 'Kevin Bacon' or not (actor_name in actor_dict):
        return []
    investigated = [actor_name]
    to_investigate = [[actor_name]]
    distance = 0
    # The loop condition checks if the list to_investigate has any remaining
    # elements.
    while to_investigate:
        # Note: As the distance increases the size of each sublist in
        # the nested list 'to_investigate' increases proportionally.
        # The last actor of each sublist is the actor to be investigated
        # The actors which occur before the actor in the sublist simply
        # represent the link from 'actor_name' to that actor.
        # Loop property: The zeroth index changes on every iteration.
        actor_link = to_investigate[0]
        actor = actor_link[distance]

        for movie in actor_dict[actor]:
            for co_star in movie_dict[movie]:
                if not (co_star in investigated):
                    if co_star == "Kevin Bacon":
                        actor_link.append("Kevin Bacon")
                        return actor_link
                    # If the co_star is not present in the list of
                    # investigated actors then make a list containing
                    # the entire link from 'actor_name' to the co_star
                    # and add it to the nested list 'to_investigate'.
                    elif not (co_star in investigated):
                        investigated.append(co_star)
                        full_link = actor_link[:]
                        full_link.append(co_star)
                        to_investigate.append(full_link)
                        # Remove the actor_link (sublist) from the
            # to_investigate (nested list)
        to_investigate.remove(actor_link)
        # Check if all the actor_links of the current distance
        # number is investigated. If that's True then increase
        # the distance by 1.
        if minimum(to_investigate) == distance + 2:
            distance += 1
    return []


def minimum(L):
    '''Return the length of the smallest sublist in then nested list 'L'.
    '''

    # Initiate smallest as 'z' as any number is smaller than it.
    smallest = 'z'
    for sublist in L:
        smallest = min(smallest, len(sublist))
    return smallest


def find_connection(actor_name, actor_dict, movie_dict):
    '''Return a list of (movie, actor) tuples (both elements of type string)
    that represent a shortest connection between 'actor_name' and 'Kevin Bacon'
    that can be found in the actor_dict and movie_dict. Each tuple in the
    returned list has a special property: the actor from the previous tuple and 
    the actor from the current tuple both appeared in the stated movie. If there
    is no connection between 'actor_name' and 'Kevin Bacon', or the 'actor_name'
    is 'Kevin Bacon', the returned list is empty. Note: The actor_dict is the
    inverse of movie_dict.
    '''

    # The shortest_link function will return the shortest link
    # of actors from 'actor_name' to 'Kevin Bacon'.
    # If there is no connection found or 'actor_name' is
    # 'Kevin Bacon' then it will return an empty list.
    link = shortest_link(actor_name, actor_dict, movie_dict)
    if not link:
        return link
    count = 0
    complete_link = []
    # Loop through the the list 'link' and find the common movie between
    # adjacent actors in the list. Store the common movie and the leading
    # actor as a tuple in the list 'complete_link'.
    for actor in link:
        if count > 0:
            present_actor = link[count]
            previous_actor = link[count - 1]
            common_movie = directly_linked_movie(previous_actor, present_actor, actor_dict, movie_dict)
            movie_actor_tuple = (common_movie, present_actor)
            complete_link.append(movie_actor_tuple)
        count += 1
    return complete_link