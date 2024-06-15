import tkinter as tk
def button_click(value):
  current = entry_display.get()
  entry_display.delete(0, tk.END)
  entry_display.insert(0, str(current) + str(value))
def clear_display():
  entry_display.delete(0, tk.END)
def calculate():
  try:
    result = eval(entry_display.get())
    entry_display.delete(0, tk.END)
    entry_display.insert(0,str(result))
  except Exception as e:
    entry_display.delete(0, tk.END)
    entry_display.insert(0, "Error")
# Create the main window
root = tk.Tk()
root.title("Calculator")
# Create and place GUI components
entry_display = tk.Entry(root, width=20, font=("Arial", 14))
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
# Buttons
buttons = [
'7', '8', '9', '/',
'4', '5', '6', '*',
'1', '2', '3', '-',
'0', '.', '00', '+']
row_val = 1
col_val = 0
for button in buttons:
  tk.Button(root, text=button, padx=20, pady=20,command=lambda b=button:button_click(b)).grid(row=row_val, column=col_val)
  col_val += 1
  if col_val > 3:
    col_val = 0
    row_val += 1
tk.Button(root, text="C", padx=20, pady=20,command=clear_display).grid(row=row_val, column=col_val)
# Equal button
col_val += 1
tk.Button(root, text="=", padx=20, pady=20,command=calculate).grid(row=row_val,column=col_val)
# Start the main loop
root.mainloop()
