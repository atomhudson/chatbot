API_KEY = "----"
import os
import openai

os.environ['OPENAI_Key']=API_KEY
openai.api_key = os.environ.get("OPENAI_Key")
keep_prompting = True
while keep_prompting:
    prompt = input('Ask anything, You want to ask...!')

    if prompt == 'exit':
        keep_prompting=False
    else:
        response=openai.Completion.create(engine='text-davinci-001',prompt=prompt,max_tokens=200)
        print(response['choices'][0]['text'])
    
    
    