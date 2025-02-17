"""
Module used to convert English to French and French to English
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

VERSION_LT='2018-05-01'

authenicator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=VERSION_LT, authenticator=authenicator)
language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Translate English to French
    """
    french_text_result = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = french_text_result['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    Translate French to English
    """
    english_text_result = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = english_text_result['translations'][0]['translation']
    return english_text
