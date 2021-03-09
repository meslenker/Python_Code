import pyttsx3
import PyPDF2


#Place pdf in directory and put name in the open statement
book = open('Beginning Azure Functions.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)

pages = pdfReader.numPages
print(pages)
for num in range(14, pages):
    speaker = pyttsx3.init()
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
