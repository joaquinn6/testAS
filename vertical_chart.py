'''Vertical factory chart'''
from chart_factory import ChartFactory
from utils import fill_with_empty_spaces as FwES


class VerticalChart(ChartFactory):
  '''
  Extension del ChartFactory que procesa el Chart Vertical
  '''

  def __init__(self, data, lines_per_chart, type_chart) -> None:
    super().__init__(data, type_chart)
    self._lines_per_chart = lines_per_chart

  def _fill_with_empty_lines(self, is_positive: bool, bar_draw: list, size_line: int) -> list:
    '''Rellena de caracteres vacíos el espacio sobrante
    Argumentos:
      is_positive: (bool) Booleano que me indica si se rellena hacia arriba o hacia abajo
      bar_draw: (list) Lista de strings que dibujan la barra.
      size_line: (int) tamaño que deben cubrir los espacios vacíos
    Devuelve:
      Una lista ordenada de como se imprimirá la barra con espacios
    '''
    size = len(bar_draw)
    if size != self._lines_per_chart:
      for _ in range(self._lines_per_chart-size):
        if is_positive:
          bar_draw.insert(0, FwES(size_line, ''))
        else:
          bar_draw.append(FwES(size_line, ''))
    for _ in range(self._lines_per_chart) if is_positive else range(self._lines_per_chart - 1):
      if is_positive:
        bar_draw.append(FwES(size_line, ''))
      else:
        bar_draw.insert(0, FwES(size_line, ''))

    return bar_draw

  def _join_lines(self, list_bars: list, max_lines_per_chart: int) -> list:
    '''Crea un array de strings para dibujar la gráfica de barra
    uniendo todas las barras por indice.
    Argumentos:
      list_bars: (list) lista totales de barras a graficar
      max_lines_per_chart: (int) entero de cantidad de lineas totales por barra
    Devuelve:
      Una lista unificada de las barras lista para imprimir
    '''
    for i in range(max_lines_per_chart):
      self._bar_draws.append(''.join(bar_draw[i-1] for bar_draw in list_bars))

  def _calculate_width_size_line(self, label: str, min_length: int, bar_length: int) -> int:
    '''Calcula la longitud en ancho que debe tener la barra para que el label
    alcance en la gráfica sin desplazar la siguiente
    Argumentos:
      label: (str) La etiqueta que tendrá la barra
      min_length: (int) El tamaño mínimo que tendría la barra de ser un label corto
      bar_length: (int) El tamaño que tiene la barra sin los espacios a los lados
    Devuelve:
      Un entero que indica el tamaño que debe tener la barra
    '''
    return min_length if len(label) <= bar_length else len(label) + 2

  def _add_line(self, bar_draw: list, str_line: str, is_positive: bool):
    '''Agrega la linea al principio o al final según el porcentaje sea positivo o negativo
    Argumentos:
      bar_draw: (list) lista de lineas a la que se agregara la nueva
      str_line: (str) linea a agregar
      is_positivo: (bool) booleano que determina la dirección donde se insertara 
    '''
    if is_positive:
      bar_draw.insert(0, str_line)
    else:
      bar_draw.append(str_line)
