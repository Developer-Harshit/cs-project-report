import os
from build import parentDir


pages = []
for filename in range(1, 5):
    f = open(os.path.join(parentDir, "code", f"{filename}.txt"), "r")
    pages.append(f.readlines())
    f.close()

htmlcode = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Project Report</title>
    <link rel="stylesheet" href="./public/css/code.css" />
    <link rel="stylesheet" href="./public/css/paper.css" />
  </head>
  <body class="A4" >
"""


linecount = 1
for lines in pages:
    htmlcode += """<section class='sheet padding-10mm'>
<code class='code'>"""
    for line in lines:
        htmlcode += (
            "<span class='counter'>"
            + str(linecount)
            + "</span>"
            + "<span class='code-line'>"
            + line
            + "</span>"
        )
        linecount += 1
    htmlcode += "</code></section>"
htmlcode += "</body></html>"
f = open(parentDir + "code.html", "w")
f.write(htmlcode)
