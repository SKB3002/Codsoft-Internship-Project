import gradio as gr
import re


conversation = {
    "hi": "Hello! How can I help you?",
    "hello": "Hello! How can I help you?",
    "hey": "Hello! How can I help you?",
    "how are you": "I’m just a bot, but I’m doing fine....\nHow about you?",
    "bye": "Goodbye! Take care.",
    "goodbye": "Goodbye! Take care.",
    "im great": "Great to hear that!  Do you study or work?",
    "i great": "Great to hear that!  Do you study or work?",
    "im doing great": "Great to hear that!  Do you study or work?",
    "im doing fine too": "Great to hear that!  Do you study or work?",
    "im fine" : "Great to hear that!  Do you study or work?",
    "i am good": "Glad to hear that! Do you study or work?",
    "good": "Glad to hear that! Do you study or work?",
    "i study": "That’s great! What subject do you enjoy the most?",
    "study": "That’s great! What subject do you enjoy the most?",
    "i work": "That wonderful,have you build any great projects yet?",
    "work" : "That wonderful,have you build any great projects yet?",
    "i like ai": "That is fascinating! Have you tried building any projects yet?",
    "i like maths": "That is fascinating! Have you tried building any projects yet?",
    "i like science": "That is fascinating! Have you tried building any projects yet?",
    "yes i did": "Awesome! What kind of project did you build?",
    "yes": "Awesome! What kind of project did you build?",
    "yup": "Awesome! What kind of project did you build?",
    "nope": "No worries!",
    "no": "No worries!",
    "not yet" : "No worries!",
    "i built a chatbot": "That’s so cool! Was it rule-based or ML-based?",
    "rule based": "Wow! Thats wonderful."
}

name = None

def chatbot(user_input, history):
   
    global name 
    # normalize input: lowercase + strip spaces
    user_input_clean = user_input.lower()

    # special cases
    if user_input_clean in ["quit", "exit"]:
        history.append((user_input, "Goodbye!"))
        return history

    # dictionary lookup
    response = conversation.get(user_input_clean, "Sorry, I don’t understand that. Could you rephrase?")

    # append properly: (user message, bot reply)
    history.append((user_input, response))
    return history


# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("## 🤖 Rule-Based Chatbot")

    chatbot_ui = gr.Chatbot()
    msg = gr.Textbox(placeholder="Type your message here...")

    clear = gr.Button("Clear Chat")

    def respond(user_input, history):
        return "", chatbot(user_input, history)

    msg.submit(respond, [msg, chatbot_ui], [msg, chatbot_ui])
    clear.click(lambda: [], None, chatbot_ui, queue=False)

demo.launch()
