# Mock core banking logic (no real bank connection)

from typing import Dict


# In-memory "database" for demo
USER_BALANCES = {
    "user123": 15000.50,
    "user456": 3200.00,
}

USER_TRANSACTIONS = {
    "user123": [
        {"id": 1, "type": "debit", "amount": 500.0, "description": "Electricity Bill"},
        {"id": 2, "type": "credit", "amount": 2000.0, "description": "Salary"},
    ],
    "user456": [
        {"id": 1, "type": "debit", "amount": 1000.0, "description": "Groceries"},
    ],
}


def check_balance(user_id: str) -> Dict:
    balance = USER_BALANCES.get(user_id, 0.0)
    return {
        "user_id": user_id,
        "balance": balance
    }


def view_transactions(user_id: str) -> Dict:
    txns = USER_TRANSACTIONS.get(user_id, [])
    return {
        "user_id": user_id,
        "transactions": txns
    }


def transfer_money(sender_id: str, receiver_name: str, amount: float) -> Dict:
    # For demo: just deduct amount from sender, no real receiver logic
    balance = USER_BALANCES.get(sender_id, 0.0)

    if amount <= 0:
        return {
            "success": False,
            "message": "Invalid amount."
        }

    if amount > balance:
        return {
            "success": False,
            "message": "Insufficient balance."
        }

    USER_BALANCES[sender_id] = balance - amount

    # Append a mock transaction
    txns = USER_TRANSACTIONS.setdefault(sender_id, [])
    txns.append({
        "id": len(txns) + 1,
        "type": "debit",
        "amount": amount,
        "description": f"Transfer to {receiver_name}"
    })

    return {
        "success": True,
        "message": f"Transferred ₹{amount} to {receiver_name}",
        "new_balance": USER_BALANCES[sender_id]
    }
