from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)


# --------------------------------------------------
# Predefined chatbot responses
# --------------------------------------------------

RESPONSES = {
    "hello": "Hello! Welcome to Nova. How can I help?",
    "hi": "Hi! What can I help you with?",
    "hey": "Hey! Ask me something about DecodeLabs or this AI project.",

    "how are you": "I'm doing well. Thanks for asking!",

    "what is ai": (
        "Artificial Intelligence is the field of building systems "
        "that can perform tasks associated with human intelligence."
    ),

    "what is decodelabs": (
        "DecodeLabs helps students and young professionals build "
        "career-ready skills through practical, mentor-guided virtual internships."
    ),

    "what does decodelabs do": (
        "DecodeLabs focuses on practical projects, mentor guidance, "
        "industry tools, and portfolio-ready outcomes."
    ),

    "what is the ai internship": (
        "The Artificial Intelligence internship focuses on AI fundamentals, "
        "machine learning, and neural networks."
    ),

    "what will i learn in ai": (
        "The AI track covers AI fundamentals, machine learning, "
        "and neural networks, with practical project work and guided checkpoints."
    ),

    "is the internship remote": (
        "Yes. DecodeLabs describes its internship programs as virtual "
        "and remote-friendly."
    ),

    "how long is the internship": (
        "The internship program is structured as a 4-week program."
    ),

    "is there mentorship": (
        "Yes. The program includes mentor guidance, doubt support, "
        "and project checkpoints."
    ),

    "do i get feedback": (
        "Yes. DecodeLabs describes mentor checkpoints, project feedback, "
        "and guidance on implementation quality and presentation."
    ),

    "will i work on projects": (
        "Yes. The internship is project-based and includes practical deliverables."
    ),

    "is it beginner friendly": (
        "The website says most tracks are beginner-friendly and mentor-guided, "
        "with role-based options for intermediate learners."
    ),

    "what other internships are available": (
        "The website lists tracks including Artificial Intelligence, "
        "Full Stack Development, Python Programming, Data Science, "
        "Data Analytics, and Java Programming."
    ),

    "what is project 1": (
        "Project 1 is a Rule-Based AI Chatbot. "
        "It is designed to practice control flow, decision-making logic, "
        "and basic AI concepts."
    ),

    "what are the project requirements": (
        "Project 1 requires greeting and exit handling, if-else logic "
        "for responses, and a continuous conversation loop."
    ),

    "does this project need a dataset": (
        "No. This project is rule-based, so its responses are predefined "
        "rules rather than predictions learned from a dataset."
    ),

    "what can you do": (
        "I can answer questions about DecodeLabs, the AI internship, "
        "and Project 1."
    ),

    "help": (
        "You can ask me things like: What is AI? "
        "What is DecodeLabs? What is Project 1? "
        "Does this project need a dataset? "
        "How long is the internship? Is there mentorship?"
    ),

    "thanks": "You're welcome!",
    "thank you": "You're welcome!"
}


# --------------------------------------------------
# Clean and normalize user input
# --------------------------------------------------

def clean_input(text):
    """
    Makes user input easier to understand.

    Example:
    '  What is Project 1?  '
    becomes:
    'what is project 1'
    """

    text = text.strip().lower()

    # Remove punctuation such as ?, !, ., ,
    text = re.sub(r"[^\w\s]", "", text)

    # Remove extra spaces
    text = " ".join(text.split())

    return text


# --------------------------------------------------
# Generate chatbot response
# --------------------------------------------------

def get_response(user_input):

    message = clean_input(user_input)

    # Empty message
    if not message:
        return "Please type something so I can help you.", False

    # --------------------------------------------------
    # Exit commands
    # --------------------------------------------------

    if any(word in message.split() for word in {"bye", "goodbye", "exit", "quit"}):
        return "Goodbye! Good luck with your AI journey.", True


    # --------------------------------------------------
    # Greetings
    # --------------------------------------------------

    elif message in {
        "hello",
        "hi",
        "hey",
        "hello nova",
        "hi nova",
        "hey nova"
    }:
        return "Hello! Welcome to Nova. How can I help?", False


    # --------------------------------------------------
    # Exact predefined responses
    # --------------------------------------------------

    elif message in RESPONSES:
        return RESPONSES[message], False


    # --------------------------------------------------
    # AI related questions
    # --------------------------------------------------

    elif (
        "artificial intelligence" in message
        or message == "ai"
        or "what is ai" in message
        or "explain ai" in message
        or "tell me about ai" in message
    ):
        return (
            "Artificial Intelligence is the field of building systems "
            "that can perform tasks associated with human intelligence."
        ), False


    # --------------------------------------------------
    # DecodeLabs questions
    # --------------------------------------------------

    elif (
        "decodelabs" in message
        and (
            "what" in message
            or "about" in message
            or "tell" in message
            or "explain" in message
        )
    ):
        return (
            "DecodeLabs helps students and young professionals build "
            "career-ready skills through practical, mentor-guided "
            "virtual internships."
        ), False


    # --------------------------------------------------
    # Project 1 questions
    # --------------------------------------------------

    elif (
        "project 1" in message
        or "project one" in message
    ):
        return (
            "Project 1 is a Rule-Based AI Chatbot. "
            "It is designed to practice control flow, "
            "decision-making logic, and basic AI concepts."
        ), False


    # --------------------------------------------------
    # Dataset questions
    # --------------------------------------------------

    elif "dataset" in message or "data set" in message:

        return (
            "No. Project 1 does not require a dataset. "
            "It is a rule-based chatbot that uses predefined "
            "responses and if-else logic."
        ), False


    # --------------------------------------------------
    # Internship duration
    # --------------------------------------------------

    elif (
        "how long" in message
        and "internship" in message
    ):
        return (
            "The internship program is structured as a 4-week program."
        ), False


    elif (
        "duration" in message
        and "internship" in message
    ):
        return (
            "The internship program is structured as a 4-week program."
        ), False


    # --------------------------------------------------
    # Mentorship
    # --------------------------------------------------

    elif (
        "mentor" in message
        or "mentorship" in message
        or "guidance" in message
    ):
        return (
            "Yes. The program includes mentor guidance, "
            "support, and project checkpoints."
        ), False


    # --------------------------------------------------
    # Internship questions
    # --------------------------------------------------

    elif "internship" in message:

        return (
            "The DecodeLabs AI internship focuses on AI fundamentals, "
            "machine learning, and neural networks, along with practical "
            "project work and mentor guidance."
        ), False


    # --------------------------------------------------
    # Machine Learning
    # --------------------------------------------------

    elif (
        "machine learning" in message
        or "ml" in message
    ):
        return (
            "Machine Learning is a branch of AI where systems learn "
            "patterns from data to make predictions or decisions."
        ), False


    # --------------------------------------------------
    # Neural Networks
    # --------------------------------------------------

    elif (
        "neural network" in message
        or "neural networks" in message
        or "deep learning" in message
    ):
        return (
            "Neural networks are computing models inspired by the "
            "way biological neurons process information. They are "
            "widely used in modern AI and deep learning."
        ), False


    # --------------------------------------------------
    # What can you do?
    # --------------------------------------------------

    elif (
        "what can you do" in message
        or "what do you do" in message
        or message == "help me"
    ):
        return (
            "I can answer questions about DecodeLabs, the AI internship, "
            "Project 1, datasets, mentorship, and basic AI concepts."
        ), False


    # --------------------------------------------------
    # Thanks
    # --------------------------------------------------

    elif (
        "thank" in message
        or "thanks" in message
    ):
        return "You're welcome!", False


    # --------------------------------------------------
    # Unknown question
    # --------------------------------------------------

    else:
        return (
            "I'm not sure about that yet. "
            "Try asking me about AI, DecodeLabs, the AI internship, "
            "Project 1, datasets, mentorship, or project requirements."
        ), False


# --------------------------------------------------
# Home page
# --------------------------------------------------

@app.route("/")
def index():
    return render_template("index.html")


# --------------------------------------------------
# Chat API
# --------------------------------------------------

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json(silent=True) or {}

    message = data.get("message", "")

    response, should_exit = get_response(message)

    return jsonify({
        "response": response,
        "exit": should_exit
    })


# --------------------------------------------------
# Start application
# --------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)