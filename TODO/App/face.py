import functions
import time

# or you could ------ import function
Greet = time.strftime('%A ''%w ''%B ''%Y ' ' - ''%H'':''%M')
print('Date:', Greet)
while True:
    user_action = input('Type add, show, edit, completed or cut:  ')
    user_action = user_action.strip()

    if user_action:
        if user_action.startswith('add'):
            todo = user_action[4:] + '\n'

            todos = functions.get_t()

            todos.append(todo)

            functions.write_t(todos)

        elif user_action.startswith('show'):
            todos = functions.get_t('todos2.txt')

            for i, item in enumerate(todos):
                item = item.strip('\n')
                row = f'{i + 1} - {item}'
                print(row)

        elif user_action.startswith('completed'):
            try:
                todos = functions.get_t()

                number = int(user_action[9:])
                n = number - 1
                removing = todos[n].strip(
                    '\n')  # remove the selected number UI from the todos list, slap this all in removing
                todos.pop(n)

                functions.write_t('todos2.txt', todos)

                mess = f'{removing} was removed from the list'
                print(mess)
            except IndexError:
                print('you are out of range')

        elif user_action.startswith('edit'):
            try:
                number = int(user_action[5:])
                # L = f'{user_action[5:]} is being replaced'
                # print(L)
                number = number - 1

                todos = functions.get_t()

                new_todo = input('enter new todo')
                todos[number] = new_todo + '\n'

                # mess = f'{new_todo}  has been replaced'
                # print(mess)
                functions.write_t(todos)
            except ValueError:
                print('command invalid')
                continue
            except IndexError:
                print('you are out of range')
                continue

        elif user_action.startswith('cut'):

            print('fuck off')
            break
        else:
            print('user input was invalid')
