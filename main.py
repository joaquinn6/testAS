'''Modulo de principal'''
from utils import string_to_json, valid_format
from horizontal_chart import HorizontalChart
from vertical_chart import VerticalChart


def generate_bar_code(str_json: str):
  '''
  Función que transforma un string con formato json
  en una bar-chart en consola
  Argumentos:
  str_json: (str) Recibe el str_json en formato string
  '''

  try:
    data = string_to_json(str_json)
    if not valid_format(data):
      print('Formato de datos incorrecto')
      return

    horizontal_chart = HorizontalChart(data)
    horizontal_chart.draw()

    vertical_chart = VerticalChart(data)
    vertical_chart.draw()

    return
  except Exception as exc:
    print(exc.args[0])


print('Ingrese un json valido:')
string_json = input()
'{ "enero": 15.5, "febrero": 16.8, "marzo": -18.5,"abril": "-22.4", "mayo": 5, "junio": 74.8, "julio": 58.8, "agosto": 2.9, "septiembre":15.3, "octubre": 33.4, "noviembre": 12.9, "diciembre": 1}'

generate_bar_code(string_json)
