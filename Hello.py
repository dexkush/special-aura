# Hello.py

import random
import time

def print_ascii_art():
    art = """
     _   _      _ _         __        __         _     _ _ 
    | | | |    | | |        \ \      / /        | |   | | |
    | |_| | ___| | | ___     \ \ /\ / /__  _ __ | | __| | |
    |  _  |/ _ \ | |/ _ \     \ V  V / _ \| '__\| |/ _` | |
    | | | |  __/ | | (_) |     \_/\_/ (_) | |   | ||(_| |_|
    \_| |_/\___|_|_|\___/ ( )        \___/|_|   |_|\__,_(_)
                          |/                                   
    """
    print(art)

def get_user_name():
    name = input("Enter your name: ")
    return name

def random_greeting(name):
    greetings = [
        f"Hello, {name}! Ready for some fun?",
        f"Hey {name}, let's do something awesome today!",
        f"Hi {name}! How are you doing?",
        f"What's up, {name}? Let's code!",
        f"Greetings, {name}! Time to have some fun with Python!"
    ]
    return random.choice(greetings)

def fun_fact():
    facts = [
        "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
        "A group of flamingos is called a 'flamboyance'.",
        "Bananas are berries, but strawberries aren't!",
        "There are more possible iterations of a game of chess than there are atoms in the known universe.",
        "Octopuses have three hearts."
    ]
    return random.choice(facts)

def ai_transformation_info():
    info = """
    AI Transformation: AI is leading a significant shift in the modern workplace, similar to the impact of the internet.
    Efficiency and Productivity: AI can make routine tasks less time-consuming, helping you achieve goals and succeed in the evolving work landscape.
    Practical Examples: AI can analyze spreadsheets quickly, draft detailed reports, schedule meetings, create presentations, and enhance brainstorming sessions.
    """
    print(info)

def google_ai_course_info():
    info = """
    Google AI Essentials Course:
    - Designed to help learn the basics of AI and its application in routine tasks.
    - No prior AI experience needed.
    - Flexible, self-paced, and fully online.
    - Includes videos, readings, and interactive activities.
    Expert Guidance: Led by Maya, VP of Strategy and Operations at Google Research, and featuring insights from diverse AI experts at Google.
    Learning Outcomes: The course aims to help you engage with AI tools, apply AI responsibly, and prepare for AI's future in the workplace.
    Skill Badge: Completion of the course provides a skill badge to enhance your resume, social media profiles, and email signature.
    Comprehensive Learning: The course will address common questions about AI and its application in boosting productivity and career advancement.
    """
    print(info)

def main():
    print_ascii_art()
    name = get_user_name()
    print(random_greeting(name))
    time.sleep(1)  # Adding a little pause for dramatic effect
    print("\nHere's a fun fact for you:")
    print(fun_fact())
    time.sleep(2)  # Another pause before diving into AI info
    print("\nLet's talk about AI and its impact on the modern workplace:")
    ai_transformation_info()
    time.sleep(2)  # Pause before introducing the course
    print("\nInterested in learning more? Check out the Google AI Essentials Course:")
    google_ai_course_info()

if __name__ == "__main__":
    main()