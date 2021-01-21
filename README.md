# Medical-Diagnosis-Assistant
- With AI RASA NLU
- Try implement to mobile flutter inspired by AbySharma999
- This project using rasa2 and python 3.8.5 with pip3

# 1. Create your python virtual environment
- $virtualenv --system-site-packages -p python3 ./rasaku

# 2. Install RASA Core for NLU
- open your editor. Maybe like vscode or pycharm. It's up to what editor you're using the important thing can be.
- In the editor you use the python environment with venv that you created earlier.
- run in your terminal editor. 
- $pip3 install rasa 
- or if you using PyCharm, open python interpreter in setting => add(+) and install the rasa packages

# 3. For Testing using ngrok local server
- *open your Editor for run RASA NLU.
- running your rasa custom actions. 
- a. $rasa run actions 
- enable your rasa api model. 
- b. $rasa run -m models --enable-api --cors “*” --debug

- *finally test your assistant in your Flutter Mobile.
- open ngrok. path/to/ngrok/folder in your terminal
- run ngrok. 
- $./ngrok http 1234 <= (change 1234 with the port number used when you activate the api model before. (Command at step b). Look in the your terminal editor)
- *Open the Flutter project
- copy the ngrok url in your terminal. And put in Flutter Project => lib/pages/ChatPage.dart. for example (http://4d5b6c6f28be.ngrok.io/webhooks/rest/webhook)
  (/webhooks/rest/webhook) is parameter from rasa for testing rest api your rasa model.
- Dont forget activate connections and recording permissions in your phone
- And this project I just try in Mobile Android, Not yet on iOS

# Client Side
https://github.com/kardihaekal/Client-AI-Medical-Diagnosis

# Rasa Documentation
- https://rasa.com/docs/
# Ngrok Documentation
- https://ngrok.com/docs
# Flutter Documentation
- A new Flutter project.

## Getting Started

Github Search App with Flutter BLoC Design Pattern.

A few resources to get you started if this is your first Flutter project:

- [Lab: Write your first Flutter app](https://flutter.dev/docs/get-started/codelab)
- [Cookbook: Useful Flutter samples](https://flutter.dev/docs/cookbook)

For help getting started with Flutter, view our
[online documentation](https://flutter.dev/docs), which offers tutorials,
samples, guidance on mobile development, and a full API reference.
  
