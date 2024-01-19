FILEPATH = "todos3.txt"
def get_t(filepath=FILEPATH):
    '''opens and reads the filepath in this case todos2 and thes stores in varianble in this
    case file_l. then stores in todos_l then returns the content
    '''
    try:
        with open(filepath, 'r') as file_l:
            todos_l = file_l.readlines()
        return todos_l

    except FileNotFoundError as e:
        print(f"problem with{e}")                   #With this modification, if the file specified in filepath does not exist, the function will catch the
        print(f"problem{filepath}")                    # FileNotFoundError, print information about the error, and return None.
        return None

def write_t(todos_a, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_a)


print(f'{__name__} Has been imported')
if __name__ == '__main__':
    print('running directly from functions yessir ')
