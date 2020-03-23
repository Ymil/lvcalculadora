#/usr/bin/python
''' 
Calculadora simple en python con GTK
Autor: Lautaro Linquiman
Sitio web: tutorialdeprogramacion.com
Licencia: Creative Commons
'''
try:
	import gtk
except ImportError:
	print 'Nesesitas instalar PyGtk'
	print 'pip install pygtk'

import sys
if not (2,7) == sys.version_info[0:2]:
	print 'Vercion para python 2.7'
	print 'Abortando ejecucion'
	sys.exit()

class App():
	def __init__(self):
		self.__buttonStructure = (
			('1','2','3','+'), 
			('4','5','6','-'), 
			('7','8','9','*'), 
			('0', 'DEL'), 
			( '=', '/', '%'))

		self.__window = 0
		self.__entryValues = ''
		self.__entryBox = gtk.Entry(255)
		self.__VBox = gtk.VBox(homogeneous = 1, spacing = 5)
		self.__createWindow()

	def __del__(self):
		del self.__buttonStructure
		del self.__window
		del self.__entryBox
		del self.__VBox

	def showView(self):
		gtk.main()

	def __createWindow(self):
		''' Crea la ventana y llama para crear la estructura '''
		self.__window = gtk.Window()
		self.__window.set_title('Caluladora')
		self.__window.set_default_size(400,400)
		self.__window.connect('destroy', self.__eventClose)
		self.__window.add(self.__VBox)
		self.__createWindowStructure()
		self.__window.show_all()

	def __createButtonsFromStructure(self):
		''' Crea la estructura de botones '''
		for line in self.__buttonStructure:			
			hBox = gtk.HBox()
			self.__VBox.pack_start(hBox,1 ,1 ,5)
			for label in line:
				button = gtk.Button(label)
				button.connect('clicked', self.__eventHandleClick)
				hBox.pack_start(button, 1, 1, 5)				


	def __createWindowStructure(self):
		''' Crea toda la estrutura de la ventana '''
		hBox = gtk.HBox()		
		self.__entryBox.set_editable(0)
		hBox.pack_start(self.__entryBox, 1 , 1, 0)
		self.__VBox.pack_start(hBox,1 ,1 , 0)
		self.__createButtonsFromStructure()

	def __deleteValuesEntry(self):
		''' Borra los valores ingresados '''
		self.__entryValues = ''

	def __setResult(self):
		''' Hace las cuentas matematicas y muestra los resultados '''
		self.__entryValues = str(eval(self.__entryValues))
		self.__entryBox.set_text(self.__entryValues)

	def __eventClose(self, widget):
		gtk.main_quit()

	def __eventHandleClick(self, widget):
		''' Evento: Toma las deciciones de que hacer al precionar un boton '''
		label = widget.get_label()
		if(not (label == "DEL" or label == "=")):
			self.__entryValues += label
		elif(label == "="):
			self.__setResult()
		elif(label == "DEL"):
			self.__deleteValuesEntry()
		self.__entryBox.set_text(self.__entryValues)

if __name__ == "__main__":
	app = App()
	app.showView()