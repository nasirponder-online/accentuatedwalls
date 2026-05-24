from flask import Flask, request, render_template
import requests

app = Flask(__name__)

TEXTBELT_API_KEY = "b1c0cc90a35f15f6bd1bc202479b5ce213c52a22KIqnBwl1tL00WFPkHv3XMJv9v"  # free tier key (limited daily sends)
TO_NUMBER = "5855209798"

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/submitContactForm", methods=["POST"])
def submit_form():
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    phone = request.form.get("phonenumber")
    email = request.form.get("email")
    message = request.form.get("message")

    sms_text = (
        f"New Contact Form Submission:\n"
        f"Name: {firstname} {lastname}\n"
        f"Phone: {phone}\n"
        f"Email: {email}\n"
        f"Message: {message}"
    )

    response = requests.post("https://textbelt.com/text", {
        "phone": TO_NUMBER,
        "message": sms_text,
        "key": TEXTBELT_API_KEY
    })

    sms_text_user = (
        f"Hi {firstname}, this is Nasir with Accentuated Walls. We've received your message and will get back to you shortly. Thank you for your patience!"
    )

    requests.post("https://textbelt.com/text", {
        "phone": phone,
        "message": sms_text_user,
        "key": TEXTBELT_API_KEY
    })

    return render_template("index.html")
