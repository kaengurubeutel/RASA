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
        
         run()
             with serial.Serial('COM7', 57600, timeout=1) as ser:
                 ser.write(bytes('TEST', 'utf-8'))
                 time.sleep(0.5)
                 ser.write(bytes('H', 'utf-8'))   # send the pyte string 'H'
                 time.sleep(0.5)   # wait 0.5 seconds
                 ser.write(bytes('L', 'utf-8'))   # send the byte string 'L'
         
         return []