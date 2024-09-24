import os

from decouple import config

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

def get_translate_chain():
    model = ChatGroq(
        model='llama-3.1-70b-versatile',
    )
    translate_prompt = ChatPromptTemplate.from_template(
        'Traduza o texto a seguir para o idioma {language}: {text}'
    )
    translate_chain = translate_prompt | model | StrOutputParser()
    return translate_chain


def get_person_chain():
    model = ChatGroq(
        model='llama-3.1-70b-versatile',
    )
    person_prompt = ChatPromptTemplate.from_template('Me fale sobre a vida de {person}')
    person_chain = person_prompt | model | StrOutputParser()
    return person_chain


def get_person_city_chain():
    model = ChatGroq(
        model='llama-3.1-70b-versatile',
    )
    person_prompt = ChatPromptTemplate.from_template('Em qual cidade {person} nasceu?')
    city_prompt = ChatPromptTemplate.from_template(
        'Em qual pais fica a cidade {city}? Descreva a cidade responda em pt-br.'
    )
    person_chain = person_prompt | model | StrOutputParser()
    person_city_chain = (
        {'city': person_chain }
        | city_prompt
        | model
        | StrOutputParser()
    )
    return person_city_chain
