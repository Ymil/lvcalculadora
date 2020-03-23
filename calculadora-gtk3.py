''' 
Calculadora simple en python con GTK+3
Autor: Lautaro Linquiman
Youtube: https://www.youtube.com/channel/UC12DhsQbDxcjTvLTUY4ORRw
Sitio web: tutorialdeprogramacion.com
Licencia: Creative Commons
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class CalcWindow(Gtk.Window):
    estructura_calculadora = [
        ["1", "2", "3", "4", "-", "DEL"],
        ["5", "6", "7", "8", "/", "AC"],
        ["9", "0", "%", "*", "+", "="],
    ]
    
    def __init__(self):
        Gtk.Window.__init__(self, title="Calculadora")
        grid = Gtk.Grid()  
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(vbox)
        
        self.entry = Gtk.Entry()
        vbox.pack_start(self.entry, True, True, 0)
        vbox.pack_start(grid, True, True, 0)
        
        y = 0
        for fila in estructura_calculadora:
            x = 0
            for columna in fila:
                    button = Gtk.Button(label=columna)
                    button.connect("clicked", self.__click_button)
                    grid.attach(button, x, y, 1, 1)
                    x += 1
            y += 1
            
    def __click_button(self, widget):
        label = widget.get_label()
        entry_text = self.entry.get_text() 
        if( label == 'DEL' ):
            self.entry.set_text(entry_text[:-1])
        elif( label == 'AC' ):
            self.entry.set_text("")
        elif( label == '=' ):
            result = str(eval(entry_text))
            self.entry.set_text(result)
        else:
            self.entry.set_text(entry_text+label)
               
win = CalcWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
