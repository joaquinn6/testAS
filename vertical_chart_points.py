'''Vertical Chart Points'''
from vertical_chart import VerticalChart
from utils import fill_with_empty_spaces as FwES

POINTS_PER_LINE = 10
LINES_PER_CHART = 12


class VerticalChartPoints(VerticalChart):
  '''Dibuja la gráfica vertical con puntos'''

  def __init__(self, data) -> None:
    super().__init__(data, LINES_PER_CHART, 'Vertical con puntos')

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
    self._get_lines(list_bar_draws, 23)
    self._print_charts()
