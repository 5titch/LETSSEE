import functions
import PySimpleGUI as sg
import time
sg.theme('LightBlue2')

timec = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box =sg.InputText(tooltip="Enter todo", key = "Inputbox")
list = sg.Listbox(values=functions.get_t(), key="Listbox", enable_events=True,
                  size=[45,10] )
a_button = sg.Button("Add", size=8)
e_button = sg.Button("Edit", size=8)
c_button = sg.Button("Complete", size=8)
ex_button = sg.Button("Exit", size=8)
LAYOUT = [[timec],[label],[input_box, a_button],[list, e_button,],[c_button],[ex_button]],


window = sg.Window('To-Do app', layout= LAYOUT, font=('helvetica', 11))


while True:
    event,values = window.read(timeout=100)
    window['clock'].update(value=time.strftime("%d %b %Y, %H:%M:%S"))
    print(1,event)
    print(2,values)    #VALUES IS THE DICTIONARY LETS NOT FORGET
    print(3,values['Listbox'])
    print(4, values['Inputbox'])

    match event:
        case 'Add':
           # if values['Inputbox'] == '\n' or '':
          #      sg.popup('enter a value')
           # else:
            todos = functions.get_t()
            newtodo = values['Inputbox'] + '\n'
            todos.append(newtodo)
            functions.write_t(todos)
            window['Listbox'].update(values=todos)#FIND LISTBOX THEN UPDATE whats inside in this case values todos
            window['Inputbox'].update(value='')
        case sg.WIN_CLOSED:
           break
        case 'Edit':
            try:
                tte = values['Listbox'][0] # gets the v of key LB with the i of 0
                new_todo = values['Inputbox'] # gets the value of IB
                todos = functions.get_t() # gets todos
                index = todos.index(tte) #  gets the i of tte
                todos[index] = new_todo # the index of tte is now = to the new todo
                functions.write_t(todos) #writes in todos
                window['Listbox'].update(values=todos) #updates
            except IndexError:
                sg.popup('select a value to edit')

        case 'Listbox':
            window['Inputbox'].update(value=values['Listbox'][0])
        case 'Complete':
            try:
                #my way will be coded out
                todos = functions.get_t()
                tc = values['Listbox'][0]
                # my way ---index = todos.index(tc)
                #my way ---todos.pop(index)
                todos.remove(tc)
                functions.write_t(todos)
                k = f'completed {tc} '
                sg.popup(k)
                window['Listbox'].update(values=todos)
                window['Inputbox'].update(value='')# possible to edit value as IP value was edited TO ''
            except IndexError:
                sg.popup('select completed value')
        case 'Exit':
            sg.popup('Fuck off')
            break




window.close()













