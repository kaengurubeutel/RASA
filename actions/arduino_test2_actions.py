from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import serial
import time

class ActionArduinoTest1(Action):

     def name(self) -> Text:
         return "action_arduino_test2"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
         serialcomm = serial.Serial('COM3', 57600, timeout=1)
         while True:
             serialcomm.write('L'.encode())
             time.sleep(0.5)
             s = serialcomm.readline().decode('ascii')
             #serialcomm.write(bytes('H', 'utf-8'))   # send the pyte string 'H'
             #serialcomm.write(bytes('L', 'utf-8'))   # send the byte string 'L'
             #serialcomm.write(b'\r\n')
             dispatcher.utter_message(text=''+s)
             if s=="off":
                break
         
         return []