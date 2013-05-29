import nose
import bacon_functions


# Helper Function.
def sort_dict_values(D):
    '''Sort all the values (lists) of dictionary 'D'
    in a non decreasing order.
    '''
    
    for value in D.values():
        value.sort()

def test_no_actor_movie_content():
    '''Test for a file without any movie/actor content.
    '''
    
    empty_actor_data = open("empty_actor_data.txt")
    
    assert bacon_functions.parse_actor_data(empty_actor_data) == {}, \
    'Test for basic structure of actor/movie content.'

def test_for_header():
    '''Test to check if the header is parsed correctly.
    '''
    
    header_actor_data = open("header_actor_data.txt")
    correct_dict = { 'George Petrie': ["A Fire in the Sky (1978)"] }
    
    sort_dict_values(correct_dict)
    program_output = bacon_functions.parse_actor_data(header_actor_data)
    sort_dict_values(program_output)

    assert program_output == correct_dict, \
    'Test for header of actor data'

def test_for_footer():
    '''Test to check if the footer is parsed correctly.
    '''
    
    footer_actor_data = open("footer_actor_data.txt")
    correct_dict = { 'Lucien Littlefield': ['A Blonde for a Night (1928)'] }
    
    sort_dict_values(correct_dict)
    program_output = bacon_functions.parse_actor_data(footer_actor_data)
    sort_dict_values(program_output)

    assert program_output == correct_dict, \
    'Test for footer of actor data'
    

def test_basic_actor_data():
    '''Test for a file with basic actor/movie content.
    '''
        
    basic_actor_data = open("basic_actor_data.txt")
    correct_dict = { 'Al Gore': ["'Hick' Town (2009)",
                    "Hillary! Uncensored: Banned by the Media (2008)",
                    "Johnny Cash's America (2008)",
                    "Journeys with George (2002)",
                    "Last Days on Earth (2006)"],
                    'Jon Langford': ["At Last, Okemah! (2009)",
                    "Cavedweller (2004)",
                    "Johnny Cash's America (2008)"] }
    
    sort_dict_values(correct_dict)
    program_output = bacon_functions.parse_actor_data(basic_actor_data)
    sort_dict_values(program_output)

    assert program_output == correct_dict, \
    'Test for basic structure of actor/movie content.'
    
    
def test_actor_with_roman_numerals():
    '''Test for actor data containing actor's name with roman numerals.
    '''
    
    roman_numeral_actor_data = open('roman_numeral_data.txt')
    correct_dict = { 'Joey Adams': ['Duress (2009)', '"Bones" (2005)',
                    '"Karen Sisco" (2003)', '"Law & Order" (1990)',
                    '"Numb3rs" (2005)'] }
    sort_dict_values(correct_dict)
    program_output = bacon_functions.parse_actor_data(roman_numeral_actor_data)
    sort_dict_values(program_output)

    assert program_output == correct_dict, \
    'Test for actor name with roman numerals.'
    
    
def test_multiple_actors():
    '''Test for actor data containing multiple actors with the same name.
    '''
    
    multiple_actor_data = open('multiple_actor_data.txt')
    correct_dict = { 'James Morrison': ['Return to Area 51 (2002)',
                    'The 32nd Annual TV Week Logie Awards (1990)',
                    'Bordellet (1972)'] }
    sort_dict_values(correct_dict)
    program_output = bacon_functions.parse_actor_data(multiple_actor_data)
    sort_dict_values(program_output)
    
    assert program_output == correct_dict, \
    "Test for multiple actors' names."
    
    
def test_no_comma_in_actor_name():
    '''Test for actor data containing actor's name without any commas.
    '''
    
    no_comma_actor_data = open('no_comma_actor_data.txt')
    correct_dict = { 'Elvis': ['Rubber Johnny (2005)'],
                     'Ll Cool J': ['10th Anniversary Essence Awards (1997)',
                     '17th Annual Screen Actors Guild Awards (2011)'] }
    sort_dict_values(correct_dict)
    program_output = bacon_functions.parse_actor_data(no_comma_actor_data)
    sort_dict_values(program_output)
    
    assert program_output == correct_dict, \
    'Test for actor names without commas.'
    
    
def test_for_middle_name_actors():
    '''Test for actor data containing actor's with middle names.
    '''
    
    middle_name_actor_data = open('middle_name_actor_data.txt')
    correct_dict = { 'Richard Dean Anderson': ['05 Spaceys (2005)',
                     '06 Spaceys (2006)'],
                     'Robert De Niro': ['Showtime (2002)',
                     'Sleepers (1996)'] }
    
    sort_dict_values(correct_dict)
    program_output = bacon_functions.parse_actor_data(middle_name_actor_data)
    sort_dict_values(program_output)
    
    assert program_output == correct_dict, \
    'Test for actors with middle names.'
    
    
def test_for_movie_spanning_multiple_lines():
    '''Test for actor data containing an actor with a movie spanning over
    multiple lines.
    '''
    
    spanning_movie_actor_data = open('spanning_movie_actor_data.txt')
    correct_dict = { 'Frankie Avalon': ['"Live Wednesday" (1978)',
                    '"Love, American Style" (1969)'],
                     'Stephen Baldwin': ['"Clerks" (2000)'],
                    'Jim Byrnes': ['The 53rd Annual Golden Globe Awards (1996)'] }
    
    sort_dict_values(correct_dict)
    program_output = bacon_functions.parse_actor_data(spanning_movie_actor_data)
    sort_dict_values(program_output)
    
    assert program_output == correct_dict, \
    'Test for actors with movie spanning multiple lines.'
    
    
def test_for_multiple_movies():
    '''Test for actor data containing an actor with multiple common movie names.
    '''
    
    multiple_movie_actor_data = open('multiple_movie_actor_data.txt')
    correct_dict = { 'George Petrie': ['A Fire in the Sky (1978)'] }
    
    sort_dict_values(correct_dict)
    program_output = bacon_functions.parse_actor_data(multiple_movie_actor_data)
    sort_dict_values(program_output)
    
    assert program_output == correct_dict, \
    'Test for actors with multiple common movie names.'
    

if __name__ == '__main__':
    nose.runmodule()