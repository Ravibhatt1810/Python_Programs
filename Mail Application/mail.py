import tkinter as tk
import smtplib
from tkinter import messagebox

def send_email():
    # Replace these placeholders with your email credentials
    sender_email = 'your_email@gmail.com'
    sender_password = 'your_password'

    receiver_email = to_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END)

    try:
        # Connect to the SMTP server (Gmail in this example)
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password)

        # Create the email message
        email_message = f'Subject: {subject}\n\n{message}'

        # Send the email
        smtp_server.sendmail(sender_email, receiver_email, email_message)

        # Close the SMTP server
        smtp_server.quit()

        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Email could not be sent.\nError: {str(e)}")

# Create the main window
window = tk.Tk()
window.title("Mail Application")

# Create labels and entry widgets
to_label = tk.Label(window, text="To:")
to_label.pack()
to_entry = tk.Entry(window)
to_entry.pack()

subject_label = tk.Label(window, text="Subject:")
subject_label.pack()
subject_entry = tk.Entry(window)
subject_entry.pack()

message_label = tk.Label(window, text="Message:")
message_label.pack()
message_text = tk.Text(window, height=5, width=40)
message_text.pack()

# Create the send button
send_button = tk.Button(window, text="Send Email", command=send_email)
send_button.pack()

# Start the main loop
window.mainloop()
