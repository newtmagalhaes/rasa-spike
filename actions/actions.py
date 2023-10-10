# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from .constants.pizza_sizes import PIZZA_SIZES, PT_PIZZA_SIZES
from .constants.messages import ASK_PIZZA_SIZE

PIZZA_BUTTONS = [
    {"title": name, "payload": value}
    for name, value in zip(PT_PIZZA_SIZES, PIZZA_SIZES)
]


class ActionAskPizzaSize(Action):

    def name(self) -> Text:
        return "action_ask_pizza_size"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=ASK_PIZZA_SIZE, buttons=PIZZA_BUTTONS)

        return []
