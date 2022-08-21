from typing import Text
import PySimpleGUI as sg
import pyautogui

"""Implements an auto clicker
   based on Clicking - OP Auto Clicker 3.0
"""

def setupLayout():
    """Setup the GUI layout

    Returns:
        _type_: _description_
    """
    tab1_layout=[ [sg.Input('0', size=(5,1), key='-HR-'), sg.Text('hours', expand_x=True), 
               sg.Input('0', size=(5,1), key='-MIN-'), sg.Text('mins', expand_x=True), 
               sg.Input('0', size=(5,1), key='-SEC-'), sg.Text('Sec', expand_x=True)] ]

    tab_group1_layout=[ [sg.Tab('Click Internal', tab1_layout, key='-TAB1-', visible=True)] ]


    tab2_layout=[ [sg.Text('Mouse button: ', key='-MOUSEBUTTON-'), 
                   sg.Combo(key='-WHICHBUTTON-', default_value='Left', values=['Left', 'Middle', 'Right'])],
                 [sg.Text('Click type: ', key='-CLICKTYPE-'), 
                  sg.Combo(key='-CLICKTYPE-', default_value='Single', values=['Single', 'Double'])] ]

    tab_group2_layout=[ [sg.Tab('Click Options', tab2_layout, key='-TAB2-', visible=True)] ]


    tab3_layout=[ [sg.Radio('Repeat', key='-REPEAT-', default=True, group_id=1), 
                   sg.Spin(initial_value=1, size=(3,1), values=list(range(1,101)), key='-REPEATCNT-')], 
                 [sg.Radio('Repeat until stopped', group_id=1, key='-REPEATUNTILSTOPPED-'), ]]
    tab_group3_layout=[ [sg.Tab('Click Repeat', tab3_layout, key='-TAB3-', visible=True)] ]

    
    tab4_layout=[ [sg.Radio('Current location', key='-CURRENTLOCATION-', default=True, group_id=2), 
                   sg.Radio('Pick location', key='-PICKLOCATION-', group_id=2),
                    sg.Text('X'), sg.Input('0', size=(4,1), key='-X-'), sg.Text('Y'), sg.Input('0', size=(4,1), key='-Y-')] ]
    tab_group4_layout=[ [sg.Tab('Cursor position', tab4_layout)] ]


    layout = [ [sg.TabGroup(tab_group1_layout, key='-TABGROUP1-', expand_x=True )],
              [sg.TabGroup(tab_group2_layout, key='-TABGROUP2-'), 
               sg.TabGroup(tab_group3_layout, key='-TABGROUP3-')], 
               [sg.TabGroup(tab_group4_layout, key='-TABGROUP4-')], 
               [ sg.Button('Start (F6)', expand_x=True, key='-START-'), 
                sg.Button('Stop (F6)', expand_x=True, key='-STOP') ],
               [ sg.Button('Hotkey setting', expand_x=True, key='-HOTKEY-', enable_events=True), 
                sg.Button('Record & Playback', expand_x=True )]]

    return sg.Window("HGL's Auto Clicker", layout)
    

#*** main ***
window = setupLayout() #setup the screen layout

while True:
    event, values = window.read()
    
    if event in (sg.WIN_CLOSED):
        break
    else:
        print(event,values)
    
window.close()