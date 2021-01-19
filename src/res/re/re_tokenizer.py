class RETokenizer:
    def __init__(self, doc: str):
        self.tokens = list(doc) + ["EOF"]
        self.cur_char_index = -1

    def __next__(self):
        self.cur_char_index += 1
        return self.tokens[self.cur_char_index]
