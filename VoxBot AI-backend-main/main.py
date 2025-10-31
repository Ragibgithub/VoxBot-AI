import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import numpy as np
from gensim.models import Word2Vec
import random
import features.greed 
import pickle
# from face.face import face
import json
from speech1.speech import speechrecognition
import webbrowser
from features.internet import check_internet as internet
from speak.speak import speak


class ChatBotTrainer:
    def __init__(self):
        self.model = None
        self.word2vec_model = None
        self.training_data = []
        self.labels = []

    def preprocess(self, text):
        tokens = nltk.word_tokenize(text)
        lemmatizer = WordNetLemmatizer()
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
        return ' '.join(lemmatized_tokens)

    def train_word2vec(self):
        self.word2vec_model = Word2Vec(sentences=[text.split() for text in self.training_data], vector_size=100, window=5, min_count=1, workers=4)

    def vectorize_sentence(self, sentence):
        if self.word2vec_model is None:
            return np.zeros((100,))
        vector = np.zeros((100,))
        for word in sentence.split():
            if word in self.word2vec_model.wv.key_to_index:
                vector += self.word2vec_model.wv[word]
        return vector

    def preprocess_training_data(self):
        self.training_data = [self.preprocess(text) for text in self.training_data]

    def vectorize_training_data(self):
        X_train = np.array([self.vectorize_sentence(sentence) for sentence in self.training_data])
        return X_train

    def split_data(self):
        X_train, X_test, y_train, y_test = train_test_split(self.vectorize_training_data(), self.labels, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test

    def train_model(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        X_train, _, y_train, _ = self.split_data()
        self.model.fit(X_train, y_train)

    def evaluate_model(self):
        _, X_test, _, y_test = self.split_data()
        predictions = self.model.predict(X_test)
        print(classification_report(y_test, predictions))

    def train(self, intents):
        for intent, data in intents.items():
            for pattern in data['patterns']:
                self.training_data.append(pattern.lower())
                self.labels.append(intent)
        
        self.preprocess_training_data()
        self.train_word2vec()
        self.train_model()
        self.evaluate_model()

    def save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump((self.model, self.word2vec_model, self.training_data, self.labels), file)

    def load(self, filename):
        with open(filename, 'rb') as file:
            self.model, self.word2vec_model, self.training_data, self.labels = pickle.load(file)

class ChatBot:
    def __init__(self):
        self.trainer = ChatBotTrainer()
        self.load_intents()  # Load intents during initialization
        try:
            self.trainer.train(self.intents)  # Train the model
        except Exception as e:
            print("Error during training:", e)

    def load_intents(self):
        try:
            from database.data import intents # Import intents here
            self.intents = intents  # Store intents in the ChatBot instance
        except ImportError:
            print("Error: Could not load intents.")

    def predict_intent(self, user_input):
        preprocessed_input = self.trainer.preprocess(user_input.lower())
        input_vector = self.trainer.vectorize_sentence(preprocessed_input)
        if self.trainer.model is None:
            return None, None, None  # Return None for both intent and confidence if model is not trained
        predictions = self.trainer.model.predict_proba([input_vector])[0]
        max_confidence = max(predictions)
        min_confidence = min(predictions)
        intent = self.trainer.model.classes_[np.argmax(predictions)]  # Get the intent with maximum confidence
        return intent, max_confidence, min_confidence

    def get_response(self, intent):
        responses = self.intents[intent]['responses']
        return random.choice(responses)

    def start_chat(self):
        try:
            with open('log/log.json', 'r') as json_file:
                logs = json.load(json_file)
        except FileNotFoundError:
            logs = []
        # speak("starting security check")
        # name , id= face()
        # if id ==0:
        #     speak("you are not authorize")
        #     exit()
        # if id ==1:
        #     features.greed.greedf()
        #     speak("welcome Ms gungun")
        # if id ==2:
        #     features.greed.greedm()
        #     speak("welcome Mr Ragib")
        speak("Hi there! How can I assist you today?")
        while True:
            user_input = speechrecognition()  # Moved this line up to prevent NameError
            log = {
                "User": user_input,
                "intent": "",
                "maxmax_confidence": "",
                "min_confidence": "",
                "AI": ""
            }
            user_input=str(user_input)
            if user_input.lower() == 'exit' or user_input.lower() == 'bye':
                speak("Goodbye!")
                log["AI"] = "Goodbye!"
                logs.append(log)  
                break
            if user_input.lower() == 'train':
                speak("Training...")
                self.trainer.train()
                speak("Done training.")
                log["AI"] = "Done training."
                logs.append(log)
                continue
            else:
                intent, max_confidence, min_confidence = self.predict_intent(user_input)
                max_confidence = int(max_confidence * 100)
                response = self.get_response(intent)
                if max_confidence > 12:
                    if intent =="time":
                        import datetime
                        a=datetime.datetime.now().strftime("%I:%M %p")
                        response = self.get_response(intent)+str(a)
                        speak(response)
                    elif intent =="weather":
                        if internet():
                            from features.weather import weather
                            speak("enter which city")
                            city = input()
                            response = weather.get_weather(city)
                            speak(response)
                        else :
                            response="sorry internet not connneted"
                            speak(response)
                    elif intent =="open_bower":
                        if internet():
                            speak(response)
                            webbrowser.open("https://www.msn.com/en-in/feed?ocid=msedgntp&pc=U531&cvid=d282a5ae79ca44ba8c14500114e2fb2b&ei=6")
                        else :
                            response="sorry internet not connneted"
                            speak(response)
                    elif intent =="open_youtube":
                        if internet():
                            speak(response)
                            webbrowser.open("https://www.youtube.com")
                        else :  
                            response="sorry internet not connneted"
                            speak(response)
                    elif intent =="chatgpt_interaction":
                        if internet():
                            speak(response)                        
                            webbrowser.open("https://chat.openai.com/")
                        else:
                            response="sorry internet not connneted"
                            speak(response)
                    elif intent =="open_amazon":
                        if internet():
                            speak(response)
                            webbrowser.open("https://www.amazon.in/")
                        else:
                            response="sorry internet not connneted"
                            speak(response)
                    elif intent =="open_facebook":
                        if internet():
                            speak(response)
                            webbrowser.open("https://www.facebook.com/")
                        else:
                            response="sorry internet not connneted"
                            speak(response)
                    elif intent =="open_github":
                        if internet():
                            speak(response)
                            webbrowser.open("https://github.com/")
                        else:
                            response="sorry internet not connneted"
                            speak(response)
                    elif intent =="open_codepen":
                        if internet():
                            speak(response)
                            webbrowser.open("https://codepen.io/")
                        else: 
                            response="sorry internet not connneted"
                            speak(response)
                    elif intent =="calculate":
                        from features.cal import calculate
                        user_input = user_input.replace("you :","")
                        re=calculate(user_input)
                        speak(response+str(re))
                    elif intent =="search_browser":
                        if internet():
                            from features.weather import google
                            google(user_input)
                        else:
                            response="sorry internet not connneted"
                            speak(response)
                    elif intent =="open":
                        from features.open import open as op
                        op(user_input)
                        speak(f"{response}{user_input}....")
                    elif intent =="news":
                        if internet():
                            speak(response)
                            from features.open import news
                            news(user_input)
                        else :
                            response="sorry internet not connneted"
                            speak(response)
                    elif intent =="search_wikipedia":
                        if internet():
                            a=response
                            from features.wiki import wiki
                            text,response = wiki(user_input)
                            speak(a+text)
                            speak(response)
                        else:
                            response="sorry internet not connneted"
                            speak(response)
                    elif intent =="music":
                        from features.song import song
                        response=song(user_input, response)
                    else:
                        speak(f"{response}")
                    log['intent'] = intent
                    log["maxmax_confidence"] = max_confidence
                    log["AI"] = response
                    log["min_confidence"] = min_confidence
                    logs.append(log) 
                    
                else:
                    speak("Sorry, I'm not sure how to respond to that.")
                    log['AI'] = "Sorry, I'm not sure how to respond to that."
                    log["maxmax_confidence"] = max_confidence
                    log["intent"]=intent
                    log["min_confidence"] = min_confidence
                    logs.append(log)
        
        with open('log/log.json', 'w') as json_file:
            json.dump(logs, json_file, indent=4)


# Main program
chatbot = ChatBot()
chatbot.start_chat()
