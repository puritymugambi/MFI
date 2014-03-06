__author__ = 'purity'

def first(list):
    '''
    returns the first item of the list
    or an empty string if the list is empty
    '''

    try:
        return list[0]
    except IndexError:
        return ""

def remove_dash(string):
    return string.replace("-","")