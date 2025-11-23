
# Simple rule-based NLP engine (placeholder for real BERT/Whisper models)

from typing import Dict


def detect_intent_and_entities(text: str) -> Dict:
    """
    Very basic rule-based intent + entity extraction.
    Replace later with real NLP models.
    """
    text_lower = text.lower()

    intent = "smalltalk"
    entities = {}

    # Intent detection
    if "balance" in text_lower:
        intent = "check_balance"
    elif "transfer" in text_lower or "send money" in text_lower:
        intent = "transfer_money"
    elif "transactions" in text_lower or "history" in text_lower or "statement" in text_lower:
        intent = "view_transactions"

    # Simple entity extraction
    # Example: "transfer 500 to rohan"
    words = text_lower.split()
    for i, w in enumerate(words):
        if w.isdigit():
            entities["amount"] = float(w)
        if w in ["to", "for"] and i + 1 < len(words):
            entities["receiver_name"] = words[i + 1].capitalize()

    return {
        "intent": intent,
        "entities": entities
    }
