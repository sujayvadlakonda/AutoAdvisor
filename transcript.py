import pdfplumber


def remove_label(text, label):
    label_length = len(label)
    removed_text = text[label_length:]
    return removed_text.strip()


class Transcript:
    def __init__(self, path_to_pdf):
        self.pdf = pdfplumber.open(path_to_pdf)
        self.lines = self._construct_lines()


    def get_student_name(self):
        for line in self.lines:
            if line.startswith("Name:"):
                return remove_label(line, label="Name:")


        raise Exception("Student Name Not Found!")


    def get_student_id(self):
        for line in self.lines:
            if line.startswith("Student ID:"):
                return remove_label(line, label="Student ID:")


        raise Exception("Student ID Not Found!")


    def close(self):
        self.pdf.close()


    def _construct_lines(self):
        lines = []

        for page in self.pdf.pages:
            for line in page.extract_words(x_tolerance=30, keep_blank_chars=True):
                lines.append(line['text'])

        return lines
