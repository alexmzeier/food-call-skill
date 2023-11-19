from va import MycroftSkill, intent_handler
from va.adapt.intent import IntentBuilder
from va.skills.context import adds_context, removes_context
from va.dataModel import UserSkillMetis
from va import Message

import requests

def create_skill(skill_data: UserSkillMetis):
    return FoodCall(skill_data)

class FoodCall(MycroftSkill):
    def __init__(self, skill_data: UserSkillMetis):
        MycroftSkill.__init__(self, skill_data=skill_data)

    @intent_handler(IntentBuilder("FoodCallHelper").require("trigger"))
    def handle_call(self, message, websocket):
        call_api = skill_api(self.skill_data.identifier, self.skill_data.api_key, self.skill_data.skill_data, message.data["utterance"])
        print('result call api ' + call_api)
        print('Message Data Utterance ' + message.data["utterance"])
        self.speak('Ich habe das Personal benachrichtigt, dass Sie etwas benötigen', websocket=websocket)




def skill_api(identifier: str, api_key: str, skill_data:str, text: str):
    print ('skill_api')
    #payload = {'customer_id' : data.customer_id, 'api_key': data.api_key}
    payload = {
        'identifier': identifier,
        'api_key': api_key,
        'skill_data':skill_data,
        'utterance': text
    }
    #response = requests.get(url=skill.auth_skill_url, params=payload, json=dataRequest)
    response = requests.post(url="http://85.215.193.214:8001/api/skill/food-call", params=payload)
    print("request status code " + str(response.status_code))
    print('skills ' + str(response.text))
        
    if response.status_code == 200:
        #skill = add_skill_organistaion(user, data, db)                    
        return str(response.text)
    else:
        return None
