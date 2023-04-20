import itertools
import subprocess
import PyPDF4
import pdfplumber
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, portrait
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Spacer, Table, TableStyle, Paragraph
from reportlab.pdfgen import canvas
import degree_requirements
import transcript
from course_finder import get_courses
import degree_plan_page as dpp



def launch_pdf():
    # User input
    path_to_pdf = "transcripts\\keeley-jones.pdf"
    graduation = "Spring 2033"
    fast_track = True
    thesis = False
    track = degree_requirements.DegreePlans().get_libraries('data_science')

    # General Student
    student_info = transcript.Transcript(path_to_pdf)
    student_name = student_info.get_name()
    student_id = student_info.get_id()
    admitted = student_info.get_beginning_of_graduate_record()
    major = student_info.get_major()

    # Student Credit
    with pdfplumber.open(path_to_pdf) as pdf:
        courses = get_courses(pdf)

    # Track Information
    track_name = track['Name']
    track_update = track['Update']
    track_color = track['Color']
    track_core = track['Core Courses']
    track_choices = {'Name': 6040, 'Name2': 6030}
    track_electives = [15, 6000]
    track_additional = [3, 0000]
    track_pre = {'Name': 6020, 'Name2': 6010}

    # Create a new PDF document with landscape page orientation
    pdf = SimpleDocTemplate("degree_plan.pdf",
                            pagesize=portrait(letter),
                            leftMargin=50,
                            rightMargin=50,
                            topMargin=40,
                            bottomMargin=40)

    # Define Styles
    title_style = ParagraphStyle(name='Title', fontSize=12, alignment=1, leading=16)
    subtitle_style = ParagraphStyle(name='Subtitle', fontSize=12, alignment=1, leading=16)
    info_style = ParagraphStyle(name='StudentInfo', fontSize=11, alignment=0, leading=16)
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), track_color),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])

    # Define student info
    title = Paragraph("<b>DEGREE PLAN<br/>"
                    "UNIVERSITY OF TEXAS AT DALLAS<br/>"
                    "MASTER OF COMPUTER SCIENCE</b>", style=title_style)

    subtitle = Paragraph("<b>{}</b><br/>"
                        "({})".format(track_name,
                                    track_update), style=subtitle_style)

    student_info = Paragraph("Name of Student: {}<br/>"
                            "Student I.D. number: {}<br/>"
                            "Semester Admitted: {}<br/>"
                            "Anticipated Graduation: {}".format(student_name,
                                                                student_id,
                                                                admitted,
                                                                graduation), style=info_style)

    # build core table
    core_info = Paragraph("Core Credits: 15 Credit Hours (3.19 Grade Point Average Required)".format(), style=info_style)
    data = [["Course Name", "Course ID", "Semester", "Credit", "Grade"]]
    for req in track_core:
        line = [req, track_core[req]]
        for credit in courses:
            print(str(track_core[req])+" "+str(credit['course_id']))
            if str(track_core[req]) == str(credit['course_id']):
                line.append(str(credit['season']+" "+str(credit['year'])))
                line.append(credit['earned'])
                line.append(credit['grade'])
                break
        data.append(line)
    core_table = Table(data)
    core_table.setStyle(table_style)

    # build choice table
    choice_info = Paragraph("Choice Credits: (Complete X of X)".format(), style=info_style)
    data = [["Course Name", "Course ID", "Semester", "Credit", "Grade"]]
    for req in track_choices:
        line = [req, track_choices[req]]
        for credit in courses:
            if track_choices[req] == credit['course_id']:
                line.append(str(credit['season'] + " " + str(credit['year'])))
                line.append(credit['earned'])
                line.append(credit['grade'])
        data.append(line)
    choice_table = Table(data)
    choice_table.setStyle(table_style)

    # Define element order in document
    elements = [title, Spacer(1, 12),
                subtitle, Spacer(1, 12),
                student_info, Spacer(1, 12),
                core_info, core_table, Spacer(1, 12)]
    pdf.build(elements)

    # Open the PDF file
    input_pdf = PyPDF4.PdfFileReader(open("degree_plan.pdf", 'rb'))
    page = input_pdf.getPage(0)
    output_stream = BytesIO()

    # Create canvas objects
    c = canvas.Canvas(output_stream, pagesize=letter)
    c.acroForm.textfield(height=18, width=100, x=455, y=730, name="text1")
    c.acroForm.textfield(height=18, width=100, x=455, y=710, name="text2")
    c.acroForm.textfield(height=18, width=100, x=455, y=690, name="text3")
    c.acroForm.textfield(height=18, width=100, x=455, y=670, name="text4")
    c.drawString(455, 620, "FT:  Y           N")
    c.acroForm.checkbox(size=20, x=490, y=615, name="checkbox1")
    c.acroForm.checkbox(size=20, x=535, y=615, name="checkbox2")
    c.drawString(454, 596, "TH:  Y           N")
    c.acroForm.checkbox(size=20, x=490, y=590, name="checkbox3")
    c.acroForm.checkbox(size=20, x=535, y=590, name="checkbox4")
    c.showPage()
    c.save()

    # Get the output canvas content from the BytesIO object
    output_pdf_data = output_stream.getvalue()
    output_pdf = PyPDF4.PdfFileWriter()

    # Add the modified page to the output PDF
    page.mergePage(PyPDF4.PdfFileReader(BytesIO(output_pdf_data)).getPage(0))
    output_pdf.addPage(page)
    with open("degree_plan.pdf", 'wb') as f:
        output_pdf.write(f)

    # View the file
    subprocess.Popen(["degree_plan.pdf"], shell=True)

if __name__ == "__main__":
    launch_pdf()