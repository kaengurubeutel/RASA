from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ValidateOrganForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_organs_form"

    @staticmethod
    def organs_db() -> List[Text]:

        return ["Ear", "Nose"," Eye", "Skin", "Tounge", "Brain", "Salivary glands", "Parotid glands", "Submandibular glands", "Sublingual glands", "Pharynx", "Esophagus", "Stomach", "Small intestine", "Duodenum", "Jejunum", "Ileum", "Large intestine", "Liver", "Gallbladder", "Mesentery", "Pancreas"]

    def validate_organs(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        if slot_value.lower() in self.organs_db():
            # validation succeeded, set the value of the "organ" slot to value
            return {"fav_organ": slot_value}
        else:
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return {"fav_organ": None}