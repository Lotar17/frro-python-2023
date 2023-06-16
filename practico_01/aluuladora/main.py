import kivy
from kivy.app import App
from kivy.core.text import LabelBase


class CalculadoraApp(App):


    def muestra_numero(self, scr, nmb):
        if (scr.text.startswith("0") and len(scr.text) < 2) or scr.text.startswith("ERROR"):
            scr.text = nmb.text
        else:
            scr.text += nmb.text

    def muestra_operador(self, scr, op):
        if scr.text[len(scr.text) - 1] in ["+", "-", "*", "/"]:
            if op.text == ".":
                scr.text += "0."
                return
            else:
                scr.text = scr.text[:len(scr.text) - 1]
        elif scr.text[len(scr.text) - 1] == ".":
            scr.text = scr.text[:len(scr.text) - 1]
        elif op.text == "." and not self.validar_puntos(scr.text):
            return
        scr.text += op.text

    def validar_puntos(self, text):
        c = 0
        for i in text[::-1]:
            if i == ".":
                c += 1
            elif i in ["+", "-", "*", "/"]:
                break

        return True if (c == 0) else False

    def borra_numero(self, scr):
        if not (scr.text[len(scr.text) - 1] in ["+", "-", "*", "/"]):
            c = 0
            for i in scr.text[::-1]:
                c += 1
                if i in ["+", "-", "*", "/"]:
                    scr.text = scr.text[:(len(scr.text) - c + 1)]
                    return
            scr.text = "0"

    def mostrar_resultado(self, scr):
        try:
            resultado = eval(scr.text)
            scr.text = str(resultado)
        except ZeroDivisionError:
            scr.text = "ERROR: DIVISION POR CERO"
        except SyntaxError:
            scr.text = "ERROR: SINTAXIS INVALIDA"
        except Exception as e:
            scr.text = "ERROR: " + str(e).upper()


if __name__ == "__main__":
    LabelBase.register(name='Calculator',
                       fn_regular=':~/repos/frro-python-2023/practico_01/fonts/casio-fx-9860gii.ttf')
    CalculadoraApp().run()
