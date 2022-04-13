class Song():
    def __init__(self, singer: str, name: str, time: str, ft: None):
        self.singer = singer
        self.name = name
        self.time = time
        self.ft = ft

    def show(self):
        if self.ft == None:
            return f'{self.singer} -> {self.name} - {self.time}'
        else:
            return f'{self.singer}, ft. {self.ft} -> {self.name} - {self.time}'