class Song():
    def __init__(self, singer: str, name: str, time: str, ft: None):
        self.singer = singer
        self.name = name
        self.time = time
        self.ft = ft

    def show(self):
        if self.ft == None:
            return f'Now playing {self.name} by {self.singer}: [{self.time}]'
        else:
            return f'Now Playing {self.name} by {self.singer}, ft. {self.ft}: [{self.time}]'