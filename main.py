'''Modulo de principal'''
from utils import string_to_json, valid_format, higher_absolute_value, percent_of


def generate_bar_code():
  '''Función que espera una entrada json string de consola 
  he imprime un gráfico de barras igualmente en consola'''
  print('Ingrese un json valido:')
  string_json = input()
  try:
    data = string_to_json(string_json)
    if not valid_format(data):
      print('Formato de datos incorrecto')
      return

    bars = make_tuples_percents(data)
    print(bars)
  except Exception as exc:
    print(exc.args[0])


def make_tuples_percents(data: dict) -> list:
  '''Crea tuplas (etiqueta, porcentaje) a partir de un diccionario
    Argumentos:
      data: objeto de clave:valor donde valor es siempre un float
    Devuelve: Lista de tuplas con el valor convertido en porcentaje
  '''
  bars = []
  biggest_value = higher_absolute_value(data)
  for item in data.items():
    bar = (item[0], percent_of(item[1], biggest_value))
    bars.append(bar)
  return bars


generate_bar_code()
