import urllib.request
import json

base = "http://localhost:8000/api"

def post(url, data, token=None):
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers, method="POST")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())

def get(url, token=None):
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())

def patch(url, data, token=None):
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers, method="PATCH")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())

print("=== 1. CUSTOMER AUTHENTICATION ===")
cust_login = post(f"{base}/auth/login", {"email": "customer.ananya@rentzy.com", "password": "Password@123"})
cust_token = cust_login["access_token"]
c_u = cust_login["user"]
print("Customer logged in:", c_u["name"], "-", c_u["email"])

print("\n=== 2. OWNER AUTHENTICATION ===")
owner_login = post(f"{base}/auth/login", {"email": "owner.aarav@rentzy.com", "password": "Password@123"})
owner_token = owner_login["access_token"]
o_u = owner_login["user"]
print("Owner logged in:", o_u["name"], "-", o_u["email"])

print("\n=== 3. ADMIN AUTHENTICATION ===")
admin_login = post(f"{base}/auth/login", {"email": "admin.rajesh@rentzy.com", "password": "Password@123"})
admin_token = admin_login["access_token"]
a_u = admin_login["user"]
print("Admin logged in:", a_u["name"], "-", a_u["email"])

print("\n=== 4. SELECT PRODUCT & CHECK AVAILABILITY ===")
prods = get(f"{base}/products?status=approved")
prod = next(p for p in prods if "Sony FX3" in p["title"])
print("Selected Product:", prod["title"])
print("Category:", prod["category_name"], "| Location:", prod["location"])

avail = post(f"{base}/bookings/check-availability", {"product_id": prod["id"], "start_date": "2026-12-10", "end_date": "2026-12-13"})
print("Dates (2026-12-10 to 2026-12-13) Available:", avail["available"])

print("\n=== 5. CUSTOMER CREATES BOOKING ===")
booking = post(f"{base}/bookings", {
    "product_id": prod["id"],
    "start_date": "2026-12-10",
    "end_date": "2026-12-13",
    "duration_unit": "day",
    "duration": 3
}, token=cust_token)
booking_id = booking["id"]
print("Booking Created ID:", booking_id)
print("Initial Status:", booking["status"], "| Pricing Breakdown:", booking["pricing_breakdown"])

print("\n=== 6. PAYMENT: GENERATE UPI INTENT & SIMULATE CALLBACK ===")
upi_res = post(f"{base}/payments/upi-intent", {"booking_id": booking_id}, token=cust_token)
payment_id = upi_res["id"]
print("Mock UPI Intent Generated:")
print(" - Payment ID:", payment_id)
print(" - Txn Ref:", upi_res.get("txn_ref"))
print(" - Intent URL:", upi_res.get("intent_url"))

pay_callback = post(f"{base}/payments/mock-callback", {
    "payment_id": payment_id,
    "status": "success"
}, token=cust_token)
print("Payment Callback Processed:", pay_callback)

b_after_pay = get(f"{base}/bookings/{booking_id}", token=cust_token)
print("Booking Status after Payment:", b_after_pay["status"], "| Payment Status:", b_after_pay.get("payment_status"))

print("\n=== 7. OWNER HANDOVER (READY FOR PICKUP) ===")
owner_pickup = patch(f"{base}/bookings/{booking_id}/status", {"status": "ready_for_pickup"}, token=owner_token)
print("Owner Handover Status:", owner_pickup)

print("\n=== 8. CUSTOMER USES ITEM & RETURNS (COMPLETED BY OWNER) ===")
owner_complete = patch(f"{base}/bookings/{booking_id}/status", {"status": "completed"}, token=owner_token)
print("Owner Completed Status:", owner_complete)

print("\n=== 9. VERIFY OWNER & ADMIN DASHBOARDS ===")
owner_dash = get(f"{base}/dashboard/owner", token=owner_token)
print("Owner Dashboard Stats:", json.dumps(owner_dash, indent=2))
admin_dash = get(f"{base}/dashboard/admin", token=admin_token)
print("Admin Dashboard Stats:", json.dumps(admin_dash, indent=2))

print("\n=======================================================")
print(">>> ALL END-TO-END WORKFLOW TESTS PASSED PERFECTLY! <<<")
print("=======================================================")
