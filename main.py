from flask import Flask, request, render_template,jsonify
import openai
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv(OPENAI_API_KEY)
app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = api_key
chat_messages=[]
@app.route('/')
def home():
    return render_template('index.html',chat_messages=chat_messages)

@app.route('/ask', methods=['POST'])
def ask():
    global chat_messages
    user_message = request.form['user_message']
    chat_messages.append({"role":"user","content":user_message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "you are a meditation chatbot and only knows about meditations only"
            },
            {
                "role": "user",
                "content": "Hi, I want to search about meditations and their types."
            },
            {
                "role": "assistant",
                "content": "Sure! What type of meditation would you like to know about?"
            },
            {
                "role": "user",
                "content": "I want to know about mindfulness meditation.Give me the steps to do the meditation and benefits line by line."
            },
            {
                "role": "assistant",
                "content": "Certainly. Here are the details of mindfulness meditation:"
            },
            {
                "role": "assistant",
                "content": "Steps:\n"
                           "- Find a quiet place where you will not be disturbed.\n"
                           "- Sit in a comfortable position with your back straight.\n"
                           "- Close your eyes or gaze softly downward.\n"
                           "- Bring your attention to your breath.\n"
                           "- When your mind wanders, gently bring it back to your breath.\n"
                           "- Continue to focus on your breath for as long as you like."
            },
            {
                "role": "assistant",
                "content": "Benefits:\n"
                           "- Reduced stress and anxiety\n"
                           "- Improved mood\n"
                           "- Increased self-awareness\n"
                           "- Enhanced focus and concentration\n"
                           "- Improved sleep\n"
                           "- Reduced pain\n"
                           "- Stronger immune system"
            },
            {
                "role": "assistant",
                "content": "I hope this helps."
            },
            {
                "role": "user",
                "content": "Is there anything else you would like to know about meditations?"
            },
            {
                "role": "user",
                "content": "Okay, what is the history behind Vipassana meditation?"
            },
            {
                "role": "assistant",
                "content": "Vipassana, also known as Insight meditation, has its roots in ancient India. It can be traced back to around 2500 years ago. The practice of Vipassana meditation is strongly associated with the teachings of the Gautama Buddha, who was born in India and achieved enlightenment.\n"
                           "History: The Buddha emphasized the importance of direct personal experience, and Vipassana meditation was one of the key practices that he taught. He believed that deep insight into the nature of reality would lead to liberation from suffering.\n"
                           "Over the centuries, the practice of Vipassana was transmitted from generation to generation among Buddhist monastic communities.\n"
                           "However, in the 20th century, a Burmese meditation master named S.N. Goenka reintroduced the technique of Vipassana to the world in a non-sectarian and secular manner. Through the establishment of Vipassana meditation centers globally, Goenka has made this practice accessible to people from various backgrounds and religions.\n"
                           "Today, Vipassana continues to be widely practiced around the world."
            },
            
            {"role": "user",
             "content": user_message}
        ],
        temperature=1.52,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    bot_reply = response['choices'][0]['message']['content']
    bot_reply_lines = bot_reply.split('\n')
    chat_messages.append({"role":"assistant","content":bot_reply})
    return jsonify({"bot_reply":bot_reply_lines})
    #return render_template('index.html', user_message=user_message, bot_reply_lines=bot_reply_lines)

if __name__ == '__main__':
    app.run(debug=True)
