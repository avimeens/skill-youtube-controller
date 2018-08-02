from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class YoutubeControllerSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder().require('YoutubeController'))
    def handle_youtube_controller(self, message):
        self.speak_dialog('youtube.controller')


def create_skill():
    return YoutubeControllerSkill()

