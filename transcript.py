import pdfplumber


def remove_label(text, label):
    label_length = len(label)
    removed_text = text[label_length:]
    return removed_text.strip()


class Transcript:
    def __init__(self, path_to_pdf):
        self.transcript = pdfplumber.open(path_to_pdf)


    def get_student_name(self):
        first_page = self._get_first_page()
        first_page_lines = first_page.get_lines()

        for line in first_page_lines:
            text = line['text']
            if text.startswith("Name:"):
                return remove_label(text, label="Name:")

        raise Exception("Student Name Not Found!")


    def get_student_id(self):
        first_page = self._get_first_page()
        first_page_lines = first_page.get_lines()

        for line in first_page_lines:
            text = line['text']
            if text.startswith("Student ID:"):
                return remove_label(text, label="Student ID:")

        raise Exception("Student ID Not Found!")


    def close(self):
        self.transcript.close()


    def _get_first_page(self):
        return self._get_page(0)


    def _get_page(self, page_number):
        return TranscriptPage(self.transcript.pages[page_number])



class TranscriptPage:
    def __init__(self, page):
        self.page = page


    def get_lines(self):
        return self.page.extract_words(x_tolerance=30, keep_blank_chars=True)
