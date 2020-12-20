import wolframalpha
import wikipedia
from pip._vendor.distlib.compat import raw_input

# add while and try & catch to decide which way to go
while True:
    input_assistant = raw_input("Ingrese su pregunta : ")
    wikipedia.set_lang("es")  # Languange for the assistant es = Spanish

    try:
        #all the neccesary to connect wit wolfram
        wolfram_app_id = 'J7866R-V396RG4AQ8'
        client = wolframalpha.Client(wolfram_app_id)
        res = client.query(input_assistant)
        answer = next(res.results).text
        print(answer)
    except :
        #Connection with Wikipedia
        print(wikipedia.summary(input_assistant, sentences=3))
