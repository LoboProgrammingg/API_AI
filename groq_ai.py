import os
from decouple import config
from fastapi import FastAPI
from langchain_groq import ChatGroq
from chains import get_translate_chain, get_person_chain, get_person_city_chain
from langserve import add_routes


os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

groq_model = ChatGroq(model='llama-3.1-70b-versatile')

app = FastAPI(
    title='Minha API de IA',
    version='1.0',
    description='API de Inteligencia Artificial',
)

add_routes(
    app,
    groq_model,
    path='/groq',
)

add_routes(
    app,
    get_translate_chain(),
    path='/translate',
)

add_routes(
    app,
    get_person_chain(),
    path='/person',
)

add_routes(
    app,
    get_person_city_chain(),
    path='/personcity',
)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='localhost', port=8000)
