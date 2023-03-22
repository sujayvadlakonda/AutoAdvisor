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


    def get_major(self):
        match = re.search(r"^.*Major$", self.text, flags=re.MULTILINE)
        major = match.group()
        major = re.sub(r"^.*:", "", major).strip()
        major = self._split_camel_case(major)
        return major


    # https://stackoverflow.com/questions/199059/a-pythonic-way-to-insert-a-space-before-capital-letters
    # Some pdfs don't split camel case. Mike Modano is an example
    def _split_camel_case(self, text):
        return re.sub(r"(?<=\w)([A-Z])", r" \1", text)
