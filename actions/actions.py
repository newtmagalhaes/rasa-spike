# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import (ActionExecuted, ActiveLoop, BotUttered, EventType,
                             FollowupAction, SessionStarted, SlotSet)
from rasa_sdk.executor import CollectingDispatcher

from .constants.messages import ASK_PIZZA_SIZE, DEFAULT_GREETINGS
from .constants.pizza_sizes import PIZZA_BUTTONS


class ActionSessionStart(Action):
    # overrides default action
    def name(self) -> Text:
        return "action_session_start"

    @staticmethod
    def fetch_slots(tracker: Tracker) -> List[EventType]:
        """Collect slots that contain the user's name and phone number."""
        slots = []
        for key in ("pizza_size", "pizza_flavour"):
            value = tracker.get_slot(key)
            if value is not None:
                slots.append(SlotSet(key=key, value=value))
        return slots

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[EventType]:
        # the session should begin with a `session_started` event
        events = [SessionStarted()]

        # any slots that should be carried over should come after the
        # `session_started` event
        events.extend(self.fetch_slots(tracker))

        # an `action_listen` should be added at the end as a user message follows
        utter_greet = domain.get("responses", {}).get("utter_greet", DEFAULT_GREETINGS)
        events.extend((
            ActionExecuted("action_listen"),
            BotUttered(utter_greet),
            FollowupAction("pizza_form"),
            ActiveLoop("pizza_form"),
        ))
        return events


class ActionAskPizzaSize(Action):
    def name(self) -> Text:
        return "action_ask_pizza_size"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=ASK_PIZZA_SIZE, buttons=PIZZA_BUTTONS)

        return []
