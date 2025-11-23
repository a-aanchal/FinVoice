# FinVoice - AI Voice Banking Assistant
#Talk. Transact. Trust.

FinVoice is a voice-enabled banking assistant that allows users to check balances, view transaction history, and transfer money using natural language commands.
It combines FastAPI backend, a rule-based NLP engine, and a modern HTML/CSS frontend with browser Speech Recognition.

⭐ Features
🔊 Voice-Based Banking

Speak commands like “Check my balance” or “Transfer 500 to Rohan”
Built-in browser speech recognition (Chrome/Edge)

🤖 NLP Intent Detection

Detects intents:

check_balance

view_transactions

transfer_money

Extracts entities like amount and receiver name
(from nlp_engine.py 

nlp_engine

)

🏦 Core Banking Logic (Demo)

Mock functions:

Check account balance

Retrieve transaction history

Transfer money between users
(from banking_core.py 

banking_core

)

🌐 FastAPI Backend

POST /voice-command

Routes NLP results to banking functions
(from main.py 

main

)

🎨 Modern UI

Responsive card layout

Input fields + voice mic button
(from index.html 

index

)
