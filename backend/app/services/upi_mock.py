from urllib.parse import quote
from uuid import uuid4

def build_upi_intent(amount: float, booking_id: str, name: str = "Rental Marketplace") -> dict:
    txn_ref = uuid4().hex[:12].upper()
    pa = "rentalmarketplace@upi"  # mock payee
    pn = quote(name)
    tn = quote(f"Booking {booking_id}")
    am = f"{float(amount):.2f}"
    intent = f"upi://pay?pa={pa}&pn={pn}&am={am}&cu=INR&tn={tn}&tr={txn_ref}"
    return {"intent_url": intent, "txn_ref": txn_ref, "pa": pa}
