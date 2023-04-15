import json
import openai
import logging
from genie.testbed import load
import requests

openai.api_key = <insert your open api key here>

logging.basicConfig(level=logging.DEBUG)

testbed = load('genie.yml')

for dev in testbed: 
       
    dev.connect(learn_hostname=True,init_exec_commands=[],init_config_commands=[],log_stdout=True)
    
    config_output = dev.execute('show run | i username')
    
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
                    {"role": "system", "content": "You are a cybersecurity auditor "},
                    {"role": "user", "content": f"Please review the following Cisco command output to see if it is secure and recommend a more secure configuration\n { config_output }"},
                    {"role": "user", "content": "Provide a configuration template that you would configure to ensure maximum security"},
                ]
            )

    result = ''
    
    print(response.choices)
    for choice in response.choices:
        result += choice.message.content
    
    print(result)
