import pdfplumber


def remove_label(text, label):
    label_length = len(label)
    removed_text = text[label_length:]
    return removed_text.strip()


class Transcript:
    def __init__(self, path_to_pdf):
        self.transcript = pdfplumber.open(path_to_pdf)


    def get_student_name(self):
        first_page_words = self._get_first_page_words()

        for word in first_page_words:
            text = word['text']
            if text.startswith("Name:"):
                return remove_label(text, label="Name:")

        raise Exception("Student Name Not Found!")


    def _get_first_page_words(self):
        first_page = self._get_first_page()
        first_page_words = first_page.extract_words(x_tolerance=30, y_tolerance=3, keep_blank_chars=True, use_text_flow=False, horizontal_ltr=True, vertical_ttb=True, extra_attrs=[], split_at_punctuation=False)
        return first_page_words


    def _get_first_page(self):
        return self.transcript.pages[0]
