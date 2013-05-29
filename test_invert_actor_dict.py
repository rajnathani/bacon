import nose
import bacon_functions
from test_parse_actor_data import sort_dict_values 

def test_empty_dict():
    '''Test with an empty dictionary.
    '''
    
    program_output = bacon_functions.invert_actor_dict({})
    assert program_output == {},\
    'Empty dictionary test'
    
def test_empty_dict_value():
    '''Test with a single key dictionary mapping onto
    the empty list (value).
    '''
    
    program_output = bacon_functions.invert_actor_dict({'cake': []})
    assert program_output == {},\
    'Empty dictionary value test'
    
def test_single_key_single_value_dict():
    '''Test with a single key dictionary which is the
    empty string.
    '''
    
    program_output = bacon_functions.invert_actor_dict({'tart': ['sugar']})
    assert program_output == {'sugar': ['tart']},\
    'Empty string key (dictionary) test'
    
def test_single_key_multiple_values_dict():
    '''Test with a dictionary containing a single key, with multiple
    items in the list (value) which it maps to.
    '''
    
    program_output = bacon_functions.invert_actor_dict({'cake': ['icing','cherry']})
    correct_output = { 'icing': ['cake'], 'cherry': ['cake'] }
    assert program_output == correct_output,\
    'Single key multiple value list dictionary test'
    
def test_multiple_key_multiple_unique_values_dict():
    '''Test with a dictionary containing multiple keys, with multiple
    distinct items in the list (value) which they map to.
    '''
    
    D = { 'salad': ['lettuce','dressing','broccoli'], 'sandwich': [ 'ham', 'cheese'] }
    program_output = bacon_functions.invert_actor_dict(D)
    correct_output = { 'lettuce': ['salad'], 'dressing': ['salad'], 'broccoli':
                       ['salad'], 'ham': ['sandwich'], 'cheese': ['sandwich'] }
    
    assert program_output == correct_output,\
    'Multiple key multiple (distinct) value list dictionary test'
    
def test_multiple_key_multiple_overlapping_values_dict():
    '''Test with a dictionary containing multiple keys, with multiple
    overlapping items in the list (value) which they map to.
    '''
    
    D = { 'modern warfare': ['brutal','entertaining','addictive'],
          'angry birds': [ 'awesome', 'addictive'], 'counter-strike': ['brutal',
          'awesome','addictive','entertaining'] }
    program_output = bacon_functions.invert_actor_dict(D)
    correct_output = { 'awesome': ['angry birds','counter-strike'],
                       'brutal': ['counter-strike','modern warfare'],
                       'addictive': ['modern warfare','angry birds','counter-strike'],
                       'entertaining': ['counter-strike','modern warfare'] }
    sort_dict_values(program_output)
    sort_dict_values(correct_output)
    
    assert program_output == correct_output,\
    'Multiple key multiple (overlapping) value list dictionary test'
    
    
    
if __name__ == '__main__':
    nose.runmodule()
    
    
