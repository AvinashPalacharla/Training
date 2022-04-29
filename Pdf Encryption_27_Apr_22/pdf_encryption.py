import os
import PyPDF2
import pyautogui
import datetime
from PyPDF2 import PdfFileWriter, PdfFileReader
import hashlib
files = os.listdir("C:/Users/avina/OneDrive/Desktop/Training")
for x in files:
    if x.endswith(".pdf"):
        if PyPDF2.PdfFileReader(open("C:/Users/avina/OneDrive/Desktop/Training/"+x, 'rb')).isEncrypted:
            continue
        else:
            with open("C:/Users/avina/OneDrive/Desktop/Training/"+x, "rb") as in_file:
                input_pdf = PdfFileReader(in_file)
                output_pdf = PdfFileWriter()
                output_pdf.appendPagesFromReader(input_pdf)
                output_pdf.encrypt("something")
                with open("C:/Users/avina/OneDrive/Desktop/Training/"+x, "wb") as out_file:
                    output_pdf.write(out_file)

