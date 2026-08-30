# Nova — DecodeLabs Project 1 Web Chatbot

This version keeps the original rule-based chatbot logic and adds a simple web frontend.

## Structure

```text
DecodeLabs_Project1_Web/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Run in VS Code

1. Open this folder in VS Code.
2. Open Terminal.
3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate it on Windows:

```bash
venv\Scripts\activate
```

5. Install Flask:

```bash
pip install -r requirements.txt
```

6. Start the application:

```bash
python app.py
```

7. Open the local address shown in the terminal, normally:

```text
http://127.0.0.1:5000
```

## Important

The frontend does not change the assignment's AI approach. The chatbot is still rule-based. User input is normalized and matched against predefined rules. There is no machine-learning model, dataset, or external AI API.

The web layer only provides a more usable interface for the same Project 1 chatbot.
