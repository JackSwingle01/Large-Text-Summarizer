import os
import openai

from SECRET_KEY import API_KEY
openai.api_key = API_KEY

# print(openai.Model.list()) for testing key and connection


def get_summary(message):
    summary = get_completion(
        message, system_message='Summarize the most important information using bullet points: ')
    return summary


def get_completion(message, system_message=None):
    MAX_CHAT_TOKENS = 4096

    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': system_message},
            {'role': 'user', 'content': message}
        ],
        max_tokens=int(MAX_CHAT_TOKENS / 3),
        temperature=0.25
    )
    
    return completion.choices[0].message.content
