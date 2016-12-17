import gtk

class Form:
	
	def __init__(self, title):
		
		self.button_count = 0
		
		#gkt window
		window = gtk.Window()
		window.set_title(title)
		window.connect("destroy", gtk.main_quit)
		window.show_all()
		
		#vbox
		self.vbox = gtk.VBox()
		window.add(self.vbox)
		self.vbox.show_all()

	def add_button(self):
		self.button_count += 1
		bc = str(self.button_count)
		self.button = gtk.Button(label="button" + bc)
		self.vbox.pack_start(self.button, expand=False, fill=False, padding=10)
		self.vbox.show_all()

form = Form("Form1")
form.add_button()
form.add_button()

gtk.main()
