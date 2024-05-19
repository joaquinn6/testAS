'''Vertical Chart Asteriscos'''
from vertical_chart import VerticalChart
from utils import fill_with_empty_spaces as FwES

ASTERISK_PER_LINE = 8
LINES_PER_CHART = 17


class VerticalChartAsterisk(VerticalChart):
  '''Dibuja la gráfica vertical con asteriscos'''

  def __init__(self, data) -> None:
    super().__init__(data, LINES_PER_CHART, 'Vertical con asteriscos')

  def draw(self) -> None:
    '''Crea un array de strings para dibujar la gráfica de barra.
    '''
    list_bar_draws = []
    for bar_tuple in self._tuples:
      is_positive, label, percent = self._get_tuple_info(bar_tuple).values()
      size_line = 10 if len(label) <= ASTERISK_PER_LINE else len(label) + 2
      bar_draw = [FwES(size_line, f' {label}')]

      lines = int(round(percent / 6.67, 0))
      lines = self._sum_extra_line(lines, percent, 6.67)
      while lines > 0:
        if is_positive:
          bar_draw.insert(0, FwES(size_line, ' ******** '))
        else:
          bar_draw.append(FwES(size_line, ' ******** '))
        lines -= 1
      if is_positive:
        bar_draw.insert(0, FwES(size_line, f' {percent}%'))
      else:
        bar_draw.append(FwES(size_line, f' -{percent}%'))

      bar_draw = self._fill_with_empty_lines(is_positive, bar_draw, size_line)
      list_bar_draws.append(bar_draw)
    self._get_lines(list_bar_draws, 33)
    self._print_charts()
