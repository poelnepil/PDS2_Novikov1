class TextProcessor(object):
    def __init__(self):
        self._punk = ',()-[]{};?@#$%:\./^&;*_!'

    def __is_punktuation(self, char):
        if char in self._punk:
            return False
        else:
            return True

    def get_clean_string(self, text):
        clean_text = ''
        for i in text:
            if self.__is_punktuation(i) == False:
                continue
            else:
                clean_text += i
        return clean_text


b = TextProcessor()
print(b.get_clean_string('h/i, my na!!!me i###s I]v@@an!'))

class TextLoader(object):
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = ''

    @property
    def text_processor(self):
        return self.__text_processor

    @property
    def clean_string(self):
        print('cleared text output:')
        return self.__clean_string

    def set_clean_text(self, text1):
        self.__clean_string = self.__text_processor.get_clean_string(text1)
        return self.__clean_string


n = TextLoader()
n.set_clean_text('h/i, my na!!!me i###s I]v@@an!')
print(n.clean_string)

class DataInterface(object):
    def __init__(self):
        self._atr = TextLoader()

    def process_texts(self, list):
        c = []
        for i in list:
            w = self._atr.set_clean_text(i)
            c.append(w)
        return c


q = DataInterface()
print(*q.process_texts(['!@#a', '!@#b', '!#c']))

