import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo


from figure_grapher import Figure_Grapher
from validator import Validator
class Window_Creator(tk.Tk):
    """
    Class responsible for the window
    """
    def __init__(self):
        super().__init__()
        """
        Responsible for placing labels, text boxes, graph, toolbar and buttons on window
        """
        # configure the root window
        self.title('Function Plotter')
        self.configure(bg='white')
        self.attributes('-fullscreen', True)

        # Utilities
        self.validator = Validator()
        self.fg = Figure_Grapher(self)

        # General Rules
        self.general_rules = Label(self, bg='white', font='Arial 14 bold',  text="""General Rules:\n
        1) Only Numbers and x . - + / * ^ Allowed\n
        2) Leading Operators Not Allowed\n
        3) Trailing Operators Not Allowed\n
        4) Double Operators Are Not Allowed\n
        5) Unbalanced Parentheses Are Not Allowed\n
        6) Min and Max Must Be Numeric\n
        7) Put '*' Between Constant and Variable\n
        """)
        self.general_rules.place(relx=0.78, rely=0.45, anchor="center")
        # label for function
        self.function_label = Label(self, text='Enter Function: ', bg='white')
        self.function_label.place(relx=0.05, rely=0.4, anchor='center')

        # text field to input the function
        self.function_input = tk.Text(self, height = 1, width = 40, highlightbackground='black', highlightthickness=0.5)
        self.function_input.place(relx=0.19, rely=0.4, anchor='center')
        
        # label for min 
        self.label_min = Label(self, text='Min: ', bg='white')
        self.label_min.place(relx=0.1, rely=0.45, anchor='center')

        # text field to input the min
        self.min_input = tk.Text(self, height = 1, width = 10, highlightbackground='black', highlightthickness=0.5)
        self.min_input.place(relx=0.14, rely=0.45, anchor='center')

        # label for max 
        self.label_max = Label(self, text='Max: ', bg='white')
        self.label_max.place(relx=0.2, rely=0.45, anchor='center')

        # text field to input the max
        self.max_input = tk.Text(self, height = 1, width = 10, highlightbackground='black', highlightthickness=0.5)
        self.max_input.place(relx=0.24, rely=0.45, anchor='center')

        
        
        # button
        self.button = Button(self, text='Plot', bg='white',highlightbackground='white')
        self.button['command'] = self.button_clicked
        self.button.place(relx=0.19, rely=0.5, anchor='center')
        
    def show_graph(self, polynomial, min, max):
        """
        Function responsible for showing the graph using "Figure_Grapher" class
        """
        graph, toolbar= self.fg.plot(polynomial, float(min), float(max))
        graph.place(relx=0.5, rely=0.4, anchor='center')
        toolbar.place(relx=0.5, rely=0.7, anchor='center')

    def button_clicked(self):
        """
        Function that handles taking in input and calling for verification before passing
        input to get graphed
        """
        # get input from text boxes
        polynomial = self.function_input.get(1.0, 'end-1c')
        min = self.min_input.get(1.0, 'end-1c')
        max = self.max_input.get(1.0, 'end-1c')
        # check the validity of input
        msg = self.validator.validate_expression(polynomial, min, max)
        # if there's mistake display to error
        if msg != 'Success':
            showinfo(title='Information', message=msg)
            return
        # if passed then show the graph
        self.show_graph(polynomial, min, max)

if __name__ == "__main__":
    window_creator = Window_Creator()
    window_creator.mainloop()