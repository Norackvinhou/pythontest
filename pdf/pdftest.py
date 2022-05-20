from asyncore import read
import PyPDF2

#rb is read binary
PDFfile = open('meetingminutes1.pdf','rb')

reader = PyPDF2.PdfFileReader(PDFfile)
print(reader.numPages)
page = reader.getPage(0)

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())

# print(page.extractText())