intents = {
    "greetings": {
        "patterns": ["hello", "hi", "hey", "howdy", "greetings", "good morning", "good afternoon", "good evening", "hi there", "hey there", "what's up", "hello there"],
        "responses": ["Hello! How can I assist you?", "Hi there!", "Hey! What can I do for you?", "Howdy! What brings you here?", "Greetings! How may I help you?", "Good morning! How can I be of service?", "Good afternoon! What do you need assistance with?", "Good evening! How may I assist you?", "Hey there! How can I help?", "Hi! What's on your mind?", "Hello there! How can I assist you today?"]
    },
    "goodbye": {
        "patterns": ["bye", "see you later", "goodbye", "farewell", "take care", "until next time", "bye bye", "catch you later", "have a good one", "so long"],
        "responses": ["Goodbye!", "See you later!", "Have a great day!", "Farewell! Take care.", "Goodbye! Until next time.", "Take care! Have a wonderful day.", "Bye bye!", "Catch you later!", "Have a good one!", "So long!"]
    },
    "gratitude": {
        "patterns": ["thank you", "thanks", "appreciate it", "thank you so much", "thanks a lot", "much appreciated"],
        "responses": ["You're welcome!", "Happy to help!", "Glad I could assist.", "Anytime!", "You're welcome! Have a great day.", "No problem!"]
    },
    "apologies": {
        "patterns": ["sorry", "my apologies", "apologize", "I'm sorry"],
        "responses": ["No problem at all.", "It's alright.", "No need to apologize.", "That's okay.", "Don't worry about it.", "Apology accepted."]
    },
    "positive_feedback": {
        "patterns": ["great job", "well done", "awesome", "fantastic", "amazing work", "excellent"],
        "responses": ["Thank you! I appreciate your feedback.", "Glad to hear that!", "Thank you for the compliment!", "I'm glad I could meet your expectations.", "Your words motivate me!", "Thank you for your kind words."]
    },
    "negative_feedback": {
        "patterns": ["not good", "disappointed", "unsatisfied", "poor service", "needs improvement", "could be better"],
        "responses": ["I'm sorry to hear that. Can you please provide more details so I can assist you better?", "I apologize for the inconvenience. Let me help resolve the issue.", "I'm sorry you're not satisfied. Please let me know how I can improve.", "Your feedback is valuable. I'll work on improving."]
    },
    "weather": {
        "patterns": ["what's the weather like?", "weather forecast", "is it going to rain today?", "temperature today", "weather report"],
        "responses": ["The weather today is [weather_description].", "Currently, it's [temperature] degrees with [weather_description].", "The forecast predicts [weather_forecast].", "It might rain today. Don't forget your umbrella!", "The temperature today is [temperature] degrees."]
    },
    "help": {
        "patterns": ["help", "can you help me?", "I need assistance", "support"],
        "responses": ["Sure, I'll do my best to assist you.", "Of course, I'm here to help!", "How can I assist you?", "I'll help you with your query."]
    },
    "time": {
        "patterns": ["what's the time?", "current time", "time please", "what time is it?"],
        "responses": ["It's [current_time].", "The current time is [current_time].", "Right now, it's [current_time]."]
    },
    "jokes": {
        "patterns": ["tell me a joke", "joke please", "got any jokes?", "make me laugh"],
        "responses": ["Why don't we ever tell secrets on a farm? Because the potatoes have eyes and the corn has ears!", "What do you get when you cross a snowman and a vampire? Frostbite!", "Why was the math book sad? Because it had too many problems!"]
    },
    "music": {
        "patterns": ["play music", "music please", "song recommendation", "music suggestion"],
        "responses": ["Sure, playing some music for you!", "Here's a song you might like: [song_name]", "How about some music?"]
    },
    "food": {
        "patterns": ["recommend a restaurant", "food places nearby", "what's good to eat?", "restaurant suggestion"],
        "responses": ["Sure, here are some recommended restaurants: [restaurant_names]", "Hungry? Let me find some good food places for you!", "I can suggest some great places to eat nearby."]
    },
    "news": {
        "patterns": ["latest news", "news updates", "what's happening?", "current events"],
        "responses": ["Let me fetch the latest news for you.", "Here are the top headlines: [news_headlines]", "Stay updated with the latest news!"]
    },
    "movies": {
        "patterns": ["movie suggestions", "recommend a movie", "what should I watch?", "best movies"],
        "responses": ["How about watching [movie_name]?", "Here's a movie suggestion for you.", "Let me recommend some great movies!"]
    },
    "sports": {
        "patterns": ["sports news", "score updates", "latest sports events", "upcoming games"],
        "responses": ["I'll get you the latest sports updates.", "Stay updated with the current sports events!", "Let me check the sports scores for you."]
    },
    "gaming": {
        "patterns": ["video game recommendations", "best games to play", "recommend a game", "gaming suggestions"],
        "responses": ["How about trying out [game_name]?", "Here are some gaming suggestions for you!", "Let me recommend some fun games to play!"]
    },
        "tech_support": {
        "patterns": ["technical help", "computer issues", "troubleshooting", "IT support"],
        "responses": ["I can assist with technical issues. What problem are you facing?", "Let's troubleshoot your technical problem together.", "Tell me about the technical issue you're experiencing."]
    },
    "book_recommendation": {
        "patterns": ["recommend a book", "good books to read", "book suggestions", "what should I read?"],
        "responses": ["How about reading [book_title]?", "I've got some great book recommendations for you!", "Let me suggest some interesting books for you to read."]
    },
    "fitness_tips": {
        "patterns": ["fitness advice", "workout tips", "exercise suggestions", "healthy habits"],
        "responses": ["Staying fit is important! Here are some fitness tips: [fitness_tips]", "I can help you with workout suggestions and fitness advice.", "Let me provide some exercise recommendations for you."]
    },
    "travel_recommendation": {
        "patterns": ["travel suggestions", "places to visit", "recommend a destination", "travel ideas"],
        "responses": ["Looking for travel recommendations? Here are some great destinations: [travel_destinations]", "I can suggest some amazing places for your next travel adventure!", "Let me help you with travel destination ideas."]
    },
    "education": {
        "patterns": ["learning resources", "study tips", "education advice", "academic help"],
        "responses": ["I can assist with educational queries. What subject are you studying?", "Let's explore learning resources together.", "Tell me about your educational goals or questions."]
    },
    "pet_advice": {
        "patterns": ["pet care tips", "animal advice", "pet health", "taking care of pets"],
        "responses": ["Pets are wonderful! Here are some pet care tips: [pet_care_tips]", "I can provide advice on pet health and care.", "Let's talk about your pet and their well-being."]
    },
    "shopping": {
        "patterns": ["online shopping", "buying something", "shopping advice", "product recommendations"],
        "responses": ["I can help you with online shopping. What are you looking to buy?", "Let's find the perfect item for you!", "Tell me what you're interested in purchasing."]
    },
    "career_advice": {
        "patterns": ["job search help", "career guidance", "career change advice", "professional development"],
        "responses": ["I can provide career advice. What specific guidance do you need?", "Let's explore career opportunities together.", "Tell me about your career goals or concerns."]
    },
    "relationship_advice": {
        "patterns": ["relationship help", "love advice", "dating tips", "relationship problems"],
        "responses": ["Relationships can be complex. How can I assist you?", "I can offer advice on relationships and dating.", "Tell me about your relationship situation."]
    },
    "mental_health": {
        "patterns": ["mental health support", "coping strategies", "stress relief tips", "emotional well-being"],
        "responses": ["Mental health is important. How can I support you?", "I can provide guidance for managing stress and emotions.", "Let's talk about strategies for maintaining mental well-being."]
    },
    "language_learning": {
        "patterns": ["language learning tips", "language practice", "learning new languages", "language study advice"],
        "responses": ["Learning a new language can be exciting! How can I assist you?", "I can help with language learning tips and practice.", "Tell me which language you're interested in learning."]
    },
    "finance_advice": {
        "patterns": ["financial planning help", "money management tips", "investment advice", "budgeting assistance"],
        "responses": ["I can provide guidance on financial matters. What specific advice do you need?", "Let's discuss your financial goals and plans.", "Tell me about your financial situation or goals."]
    },"weather": {
    "patterns": [
        "what's the weather like?",
        "weather forecast",
        "is it going to rain today?",
        "temperature today",
        "weather report",
        "how's the weather?"
    ],
    "responses": [
        "The weather today is [weather_description].",
        "Currently, it's [temperature] degrees with [weather_description].",
        "The forecast predicts [weather_forecast].",
        "It might rain today. Don't forget your umbrella!",
        "The temperature today is [temperature] degrees."
    ]
},
"help": {
    "patterns": [
        "help",
        "can you help me?",
        "I need assistance",
        "support",
        "help me"
    ],
    "responses": [
        "Sure, I'll do my best to assist you.",
        "Of course, I'm here to help!",
        "How can I assist you?",
        "I'll help you with your query."
    ]
},
"time": {
    "patterns": [
        "what's the time?",
        "current time",
        "time please",
        "what time is it?",
        "tell me the time"
    ],
    "responses": [
        "It's ",
        "The current time is ",
        "Right now, it's "
    ]
},
"introduction": {
    "patterns": [
        "introduction",
        "What can you do",
        "Tell me about yourself.",
        "introduce yourself",
        "who are you?"
    ],
    "responses": [
        "Hello! I'm your virtual assistant.",
        "Hi there! I'm here to assist you.",
        "Hey! I'm the chatbot designed to help you.",
        "Nice to meet you! I'm your AI assistant.",
        "Greetings! I am your virtual assistant ready to help.",
        "I'm Jarvis, an AI designed to assist you. I can help with tasks like providing information, answering questions, scheduling events, and much more. Feel free to ask me anything you need help with",
        "I'm Jarvis, an advanced artificial intelligence programmed to learn and assist users. My goal is to make your life easier by providing timely and accurate information while adapting to your needs.",
        "I'm Jarvis, your personal AI assistant here to assist you with tasks, answer questions, and streamline your daily routines.",
        "Absolutely! I'm here to assist you. Just let me know what you need help with, whether it's finding information, managing your schedule, or providing recommendations.",
        "I'm equipped with various capabilities designed to make your life easier. From providing real-time information, setting reminders, managing tasks, to offering personalized recommendations, I'm here to cater to your needs.",
        "I work by processing and analyzing information using advanced algorithms and artificial intelligence techniques. I continuously learn from interactions to improve and provide better assistance tailored to your preferences.",
    ]
},
"open_bower": {
    "patterns": [
        "open Bower",
        "launch Bower",
        "start Bower",
        "run Bower"
    ],
    "responses": [
        "Sure, initiating Bower...",
        "Opening Bower for package management.",
        "Launching Bower now.",
        "Starting Bower..."
    ]
},"open_youtube": {
    "patterns": [
        "open YouTube",
        "launch YouTube",
        "start YouTube",
        "go to YouTube"
    ],
    "responses": [
        "Sure, redirecting to YouTube...",
        "Opening YouTube for you.",
        "Launching YouTube now.",
        "Starting YouTube..."
    ]
},"chatgpt_interaction": {
    "patterns": [
        "talk to ChatGPT",
        "start chatting",
        "engage ChatGPT",
        "open chatgpt"
    ],
    "responses": [
        "Sure, let's chat! How can I assist you today?",
        "I'm here to chat! Feel free to ask or discuss anything.",
        "Let's engage with ChatGPT for a conversation.",
        "Starting a conversation with ChatGPT..."
    ]
},"open_google": {
    "patterns": [
        "open Google",
        "go to Google",
        "launch Google",
        "Google"
    ],
    "responses": [
        "Sure, redirecting to Google...",
        "Opening Google for you.",
        "Launching Google now."
    ]
},"open_amazon": {
    "patterns": [
        "open Amazon",
        "go to Amazon",
        "launch Amazon",
        "Amazon"
    ],
    "responses": [
        "Sure, redirecting to Amazon...",
        "Opening Amazon for you.",
        "Launching Amazon now."
    ]
},"open_facebook": {
    "patterns": [
        "open Facebook",
        "go to Facebook",
        "launch Facebook",
        "Facebook"
    ],
    "responses": [
        "Sure, redirecting to Facebook...",
        "Opening Facebook for you.",
        "Launching Facebook now."
    ]
},"open_github": {
    "patterns": [
        "open GitHub",
        "go to GitHub",
        "launch GitHub",
        "GitHub"
    ],
    "responses": [
        "Sure, redirecting to GitHub...",
        "Opening GitHub for you.",
        "Launching GitHub now."
    ]
},"open_stackoverflow": {
    "patterns": [
        "open Stack Overflow",
        "go to Stack Overflow",
        "launch Stack Overflow",
        "Stack Overflow"
    ],
    "responses": [
        "Sure, redirecting to Stack Overflow...",
        "Opening Stack Overflow for you.",
        "Launching Stack Overflow now."
    ]
},"open_codepen": {
    "patterns": [
        "open CodePen",
        "go to CodePen",
        "launch CodePen",
        "CodePen"
    ],
    "responses": [
        "Sure, redirecting to CodePen...",
        "Opening CodePen for you.",
        "Launching CodePen now."
    ]
},"open_jsfiddle": {
    "patterns": [
        "open JSFiddle",
        "go to JSFiddle",
        "launch JSFiddle",
        "JSFiddle"
    ],
    "responses": [
        "Sure, redirecting to JSFiddle...",
        "Opening JSFiddle for you.",
        "Launching JSFiddle now."
    ]
},"search_browser": {
    "patterns": [
        "search",
        "search on browser",
        "search the web",
        "look up information",
        "perform a web search"
    ],
    "responses": [
        "Sure, initiating a web search...",
        "Opening the browser for web search.",
        "Let's search the web for you.",
        "Starting a web search..."
    ]
},"play_song": {
    "patterns": ["play a song", "play music from folder", "play a track"],
    "responses": ["Sure, playing a song for you!", "Let's enjoy some music!", "Playing music from the folder."]
},"open_code_folder": {
    "patterns": [
        "open code folder",
        "go to code directory",
        "access code directory",
        "open folder containing code"
    ],
    "responses": [
        "Sure, navigating to the code folder...",
        "Opening the code directory for you.",
        "Accessing the folder containing code...",
        "Let's open the code folder."
    ]
},"access_c_drive": {
    "patterns": [
        "open C drive",
        "go to C drive",
        "access C drive",
        "navigate to C drive"
    ],
    "responses": [
        "Sure, navigating to the c drive...",
        "Opening the c drive for you.",
        "Accessing drive c...",
        "Let's open the c drive."
    ]
},"access_d_drive": {
    "patterns": [
        "open d drive",
        "go to d drive",
        "access d drive",
        "navigate to d drive"
    ],
    "responses": [
        "Sure, navigating to the d drive...",
        "Opening the d drive for you.",
        "Accessing drive d...",
        "Let's open the d drive."
    ]
},"open": {#esa the kar liyo 
    "patterns": [
        "open",
        "start",
        "launch",
        "run"
    ],
    "responses": [
        "Opening ",
        "Starting ",
        "Launching ",
        "Running "
    ]
}
,"calculate": {
    "patterns": [
        "calculate ",
        "solve ",
        "what is ",
        "evaluate "
    ],
    "responses": [
        "The result of ",
        "The answer to ",
    ]
},"search_wikipedia": {
    "patterns": [
        "searchon Wikipedia",
        "find information abouton Wikipedia",
        "look upon Wikipedia",
        "what ison Wikipedia",
        "tell me about",
        "who is ",
        "what is ",
        "information about"
    ],
    "responses": [
        "Let me find information abouton Wikipedia.",
        "Searching Wikipedia for details about",
        "I'll look up information abouton Wikipedia.",
        "Gathering details about [person/thing] from Wikipedia.",
        "I'll fetch information about [person/thing] from Wikipedia."
    ]
}





}