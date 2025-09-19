def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) >= 6:
        del list_to_remove_elements[5] #tomar los indices como variables y restarles uno o eliminar de atras para adelante para que sea mas facil
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
    elif len(list_to_remove_elements) == 5:
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
    elif len(list_to_remove_elements) > 0 and len(list_to_remove_elements) <=5:
        del list_to_remove_elements[0]
    elif len(list_to_remove_elements) == 0:
        return list_to_remove_elements
    return list_to_remove_elements

def add_elements(list_to_add_elements):
    list_to_add_elements.append("Yellow")
    list_to_add_elements.insert(0, "Pink")
    return list_to_add_elements


def is_empty(list_to_check):
    if len(list_to_check) == 0:
        return True
    elif len(list_to_check) > 0:
        return False

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) < 3 and len(list_to_compare2) < 3:
        return False
    elif len(list_to_compare1) < 3 and len(list_to_compare2) >= 3 or len(list_to_compare1) >= 3 and len(list_to_compare2) < 3:
        return False
    elif len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
        else:
            return False

def list_of_lists(list_of_lists_to_modify):
    list_of_lists_to_modify[0] = list_of_lists_to_modify[0][:2]
    list_of_lists_to_modify[1] = list_of_lists_to_modify[1][1:4]
    list_of_lists_to_modify[2] = list_of_lists_to_modify[2][-2:]
    return list_of_lists_to_modify