from flask import Flask, request, send_file, render_template
import pyotp

app = Flask(__name__)

secret_key = pyotp.random_base32()


@app.route('/', methods=["GET", "POST"])
def generate_otp():
    if request.method == "POST":
        # Generate an OTP token
        totp = pyotp.TOTP(secret_key)
        otp = totp.now()
        # In a real application, you would send this OTP to the user (e.g., via email or SMS)
        return "Generated OTP: {}".format(otp)
    return render_template("generate_otp.html")


if __name__ == "__main__":
    app.run()
