# ID : 20CE141
# NAME : PRATIK SUTHAR

# AIM : GENERATE PDF FILE OF YOUR 3RD SEMESTER MARK-SHEET.


from reportlab.pdfgen import canvas
from reportlab.lib.colors import skyblue, black

result = canvas.Canvas("20CE141_RESULT.pdf")

result.setFillColor(skyblue)
result.setFont('Times-Roman', 32)
result.drawString(30, 770, 'CHARUSAT')
result.setFillColor(black)

result.setFontSize(6.2)
result.drawString(30, 760, 'CHAROTAR UNIVERSITY OF SCIENCE AND TECHNOLOGY')

result.setFont('Helvetica-Bold', 12)
result.drawString(220, 782, 'CHAROTAR UNIVERSITY OF SCIENCE AND TECHNOLOGY')

result.setFont('Helvetica', 8.8)
result.drawString(220, 770, 'CHARUSAT Campus, Changa - 388421 , Off Nadiad - Petlad Highway, Gujarat (India)')
result.drawString(220, 760, 'Ph. # +91-2697-265001,265021 Fax. # +91-2697-265007')
result.drawString(220, 750, 'Web : www.charusat.ac.in | Email : info@charusat.ac.in')
result.drawString(100, 730,
                  '(Formed under Gujarat State Act No. 8 of 2009, and degrees conferred u/s 22 of UGC Act. 1956)')
result.drawString(220, 720, '(Accredited with Grade \'A\' by NAAC)')

result.setFont('Helvetica-Bold', 18)
result.setFillColor(skyblue)
result.drawString(175, 700, 'SEMESTER GRADE REPORT')
result.setFillColor(black)

result.setFont('Helvetica-Bold', 16)
result.drawString(106, 670, 'FACULTY OF TECHNOLOGY AND ENGINEERING')

result.setFont('Times-Roman', 14)
result.drawString(30, 640, 'No. : R4249')
result.drawString(430, 640, 'Date : 22/12/2021')
result.drawString(30, 620, 'Name : SUTHAR PRATIK BHARATKUMAR')
result.drawString(30, 600, 'Programme : B.TECH.(COMPUTER)')
result.drawString(430, 600, 'ID.No. : 20CE141')
result.drawString(30, 580, 'Month & Year : November 2021')
result.drawString(280, 580, 'Semester : 3')
result.drawString(430, 580, 'Aadhaar : 534983186592')

result.line(20, 555, 570, 555)
result.drawString(220, 540, 'Course')
result.line(20, 535, 570, 535)

result.line(20, 555, 20, 295)  # first line...
result.line(410, 555, 410, 295)  # second line...
result.line(490, 555, 490, 295)  # third line...
result.line(570, 555, 570, 295)  # last line...

result.drawString(30, 520, 'CE244')
result.drawString(100, 520, 'SOFTWARE GROUP PROJECT-I')
result.drawString(325, 520, 'PRACTICAL')

result.drawString(30, 500, 'CE251')
result.drawString(100, 500, 'JAVA PROGRAMMING')
result.drawString(325, 500, 'THEORY')
result.drawString(325, 480, 'PRACTICAL')

result.drawString(30, 460, 'CE252')
result.drawString(100, 460, 'DIGITAL ELECTRONICS')
result.drawString(325, 460, 'THEORY')
result.drawString(325, 440, 'PRACTICAL')

result.drawString(30, 420, 'CE257')
result.drawString(100, 420, 'DATA COMMUNICATION &')
result.drawString(325, 420, 'THEORY')
result.drawString(100, 400, 'NETWORK')
result.drawString(325, 400, 'PRACTICAL')

result.drawString(30, 380, 'HS121.02A')
result.drawString(100, 380, 'CREATIVITY, PROBLEM SOLVING')
result.drawString(100, 360, 'AND INNOVATION')
result.drawString(325, 380, 'PRACTICAL')

result.drawString(30, 340, 'IT281.01')
result.drawString(100, 340, 'ICT RESOURCES & MULTIMEDIA')
result.drawString(325, 340, 'PRACTICAL')

result.drawString(30, 320, 'MA253')
result.drawString(100, 320, 'DISCRETE MATHEMATICS')
result.drawString(100, 300, 'AND ALGEBRA')
result.drawString(325, 320, 'THEORY')

result.drawString(420, 540, 'Credit(C)')

result.drawString(425, 520, '2.00')  # SGP PRACTICAL CREDIT

result.drawString(425, 500, '3.00')  # JAVA THEORY CREDIT
result.drawString(425, 480, '2.00')  # JAVA PRACTICAL CREDIT

result.drawString(425, 460, '3.00')  # DE THEORY CREDIT
result.drawString(425, 440, '1.00')  # DE PRACTICAL CREDIT

result.drawString(425, 420, '4.00')  # DCN THEORY CREDIT
result.drawString(425, 400, '1.00')  # DCN PRACTICAL CREDIT

result.drawString(425, 380, '2.00')  # HS PRACTICAL CREDIT

result.drawString(425, 340, '2.00')  # IT PRACTICAL CREDIT

result.drawString(425, 320, '4.00')  # MATH THEORY CREDIT

result.drawString(500, 540, 'Grade')

result.drawString(510, 520, 'AA')  # SGP PRACTICAL GRADE

result.drawString(510, 500, 'BB')  # JAVA THEORY GRADE
result.drawString(510, 480, 'AA')  # JAVA PRACTICAL GRADE

result.drawString(510, 460, 'AA')  # DE THEORY GRADE
result.drawString(510, 440, 'CC')  # DE PRACTICAL GRADE

result.drawString(510, 420, 'AA')  # DCN THEORY GRADE
result.drawString(510, 400, 'AA')  # DCN PRACTICAL GRADE

result.drawString(510, 380, 'AA')  # HS PRACTICAL GRADE

result.drawString(510, 340, 'AA')  # IT PRACTICAL GRADE

result.drawString(510, 320, 'AA')  # MATH THEORY GRADE
result.line(20, 295, 570, 295)

# create second table
result.line(20, 285, 570, 285)  # first horizontal...
result.line(20, 265, 570, 265)  # second horizontal...
result.line(20, 245, 490, 245)  # third horizontal...
result.line(20, 225, 570, 225)  # fourth horizontal...

result.line(20, 285, 20, 225)
result.line(115, 265, 115, 225)
result.line(205, 265, 205, 225)

result.line(255, 285, 255, 225)
result.line(345, 265, 345, 225)
result.line(435, 265, 435, 225)

result.line(490, 285, 490, 225)
result.line(570, 285, 570, 225)

result.drawString(90, 270, 'Semester Performance')
result.drawString(30, 250, 'Total Credits')
result.drawString(50, 230, '24.00')
result.drawString(120, 250, 'Credit Earned')
result.drawString(140, 230, '24.00')
result.drawString(210, 250, 'SGPA')
result.drawString(215, 230, '9.58')

result.drawString(320, 270, 'Cumulative Performance')
result.drawString(260, 250, 'Total Credits')
result.drawString(280, 230, '61.00')
result.drawString(350, 250, 'Credit Earned')
result.drawString(370, 230, '61.00')
result.drawString(440, 250, 'CGPA')
result.drawString(445, 230, '9.41')

result.drawString(515, 270, 'Class')
result.drawString(500, 240, 'Distinction')

result.drawString(30, 200, 'Previous SGPA : 9.63')
result.drawString(230, 200, 'Previous CGPA : 9.30')
result.drawString(420, 200, 'No. of BackLog : 0')


result.setFont('Times-Roman', 14)
result.drawString(450, 90, 'Registrar')

result.line(40, 170, 120, 170)
result.line(40, 90, 120, 90)
result.drawString(55, 130, 'PHOTO')
result.line(40, 90, 40, 170)
result.line(120, 90, 120, 170)

result.setFont('Helvetica', 9)
result.drawString(240, 180, 'EX/REG/CE/NT/2/21/148')

result.setFont('Helvetica', 7)
result.drawString(210, 50, 'NB : infringement / tampering of this document is legal offence')
result.drawString(500, 50, 'Details overleaf')
result.save()
