import openai
from flask import jsonify
openai.api_key = ""

def complete_prompt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"user","content":prompt}
        ]
    )
    return jsonify(response.choices[0].message.content)
