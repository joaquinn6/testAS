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

    bars_tuples = make_tuples_percents(data)
    bars_draws = []
    for bar_tuple in bars_tuples:
      bars_draws.append(draw_vertical_bar(bar_tuple))
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
    bar_tuple = (item[0], percent_of(item[1], biggest_value))
    bars.append(bar_tuple)
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
  size_line = 12 if len(label) <= 10 else len(label) + 2

  bar_draw = [FwES(size_line, f' {label}')]
  if percent >= 10:
    lines = int(round(percent / 10, 0))
    for _ in range(lines):
      if is_positive:
        bar_draw.insert(0, FwES(size_line, ' .......... '))
      else:
        bar_draw.append(FwES(size_line, ' .......... '))
  points = int(round(percent % 10, 0))
  if points >= 1:
    line = ' '
    while points != 0:
      line = f'{line}.'
      points -= 1

    if is_positive:
      bar_draw.insert(0, FwES(size_line, line))
    else:
      bar_draw.append(FwES(size_line, line))
  if is_positive:
    bar_draw.insert(0, FwES(size_line, f' {percent}%'))
  else:
    bar_draw.append(FwES(size_line, f' -{percent}%'))
  bar_draw = fill_with_empty_lines(is_positive, bar_draw, size_line)
  return bar_draw


def fill_with_empty_lines(is_positive: bool, bar_draw: list, size_line: int):
  '''Rellena de caracteres vacíos el espacio sobrante
  Argumentos:
    is_positive: (bool) Booleano que me indica si se rellena hacia arriba o hacia abajo
    bar_draw: (list) Lista de strings que dibujan la barra.
    size_line: (int) tamaño que deben cubrir los espacios vacíos
  Devuelve:
    Una lista ordenada de como se imprimirá la barra con espacios
  '''
  size = len(bar_draw)
  if size != 12:
    for _ in range(12-size):
      if is_positive:
        bar_draw.insert(0, FwES(size_line, ''))
      else:
        bar_draw.append(FwES(size_line, ''))
  for _ in range(12) if is_positive else range(11):
    if is_positive:
      bar_draw.append(FwES(size_line, ''))
    else:
      bar_draw.insert(0, FwES(size_line, ''))

  return bar_draw


""" print('Ingrese un json valido:')
string_json = input() """
STRING_JSON = '{ "enero": 15.5, "febrero": 16.8, "marzo": -18.5,"abril": "-22.4", "mayo": 5, "junio": 74.8, "julio": 58.8, "agosto": 2.9, "septiembre":15.3, "octubre": 33.4, "noviembre": 12.9, "diciembre": 1}'
generate_bar_code(STRING_JSON)
