'''Modulo de principal'''
from utils import (string_to_json, valid_format, higher_absolute_value,
                   percent_of, fill_with_empty_spaces as FwES)


def generate_bar_code(str_json: str):
  '''
  Función que transforma un string con formato json
  en una bar-char en consola
  Argumentos:
  str_json: (str) Recibe el str_json en formato string
  '''

  try:
    data = string_to_json(str_json)
    if not valid_format(data):
      print('Formato de datos incorrecto')
      return

    bars = make_tuples_percents(data)
    bars_draws = []
    for bar in bars:
      bars_draws.append(draw_vertical_bar(bar))
    for i in range(23):
      print(''.join(bar_draw[i-1] for bar_draw in bars_draws))

    return
  except Exception as exc:
    print(exc.args[0])


def make_tuples_percents(data: dict) -> list:
  '''Crea tuplas (etiqueta, porcentaje) a partir de un diccionario
    Argumentos:
      data: (dict) objeto de clave:valor donde valor es siempre un float
    Devuelve: (list) Lista de tuplas con el valor convertido en porcentaje
  '''
  bars = []
  biggest_value = higher_absolute_value(data)
  for item in data.items():
    bar = (item[0], percent_of(item[1], biggest_value))
    bars.append(bar)
  return bars


def draw_vertical_bar(bar_tuple: tuple) -> list:
  '''Crea un array para dibujar la gráfica de barra.
  Argumentos:
    bar_tuple: (tuple) EL primer valor es el nombre de la etiqueta de la barra
    y el 2do el porcentaje de la barra.
  Devuelve:
    Una lista ordenada de como se imprimirá la barra
  '''
  is_positive = bar_tuple[1] > 0
  label, percent = bar_tuple[0], abs(bar_tuple[1])
  bar_draw = [FwES(12, f' {label}')]
  if percent >= 10:
    lines = int(round(percent / 10, 0))
    for _ in range(lines):
      if is_positive:
        bar_draw.insert(0, ' .......... ')
      else:
        bar_draw.append(' .......... ')
  points = int(round(percent % 10, 0))
  if points >= 1:
    line = ' '
    while points != 0:
      line = f'{line}.'
      points -= 1

    if is_positive:
      bar_draw.insert(0, FwES(12, line))
    else:
      bar_draw.append(FwES(12, line))
  if is_positive:
    bar_draw.insert(0, FwES(12, f' {percent}%'))
  else:
    bar_draw.append(FwES(12, f' -{percent}%'))
  bar_draw = fill_with_empty_lines(is_positive, bar_draw)
  return bar_draw


def fill_with_empty_lines(is_positive: bool, bar_draw: list):
  '''Rellena de caracteres vacíos el espacio sobrante
  Argumentos:
    is_positive: (bool) Booleano que me indica si se rellena hacia arriba o hacia abajo
    bar_draw: (bool) Lista de strings que dibujan la barra.
  Devuelve:
    Una lista ordenada de como se imprimirá la barra con espacios
  '''
  size = len(bar_draw)
  if size != 12:
    for _ in range(12-size):
      if is_positive:
        bar_draw.insert(0, '            ')
      else:
        bar_draw.append('            ')
  for _ in range(12) if is_positive else range(11):
    if is_positive:
      bar_draw.append('            ')
    else:
      bar_draw.insert(0, '            ')

  return bar_draw


""" print('Ingrese un json valido:')
string_json = input() """
STRING_JSON = '{ "enero": 15.5, "febrero": 16.8, "marzo": -18.5,"abril": "-22.4", "mayo": 5, "junio": 74.8}'
generate_bar_code(STRING_JSON)
