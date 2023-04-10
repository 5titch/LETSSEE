import functions
import PySimpleGUI as sg
label = sg.Text("Type in a to-do")
input_box =sg.InputText(tooltip="Enter todo", key = "Inputbox")
list = sg.Listbox(values=functions.get_t(), key="Listbox", enable_events=True,
                  size=[45,10] )
a_button = sg.Button("Add")
e_button = sg.Button("Edit")



window = sg.Window('To-Do app', layout=[[label],
        [input_box, a_button],[list, e_button]], font=('helvetica', 11))


while True:
    event,values = window.read()
    print(1,event)
    print(2,values)    #VALUES IS THE DICTIONARY LETS NOT FORGET
    print(3,values['Listbox'])

    match event:
        case 'Add':
            todos = functions.get_t()
            newtodo = values['Inputbox'] + '\n'
            todos.append(newtodo)
            functions.write_t(todos)
            window['Listbox'].update(values=todos)
        case sg.WIN_CLOSED:
           break
        case 'Edit':
            tte = values['Listbox'][0] # gets the v of key LB with the i of 0
            new_todo = values['Inputbox'] # gets the value of IB
            todos = functions.get_t() # gets todos
            index = todos.index(tte) #  gets the i of tte
            todos[index] = new_todo # the index of tte is now = to the new todo
            functions.write_t(todos) #writes in todos
            window['Listbox'].update(values=todos) #updates
        case 'Listbox':
            window['Inputbox'].update(value=values['Listbox'][0])



window.close()

