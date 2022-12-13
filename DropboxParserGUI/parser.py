import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from PyQt6 import uic
import glob
import re

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui.ui', self)
        self.setWindowTitle('Amazon Dropbox Log Parser')
        self.input_Browse.clicked.connect(self.browseInputPath)
        self.output_Browse.clicked.connect(self.browseOutputPath)
        self.log_Parse.clicked.connect(self.parseLogs)

    def browseInputPath(self):
    	input_Browse = QFileDialog.getExistingDirectory(self, 'Input Path',)
    	self.input_Path.setText(input_Browse)

    def browseOutputPath(self):	
    	output_Browse = QFileDialog.getExistingDirectory(self, 'Output Path',)
    	self.output_Path.setText(output_Browse)

    def parseLogs(self):
    	read_files = glob.glob(input_Path)

    	with open(browseOutputPath(output_Browse) + 'carvedloglines.txt', "wb") as outfile:
    	    for f in read_files:
    	        with open(f, "rb") as infile:
    	            outfile.write(infile.read())
    				
    	#Touch Event Received Section
    	print('#### TouchEventReceived Section ####\n')
    	with open (browseOutputPath(output_Browse) + 'carvedloglines.txt', 'wb') as outfile:
    	    outfile.write('#### TouchEventReceived Section ####\n\n')
    	hits = []
    	linenum = 0
    	pattern = re.compile("Touch event received")  # Compile a case-insensitive regex
    	with open (browseOutputPath(output_Browse) + 'carvedloglines.txt', 'rt') as myfile:    
    	    for line in myfile:
    	        linenum += 1
    	        if pattern.search(line) != None:      # If a match is found 
    	            hits.append((linenum, line.rstrip('\n')))
    	with open (browseOutputPath(output_Browse) + 'carvedloglines.txt', 'a') as outfile:
    	    for hit in hits:                            # Iterate over the list of tuples
    	        outfile.write(hit[1] + '\n')

    	#ComposeMessageActivit Section
    	print('#### ComposeMessageActivit Section ####\n')
    	with open (browseOutputPath(output_Browse) + 'carvedloglines.txt', 'a') as outfile:
    	    outfile.write('\n#### ComposeMessageActivit Section ####\n\n')
    	hits = []
    	linenum = 0
    	pattern = re.compile("ComposeMessagingActivit")  # Compile a case-insensitive regex
    	with open (browseOutputPath(output_Browse) + 'carvedloglines.txt', 'rt') as myfile:    
    	    for line in myfile:
    	        linenum += 1
    	        if pattern.search(line) != None:      # If a match is found 
    	            hits.append((linenum, line.rstrip('\n')))
    	with open (browseOutputPath(output_Browse) + 'carvedloglines.txt', 'a') as outfile:
    	    for hit in hits:                            # Iterate over the list of tuples
    	        outfile.write(hit[1] + '\n')

    	#SwipedOpen Section
    	print('#### SwipedOpen Section ####\n')
    	with open (browseOutputPath(output_Browse) + 'carvedloglines.txt', 'a') as outfile:
    	    outfile.write('\n#### SwipedOpen Section ####\n\n')
    	hits = []
    	linenum = 0
    	pattern = re.compile("SWIPED_OPEN")  # Compile a case-insensitive regex
    	with open (browseOutputPath(output_Browse) + 'carvedloglines.txt', 'rt') as myfile:    
    	    for line in myfile:
    	        linenum += 1
    	        if pattern.search(line) != None:      # If a match is found 
    	            hits.append((linenum, line.rstrip('\n')))
    	with open (browseOutputPath(output_Browse) + 'carvedloglines.txt', 'a') as outfile:
    	    for hit in hits:                            # Iterate over the list of tuples
    	        outfile.write(hit[1] + '\n')

    	#OpeningAnimationComplete Section
    	print('#### OpeningAnimationComplete Section ####\n')
    	with open (browseOutputPath(output_Browse) + 'carvedloglines.txt', 'a') as outfile:
    	    outfile.write('\n#### OpeningAnimationComplete Section ####\n\n')
    	hits = []
    	linenum = 0
    	pattern = re.compile("OPENING_ANIMATION_COMPLETE")  # Compile a case-insensitive regex
    	with open (browseOutputPath(output_Browse) + 'carvedloglines.txt', 'rt') as myfile:    
    	    for line in myfile:
    	        linenum += 1
    	        if pattern.search(line) != None:      # If a match is found 
    	            hits.append((linenum, line.rstrip('\n')))
    	with open (browseOutputPath(output_Browse) + 'carvedloglines.txt', 'a') as outfile:
    	    for hit in hits:                            # Iterate over the list of tuples
    	        outfile.write(hit[1] + '\n')

    	#ToolTypeFinger Section
    	print('#### ToolTypeFinger Section ####\n')
    	with open (browseOutputPath(output_Browse) + 'carvedloglines.txt', 'a') as outfile:
    	    outfile.write('\n#### ToolTypeFinger Section ####\n\n')
    	hits = []
    	linenum = 0
    	pattern = re.compile("TOOL_TYPE_FINGER")  # Compile a case-insensitive regex
    	with open (browseOutputPath(output_Browse) + 'carvedloglines.txt', 'rt') as myfile:    
    	    for line in myfile:
    	        linenum += 1
    	        if pattern.search(line) != None:      # If a match is found 
    	            hits.append((linenum, line.rstrip('\n')))
    	with open (browseOutputPath(output_Browse) + 'carvedloglines.txt', 'a') as outfile:
    	    for hit in hits:                            # Iterate over the list of tuples
    	        outfile.write(hit[1] + '\n')

    	#senderCommsId Section
    	print('#### SenderCommsId Section ####\n')
    	with open (browseOutputPath(output_Browse) + 'carvedloglines.txt', 'a') as outfile:
    	    outfile.write('\n#### SenderCommsId Section ####\n\n')
    	hits = []
    	linenum = 0
    	pattern = re.compile("senderCommsId")  # Compile a case-insensitive regex
    	with open (browseOutputPath(output_Browse) + 'carvedloglines.txt', 'rt') as myfile:    
    	    for line in myfile:
    	        linenum += 1
    	        if pattern.search(line) != None:      # If a match is found 
    	            hits.append((linenum, line.rstrip('\n')))
    	with open (browseOutputPath(output_Browse) + 'carvedloglines.txt', 'a') as outfile:
    	    for hit in hits:                            # Iterate over the list of tuples
    	        outfile.write(hit[1] + '\n')

    	#KeyboardOpening Section
    	print('#### KeyboardOpening Section ####\n')
    	with open (browseOutputPath(output_Browse) + 'carvedloglines.txt', 'a') as outfile:
    	    outfile.write('\n#### KeyboardOpening Section ####\n\n')
    	hits = []
    	linenum = 0
    	pattern = re.compile("KEYBOARD_OPENING")  # Compile a case-insensitive regex
    	with open (browseOutputPath(output_Browse) + 'carvedloglines.txt', 'rt') as myfile:    
    	    for line in myfile:
    	        linenum += 1
    	        if pattern.search(line) != None:      # If a match is found 
    	            hits.append((linenum, line.rstrip('\n')))
    	with open (browseOutputPath(output_Browse) + 'carvedloglines.txt', 'a') as outfile:
    	    for hit in hits:                            # Iterate over the list of tuples
    	        outfile.write(hit[1] + '\n')

    	#KeyboardClosing Section
    	print('#### KeyboardClosing Section ####\n')
    	with open (browseOutputPath(output_Browse) + 'carvedloglines.txt', 'a') as outfile:
    	    outfile.write('\n#### KeyboardClosing Section ####\n\n')
    	hits = []
    	linenum = 0
    	pattern = re.compile("KEYBOARD_CLOSING")  # Compile a case-insensitive regex
    	with open (browseOutputPath(output_Browse) + 'carvedloglines.txt', 'rt') as myfile:    
    	    for line in myfile:
    	        linenum += 1
    	        if pattern.search(line) != None:      # If a match is found 
    	            hits.append((linenum, line.rstrip('\n')))
    	with open (browseOutputPath(output_Browse) + 'carvedloglines.txt', 'a') as outfile:
    	    for hit in hits:                            # Iterate over the list of tuples
    	        outfile.write(hit[1] + '\n')

if __name__ == '__main__':

	app = QApplication(sys.argv)

window = MainWindow()
window.show()

try:
	sys.exit(app.exec())
except SystemExit:
	print('Closing Window...')