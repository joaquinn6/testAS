'''Horizontal factory chart'''
from chart_factory import ChartFactory
from utils import fill_with_empty_spaces as FwES


class HorizontalChart(ChartFactory):
  '''
  Extension del ChartFactory que procesa el Chart Horizontal
  '''

  def __init__(self, data) -> None:
    super().__init__(data, 'Horizontal')
    self._len_biggest_label = self._get_size_biggest_label()

  def _get_size_biggest_label(self) -> int:
    '''Extrae el tamaño del label mas largo
    Devuelve:
      Integer que da el tamaño del texto mas largo
    '''
    lens_labels = [len(tuple[0]) for tuple in self._tuples]
    return max(lens_labels)

  def draw(self) -> None:
    '''Crea un array de strings para dibujar la gráfica de barra.
    '''

    for bar_tuple in self._tuples:
      bar_chart = self._create_single_line(bar_tuple)
      self._bar_draws.append(bar_chart)
    self._print_charts()

  def _create_single_line(self, bar_tuple: tuple) -> str:
    '''Crea la fila que representa la tuple
      Argumentos:
        bar_tuple: (tuple) La tuple que se va a graficar
      Devuelve:
        Un string que dibuja la grafica de la tuple
    '''
    is_positive, label, percent = self._get_tuple_info(bar_tuple).values()
    bar_chart = f'-{FwES(self._len_biggest_label, label)}-'
    lines = self._calculate_lines(percent, 2.5, True)
    while lines > 0:
      if is_positive:
        bar_chart = f'{bar_chart}|'
      else:
        bar_chart = f'|{bar_chart}'
      lines -= 1
    if is_positive:
      bar_chart = f'{bar_chart}{percent}%'
      bar_chart = f'{FwES(40,"")}{bar_chart}'
    else:
      bar_chart = f'-{percent}%{bar_chart}'
      bar_chart = f'{FwES(42 + self._len_biggest_label,bar_chart, False)}'
    return bar_chart
