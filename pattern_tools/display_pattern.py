from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

drawing = svg2rlg("out.svg")
renderPDF.drawToFile(drawing, "out.pdf")