# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionCoronaTracker(Action):

     def name(self) -> Text:
         return "action_corona_tracker"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get("https://api.covid19india.org/data.json").json()

        entities = tracker.latest_message['entities']
        print("Last Message Now ", entities)
        state = None
        for e in entities:
            if e['entity'] == "state":
                state = e['value']

        message = "Please enter correct state name"

        if state == "india":
            state = "Total"

        if state == "mp":
            state = "Madhya Pradesh"

        if state == "ap":
            state = "Andhra Pradesh"

        if state == "ar":
            state = "Arunachal Pradesh"

        if state == "hp":
            state = "Himachal Pradesh"

        if state == "jk":
            state = "Jammu and Kashmir"

        if state == "j&k":
            state = "Jammu and Kashmir"

        if state == "up":
            state = "Uttar Pradesh"

        if state == "wb":
            state = "West Bengal"

        for data in response["statewise"]:
            if data["state"] == state.title():
                print(data)
                message = "Confirmed: " + data["confirmed"] + " Active: " + data["active"] + " Recovered: " + data["recovered"] + " Deaths: "+ data["deaths"]+ " as On " + data["lastupdatedtime"]
            if data["state"].__contains__(' and ') and state.__contains__(' and '):
                state1 = list(data["state"].split())
                state2 = list(state.split())
                if state1[1] == state2[1] and state1[0] == str(state2[0]).title():
                    print(data)
                    message = "Confirmed: " + data["confirmed"] + " Active: " + data["active"] + " Recovered: " + data["recovered"] +" Deaths: "+ data["deaths"]+ " as On " + data["lastupdatedtime"]

        dispatcher.utter_message(text=message)

        return []

class ActionWorldTracker(Action):

     def name(self) -> Text:
         return "action_world_corona"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         response = requests.get("https://api.covid19api.com/summary").json()

         entities = tracker.latest_message['entities']
         print("Last Message Now ", entities)
         Country = None
         for e in entities:
             if e['entity'] == "Country":
                 Country = e['value']

         message = "Please enter correct Country name"

         for data in response["Countries"]:
             if data["Country"] == Country.title():
                 print(data)
                 active=(data["TotalConfirmed"]-data["TotalRecovered"]-data["TotalDeaths"])
                 message = "Confirmed: " + str(data["TotalConfirmed"]) + " Active: " + str(active) + " Recovered: " + str(data[
                     "TotalRecovered"] )+ " Deaths: " + str(data["TotalDeaths"]) + " as On " + str(data["Date"])

             if data["Country"].__contains__(' and ') and Country.__contains__(' and '):
                 Country1 = list(data["Country"].split())
                 Country2 = list(Country.split())
                 if Country1[1] == Country2[1] and Country1[0] == str(Country2[0]).title() and Country1[2] == str(Country2[2]).title() :
                     print(data)
                     active = (data["TotalConfirmed"] - data["TotalRecovered"] - data["TotalDeaths"])
                     message = "Confirmed: " + str(data["TotalConfirmed"]) + " Active: " + str(active) + " Recovered: " + str(data[
                         "TotalRecovered"]) + " Deaths: " + str(data["TotalDeaths"])+ " as On " + str(data["Date"])

             if (data["Country"].__contains__(' of') or data["Country"].__contains__(' of')) and (Country.__contains__(' of ') or Country.__contains__(' of')):
                 Country1 = list(data["Country"].split())
                 Country2 = list(Country.split())
                 if Country1[0] == str(Country2[0]).title() and Country1[1] == str(
                         Country2[1]).title():
                     print(data)
                     active = (data["TotalConfirmed"] - data["TotalRecovered"] - data["TotalDeaths"])
                     message = "Confirmed: " + str(data["TotalConfirmed"]) + " Active: " + str(
                         active) + " Recovered: " + str(data[
                                                            "TotalRecovered"]) + " Deaths: " + str(
                         data["TotalDeaths"]) + " as On " + str(data["Date"])

         dispatcher.utter_message(text=message)

         return []

class ActionGlobal(Action):

     def name(self) -> Text:
         return "action_Global_Count"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         response = requests.get("https://api.covid19api.com/summary").json()

         entities = tracker.latest_message['entities']
         print("Last Message Now ", entities)
         Global = None
         for e in entities:
             if e['entity'] == "Global":
                 Global = e['value']

         data=list()
         for key,value in response["Global"].items():
             print(key)
             if key == "TotalConfirmed":
                 data.append(value)
             if key == "TotalDeaths":
                 data.append(value)
             if key == "TotalRecovered":
                 data.append(value)

         active = (data[0] - data[1] - data[2])
         message = "Confirmed: " + str(data[0]) + " Active: " + str(active) + " Recovered: " + str(data[2]) + " Deaths: " + str(data[1])

         dispatcher.utter_message(text=message)

         return []


class ActionDeathRate(Action):

    def name(self) -> Text:
        return "action_world_deathrate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get("https://api.covid19api.com/summary").json()

        entities = tracker.latest_message['entities']
        print("Last Message Now ", entities)
        Country = None
        for e in entities:
            if e['entity'] == "Country":
                Country = e['value']

        message = "Please enter correct Country name"

        for data in response["Countries"]:
            if data["Country"] == Country.title():
                print(data)
                deathrate = (data["TotalDeaths"]/data["TotalConfirmed"])
                deathrate = deathrate * 100
                print(deathrate)
                message = "Death rate of " + str(data["Country"]) + " is : "+ "{:.2f}".format(deathrate) + "%"

            if data["Country"].__contains__(' and ') and Country.__contains__(' and '):
                Country1 = list(data["Country"].split())
                Country2 = list(Country.split())
                if Country1[1] == Country2[1] and Country1[0] == str(Country2[0]).title() and Country1[2] == str(
                        Country2[2]).title():
                    print(data)
                    deathrate = (data["TotalDeaths"] / data["TotalConfirmed"])
                    deathrate = deathrate * 100
                    print(deathrate)
                    message = "Death rate of " + str(data["Country"]) + " is : " + "{:.2f}".format(deathrate) + "%"

            if (data["Country"].__contains__('of') or data["Country"].__contains__('of')) and (
                    Country.__contains__(' of ') or Country.__contains__(' of')):
                Country1 = list(data["Country"].split())
                Country2 = list(Country.split())
                if Country1[0] == str(Country2[0]).title() and Country1[1] == str(
                        Country2[1]).title():
                    print(data)
                    deathrate = (data["TotalDeaths"] / data["TotalConfirmed"])
                    deathrate = deathrate * 100
                    print(deathrate)
                    message = "Death rate of " + str(data["Country"]) + " is : " + "{:.2f}".format(deathrate) + "%"

        dispatcher.utter_message(text=message)

        return []


class ActionStateDeathRate(Action):

    def name(self) -> Text:
        return "action_State_death_rate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get("https://api.covid19india.org/data.json").json()

        entities = tracker.latest_message['entities']
        print("Last Message Now ", entities)
        state = None
        for e in entities:
            if e['entity'] == "state":
                state = e['value']

        message = "Please enter correct state name"

        if state == "india":
            state = "Total"

        if state == "mp":
            state = "Madhya Pradesh"

        if state == "ap":
            state = "Andhra Pradesh"

        if state == "ar":
            state = "Arunachal Pradesh"

        if state == "hp":
            state = "Himachal Pradesh"

        if state == "jk":
            state = "Jammu and Kashmir"

        if state == "j&k":
            state = "Jammu and Kashmir"

        if state == "up":
            state = "Uttar Pradesh"

        if state == "wb":
            state = "West Bengal"

        for data in response["statewise"]:
            if data["state"] == state.title():
                deathrate= (int(data["deaths"])/int(data["confirmed"]))
                deathrate = deathrate * 100
                print(deathrate)
                message = "Death rate of " + str(data["state"]) + " is : " + "{:.2f}".format(deathrate) + "%"
            if data["state"].__contains__(' and ') and state.__contains__(' and '):
                state1 = list(data["state"].split())
                state2 = list(state.split())
                if state1[1] == state2[1] and state1[0] == str(state2[0]).title():
                    deathrate = (int(data["deaths"]) / int(data["confirmed"]))
                    deathrate = deathrate * 100
                    print(deathrate)
                    message = "Death rate of " + str(data["state"]) + " is : " + "{:.2f}".format(deathrate) + "%"

        dispatcher.utter_message(text=message)

        return []


class ActionGlobalDeathRate(Action):

    def name(self) -> Text:
        return "action_Global_Death_rate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get("https://api.covid19api.com/summary").json()

        entities = tracker.latest_message['entities']
        print("Last Message Now ", entities)
        Global = None
        for e in entities:
            if e['entity'] == "Global":
                Global = e['value']

        data = list()
        for key, value in response["Global"].items():
            print(key)
            if key == "TotalConfirmed":
                data.append(value)
            if key == "TotalDeaths":
                data.append(value)
            if key == "TotalRecovered":
                data.append(value)

        deathrate= (data[1]/data[0])
        deathrate = deathrate * 100
        message = "Global death rate is : " + "{:.2f}".format(deathrate) + "%"

        dispatcher.utter_message(text=message)

        return []

class ActionRecoveryRate(Action):

    def name(self) -> Text:
        return "action_world_Recoveryrate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get("https://api.covid19api.com/summary").json()

        entities = tracker.latest_message['entities']
        print("Last Message Now ", entities)
        Country = None
        for e in entities:
            if e['entity'] == "Country":
                Country = e['value']

        message = "Please enter correct Country name"

        for data in response["Countries"]:
            if data["Country"] == Country.title():
                print(data)
                deathrate = (data["TotalRecovered"]/data["TotalConfirmed"])
                deathrate = deathrate * 100
                print(deathrate)
                message = "Recovery rate of " + str(data["Country"]) + " is : "+ "{:.2f}".format(deathrate) + "%"

            if data["Country"].__contains__(' and ') and Country.__contains__(' and '):
                Country1 = list(data["Country"].split())
                Country2 = list(Country.split())
                if Country1[1] == Country2[1] and Country1[0] == str(Country2[0]).title() and Country1[2] == str(
                        Country2[2]).title():
                    print(data)
                    deathrate = (data["TotalRecovered"] / data["TotalConfirmed"])
                    deathrate = deathrate * 100
                    print(deathrate)
                    message = "Recovery rate of " + str(data["Country"]) + " is : " + "{:.2f}".format(deathrate) + "%"

            if (data["Country"].__contains__('of') or data["Country"].__contains__('of')) and (
                    Country.__contains__(' of ') or Country.__contains__(' of')):
                Country1 = list(data["Country"].split())
                Country2 = list(Country.split())
                if Country1[0] == str(Country2[0]).title() and Country1[1] == str(
                        Country2[1]).title():
                    print(data)
                    deathrate = (data["TotalRecovered"] / data["TotalConfirmed"])
                    deathrate = deathrate * 100
                    print(deathrate)
                    message = "Recovery rate of " + str(data["Country"]) + " is : " + "{:.2f}".format(deathrate) + "%"

        dispatcher.utter_message(text=message)

        return []


class ActionStateRecoveryRate(Action):

    def name(self) -> Text:
        return "action_State_Recovery_rate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get("https://api.covid19india.org/data.json").json()

        entities = tracker.latest_message['entities']
        print("Last Message Now ", entities)
        state = None
        for e in entities:
            if e['entity'] == "state":
                state = e['value']

        message = "Please enter correct state name"

        if state == "india":
            state = "Total"

        if state == "mp":
            state = "Madhya Pradesh"

        if state == "ap":
            state = "Andhra Pradesh"

        if state == "ar":
            state = "Arunachal Pradesh"

        if state == "hp":
            state = "Himachal Pradesh"

        if state == "jk":
            state = "Jammu and Kashmir"

        if state == "j&k":
            state = "Jammu and Kashmir"

        if state == "up":
            state = "Uttar Pradesh"

        if state == "wb":
            state = "West Bengal"

        for data in response["statewise"]:
            if data["state"] == state.title():
                deathrate= (int(data["recovered"])/int(data["confirmed"]))
                deathrate = deathrate * 100
                print(deathrate)
                message = "Recovery rate of " + str(data["state"]) + " is : " + "{:.2f}".format(deathrate) + "%"
            if data["state"].__contains__(' and ') and state.__contains__(' and '):
                state1 = list(data["state"].split())
                state2 = list(state.split())
                if state1[1] == state2[1] and state1[0] == str(state2[0]).title():
                    deathrate = (int(data["recovered"])/int(data["confirmed"]))
                    deathrate = deathrate * 100
                    print(deathrate)
                    message = "Recovery rate of " + str(data["state"]) + " is : " + "{:.2f}".format(deathrate) + "%"

        dispatcher.utter_message(text=message)

        return []


class ActionGlobalRecoveryRate(Action):

    def name(self) -> Text:
        return "action_Global_Recovery_rate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get("https://api.covid19api.com/summary").json()

        entities = tracker.latest_message['entities']
        print("Last Message Now ", entities)
        Global = None
        for e in entities:
            if e['entity'] == "Global":
                Global = e['value']

        data = list()
        for key, value in response["Global"].items():
            print(key)
            if key == "TotalConfirmed":
                data.append(value)
            if key == "TotalDeaths":
                data.append(value)
            if key == "TotalRecovered":
                data.append(value)

        deathrate= (data[2]/data[0])
        deathrate = deathrate * 100
        message = "Global Recovery rate is : " + "{:.2f}".format(deathrate) + "%"

        dispatcher.utter_message(text=message)

        return []