import functions
import PySimpleGUI as sg
label = sg.Text("Type in a to-do")
input_box =sg.InputText(tooltip="Enter todo")
a_button = sg.Button("Add")


window = sg.Window('To-Do app', layout=[[label], [input_box, a_button]])
window.read()
print("hello")
window.close()




