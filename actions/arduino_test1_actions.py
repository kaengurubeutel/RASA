from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import serial
import time

class ActionArduinoTest1(Action):

     def name(self) -> Text:
         return "action_arduino_test1"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
         serialcomm = serial.Serial('COM3', 57600, timeout=1)
         i = 0
         while True:
             serialcomm.write('ACTION_1'.encode())
             time.sleep(0.5)
             s = serialcomm.readline().decode('ascii')

             i = i+1
             if s:
                print(s)

             if i==4:
                time.sleep(1)
                dispatcher.utter_message(text=''+s)
                break
             if s=="off":
                break
         
         return []