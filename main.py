from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):

  def build(self):
    self.title = 'ماشین حساب موبایل'
    layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

    # صفحه نمایش ماشین حساب
    self.solution = TextInput(
        multiline=False,
        readonly=True,
        font_size=122,
        halign='right',
        background_color=(0.95, 0.95, 0.95, 1),
    )
    layout.add_widget(self.solution)

    # چیدمان دکمه‌ها
    buttons = [
        ['7', '8', '9', '/'],
        ['4', '5', '6', '*'],
        ['1', '2', '3', '-'],
        ['C', '0', '=', '+'],
    ]

    for row in buttons:
      h_layout = BoxLayout(spacing=10)
      for label in row:
        button = Button(text=label, font_size=80)
        button.bind(on_press=self.on_button_press)
        h_layout.add_widget(button)
      layout.add_widget(h_layout)

    return layout

  def on_button_press(self, instance):
    text = instance.text
    current = self.solution.text

    if text == 'C':
      self.solution.text = ''
    elif text == '=':
      try:
        self.solution.text = str(eval(current))
      except Exception:
        self.solution.text = 'خطا'
    else:
      self.solution.text = current + text


if __name__ == '__main__':
  CalculatorApp().run()
