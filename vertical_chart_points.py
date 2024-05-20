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
    list_bar_draws = self._create_bar_draws()
    self._get_lines(list_bar_draws, 23)
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
    size_line = self._calculate_size_line(label, 12, POINTS_PER_LINE)
    bar_draw = [FwES(size_line, f' {label}')]
    # Agregando las lineas enteras
    if percent >= POINTS_PER_LINE:
      lines = self._calculate_lines(percent, POINTS_PER_LINE, False)
      while lines > 0:
        self._add_line(bar_draw, FwES(size_line, ' .......... '), is_positive)
        lines -= 1
    # Agregando los puntos de ser necesario
    points = self._calculate_points(percent)
    if points >= 1:
      self._add_line(bar_draw, FwES(
          size_line, self._get_line_individual_points(points)), is_positive)
    # Agregando el porcentaje
    self._add_line(bar_draw, FwES(
        size_line, f' {"-" if not is_positive else ""}{percent}%'), is_positive)
    bar_draw = self._fill_with_empty_lines(is_positive, bar_draw, size_line)
    return bar_draw

  def _calculate_points(self, percent: float) -> int:
    '''Calcula la cantidad de puntos que debe tener los porcentajes que faltan por graficar
    Argumentos:
      percent: (float) Porcentaje a graficar
    Devuelve:
      Un entero que representa la cantidad de puntos a dibujar
    '''
    return int(round(percent % POINTS_PER_LINE, 0))

  def _get_line_individual_points(self, points: int) -> str:
    '''Retorna una linea con la cantidad de puntos que debe llevar la linea
    Argumentos: 
      points: (int) Cantidad de puntos que lleva la linea
    Devuelve:
      La linea en formato string'''
    line = ' '
    while points != 0:
      line = f'{line}.'
      points -= 1
    return line
