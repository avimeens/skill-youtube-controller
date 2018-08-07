from mycroft import MycroftSkill, intent_handler

def sox_fmt(seconds):
    # sox format hh:mm:ss.frac
    # h = int(seconds // 3600)
    # m = int((seconds // 60) % 60)
    # s = seconds % 60
    out = '{:02d}:{:02d}:{:f}'.format(int(seconds // 3600),
                                      int((seconds // 60) % 60), 
                                      seconds % 60) 
    return out

class YoutubeControllerSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self._p = None
        self._start = None
        self._uri = None

    def initialize(self):
        self.register_rasa_intent('search.json', self.handle_youtube_search)
        self.register_rasa_intent('rewind.json', self.handle_rewind)

    def handle_youtube_search(self, message):
        query = message.data.get("query")
        if query is None:
            self.speak_dialog('no.query')
            return
        resp = {'query': query}
        self.speak_dialog('search.confirm', data=resp)
        # download the file first
        self.play("air-filter.wav")

    def handle_rewind(self, message):
        time = messge.data.get("time")
        if time is None:
            self.speak_dialog('no.time')
            return
        if (time == 'start'):
            self.speak_dialog("Restarting the audio from the beginning")
            return
        unit = message.data.get("unit")
        if unit is None:
            self.speak_dialog('no.unit')
            return
        resp = {'time': time, 'unit' : unit}
        self.speak_dialog('rewind.confirm', data=resp)

    def play(self, file1, start=0, stop=0):
        '''Play a portion of a file given start and
        stop locations in fractional seconds.'''
        self._uri = file1
        self.jump_to(start, stop)

    def jump_to(self, start, stop=0):
        '''Play a portion of a file given start and
        stop locations in fractional seconds.'''
        if start < 0 or stop < 0:
            raise ValueError('negative start or stop')
        self.stop()
        args = ['play', self._uri, 'trim', sox_fmt(start)]
        if stop > 0:
            args.append('=' + sox_fmt(stop)) 
        self._p = Popen(args) 
        self._start = monotonic() - start

    def jump(self, seconds, duration=0):
        '''Play a portion of a file given an +/- offset
        and duration in fractional seconds.'''
        if duration < 0:
            raise ValueError('negative duration')
        at = monotonic() - self._start
        to = at + seconds
        if to < 0:
            to = 0
        self.jump_to(to, to + duration if duration else 0)

    def stop(self):
        if self._p:
            if self._p.returncode is None:
                self._p.terminate()
            self._p = None
        pass

def create_skill():
    return YoutubeControllerSkill()

