import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

version_lt='2018-05-01'

authenicator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=version_lt, authenticator=authenicator)
language_translator.set_service_url(url)

def englishToFrench(englishText):
    frenchText = language_translator.translate(text=englishText, model_id='en-fr').get_result()
    return frenchText

def frenchToEnglish(frenchText):
    englishText = language_translator.translate(text=frenchText, model_id='fr-en').get_result()
    return englishText