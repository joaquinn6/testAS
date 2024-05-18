'''Factory chart'''
from utils import higher_absolute_value, percent_of


class ChartFactory:
  '''Factory Chart'''

  def __init__(self, data, direction) -> None:
    self._tuples = self._make_tuples_percents(data)
    self._direction = direction
    self._bar_draws = []

  def _make_tuples_percents(self, data) -> list:
    '''Crea tuples (etiqueta, porcentaje) a partir de un diccionario
      Argumentos:
        data: (dict) objeto de clave:valor donde valor es siempre un float
      Devuelve: (list) Lista de tuples con el valor convertido en porcentaje
    '''
    bars = []
    biggest_value = higher_absolute_value(data)
    for item in data.items():
      bar_tuple = (item[0], percent_of(item[1], biggest_value))
      bars.append(bar_tuple)
    return bars

  def _print_charts(self) -> None:
    '''Imprime la gráfica'''
    print('\n')
    print(f'Imprimiendo gráfica de barras en {self._direction}:')
    print('\n')
    for bar_draw in self._bar_draws:
      print(bar_draw)
    print('\n')

  def _get_tuple_info(self, bar_tuple: tuple) -> bool:
    '''Retorna True si el porcentaje de la tuple es positivo
      Argumentos:
        bar_tuple: (tuple) tuple de label,valor donde valor es siempre un float
      Devuelve: (dict) Diccionario que devuelve la información de la tuple necesaria
    '''
    return {
        'is_positive': bar_tuple[1] > 0,
        'label': bar_tuple[0],
        'percent': abs(bar_tuple[1])
    }
