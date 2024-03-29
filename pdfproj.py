import os
import sys
import PyPDF2

template = PyPDF2.PdfFileReader(open("FileToBeWatermarked.pdf", "rb"))
watermark = PyPDF2.PdfFileReader(open("WatermarkedFile.pdf", "rb"))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
	page = template.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)

	with open('Watermarked_0utput.pdf', 'wb') as file:
		output.write(file)

