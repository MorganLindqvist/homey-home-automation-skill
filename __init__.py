from mycroft import MycroftSkill, intent_file_handler


class HomeyHomeAutomation(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('automation.home.homey.intent')
    def handle_automation_home_homey(self, message):
        self.speak_dialog('automation.home.homey')


def create_skill():
    return HomeyHomeAutomation()

