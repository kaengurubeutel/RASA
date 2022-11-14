from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



class ActionGiveSlot(Action):

     def name(self) -> Text:
         return "action_give_slot"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         slot = tracker.get_Slot("fav_organ")
         dispatcher.utter_message(text="This is the slot: " + {slot})
         
         return []