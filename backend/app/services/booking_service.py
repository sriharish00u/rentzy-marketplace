from datetime import datetime

ACTIVE_STATUSES = {"pending","approved","payment_pending","confirmed","ready_for_pickup","active","return_requested","returned","inspection_pending","dispute"}

def dates_overlap(a_start, a_end, b_start, b_end):
    # ISO yyyy-mm-dd strings compare lexicographically
    return a_start <= b_end and b_start <= a_end


def compute_total(pricing: dict, duration_unit: str, duration: int, deposit: float, platform_fee_pct: float = 0.05):
    rate = float(pricing.get(duration_unit, 0) or 0)
    rental = rate * max(1, int(duration))
    platform_fee = round(rental * platform_fee_pct, 2)
    total = round(rental + float(deposit) + platform_fee, 2)
    return {"rate": rate, "rental": rental, "deposit": float(deposit), "platform_fee": platform_fee, "total": total}
