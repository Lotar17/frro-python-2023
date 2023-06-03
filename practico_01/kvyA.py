import kivy
from kivy.app import App
status = 0
def muestraNumero(scrtext: str, nmbtext: str, status) :
    if status == 1:
        scrtext = nmbtext
        status = 0
    try:
        eval(scrtext+nmbtext)
    except:
        status = 1
    else:
        scrtext += nmbtext
class buttonApp(App):
    pass

if __name__ == '__main__':
    buttonApp().run()

