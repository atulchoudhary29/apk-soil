from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import numpy as np

class MainScreen(Screen):
    pass

class PredictionScreen(Screen):
    def on_enter(self):
        # Create a random distribution and plot it
        data = np.random.randn(1000)
        plt.hist(data, bins=30)
        plt.title("Random Data Distribution")
        
        # Add the plot to the placeholder in the kv
        self.ids.plot_box.add_widget(FigureCanvasKivyAgg(plt.gcf()))

class MyApp(MDApp):

    def build(self):
        Builder.load_file('main.kv')
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(PredictionScreen(name='prediction'))
        sm.current = 'main'
        return sm

    def open_popup(self):
        btn1 = MDFlatButton(
            text="Camera",
            on_release=self.go_to_prediction
        )

        btn2 = MDFlatButton(
            text="Select From Gallery",
            on_release=self.go_to_prediction
        )

        content = BoxLayout(
            orientation='vertical',
            spacing='10dp',
            size_hint=(None, None),
            width="240dp"
        )
        content.add_widget(btn1)
        content.add_widget(btn2)

        self.dialog = MDDialog(
            title="Select from below",
            type="custom",
            content_cls=content,
            size_hint=(None, None),
            size=("280dp", "200dp")
        )

        self.dialog.open()

    def go_to_prediction(self, *args):
        self.root.current = 'prediction'
        self.dialog.dismiss()

if __name__ == "__main__":
    MyApp().run()
