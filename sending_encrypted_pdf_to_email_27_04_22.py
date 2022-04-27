import os
import sqlite3
from tkinter import filedialog as fd
from PyPDF2 import PdfFileWriter, PdfFileReader
from datetime import datetime

folder=fd.askdirectory()
files=os.listdir(folder)

#read the pdf files one  by one
for file in files:
    if(file.endswith(".pdf")):
        nn = os.path.join(folder, file)
        #if pdf is already encrypted ignore
        if PdfFileReader(open(nn,'rb')).isEncrypted:
            continue
        # if not do
        #read the pdf
        name = os.path.join(folder, file)
        with open(name,'rb') as f:
            out = PdfFileWriter()
            input = PdfFileReader(f)
            num = input.numPages
            for idx in range(num):
                # Get the page at index idx
                page = input.getPage(idx)
                # Add it to the output file
                out.addPage(page)
                password = file[:-4]
                out.encrypt(password)
                #create dynamic nature in saving your file
                curr=datetime.now().replace(microsecond=0)
                format="%y_%b_%d_%H_%M_%S"
                new_format= datetime.strftime(curr,format)
                file_n = file[:-4] + new_format + ".pdf"
                # save it with timestamp
                filename = os.path.join(folder, file_n)

                with open(filename, "wb") as k:
                    out.write(k)
                    #write the content like name,size,password in database
                    import mysql.connector

                    db = mysql.connector.connect(
                        port=3306,
                        user="root",
                        password="MySQL@12321@!"
                    )

                    cursor = db.cursor()
                    cursor.execute("use training")
                    cursor.execute("alter table pdf add unique(filename); ")
                    query = "INSERT INTO pdf (filename, filesize, type) VALUES (%s, %s,%s)"
                    file_size = os.path.getsize(name)
                    #print(file_size,type(file_size))
                    values = (file, file_size, password)
                    cursor.execute(query, values)
                    query = "SELECT * FROM file"

                    cursor.execute(query)

                    ## fetching all records from the 'cursor' object
                    records = cursor.fetchall()

                    ## Showing the data
                    for record in records:
                        print(record)


                    db.commit()
                    cursor.close()
