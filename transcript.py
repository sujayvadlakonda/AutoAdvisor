import pdfplumber
import re


class Transcript:
    def __init__(self, path_to_pdf):
        self.text = ''

        with pdfplumber.open(path_to_pdf) as pdf:
            for page in pdf.pages:
                self.text += page.extract_text()


    def get_name(self):
        match = re.search(r"^Name.*$", self.text, flags=re.MULTILINE)
        name = match.group()
        name = re.sub(r"Name: ", "", name)
        return name


    def get_id(self):
        match = re.search(r"^Student ID.*$", self.text, flags=re.MULTILINE)
        id = match.group()
        id = re.sub(r"Student ID: ", "", id)
        return id
