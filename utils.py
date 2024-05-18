'''Modulo de utilidades'''
import json


def string_to_json(json_string: str) -> dict:
  '''Recibe un json en formato string y lo transforma en un diccionario
  Argumentos:
    json_string: (str) Json en formato string
  Devuelve:
    Un diccionario a partir del json_string
  '''
  try:
    json_object = json.loads(json_string)
    return json_object
  except Exception as exc:
    raise Exception(f'Json invalido: {exc.args[0]}') from exc


def valid_format(data: dict) -> bool:
  '''Valida si todos los valores de un diccionario son floats o pueden ser convertidos a floats.
  Argumentos:
    data: (dict) El diccionario que se desea validar. 
  Devuelve:
    True si todos los valores del diccionario son floats o pueden ser convertidos a floats
    False en caso contrario.
  '''
  for item in data.items():
    if isinstance(data[item[0]], float):
      continue
    try:
      data[item[0]] = float(item[1])
    except ValueError:
      return False
  return True


def higher_absolute_value(data: dict) -> float:
  '''Calcula el valor absoluto más alto de un objeto
  Argumentos:
    data: (dict) diccionario clave:valor donde valor sera siempre un float
  Devuelve:
    Un numero flotante que representa el valor absoluto más alto
  '''
  valor_absoluto_max = max(abs(item[1]) for item in data.items())
  return valor_absoluto_max


def percent_of(value: float, percent_100: float) -> float:
  '''Calcula el porcentaje de un valor en relación a otro valor.
  Argumentos:
    value: (float) El valor del que se desea calcular el porcentaje. Debe ser un número flotante.
    percent_100: (float) El valor que representa el 100%. Debe ser un número flotante.
  Devuelve:
    Un número flotante que representa el porcentaje del `value` en relación al `percent_100`
    redondeado a 2 decimales.
  '''
  porcentaje = value * 100 / percent_100
  return round(porcentaje, 2)


def fill_with_empty_spaces(size: int, line: str) -> str:
  '''Complementa las lineas con espacios vacíos para
  cumplir el tamaño requerido de ancho
  Argumentos:
    size: (int) Integer que nos indica el tamaño del string
    line: (str) String que equivale a la linea de texto a complementar
  Devuelve:
    String con espacios complementados
  '''
  if len(line) < size:
    while len(line) < size:
      line = f'{line} '
  return line
