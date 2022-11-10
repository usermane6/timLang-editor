import tkinter as tk
import timInterpreter as tm

# ----------- Setup ----------
window = tk.Tk()
window.geometry("1200x750")
window.title("Tim")

file_name = tk.StringVar()
default_file = "tim"
# ------------ Functions ------------

def retrieve_code():
    input = input_txt.get("1.0", "end-1c")
    return input

def get_file(mode : str):
    name = file_txt.get()
    path = "timLang editor/scripts/" + name + ".tim"
    file = open(path, mode)
    return file, path

def load():
    file, path = get_file("r")
    file = file.read()
    input_txt.delete("1.0", "end")
    input_txt.insert("1.0", file)

def save():
    file, path = get_file("w")
    new_code = retrieve_code()
    file.write(new_code)

def run():
    file, path = get_file("r")
    tm.run(path)

# ------------ Elements ------------

input_txt = tk.Text(window, height = 40,
                width = 100,
                bg = "light yellow")

save_btn = tk.Button(window, height = 2,
                width = 20,
                text ="Save",
                command = save)

run_btn = tk.Button(window, height = 2,
                width = 20,
                text = "Run!",
                command = run)

load_btn = tk.Button(window, height = 2, 
                width = 20,
                text = "Load",
                command=load)

file_lbl = tk.Label(window, text="\nFile Name:", height=2)
file_txt = tk.Entry(window, textvariable = file_name)

file_txt.insert(1, default_file)
# ------------ displaying ------------ 
input_txt.grid(row=1, rowspan=150, 
            column=1)

save_btn.grid(row=1, column=2)

load_btn.grid(row=2, column=2)

run_btn.grid(row=3, column=2)

file_lbl.grid(row=1, column=3, padx=100)
file_txt.grid(row=2, column=3, padx=100)

load()
window.mainloop()