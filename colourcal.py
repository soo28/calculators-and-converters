import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def calculate():
    try:
        # Get inputs
        hex1 = entry_hex1.get().strip()
        hex2 = entry_hex2.get().strip()
        operation = operation_var.get()

        # Convert hex to int
        num1 = int(hex1, 16)
        num2 = int(hex2, 16)

        # Perform operation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 // num2
        else:
            return

        # Display results
        result_hex_var.set(hex(result).upper())
        result_dec_var.set(str(result))

    except ValueError:
        messagebox.showerror("Invalid Input", "Enter valid hexadecimal values.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Division by zero is not allowed.")


# Main window
root = tk.Tk()
root.title("Hex Code Calculator")
root.geometry("320x250")
root.resizable(False, False)

# Inputs
tk.Label(root, text="Hex Value 1").pack(pady=(10, 0))
entry_hex1 = tk.Entry(root)
entry_hex1.pack()

tk.Label(root, text="Operation").pack(pady=(10, 0))
operation_var = tk.StringVar(value="+")
operation_menu = ttk.Combobox(
    root,
    textvariable=operation_var,
    values=["+", "-", "*", "/"],
    state="readonly",
)
operation_menu.pack()

tk.Label(root, text="Hex Value 2").pack(pady=(10, 0))
entry_hex2 = tk.Entry(root)
entry_hex2.pack()

# Calculate button
tk.Button(root, text="Calculate", command=calculate).pack(pady=15)

# Results
tk.Label(root, text="Result (Hex)").pack()
result_hex_var = tk.StringVar()
tk.Label(root, textvariable=result_hex_var).pack()

tk.Label(root, text="Result (Decimal)").pack()
result_dec_var = tk.StringVar()
tk.Label(root, textvariable=result_dec_var).pack()

root.mainloop()
