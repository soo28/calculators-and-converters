import tkinter as tk


class CurrencyConverter:
    def __init__(self):
        # Base currency: USD
        self.rates = {
            "USD": 1.0,
            "EUR": 0.92,
            "GBP": 0.78,
            "JPY": 155.0,
            "CAD": 1.36
        }

    def convert(self, amount: float, from_cur: str, to_cur: str) -> float:
        if from_cur not in self.rates or to_cur not in self.rates:
            raise ValueError("Unsupported currency")

        usd_amount = amount / self.rates[from_cur]
        return usd_amount * self.rates[to_cur]


class ConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        self.converter = CurrencyConverter()
        self.currencies = list(self.converter.rates.keys())

        self.amount_var = tk.StringVar(value="0")
        self.result_var = tk.StringVar(value="0.00")

        self.from_var = tk.StringVar(value="USD")
        self.to_var = tk.StringVar(value="EUR")

        self._build_ui()

    def _build_ui(self):
        tk.Label(self.root, text="Amount").grid(row=0, column=0, pady=5)
        tk.Entry(self.root, textvariable=self.amount_var, width=15).grid(row=0, column=1)

        tk.Label(self.root, text="From").grid(row=1, column=0)
        tk.OptionMenu(self.root, self.from_var, *self.currencies).grid(row=1, column=1)

        tk.Label(self.root, text="To").grid(row=2, column=0)
        tk.OptionMenu(self.root, s)
