import smtplib

# take input from the user
sender_email = input("Enter your email address: ")
receiver_email = input("Enter the recipient's email address: ")
email_subject = input("Enter the email subject: ")
email_body = input("Enter the email body: ")
confirmation = input("Are you sure you want to send this email? (Y/N)")

if confirmation.lower() == 'y':
    password = input("Enter your email password: ")

    # set up the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.starttls()

        # login to the email account
        smtp_connection.login(sender_email, password)

        # construct the message
        message = f"Subject: {email_subject}\n\n{email_body}"

        # send the email
        smtp_connection.sendmail(sender_email, receiver_email, message)

        print("Email sent successfully.")
    except Exception as e:
        print("An error occurred while sending the email: ", e)
    finally:
        smtp_connection.quit()
else:
    print("Email sending canceled by user.")

