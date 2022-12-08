from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import serial
import time

class ActionArduinoTest(Action):

     def name(self) -> Text:
         return "action_arduino_test"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
         for i in range(10):
             with serial.Serial('COM7', 57600, timeout=1) as ser:
                 time.sleep(0.5)
                 ser.write('H'.encode('utf-8'))   # send the pyte string 'H'
                 dispatcher.utter_message(text="1")
                 time.sleep(0.5)   # wait 0.5 seconds
                 ser.write('L'.encode('utf-8'))   # send the byte string 'L'
                 dispatcher.utter_message(text="2!")
         
         return []