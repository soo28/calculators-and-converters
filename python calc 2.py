import tkinter as tk


class Calculator8Bit:
    MAX_DIGITS = 9
    MAX_VALUE = 10**MAX_DIGITS - 1
    MIN_VALUE = -MAX_VALUE

    def __init__(self):
        self.reset()

    def reset(self):
        self.accumulator = 0
        self.current = 0
        self.operator = None
        self.new_input = True

    def _clamp(self, value: int) -> int:
        return max(self.MIN_VALUE, min(self.MAX_VALUE, value))

    def input_digit(self, digit: int):
        if self.new_input:
            self.current = digit
            self.new_input = False
        else:
            self.current = self._clamp(self.current * 10 + digit)

    def set_operator(self, op: str):
        if not self.new_input:
            self._compute()
        self.operator = op
        self.accumulator = self.current
        self.new_input = True

    def equals(self):
        self._compute()
        self.operator = None
        self.new_input = True

    def _compute(self):
        if self.operator is None:
            return

        a, b = self.accumulator, self.current

        if self.operator == "+":
            result = a + b
        elif self.operator == "-":
            result = a - b
        elif self.operator == "*":
            result = a * b
        elif self.operator == "/":
            result = 0 if b == 0 else int(a / b)

        self.current = self._clamp(result)

    def display(self) -> str:
        return str(self.current).rjust(self.MAX_DIGITS)


class CalculatorGUI:
    def __init__(self, root):
        self.calc = Calculator8Bit()
        self.root = root
        self.root.title("8-Bit Calculator")

        self.display = tk.Entry(
            root,
            font=("Courier", 20),
            justify="right",
            width=10,
            bd=5
        )
        self.display.grid(row=0, column=0, columnspan=4)
        self._update_display()

        self._build_buttons()

    def _build_buttons(self):
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]

        for text, row, col in buttons:
            tk.Button(
                self.root,
                text=text,
                width=5,
                height=2,
                command=lambda t=text: self._on_press(t)
            ).grid(row=row, column=col)

    def _on_press(self, key):
        if key.isdigit():
            self.calc.input_digit(int(key))
        elif key in "+-*/":
            self.calc.set_operator(key)
        elif key == "=":
            self.calc.equals()
        elif key == "C":
            self.calc.reset()

        self._update_display()

    def _update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.calc.display())


if __name__ == "__main__":
    root = tk.Tk()
    CalculatorGUI(root)
    root.mainloop()
