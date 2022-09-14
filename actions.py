# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import random

class ActionGuessing(Action):
   
    def name(self) -> Text:
        return "action_guessing"
 
    def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        animal_list = ["cat", "dog", "snake", "parrot", "tardigrade"]
        random_animal = random.choice(animal_list)
        print(random_animal)

        return [SlotSet(key = "animal", value = random_animal)]

class ActionColorAsk(Action):
   
    def name(self) -> Text:
        return "action_color_ask"
 
    def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        color_dict = {"cat" : "black",
                "dog" : "brown",
                "snake": "yellow",
                "parrot": "red",
                "tardigrade":"white"}

        asked_color = tracker.get_slot("color") #color slot asked by the user
        random_animal = tracker.get_slot("animal")
        dispatcher.utter_message(text=f"You asked if the animal is {asked_color}.")

        if asked_color in color_dict[random_animal]:
            dispatcher.utter_message(text=f"And it is correct, the animal is {asked_color}.")
        else:
            dispatcher.utter_message(text=f"But it is not correct, the animal is not {asked_color}.")

class ActionBodypartsAsk(Action):
   
    def name(self) -> Text:
        return "action_bodyparts_ask"
 
    def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        bodyparts_dict = {"cat" : "fur",
                "dog" : "fur",
                "snake": "fangs",
                "parrot": "wings",
                "tardigrade":"a snout"}
        #print("pppppppppppppppppppp")
        asked_bodyparts = tracker.get_slot("bodyparts") #color slot asked by the user
        random_animal = tracker.get_slot("animal")
        dispatcher.utter_message(text=f"You asked if the animal has {asked_bodyparts}.")
        #print(random_animal, asked_bodyparts, "treti vec")
        if asked_bodyparts in bodyparts_dict[random_animal]:
            dispatcher.utter_message(text=f"And it is correct, the animal has {asked_bodyparts}.")
        else:
            dispatcher.utter_message(text=f"But it is not correct, the animal does not have {asked_bodyparts}.")

class ActionBehaviorAsk(Action):
   
    def name(self) -> Text:
        return "action_behavior_ask"
 
    def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        behavior_dict = {"cat" : "meow",
                "dog" : "bark",
                "snake": "hiss",
                "parrot": "sing",
                "tardigrade":"swim"}

        asked_behavior = tracker.get_slot("behavior") #color slot asked by the user
        random_animal = tracker.get_slot("animal")
        dispatcher.utter_message(text=f"You asked if the animal {asked_behavior}s.")
        
        if asked_behavior in behavior_dict[random_animal]:
            dispatcher.utter_message(text=f"And it is correct, the animal does {asked_behavior}.")
        else:
            dispatcher.utter_message(text=f"But it is not correct, the animal does {asked_behavior}.")