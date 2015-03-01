import sys 
from PyQt4.QtCore import *
from PyQt4.QtGui import * 
from PyQt4.QtWebKit import * 
import re
import os

class convertor():
	def __init__(self, url):
		self.web = QWebView()
		#Read the URL given
		self.web.load(QUrl(url))
		self.printer = QPrinter()
		#setting format
		self.printer.setPageSize(QPrinter.A5)
		self.printer.setOrientation(QPrinter.Landscape)
		self.printer.setOutputFormat(QPrinter.PdfFormat)
		pdf_name='questions/'+url.rsplit('/',1)[1]
		self.printer.setOutputFileName(pdf_name)
		QObject.connect(self.web, SIGNAL("loadFinished(bool)"), self.convertIt)

	def convertIt(self):
		    self.web.print_(self.printer)
		    QApplication.exit()

app = QApplication(sys.argv)

def runconvert(u):
    c=convertor(u)
    c
    app.exec_()


"""outputPDF = PdfFileWriter()
packet = StringIO.StringIO()
# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=letter)
can.setFont("Helvetica", 9)
# Writting the new line
oknow = time.strftime("%a, %d %b %Y %H:%M")
can.drawString(5, 2, url)
can.drawString(605, 2, oknow)
can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(file(tem_pdf, "rb"))
pages = existing_pdf.getNumPages()
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
for x in range(0,pages):
    page = existing_pdf.getPage(x)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
# finally, write "output" to a real file
outputStream = file(final_file, "wb")
output.write(outputStream)
outputStream.close()"""