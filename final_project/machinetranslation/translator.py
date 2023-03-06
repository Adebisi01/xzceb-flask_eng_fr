""" This Module translate test from french to english and vice versa"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url(url)


def english_to_french(english_text):
    """This function translate text from english to french"""
    if (english_text == None or english_text == ''):
        return None
    else:
        translation = language_translator.translate(
            text=english_text, model_id='en-fr').get_result()
        french_text_json = json.dumps(
            translation, indent=2, ensure_ascii=False)
        french_text_dict = json.loads(french_text_json)
        french_text = french_text_dict['translations'][0]['translation']
        # print(french_text)
        return french_text


def french_to_english(french_text):
    """This function translate text from french to english"""
    if (french_text == None or french_text == ''):
        return None
    else:
        translation = language_translator.translate(
            text=french_text, model_id='fr-en').get_result()
        english_text_json = json.dumps(
            translation, indent=2, ensure_ascii=False)
        english_text_dict = json.loads(english_text_json)
        english_text = english_text_dict['translations'][0]['translation']
        # print(english_text)
        return english_text


# print(french_to_english(None))
