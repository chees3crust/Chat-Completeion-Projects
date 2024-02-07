#This teaches us how to use openai API for self-made chatbots

'''
    First we need to install openai library
        pip install openai
    Get the secret key for your account from openai website and set it as environment var or in the program

'''

import os
from openai import OpenAI

# This is used when the apikey is stored in a file
f = open('API_KEY.txt','r')
api_key = f.read()

client = OpenAI(
    # This is the default and can be omitted. This is used when the apikey is set as environment variable
    #api_key=os.environ.get("OPENAI_API_KEY"), 
    api_key = api_key
)


'''
----OPENAI Chat Completion ----

from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": "Who won the world series in 2020?"}
  ]
)
print(response.choices[0].message.content)

'''

#This is the function that uses openaichatcompletion to handel prompts
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}] # this can have multi roles like system, user and assistant
    response = client.chat.completions.create(
        model=model,
        #response_format={ "type": "json_object" },
        messages=messages, #array input
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"] # the response can be generated in other formats also

# The response will always contain `finish_reason`

#Example prompt

text = f"""
You should express what you want a model to do by \ 
providing instructions that are as clear and \ 
specific as you can possibly make them. \ 
This will guide the model towards the desired output, \ 
and reduce the chances of receiving irrelevant \ 
or incorrect responses. Don't confuse writing a \ 
clear prompt with writing a short prompt. \ 
In many cases, longer prompts provide more clarity \ 
and context for the model, which can lead to \ 
more detailed and relevant outputs.
"""
prompt = f"""
Summarize the text delimited by triple backticks \ 
into a single sentence.
```{text}```
"""
response = get_completion(prompt)
print(response)


