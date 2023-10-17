from mycroft import MycroftSkill, intent_file_handler


class FoodCall(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('call.food.intent')
    def handle_call_food(self, message):
        self.speak_dialog('call.food')


def create_skill():
    return FoodCall()

