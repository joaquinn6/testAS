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
    list_bar_draws = self._create_bar_draws()
    self._get_lines(list_bar_draws, 33)
    self._print_charts()

  def _create_bar_draws(self) -> list:
    '''Crea la lista de barras a a partir de las tuples
    Devuelve:
      La lista de listas de barras graficadas'''
    list_bar_draws = []
    for bar_tuple in self._tuples:
      bar_draw = self._create_single_bar_draw(bar_tuple)
      list_bar_draws.append(bar_draw)
    return list_bar_draws

  def _create_single_bar_draw(self, bar_tuple: tuple) -> list:
    '''Crea la lista de strings que representa la tuple
      Argumentos:
        bar_tuple: (tuple) La tuple que se va a graficar
      Devuelve:
        Una lista de strings que dibuja la grafica de la tuple
    '''
    is_positive, label, percent = self._get_tuple_info(bar_tuple).values()
    size_line = self._calculate_size_line(label, 10, ASTERISK_PER_LINE)
    bar_draw = [FwES(size_line, f' {label}')]

    lines = self._calculate_lines(percent, 6.67, True)
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
    return bar_draw
