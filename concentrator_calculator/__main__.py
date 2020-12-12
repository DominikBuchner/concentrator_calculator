import PySimpleGUI as sg
import pandas as pd
import pkg_resources

data = pkg_resources.resource_filename(__name__, 'data/centrifuge_data.xlsx')

## main function to start the GUI
def main():
    ## collect data needed for gui computation
    gui_data = pd.read_excel(data)

    ## collect concentrator names
    infile = pd.ExcelFile(data)
    concentrator_types = infile.sheet_names
    infile.close()

    ## collect liquid types
    liquids = [column.split(' ')[0] for column in gui_data.columns.to_list()[2:]]

    ## collect temperatures
    temps = gui_data['Temperature [°C]'].unique()

    ## layout definition
    layout = [
    [sg.Frame(layout = [
    [sg.Radio(type, 'TYPE') for type in concentrator_types]],
    title = 'Select the type of concentrator')],
    [sg.Frame(layout = [
    [sg.Radio(liquid, 'LIQUID') for liquid in liquids]],
    title = 'Liquid to concentrate')],
    [sg.Frame(layout = [
    [sg.Radio('{} °C'.format(temp), 'TEMP') for temp in temps]],
    title = 'Select a temperature')],
    [sg.Frame(layout = [
    [sg.Text('Starting volume:'), sg.Spin([i for i in range(1, 2001)], size = (4, 1), key = 'STARTING_VOL')],
    [sg.Text('Desired volume:'), sg.Spin([i for i in range(1, 2001)], size = (4, 1), key = 'DESIRED_VOL')]

    ], title = 'test')]
    ]

    window = sg.Window('Concentrator calculator', layout)

    while True:
        event, values = window.read(timeout = 100)

        ## if x or exit are clicked, close the window
        if event == None or event == 'Exit':
            break

    window.close()

## run if called as a toplevel script
if __name__ == "__main__":
    main()
