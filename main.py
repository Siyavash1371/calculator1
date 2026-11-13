from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.metrics import sp

ALLOWED = set("0123456789+-*/.() ")


class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.display = TextInput(
            font_size=sp(40), readonly=True, halign="right",
            multiline=False, size_hint=(1, 0.2),
        )
        self.add_widget(self.display)

        grid = GridLayout(cols=4, spacing=5, padding=5, size_hint=(1, 0.8))
        keys = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "C", "<", "Siya", "porali",
        ]
        for key in keys:
            btn = Button(text=key, font_size=sp(20))
            btn.bind(on_press=self.on_press)
            grid.add_widget(btn)
        self.add_widget(grid)

    def on_press(self, button):
        key = button.text
        if key == "C":
            self.display.text = ""
        elif key == "<":
            self.display.text = self.display.text[:-1]
        elif key == "=":
            self.calculate()
        else:
            self.display.text += key

    def calculate(self):
        expr = self.display.text
        try:
            if not expr or not set(expr) <= ALLOWED:
                raise ValueError
            result = eval(expr)
            self.display.text = str(result)
        except ZeroDivisionError:
            self.display.text = "Div by 0"
        except Exception:
            self.display.text = "Error"


class CalculatorApp(App):
    def build(self):
        return Calculator()


CalculatorApp().run()
