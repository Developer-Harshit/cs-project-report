import os

inputFolder = "pages/"
pdfFolder = "pdf/"

inputList = [
    "index",
    "intro",
    "tools",
    "methods",
    "implement",
    "flowchart",
    "code",
    "conclusion",
]

if __name__ == "__main__":
    i = 0
    commandString = "yarn code "

    for filename in inputList:
        inputPath = f"{inputFolder}{filename}.html"
        outputPath = f"{pdfFolder}0{i}.pdf"
        commandString += f"&& yarn pdf {inputPath} {outputPath} "

        i += 1
    commandString += "&& yarn merge"
    os.system(commandString)
