import tkinter as tk
from orderPlacing import PlaceOrders
from downloadsymbol import LoadSymbol


def button_click(button_num):
    placeOrder = PlaceOrders()
    loadStrike = LoadSymbol()
    qty = int(text_input.get("0.0", tk.END))
    sl = int(text_input1.get("0.0", tk.END))
    strike = str(text_input2.get("0.0", tk.END))
    if button_num==1:
        response = placeOrder.placeOrder("B", qty)
        response=response+"\n"+placeOrder.placeOrder("SL", qty, sl)
    elif button_num==2:
        response = placeOrder.placeOrder("S", qty)
    elif button_num==3:
        response = placeOrder.placeOrder("SL", qty, sl)
    elif button_num==4:
        response = placeOrder.placeOrder("MSL", qty, sl)
    if button_num==5:
        response= loadStrike.downloadStrikeData(strike)
    output_text.insert(tk.END, f"{response}\n")

# Create the main window
root = tk.Tk()
root.grid_columnconfigure(0, weight=1 )
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=1)
root.title("Angel order placing")

# Define the buttons
button1 = tk.Button(root, text="BUY", command=lambda: button_click(1), height=1, width=3)
button2 = tk.Button(root, text="SELL", command=lambda: button_click(2), height=1, width=3)
button3 = tk.Button(root, text="SL", command=lambda: button_click(3), height=1, width=3)
button4 = tk.Button(root, text="Modify SL", command=lambda: button_click(4), height=1, width=5)
button5 = tk.Button(root, text="Load Strike", command=lambda: button_click(5), height=1, width=6)
text_input = tk.Text(root, height=2, width=6)
text_input1 = tk.Text(root, height=2, width=6)
text_input2 = tk.Text(root, height=2, width=30)

# Create the output text box
output_text = tk.Text(root, width=40, height=10)

# Place the buttons and text box in the window using the grid layout manager
button1.grid(row=0, column=0, padx=5, pady=5)
button2.grid(row=0, column=1, padx=5, pady=5)
button3.grid(row=0, column=2, padx=5, pady=5)
button4.grid(row=0, column=3, padx=5, pady=5)
button5.grid(row=0, column=4, padx=5, pady=5)
text_input.grid(row=0, column=5, padx=5, pady=5)
text_input1.grid(row=0, column=6, padx=5, pady=5)
text_input2.grid(row=0, column=7, padx=5, pady=5)
output_text.grid(row=1, columnspan=8, sticky='snew')

text_input.insert("1.0", "1")
text_input1.insert("1.0", "10")
text_input2.insert("1.0", PlaceOrders.getCurrentSymbol())


# Start the GUI event loop
root.mainloop()