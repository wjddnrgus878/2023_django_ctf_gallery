import PyPDF2
import os

def extract_text_from_pdf(file_path):
    pdf_file_obj = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    text = ''
    for page_num in range(pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page_num)
        text += page_obj.extractText()
    pdf_file_obj.close()
    return text

file_path = r"./강의/공개키암호론/chap07.pdf"
extract_text_from_pdf(file_path)
