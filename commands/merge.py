from pypdf import PdfMerger
from build import inputList, pdfFolder

merger = PdfMerger()


pdfFolder = "pdf/"

# inputList = [
#     "index",
#     "intro",
#     "tools",
#     "methods",
#     "implement",
#     "flowchart",
#     "code",
#     "conclusion",
# ]


for i in range(len(inputList)):
    filePath = f"{pdfFolder}0{i}.pdf"
    merger.append(filePath)
merger.write("dist/" + "output.pdf")
merger.close()
