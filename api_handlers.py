from dotenv import load_dotenv
import os
import anthropic
import random
import json

from prompts import (
    QUESTION_TYPES,
    CONVERSATION_SYSTEM,
    START_NEW_TOPIC_SYSTEM,
    AI_FEEDBACK_SYSTEM,
    NEW_WORDS_SYSTEM,
)

load_dotenv()

API_KEY = os.getenv("ANTHROPIC_API_KEY")
CLIENT = anthropic.Anthropic(
    api_key=API_KEY,
)


def start_new_topic(language="Spanish"):
    topics = "\n".join(random.sample(QUESTION_TYPES, 2))
    topics = topics.format(language=language)
    prompt_full = START_NEW_TOPIC_SYSTEM.format(language=language, topics=topics)
    message = CLIENT.messages.create(
        model="claude-3-5-sonnet-20241022",
        system=prompt_full,
        max_tokens=1024,
        temperature=1,
        messages=[{"role": "user", "content": "Hello, Claude"}],
    )

    return message.content[0].text


def _reformat_conversation_for_claude(conversation):

    roles_dict = {"user": "user", "ai": "assistant"}
    return [
        {"role": roles_dict[c["type"]], "content": c["content"]} for c in conversation
    ]


def submit_answer_to_ai(conversation, language="Spanish"):
    conversation_for_claude = _reformat_conversation_for_claude(conversation)

    message = CLIENT.messages.create(
        model="claude-3-5-sonnet-20241022",
        system=CONVERSATION_SYSTEM.format(language=language),
        max_tokens=1024,
        temperature=1,
        messages=conversation_for_claude,
    )

    return message.content[0].text


def get_feedback(conversation, language="Spanish"):
    conversation_for_claude = _reformat_conversation_for_claude(conversation)

    message = CLIENT.messages.create(
        model="claude-3-5-sonnet-20241022",
        system=AI_FEEDBACK_SYSTEM.format(language=language),
        max_tokens=1024,
        temperature=1,
        messages=conversation_for_claude,
    )

    return json.loads(message.content[0].text)


def get_new_words(conversation, response, language="Spanish"):
    conversation_for_claude = _reformat_conversation_for_claude(conversation)

    conversation_for_claude_as_str = "\n".join(
        ["Role: {role}, Message {content}".format(**d) for d in conversation_for_claude]
    )

    conversation_for_claude_as_str += "\n Role: assistant, Message: {response}".format(
        response=response
    )

    message = CLIENT.messages.create(
        model="claude-3-5-sonnet-20241022",
        system=NEW_WORDS_SYSTEM.format(language=language),
        max_tokens=1024,
        temperature=1,
        messages=[{"role": "user", "content": conversation_for_claude_as_str}],
    )

    return json.loads(message.content[0].text)

