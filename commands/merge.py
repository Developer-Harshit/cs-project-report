import os
from pypdf import PdfMerger
from build import inputList, pdfFolder, parentDir


merger = PdfMerger()


for i in range(len(inputList)):
    filePath = f"{pdfFolder}0{i}.pdf"
    merger.append(filePath)
merger.write(f"{parentDir}dist/build.pdf")
merger.close()
