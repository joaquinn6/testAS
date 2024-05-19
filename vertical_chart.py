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

  def _get_lines(self, list_bars, max_lines_per_chart):
    '''Crea un array de strings para dibujar la gráfica de barra
    uniendo todas las barras por indice.
    '''
    for i in range(max_lines_per_chart):
      self._bar_draws.append(''.join(bar_draw[i-1] for bar_draw in list_bars))
