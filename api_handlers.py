from dotenv import load_dotenv
import os
import anthropic
import random


load_dotenv()

API_KEY = os.getenv("ANTHROPIC_API_KEY")
CLIENT = anthropic.Anthropic(
    api_key=API_KEY,
)

QUESTION_TYPES = [
"- Cultural questions: Imagine you are going to visit [insert {language}-speaking country]. What would you like to see?",
# "- Hypotheticals (as these test grammar): If you had chosen a different career path, what might you have chosen and why?",
# "- Obscure topics (to stretch their vocabulary): What's a place from your childhood that you often come back to? ",
# "- Personal topics (to stretch their vocabulary): What do you do for work, and what's something people always realize about your profession?",
"- Introduce a topic: Have you ever experience a certain {language} food, music, or holidy?",
# "- Personal topics: where do you live, and what do you like most about your neighborhood? ",
# "- Personal topics: how do you usually get around? driving? walking? biking? What do you like and dislike about this? ",
# "- Opinion topics:  what's your favorite TV show, and why do you like it?",
# "- Leisure: do you enjoy going to the beach? Why or why not?"
]


CONVERSATION_STARTER_SYSTEM = """You are a language learning bot who helps intermediate students practice {language}.

Your job is to start a new conversation with your student by asking them a question. 
This question should be interesting and intermediate/advanced. For example, some topics I might think to ask would be as follows.

{topics}

Don't simply repeat these topics, but use them as a guide for the difficulty level we're looking for. Be creative.
Always ask your questions in {language}. Your question should be friendly, and be 1-2 sentences.
Respond with just the question and nothing else: 
"""

CONVERSATION_SYSTEM = """You are a language learning bot who helps intermediate students practice {language}.

Your job is to continue a conversation with your student by asking them another question. 
Try to expand on whatever they said. Start by responding - for example, "That's interesting because of XYZ" or "That reminds me of XYZ".
Then pose a follow-up question. 
If the user is rude, tell them to be respectful. 
If the user writes something unclear on nonsensical, tell them you don't understand and ask to rephrase. 
If the user doesn't write in {language}, remind them to use {language}

Always respond to them in {language}. Your response should be 1-2 sentences.  
"""


def start_new_conversation(language="Spanish"):
    topics = "\n".join(random.sample(QUESTION_TYPES, 2))
    topics = topics.format(language=language)
    prompt_full = CONVERSATION_STARTER_SYSTEM.format(language=language, topics=topics)
    message = CLIENT.messages.create(
        model="claude-3-5-sonnet-20241022",
        system=prompt_full,
        max_tokens=1024,
        temperature=1,
        messages=[
            {"role": "user", "content": "Hello, Claude"}
        ]
    )

    return message.content[0].text


def _reformat_conversation_for_claude(conversation):

    roles_dict = {
        "user": "user",
        "ai":  "assistant"
    }
    return [
        {"role": roles_dict[c["type"]], "content": c["content"]}
         for c in conversation

    ]


def continue_conversation(conversation, language="Spanish"):
    conversation_for_claude = _reformat_conversation_for_claude(conversation)
    print("conversation", _reformat_conversation_for_claude(conversation))

    message = CLIENT.messages.create(
        model="claude-3-5-sonnet-20241022",
        system=CONVERSATION_SYSTEM.format(language=language),
        max_tokens=1024,
        temperature=1,
        messages=conversation_for_claude
    )

    return message.content[0].text







"""
Please respond with JUST the questions and nothing else. The should be formatted as a json object as follows:
{{
    "question1": str,
    "question2": str,
}}"""