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
        first_page_words = self._get_first_page_words()

        for word in first_page_words:
            text = word['text']
            if text.startswith("Student ID:"):
                return remove_label(text, label="Student ID:")

        raise Exception("Student ID Not Found!")


    def _get_first_page_words(self):
        first_page = self._get_first_page()
        first_page_words = first_page.extract_words(x_tolerance=30, keep_blank_chars=True)

        return first_page_words


    def _get_first_page(self):
        return self.transcript.pages[0]
