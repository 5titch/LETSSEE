def get_t(filepath='todos2.txt'):
    '''opens and reads the filepath in this case todos2 and thes stores in varianble in this
    case file_l. then stores in todos_l then returns the content
    '''
    with open(filepath, 'r') as file_l:
        todos_l = file_l.readlines()
    return todos_l


def write_t(todos_a, filepath='todos2.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos_a)


print(f'{__name__} Has been imported')
if __name__ == '__main__':
    print('running directly from functions')
