from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
class Figure_Grapher:
    def __init__(self, window) -> None:
        self.window = window

    def plot(self, polynomial, min, max):
        # the figure that will contain the plot
        fig = Figure(figsize = (5, 5), dpi = 100)
        
        x = np.linspace(min, max, 100000)
        y = eval(polynomial.replace('^', '**'))
    
        # adding the subplot
        _plot = fig.add_subplot(111)

        # plotting the graph
        _plot.grid()

        if 'x' not in polynomial:
            _plot.axhline(y)
        else:
            _plot.plot(x, y)

        _plot.set_title("The Plot for:\n{}".format(polynomial))
        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig, master = self.window)  
        canvas.draw()
    
        graph = canvas.get_tk_widget()
            
        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas, self.window)
        toolbar.update()
    
        return graph, toolbar