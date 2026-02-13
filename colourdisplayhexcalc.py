import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def clean_hex(value):
    value = value.strip().replace("#", "")
    if len(value) != 6:
        raise ValueError
    return value.upper()


def hex_to_rgb(hex_value):
    return (
        int(hex_value[0:2], 16),
        int(hex_value[2:4], 16),
        int(hex_value[4:6], 16),
    )


def rgb_to_hex(rgb):
    return "#{:02X}{:02X}{:02X}".format(*rgb)


def clamp(value):
    return max(0, min(255, value))


def calculate():
    try:
        hex1 = clean_hex(entry_hex1.get())
        hex2 = clean_hex(entry_hex2.get())
        operation = operation_var.get()

        r1, g1, b1 = hex_to_rgb(hex1)
        r2, g2, b2 = hex_to_rgb(hex2)

        if operation == "+":
            result = (r1 + r2, g1 + g2, b1 + b2)
        elif operation == "-":
            result = (r1 - r2, g1 - g2, b1 - b2)
        elif operation == "*":
            result = (
                int(r1 * r2 / 255),
                int(g1 * g2 / 255),
                int(b1 * b2 / 255),
            )
        elif operation == "/":
            result = (
                int(r1 / r2 * 255) if r2 != 0 else 0,
                int(g1 / g2 * 255) if g2 != 0 else 0,
                int(b1 / b2 * 255) if b2 != 0 else 0,
            )
        else:
            return

        # Clamp values
        result = tuple(clamp(v) for v in result)

        # Update outputs
        result_hex = rgb_to_hex(result)
        result_hex_var.set(result_hex)
        result_rgb_var.set(f"RGB: {result}")

        # Update color display
        color_display.config(bg=result_hex)

    except ValueError:
        messagebox.showerror("Invalid Input", "Enter valid 6-digit hex color codes.")


# Main window
root = tk.Tk()
root.title("Hex Color Calculator")
root.geometry("360x400")
root.resizable(False, False)

# Inputs
tk.Label(root, text="Hex Color 1 (#RRGGBB)").pack(pady=(10, 0))
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

tk.Label(root, text="Hex Color 2 (#RRGGBB)").pack(pady=(10, 0))
entry_hex2 = tk.Entry(root)
entry_hex2.pack()

# Calculate button
tk.Button(root, text="Calculate", command=calculate).pack(pady=15)

# Result display
tk.Label(root, text="Result Hex").pack()
result_hex_var = tk.StringVar()
tk.Label(root, textvariable=result_hex_var, font=("Arial", 12, "bold")).pack()

result_rgb_var = tk.StringVar()
tk.Label(root, textvariable=result_rgb_var).pack(pady=5)

# Color preview panel
tk.Label(root, text="Color Preview").pack(pady=(15, 5))
color_display = tk.Frame(root, width=200, height=100, bg="#FFFFFF", relief="sunken", borderwidth=2)
color_display.pack()

root.mainloop()
