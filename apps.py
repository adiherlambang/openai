import openai
from flask import jsonify
openai.api_key = "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"

def complete_prompt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"user","content":prompt}
        ]
    )
    return jsonify(response.choices[0].message.content)
