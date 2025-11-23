from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Dict

from nlp_engine import detect_intent_and_entities
from banking_core import check_balance, view_transactions, transfer_money

app = FastAPI(
    title="FinVoice – AI Voice Assistant for Financial Operations",
    description="Talk. Transact. Trust.",
    version="1.0.0"
)


class VoiceCommand(BaseModel):
    text: str
    user_id: str
    language: Optional[str] = "en"


@app.get("/")
def read_root():
    return {
        "message": "Welcome to FinVoice API",
        "status": "running"
    }


@app.post("/voice-command")
def handle_voice_command(cmd: VoiceCommand) -> Dict:
    """
    Simulates handling a voice command.
    In real system: STT + NLP + Banking APIs + TTS.
    """
    nlp_result = detect_intent_and_entities(cmd.text)
    intent = nlp_result["intent"]
    entities = nlp_result["entities"]

    response: Dict = {
        "intent": intent,
        "entities": entities,
        "user_id": cmd.user_id
    }

    # Route intent to banking core logic
    if intent == "check_balance":
        balance_info = check_balance(cmd.user_id)
        response["assistant_reply"] = (
            f"Your current balance is ₹{balance_info['balance']:.2f}."
        )
        response["data"] = balance_info

    elif intent == "view_transactions":
        txn_info = view_transactions(cmd.user_id)
        response["assistant_reply"] = (
            f"I found {len(txn_info['transactions'])} recent transactions for you."
        )
        response["data"] = txn_info

    elif intent == "transfer_money":
        amount = entities.get("amount")
        receiver_name = entities.get("receiver_name", "recipient")

        if amount is None:
            response["assistant_reply"] = (
                "Please tell me the amount you want to transfer."
            )
        else:
            transfer_result = transfer_money(cmd.user_id, receiver_name, amount)
            response["assistant_reply"] = transfer_result["message"]
            response["data"] = transfer_result

    else:
        response["assistant_reply"] = (
            "I am not sure how to help with that yet. "
            "You can ask me to check your balance, view transactions, or transfer money."
        )

    return response
