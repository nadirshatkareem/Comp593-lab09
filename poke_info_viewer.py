""" 
Description: 
  Graphical user interface that displays select information about a 
  user-specified Pokemon fetched from the PokeAPI 

Usage:
  python poke_info_viewer.py
"""
from tkinter import *
from tkinter import ttk
from poke_api import get_pokemon_info
from tkinter import messagebox

# Create the main window
root = Tk()
root.title("Pokemon Information")
root.resizable(False, False)
#root.geometry('590x300')

# TODO: Create the frames
frame_input =  ttk.Frame(root)
frame_input.grid(rows=0, column=0, columnspan=2, pady=(20,10))

frame_info = ttk.LabelFrame(root, text="info")
frame_info.grid(row=1, column=0, padx=(20,10), pady=(10,20), sticky=N)

frame_stats = ttk.LabelFrame(root, text="stat")
frame_info.grid(row=1, column=1, padx=(10,20), pady=(10,20), sticky=N)

#populate the user input frame with widgets

label_name = ttk.Label(frame_input, text= "Pokemon Name:")
label_name.grid(row=0, column=0, padx=(10, 5), pady=(10))

enter_name = ttk.Entry(frame_input)
enter_name.insert(0,'mewtwo')
enter_name.grid(row=0, column=1)

def handle_button_get_info():
    poke_name = enter_name.get().strip()
    if poke_name == '': return
    poke_info = get_pokemon_info(poke_name)
    if poke_info :
        label_height_value['text'] = str(poke_info('height')) + ' dm' 
        label_weight_value['text'] = str(poke_info('weight')) + ' hg' 
        types_list = [t['type']['name'].capitalize() for t in poke_info['types']]
        label_type_val['text'] = ','.join(types_list)
        

    else:
        err_msg = f'unable to fetch information for {poke_name.capitalize()} from the poke API' 

button_get_info = ttk.Button(frame_input, text="get Info", command=handle_button_get_info)
button_get_info.grid(row=0, column=2, padx=10, pady=10)

# TODO: Populate the user input frame with widgets

label_height = ttk.Label(frame_info, text="height:")
label_height.grid(row=0, column=0, padx=(10,5), pady=(10,5), sticky=E)
label_height_value = ttk.Label(frame_info, width=20)
label_height_value.grid(row=1, column=1, padx=(0,10), pady=(10,5), sticky=W)

label_height = ttk.Label(frame_info, text="weight:")
label_height.grid(row=1, column=0, padx=(10,5), pady=(10,5), sticky=E)
label_height_value = ttk.Label(frame_info, width=20)
label_height_value.grid(row=1, column=1, padx=(0,10), pady=(10,5), sticky=W)


# TODO: Define button click event handler function


#stats fame, max value is 255 for all stat

STAT_MAX_VALUE = 255.0
PRG__BAR_LENGTH = 200
label_hp = ttk.Label(frame_stats, text="HP:")
label_hp.grid(row=0, column=0, padx=(10,5), sticky=E)
bar_hp = ttk.Progressbar(frame_stats, length= PRG__BAR_LENGTH, maximum=STAT_MAX_VALUE)
bar_hp.grid(row=0, column=1, padx=(0,10), pady=(10,5))

label_attack = ttk.Label(frame_stats, text="Attack:")
label_attack.grid(row=1, column=0, padx=(10,5), pady=5, stikcy=E)
bar_attack = ttk.Progressbar(frame_stats, length=PRG__BAR_LENGTH, maximum=STAT_MAX_VALUE)
bar_attack.grid(row=1, column=1, padx=(0,10), pady=5)

label_defense = ttk.Label(frame_stats, text="Defense")
label_defense.grid(row=2, column=0, )





root.mainloop()