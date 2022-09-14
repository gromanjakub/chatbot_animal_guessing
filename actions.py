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
from word2number import w2n
import random

class ActionGuessing(Action):
   
    def name(self) -> Text:
        return "action_guessing"
 
    def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        random_animal_check = tracker.get_slot("animal")
        if (random_animal_check not in ["cat", "dog", "snake", "parrot", "tardigrade"]):

            animal_list = ["cat", "dog", "snake", "parrot", "tardigrade"]
        
            random_animal = random.choice(animal_list)
            #print("vybiram random animal, je to "+ random_animal)
        

            return [SlotSet(key = "animal", value = random_animal)]
        else:
            pass

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

class ActionLegsAsk(Action):
   
    def name(self) -> Text:
        return "action_legs_ask"
 
    def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:



        asked_legs = tracker.get_slot("legs") #color slot asked by the user
        if type(asked_legs) != int:
            asked_legs = w2n.word_to_num(asked_legs)
        else:
            pass
        
        legnum_dict = {"cat" : 4,
                "dog" : 4,
                "snake": 0,
                "parrot": 2,
                "tardigrade":8}

        random_animal = tracker.get_slot("animal")

        dispatcher.utter_message(text=f"You asked if the animal has {asked_legs} legs.")
        
        if asked_legs == legnum_dict[random_animal]:
            dispatcher.utter_message(text=f"And it is correct, the animal does have {asked_legs} legs.")
        else:
            if asked_legs > legnum_dict[random_animal]:
                dispatcher.utter_message(text=f"But it is not correct, the animal has less than {asked_legs} legs.")
            else:
                dispatcher.utter_message(text=f"But it is not correct, the animal has more than {asked_legs} legs.")


class ActionAnimalAsk(Action):
   
    def name(self) -> Text:
        return "action_animal_ask"
 
    def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        animal_name = tracker.get_slot("animal")
        guessed_animal_name = tracker.get_slot("guessed_animal")
        dispatcher.utter_message(text=f"You asked if the animal is {guessed_animal_name}.")
        
        if guessed_animal_name == animal_name:
            dispatcher.utter_message(text=f"Congratulations, you guessed it correctly, it is a {guessed_animal_name} indeed.")
            dispatcher.utter_message(text=f"Say 'Hello' to play again.")
            return [SlotSet(key = "animal", value = None)]
        else:
            dispatcher.utter_message(text=f"But it is not correct, the animal is not {guessed_animal_name}.")