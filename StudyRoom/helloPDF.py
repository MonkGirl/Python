from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF

d = Drawing(100, 100)
s = String(50, 50, 'Hello, World!', textAnchor='middle')

d.add(s)

rederPDF.drawToFile(d, 'hello.pdf','A simple PDF file')
