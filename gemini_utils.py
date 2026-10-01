import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-1.5-flash")


def get_home_recommendations(budget, room, style):
    prompt = f"""
    You are PocketSmart AI, a smart budget assistant.

    User wants to decorate:
    Room: {room}
    Style: {style}
    Total Budget: ₹{budget}

    Give practical recommendations within the budget.

    Provide:
    1. Item name
    2. Estimated price
    3. Quantity
    4. Why it is suitable
    5. Suggested platform

    Make sure the total estimated cost does not exceed the budget.
    """

    response = model.generate_content(prompt)
    return response.text


def get_party_recommendations(budget, guests, event_type):
    prompt = f"""
    You are PocketSmart AI.

    Plan a {event_type} party.

    Budget: ₹{budget}
    Number of guests: {guests}

    Suggest:
    - Food
    - Decoration
    - Venue
    - Entertainment

    Allocate the budget intelligently and keep the total
    within the user's budget.

    Return simple and practical recommendations.
    """

    response = model.generate_content(prompt)
    return response.text


def get_jewelry_recommendations(budget, occasion, style):
    prompt = f"""
    You are PocketSmart AI jewelry recommendation assistant.

    Budget: ₹{budget}
    Occasion: {occasion}
    Style: {style}

    Recommend suitable jewelry.

    Include:
    - Jewelry type
    - Estimated price
    - Material
    - Matching suggestion
    - Suitable platform

    Keep recommendations within budget.
    """

    response = model.generate_content(prompt)
    return response.text
