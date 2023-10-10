def create_an_empty_list():
    return []

def create_four_element_list():
    # Create a list with four elements
    my_list = list(['apple', 42, True, 3.14])
    return my_list

def add_element_to_end_of_list(l, element):
    l.append(element)
    

def add_element_to_start_of_list(l, element):
    l.insert(0, element)

def remove_element_from_end_of_list(l):
    l.pop(l)

def remove_element_from_start_of_list(l):
    l.pop(0)

def retrieve_first_element_from_list(l):
    return l[0]

def retrieve_element_from_index(l, index):
    return l[index]

def retrieve_last_element_from_list(l):
    return l[-1]
