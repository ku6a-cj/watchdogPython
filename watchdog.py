from protonmail import ProtonMail

# Login credentials
username = "MaILPrOtOn@proton.me"
password = "extrasecretstuff"

# Initialize and login
proton = ProtonMail()
proton.login(username, password)

# Create a message
new_message = proton.create_message(
    recipients=["somegmail@gmail.com"],
    subject="Test Email from Python",
    body="Hello, this is a test email sent using Python on pc without Proton Mail Bridge. ;p"
)

# Send the message
proton.send_message(new_message)
