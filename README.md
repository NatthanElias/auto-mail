# Python Auto-mail
This Python script is designed to send multiple emails with attachments using Gmail's SMTP server. It can be useful for sending job applications to potential employers.

## Problem Solved
While studying some Python, I encountered a real-world problem: assisting my girlfriend in sending multiple emails to potential employers. To address this, I developed this program.
  
## Usage

1. Make sure you have Python installed on your system.
2. Clone or download this repository.
3. Update `senha.txt` with one of your Gmail App Passwords.
4. Update `lista_emails.txt` with the list of recipient email addresses.
5. Customize the email body in the script (`texto_email` variable).
6. Place the attachment (e.g., CV.pdf) in the same directory as the script.
7. Run the script using `python script.py`.

## Note

- This script is configured to work with Gmail's SMTP server. If you're using a different email provider, you may need to modify the SMTP settings accordingly.
- Be cautious with your Gmail password. Avoid hardcoding it directly in the script if sharing the code publicly.
- Ensure that you're following the terms of service of your email provider and avoid spamming.
