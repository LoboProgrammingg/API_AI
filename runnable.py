from langserve import RemoteRunnable


groq = RemoteRunnable('http://localhost:8000/groq/')
translate_chain = RemoteRunnable('http://localhost:8000/translate/')
person_chain = RemoteRunnable('http://localhost:8000/person/')
person_city_chain = RemoteRunnable('http://localhost:8000/personcity/')

response = groq.invoke('Me fale sobre Nikola Tesla')
print(response)

response = translate_chain.invoke(
    {'language': 'italiano', 'text': 'Ola, me chamo Matheus e estudo TI'}
)
print(response)

response = person_chain.invoke(
    {'person': 'Ronaldinho Gaucho'}
)

print(response)

response = person_city_chain.invoke(
    {'person': 'Michael Jackson'}
)
print(response)