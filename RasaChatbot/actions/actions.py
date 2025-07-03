import pandas as pd
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from typing import Dict, Text, List, Optional, Any


class ActionGetUniversities(Action):
    def name(self):
        return "action_get_universities"

    # async def extract_slot_erasmus(
    #         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict):
    #     intent = tracker.latest_message["intent"].get("erasmus")
    #
    #     if intent == "affirm":
    #         return [SlotSet("slot_erasmus", True)]
    #     elif intent == "deny":
    #         return [SlotSet("slot_erasmus", False)]

    @staticmethod
    def degree_list_db() -> List[Text]:
        return ["business", "computer science", "management", "tourism", "engineering",
                "economics", "IM", "health",
                "design", "psychology", "sport", "logistics"]

    async def extract_slot_study_program(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict):
        if tracker.latest_message.get('intent') == 'tell_degree':
            raw_degree = tracker.latest_message.get('entity')
            if raw_degree.lower() in self.degree_list_db():
                degree = raw_degree
            elif raw_degree.lower() == "Business Informatics":
                degree = ["business", "computer science"]
            elif raw_degree.lower() == "Health Informatics":
                degree = ["health", "computer science"]
            elif raw_degree.lower() == "Technology Management":
                degree = ["management", "computer science"]
            else:
                degree = None
        return {"slot_study_program": degree}

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        # '''Convert pdf to csv'''
        # pdf_path = "https://www.th-deg.de/Studierende/Auslandsstudium/partnerunis_studenten.pdf"
        # df_list = tabula.read_pdf(pdf_path, pages='all')
        # df = pd.concat(df_list)
        # df.to_csv('output.csv', index=False)
        #
        # '''Cleaning the data'''
        # raw_df = pd.read_csv('output.csv', header=None)
        # raw_df.dropna(how='all', inplace=True)
        # last_index = raw_df.index[-1]
        # extra_rows = [raw_df.iloc[0, i:i + 5] for i in range(0, len(df.columns), 5)]
        # for row in extra_rows:
        #     last_index += 1
        #     raw_df.loc[last_index] = row
        #
        # raw_df.drop(raw_df.columns[5:29], axis=1, inplace=True, errors='ignore')
        # raw_df.ffill(inplace=True)
        # raw_df.drop_duplicates(inplace=True, keep='first')
        #
        #
        #
        # merged_df = pd.DataFrame()
        # for index in range(1, len(raw_df)):
        #     prev_row = raw_df.iloc[index - 1]
        #     this_row = raw_df.iloc[index]
        #     merged_row = pd.concat([prev_row, this_row])
        #     merged_df = merged_df._append(merged_row, ignore_index=True)
        #     merged_df.to_csv('output.csv', index=False)
        #
        # for index, row in merged_row.iterrows():
        #     partner_university = merged_df.iloc[index, 1]
        #     if partner_university in self.degree_list_db():
        #         merged_df.drop(axis='columns', index=index, inplace=True, errors='ignore')
        print("hello")
        df = pd.read_csv(r'C:\Users\libra\PycharmProject\testChatbot\RasaChatbot\actions\University.csv',
                         sep=';', encoding_errors='ignore', encoding='utf-8')

        raw_unis = []
        study_program = tracker.get_slot('slot_degree_program')
        erasmus = tracker.get_slot('slot_erasmus')

        for index, row in df.iterrows():
            partner_university = df.iloc[index, 1]
            study_fields = df.iloc[index, 2]

            if study_program is not None:
                if erasmus:
                    if ((study_program.lower() in study_fields.lower()
                         and "erasmus".capitalize() in study_fields)
                            or study_fields == 'All Study Programs'):
                        raw_unis.append(partner_university)
                else:
                    if (study_program.lower() in study_fields.lower()
                            or study_fields == 'All Study Programs'):
                        raw_unis.append(partner_university)
            else:
                if study_fields == "All Study Programs":
                    raw_unis.append(partner_university)

        universities = [item for item in raw_unis if 'www.' not in item]
        description = ", ".join(universities)
        dispatcher.utter_message(
            text=f"Here you go! {description}")
        dispatcher.utter_message(text="Please use this as a starting point for applying for a semester abroad.")
