import subprocess
import PyPDF4
import degree_requirements
import transcript
from io import BytesIO
from course_finder import get_courses
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, portrait
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Spacer, Table, TableStyle, Paragraph
from reportlab.pdfgen import canvas

def plan_printer(path, gui_entry):
    fast_track = gui_entry[0]
    thesis = gui_entry[1]
    grad = gui_entry[2]
    track_value = gui_entry[3]
    track = degree_requirements.DegreePlans().get_libraries(track_value)

    # General Student
    student_info = transcript.Transcript(path)
    student_name = student_info.get_name()
    student_id = student_info.get_id()
    admit = student_info.get_beginning_of_graduate_record()

    # Student Credit
    courses = get_courses(path)

    # Track Information
    track_name = track['Name']
    track_update = track['Update']
    track_color = track['Color']
    track.pop('Name')
    track.pop('Update')
    track.pop('Color')

    # Define Styles
    title_style = ParagraphStyle(name='Title', fontSize=9, alignment=1, leading=12)
    subtitle_style = ParagraphStyle(name='Subtitle', fontSize=9, alignment=1, leading=12)
    info_style = ParagraphStyle(name='StudentInfo', fontSize=8, alignment=0, leading=12)
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), track_color),  # header row
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # all other rows
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),  # header row
        ('FONTSIZE', (0, 0), (-1, -1), 8),  # all other rows
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])

    # Create a new PDF document with landscape page orientation
    elements = []
    pdf = SimpleDocTemplate("degree_plan.pdf",
                            pagesize=portrait(letter),
                            leftMargin=50,
                            rightMargin=50,
                            topMargin=40,
                            bottomMargin=40)

    # Define student info
    elements.append(Paragraph("<b>DEGREE PLAN<br/>"
                              "UNIVERSITY OF TEXAS AT DALLAS<br/>"
                              "MASTER OF COMPUTER SCIENCE</b>", style=title_style))
    elements.append(Spacer(1, 4))
    elements.append(Paragraph("<b>{}</b><br/>"
                              "({})".format(track_name, track_update), style=subtitle_style))
    elements.append(Spacer(1, 4))
    elements.append(Paragraph("Name of Student: {}<br/>"
                              "Student I.D. number: {}<br/>"
                              "Semester Admitted: {}<br/>"
                              "Anticipated Graduation: {}".format(student_name, student_id, admit, grad), style=info_style))
    elements.append(Spacer(1, 4))

    # Define Elements
    for entry in track:
        try:
            keys = track[entry].keys()
            data = [["                            Course Name                            ",
                     "       Course ID       ",
                     "       Semester        ",
                     "        Credit         ",
                     "         Grade         "]]
            for key in keys:
                line = [key, track[entry][key]]
                for credit in courses:
                    if str(track[entry][key]) == str(credit['course_id']):
                        line.append(str(credit['season'] + " " + str(credit['year'])))
                        line.append(credit['earned'])
                        line.append(credit['grade'])
                        courses.remove(credit)
                        break
                data.append(line)
            table = Table(data)
            table.setStyle(table_style)
            elements.append(table)
            elements.append(Spacer(1, 4))
        except AttributeError:
            try:
                track[entry].sort()
                data = [["                            Course Name                            ",
                         "       Course ID       ",
                         "       Semester        ",
                         "        Credit         ",
                         "         Grade         "]]
                for slot in track[entry]:
                    found = False
                    for credit in courses:
                        if int(slot) < int(credit['course_id'][-4:]):
                            data.append([credit['course_name'],
                                         credit['course_id'],
                                         str(credit['season'] + " " + str(credit['year'])),
                                         credit['earned'],
                                         credit['grade']])
                            courses.remove(credit)
                            found = True
                            break
                    if not found:
                        data.append(['', '', '', '', ''])
                table = Table(data)
                table.setStyle(table_style)
                elements.append(table)
                elements.append(Spacer(1, 4))
            except AttributeError:
                elements.append(Paragraph(track[entry].format(), style=info_style))
    pdf.build(elements)

    # Create canvas objects
    output_stream = BytesIO()
    c = canvas.Canvas(output_stream, pagesize=letter)
    c.acroForm.textfield(height=18, width=100, x=455, y=730, name="text1")
    c.acroForm.textfield(height=18, width=100, x=455, y=710, name="text2")
    c.acroForm.textfield(height=18, width=100, x=455, y=690, name="text3")
    c.acroForm.textfield(height=18, width=100, x=455, y=670, name="text4")
    c.drawString(455, 640, "FT:           TH:")
    c.acroForm.checkbox(size=20, x=480, y=635, name="fastrack", checked=fast_track)
    c.acroForm.checkbox(size=20, x=535, y=635, name="Thesis", checked=thesis)
    c.showPage()
    c.save()

    # Get the output canvas content from the BytesIO object
    output_pdf_data = output_stream.getvalue()
    output_pdf = PyPDF4.PdfFileWriter()

    # Add the modified page to the output PDF
    input_pdf = PyPDF4.PdfFileReader(open("degree_plan.pdf", 'rb'))
    for page in input_pdf.pages:
        if page == input_pdf.getPage(0):
            page.mergePage(PyPDF4.PdfFileReader(BytesIO(output_pdf_data)).getPage(0))
            output_pdf.addPage(page)
        else:
            output_pdf.addPage(page)
    with open("degree_plan.pdf", 'wb') as f:
        output_pdf.write(f)

    # View the file
    subprocess.Popen(["degree_plan.pdf"], shell=True)