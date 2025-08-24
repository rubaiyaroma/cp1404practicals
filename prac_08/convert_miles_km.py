from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERSION_FACTOR = 1.60934


class MilesConverterApp(App):
    output_text = StringProperty()


    def build(self):
        self.title = "Miles to Kilometres Converter"
        self.output_text = "0.0"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root


    def handle_calculate(self):
        miles = self.get_miles()
        km = miles * CONVERSION_FACTOR
        self.output_text = str(km)


    def handle_increment(self, change):
        miles = self.get_miles() + change
        self.root.ids.input_miles.text = str(miles)
        self.handle_calculate()


    def get_miles(self):
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0


MilesConverterApp().run()

