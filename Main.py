import json
import openai
import logging
import pandas as pd
from genie.testbed import load
import requests

openai.api_key = <insert your API key here>

logging.basicConfig(level=logging.DEBUG)

testbed = load('device.yml')

for dev in testbed: 
       
    dev.connect(learn_hostname=True,init_exec_commands=[],init_config_commands=[],log_stdout=True)
    
    config_output = dev.execute('show run | i username') # this can be replaced with any command that interests you
    
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
                    {"role": "system", "content": "You are a cybersecurity auditor "},
                    {"role": "user", "content": f"Please review the following Cisco command output to see if it is secure and recommend a more secure configuration\n { config_output }"},
                ]
            )

    result = ''
    
    print(response.choices)
    for choice in response.choices:
        result += choice.message.content
    
    print(result)
