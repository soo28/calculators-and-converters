# unit_converter_gui.py
import tkinter as tk
from tkinter import ttk, messagebox


def convert_length(value, from_unit, to_unit):
    factors = {
        "m": 1.0,
        "km": 1000.0,
        "cm": 0.01,
        "mm": 0.001,
        "mi": 1609.34,
        "ft": 0.3048,
        "in": 0.0254,
    }
    return value * factors[from_unit] / factors[to_unit]


def convert_mass(value, from_unit, to_unit):
    factors = {
        "kg": 1.0,
        "g": 0.001,
        "mg": 0.000001,
        "lb": 0.453592,
        "oz": 0.0283495,
    }
    return value * factors[from_unit] / factors[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    if from_unit == "F":
        value = (value - 32) * 5 / 9
    elif from_unit == "K":
        value -= 273.15

    if to_unit == "F":
        return value * 9 / 5 + 32
    elif to_unit == "K":
        return value + 273.15

    return value


CONVERTERS = {
    "Length": (convert_length, ["m", "km", "cm", "mm", "mi", "ft", "in"]),
    "Mass": (convert_mass, ["kg", "g", "mg", "lb", "oz"]),
    "Temperature": (convert_temperature, ["C", "F", "K"]),
}


class UnitConverterGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Unit Converter")
        self.resizable(False, False)

        self.category = tk.StringVar(value="Length")
        self.from_unit = tk.StringVar()
        self.to_unit = tk.StringVar()
        self.value = tk.StringVar()
        self.result = tk.StringVar(value="Result")

        self._build_ui()
        self._update_units()

    def _build_ui(self):
        ttk.Label(self, text="Category").grid(row=0, column=0, padx=8, pady=5)
        ttk.OptionMenu(
            self, self.category, self.category.get(),
            *CONVERTERS.keys(), command=lambda _: self._update_units()
        ).grid(row=0, column=1, padx=8, pady=5)

        ttk.Label(self, text="Value").grid(row=1, column=0, padx=8, pady=5)
        ttk.Entry(self, textvariable=self.value).grid(row=1, column=1, padx=8, pady=5)

        ttk.Label(self, text="From").grid(row=2, column=0, padx=8, pady=5)
        self.from_menu = ttk.OptionMenu(self, self.from_unit, "")
        self.from_menu.grid(row=2, column=1, padx=8, pady=5)

        ttk.Label(self, text="To").grid(row=3, column=0, padx=8, pady=5)
        self.to_menu = ttk.OptionMenu(self, self.to_unit, "")
        self.to_menu.grid(row=3, column=1, padx=8, pady=5)

        ttk.Button(self, text="Convert", command=self._convert).grid(
            row=4, column=0, columnspan=2, pady=10
        )

        ttk.Label(self, textvariable=self.result, font=("Segoe UI", 10, "bold")).grid(
            row=5, column=0, columnspan=2, pady=5
        )

    def _update_units(self):
        _, units = CONVERTERS[self.category.get()]

        self.from_unit.set(units[0])
        self.to_unit.set(units[1] if len(units) > 1 else units[0])

        self.from_menu["menu"].delete(0, "end")
        self.to_menu["menu"].delete(0, "end")

        for unit in units:
            self.from_menu["menu"].add_command(
                label=unit, command=lambda u=unit: self.from_unit.set(u)
            )
            self.to_menu["menu"].add_command(
                label=unit, command=lambda u=unit: self.to_unit.set(u)
            )

    def _convert(self):
        try:
            value = float(self.value.get())
            func, _ = CONVERTERS[self.category.get()]
            result = func(value, self.from_unit.get(), self.to_unit.get())
            self.result.set(f"Result: {result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    app = UnitConverterGUI()
    app.mainloop()
