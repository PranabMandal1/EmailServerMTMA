from flask import Flask, request, jsonify
import smtplib

app = Flask(__name__)

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your-email@gmail.com"
SENDER_PASSWORD = "your-app-password"

@app.route("/")
def home():
    return "Flask App is Running!"

@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.json
    recipient = data.get("email")
    subject = "Test Email"
    body = "This is a test email from Flask."

    if not recipient:
        return jsonify({"error": "Email is required"}), 400

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(SENDER_EMAIL, recipient, message)
        server.quit()
        return jsonify({"message": "Email sent successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
