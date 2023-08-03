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
frame_input.grid(row=0, column=0, columnspan=2, pady=(20,10))

frame_info = ttk.LabelFrame(root, text="info")
frame_info.grid(row=1, column=0, padx=(20,10), pady=(10,20), sticky=N)

frame_stats = ttk.LabelFrame(root, text="stat")
frame_info.grid(row=1, column=1, padx=(10,20), pady=(10,20), sticky=N)

#populate the user input frame with widgets

label_name = ttk.Label(frame_input, text= "Pokemon Name:")
label_name.grid(row=0, column=0, padx=(10, 5), pady=10)

enter_name = ttk.Entry(frame_input)
enter_name.insert(0,'mewtwo')
enter_name.grid(row=0, column=1)

def handle_button_get_info():
    poke_name = enter_name.get().strip()
    if poke_name == '': return
    poke_info = get_pokemon_info(poke_name)
    if poke_info :
        label_height_value['text'] = str(poke_info['height']) + ' dm' 
        label_weight_value['text'] = str(poke_info['weight']) + ' hg' 
        types_list = [t['type']['name'].capitalize() for t in poke_info['types']]
        label_type_val['text'] = ','.join(types_list)
        bar_hp['value'] = poke_info['stats'][0]['base_stat']
        bar_attack['value'] = poke_info['stats'][1]['base_stat']
        bar_defense['value'] = poke_info['stats'][2]['base_stat']
        bar_special_attack['value'] = poke_info['stats'][3]['base_stat']
        bar_sepcial_defense['value'] = poke_info['stats'][4]['base_stat']
        bar_speed['value'] = poke_info['stats'][5]['base_stat']

    else:
        err_msg = f'unable to fetch information for {poke_name.capitalize()} from the poke API'
        messagebox.showinfo(title='Error', message=err_msg, icon='error')


button_get_info = ttk.Button(frame_input, text="Get Info", command=handle_button_get_info)
button_get_info.grid(row=0, column=2, padx=10, pady=10)

# TODO: Populate the user input frame with widgets

label_height = ttk.Label(frame_info, text="height:")
label_height.grid(row=0, column=0, padx=(10,5), pady=(10,5), sticky=E)
label_height_value = ttk.Label(frame_info, width=20)
label_height_value.grid(row=0, column=1, padx=(0,10), pady=(10,5), sticky=W)

label_weight = ttk.Label(frame_info, text="weight:")
label_weight.grid(row=1, column=0, padx=(10,5), pady=5, sticky=E)
label_weight_value = ttk.Label(frame_info, width=20)
label_weight_value.grid(row=1, column=1, padx=(0,10), pady=5, sticky=W)

label_type = ttk.Label(frame_info, text="Type:")
label_type.grid(row=2, column=0, padx=(10,5), pady=5, sticky=E)
label_type_value = ttk.Label(frame_info, width=20)
label_weight_value.grid(row=2, column=1, padx=(0,10), pady=5, sticky=W)


# TODO: Define button click event handler function


#stats fame, max value is 255 for all stat

STAT_MAX_VALUE = 255.0
PRG__BAR_LENGTH = 200
label_hp = ttk.Label(frame_stats, text="HP:")
label_hp.grid(row=0, column=0, padx=(10,5),pady=(10,5), sticky=E)
bar_hp = ttk.Progressbar(frame_stats, length= PRG__BAR_LENGTH, maximum=STAT_MAX_VALUE)
bar_hp.grid(row=0, column=1, padx=(0,10), pady=(10,5))

label_attack = ttk.Label(frame_stats, text="Attack:")
label_attack.grid(row=1, column=0, padx=(10,5), pady=5, sticky=E)
bar_attack = ttk.Progressbar(frame_stats, length=PRG__BAR_LENGTH, maximum=STAT_MAX_VALUE)
bar_attack.grid(row=1, column=1, padx=(0,10), pady=5)

label_defense = ttk.Label(frame_stats, text="Defense:")
label_defense.grid(row=2, column=0, padx=(10,5), pady=5, sticky=E)
bar_defense = ttk.Progressbar(frame_stats, length=PRG__BAR_LENGTH, maximum=STAT_MAX_VALUE)
bar_defense.grid(row=2, column=1, padx=(0,10), pady=5)

label_special_attack = ttk.Label(frame_stats, text="Special Attack:")
label_special_attack.grid(row=3, column=0, padx=(10,5), pady=5, sticky=E)
bar_special_attack = ttk.Progressbar(frame_stats, length=PRG__BAR_LENGTH, maximum=STAT_MAX_VALUE)
bar_special_attack.grid(row=3, column=1, padx=(0,10), pady=5)

label_special_defense = ttk.Label(frame_stats, text="Special Defense:")
label_special_defense.grid(row=4, column=0, padx=(10,5), pady=5, sticky=E)
bar_special_defense = ttk.Progressbar(frame_stats, length=PRG__BAR_LENGTH, maximum=STAT_MAX_VALUE)
bar_special_defense.grid(row=4, column=1, padx=(0,10), pady=5)

label_speed = ttk.Label(frame_stats, text="Speed:")
label_speed.grid(row=5, column=0, padx=(10,5), pady=(5,10), sticky=E)
bar_speed = ttk.Progressbar(frame_stats, length=PRG__BAR_LENGTH, maximum=STAT_MAX_VALUE)
bar_defense.grid(row=5, column=1, padx=(0,10), pady=(5,10))



root.mainloop()