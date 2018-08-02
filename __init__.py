from mycroft import MycroftSkill, intent_handler


class YoutubeControllerSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

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

    def handle_rewind(self, message):
        time = messge.data.get("time")
        if time is None:
            self.speak_dialog('no.time')
            return
        if (time == 'start')
            self.speak_dialog("Restarting the audio from the beginning")
            return
        unit = message.data.get("unit")
        if unit is None:
            self.speak_dialog('no.unit')
            return
        resp = {'time': time, 'unit' : unit}
        self.speak_dialog('rewind.confirm', data=resp)

def create_skill():
    return YoutubeControllerSkill()

