'''Vertical factory chart'''
from utils import fill_with_empty_spaces as FwES
from chart_factory import ChartFactory

POINTS_PER_LINE = 10
LINES_PER_CHART = 12


class VerticalChart(ChartFactory):
  '''
  Extension del ChartFactory que procesa el Chart Vertical
  '''

  def __init__(self, data) -> None:
    super().__init__(data, 'Vertical')

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
    if size != LINES_PER_CHART:
      for _ in range(LINES_PER_CHART-size):
        if is_positive:
          bar_draw.insert(0, FwES(size_line, ''))
        else:
          bar_draw.append(FwES(size_line, ''))
    for _ in range(LINES_PER_CHART) if is_positive else range(11):
      if is_positive:
        bar_draw.append(FwES(size_line, ''))
      else:
        bar_draw.insert(0, FwES(size_line, ''))

    return bar_draw

  def _get_lines(self, list_bars):
    '''Crea un array de strings para dibujar la gráfica de barra
    uniendo todas las barras por indice.
    '''
    for i in range(23):
      self._bar_draws.append(''.join(bar_draw[i-1] for bar_draw in list_bars))

  def draw(self) -> None:
    '''Crea un array de strings para dibujar la gráfica de barra.
    '''
    list_bar_draws = []
    for bar_tuple in self._tuples:
      is_positive, label, percent = self._get_tuple_info(bar_tuple).values()
      size_line = 12 if len(label) <= POINTS_PER_LINE else len(label) + 2
      bar_draw = [FwES(size_line, f' {label}')]
      if percent >= POINTS_PER_LINE:
        lines = int(round(percent / POINTS_PER_LINE, 0))
        for _ in range(lines):
          if is_positive:
            bar_draw.insert(0, FwES(size_line, ' .......... '))
          else:
            bar_draw.append(FwES(size_line, ' .......... '))
      points = int(round(percent % POINTS_PER_LINE, 0))
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
      bar_draw = self._fill_with_empty_lines(is_positive, bar_draw, size_line)
      list_bar_draws.append(bar_draw)
    self._get_lines(list_bar_draws)
    self._print_charts()
