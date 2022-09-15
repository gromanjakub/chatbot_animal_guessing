from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from word2number import w2n
import random


class ActionGuessing(Action): #this class chooses a random animal from a list and fills the "animal" slot with it

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

            return [SlotSet(key="animal", value=random_animal)]
        else:
            pass


class ActionColorAsk(Action): #this class handles the user's questions about the color

    def name(self) -> Text:
        return "action_color_ask"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        color_dict = {"cat": "black",
                      "dog": "brown",
                      "snake": "yellow",
                      "parrot": "red",
                      "tardigrade": "white"}

        asked_color = tracker.get_slot("color")  # color slot asked by the user
        random_animal = tracker.get_slot("animal")

        dispatcher.utter_message(
            text=f"You asked if the animal is {asked_color}.")

        if asked_color in color_dict[random_animal]:
            dispatcher.utter_message(
                text=f"And it is correct, the animal is {asked_color}.")
        else:
            dispatcher.utter_message(
                text=f"But it is not correct, the animal is not {asked_color}.")


class ActionBodypartsAsk(Action): #this class handles the user's questions about the body parts

    def name(self) -> Text:
        return "action_bodyparts_ask"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        bodyparts_dict = {"cat": "fur",
                          "dog": "fur",
                          "snake": "fangs",
                          "parrot": "wings",
                          "tardigrade": "a snout"}
        asked_bodyparts = tracker.get_slot(
            "bodyparts")  
        random_animal = tracker.get_slot("animal")
        dispatcher.utter_message(
            text=f"You asked if the animal has {asked_bodyparts}.")
        if asked_bodyparts in bodyparts_dict[random_animal]:
            dispatcher.utter_message(
                text=f"And it is correct, the animal has {asked_bodyparts}.")
        else:
            dispatcher.utter_message(
                text=f"But it is not correct, the animal does not have {asked_bodyparts}.")


class ActionBehaviorAsk(Action): #this class handles the user's questions about the behavior

    def name(self) -> Text:
        return "action_behavior_ask"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        behavior_dict = {"cat": "meow",
                         "dog": "bark",
                         "snake": "hiss",
                         "parrot": "sing",
                         "tardigrade": "swim"}

        asked_behavior = tracker.get_slot(
            "behavior")  
        random_animal = tracker.get_slot("animal")
        dispatcher.utter_message(
            text=f"You asked if the animal {asked_behavior}s.")

        if asked_behavior in behavior_dict[random_animal]:
            dispatcher.utter_message(
                text=f"And it is correct, the animal does {asked_behavior}.")
        else:
            dispatcher.utter_message(
                text=f"But it is not correct, the animal does not {asked_behavior}.")


class ActionLegsAsk(Action): #this class handles the user's questions about the legs

    def name(self) -> Text:
        return "action_legs_ask"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        legnum_dict = {"cat": 4,
         "dog": 4,
         "snake": 0,
         "parrot": 2,
         "tardigrade": 8}
        random_animal = tracker.get_slot("animal")

        asked_legs = tracker.get_slot("legs") 
        actual_legs = legnum_dict[random_animal]
        if str(asked_legs) in "how many How many":
            dispatcher.utter_message(text=f"You asked how many legs does the animal have.")
            dispatcher.utter_message(text=f"The animal has {actual_legs} legs.")
           
        else:
            if type(asked_legs) != int:
                asked_legs = w2n.word_to_num(asked_legs)
            
        
            

            dispatcher.utter_message(
                text=f"You asked if the animal has {asked_legs} legs.")

            if asked_legs == legnum_dict[random_animal]:
                dispatcher.utter_message(
                    text=f"And it is correct, the animal does have {asked_legs} legs.")
            else:
                if int(asked_legs) > int(legnum_dict[random_animal]):
                    dispatcher.utter_message(
                        text=f"But it is not correct, the animal has less than {asked_legs} legs.")
                else:
                    dispatcher.utter_message(
                        text=f"But it is not correct, the animal has more than {asked_legs} legs.")


class ActionAnimalAsk(Action): #this class handles the user's guesses of the specific animal

    def name(self) -> Text:
        return "action_animal_ask"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        animal_name = tracker.get_slot("animal")
        guessed_animal_name = tracker.get_slot("guessed_animal")
        dispatcher.utter_message(
            text=f"You asked if the animal is {guessed_animal_name}.")

        if guessed_animal_name == animal_name:
            dispatcher.utter_message(
                text=f"Congratulations, you guessed it correctly, it is a {guessed_animal_name} indeed.")
            dispatcher.utter_message(text=f"Say 'Hello' to play again.")
            return [SlotSet(key="animal", value=" ")]
        else:
            dispatcher.utter_message(
                text=f"But it is not correct, the animal is not {guessed_animal_name}.")
