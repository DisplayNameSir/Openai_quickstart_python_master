import os
import openai #remember to pip install pandas openai
from dotenv import load_dotenv  #remember to pip install python-dotenv
load_dotenv()

#Sign up for OpenAI here https://beta.openai.com/signup
# and obtain an API key from here https://platform.openai.com/account/api-keys
#Replace the OPEN_API_KEY below with your own key:
openai.api_key = os.getenv("OPENAI_API_KEY")

#If you are using Anaconda Spyder, make sure it is updated to version 5.3.3
# or later
# from the Anaconda prompt, type 2 commands
#  conda update anaconda
#  conda install spyder=5.3.3

def generate_response(prompt, stop=None):
    # More details about the different engines here
    #  https://beta.openai.com/docs/models/gpt-3
    model_engine = "text-davinci-002"  # https://platform.openai.com/docs/models/overview
    prompt = (f"Answer {prompt} in rhymes")

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=3000,
        n=5,
        stop="cheating",
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

while (True):
    prompt = input("\nWhat would you like to ask me today? (or type 'quitme' to quit): \n")
    if(prompt == 'quitme'):
        break
    response = generate_response(prompt)
    print("\n" + response)
    stop = input("\nHow was the previous response? (or leave blank for None): \n")
    response = generate_response(stop)