import re

NBSP = "\u00A0"


class Typograph():
    def __init__(self, text):
        self.typographed_text = self.get_typographed_text(text)

    def replace_quotes(self, text):
        return re.sub(r'([\'"])(.*?)(\1)', r'«\2»', text)

    def replace_dashes(self, text):
        text = re.sub(r' - ', r' – ', text)
        return text

    def replace_telephone_number_delimiters(self, text):
        return re.sub(
            r'\b[\+\(]?(\d)[-\s+\(]?(\d{2,3})[-\s+\)]?\s?'
            r'(\d{2,3})[-\s]?(\d{1,3})[-\s]?(\d+)\b',
            r'\1(\2)\3–\4–\5',
            text)

    def delete_extra_spaces_and_lines(self, text):
        return re.sub(r'\s{2,}', r' ', text)

    def link_word_to_number(self, text):
        return re.sub(
            r'([а-яА-Яa-zA-Z.]+)\s?(\d+)',
            r'\1{}\2'.format(NBSP),
            text)

    def link_number_to_word(self, text):
        return re.sub(
            r'(\d+)\s?([а-яА-Яa-zA-Z.]+)',
            r'\1{}\2'.format(NBSP),
            text)

    def link_short_word_to_next_word(self, text):
        return re.sub(
            r'(\s+[а-яА-Яa-zA-Z]{1,2})\s+',
            r'\1{}'.format(NBSP),
            text)

    def get_typographed_text(self, text):
        text = self.delete_extra_spaces_and_lines(text)
        text = self.replace_quotes(text)
        text = self.replace_dashes(text)
        text = self.replace_telephone_number_delimiters(text)
        text = self.link_short_word_to_next_word(text)
        text = self.link_word_to_number(text)
        text = self.link_number_to_word(text)
        return text
