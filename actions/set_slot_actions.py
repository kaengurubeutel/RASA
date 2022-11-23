from typing import Any, Text, Dict, List

from rasa.sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



class ActionGiveSlot(Action):

     def name(self) -> Text:
         return "action_set_slot"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         organ = tracker.latest_message("fav_organ")
         dispatcher.utter_message(text=f"This is the organ: {organ}")
         
         return [SlotSet("fav_organ", organ)]