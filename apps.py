import openai
from flask import jsonify
import os
import sys

sys.dont_write_bytecode = True

os.environ['API_KEY'] = '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'

openai.api_key = os.environ.get('API_KEY')

def complete_prompt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"user","content":prompt}
        ]
    )
    return jsonify(response.choices[0].message.content)
