import re

text = "Contact us at support@google.com, sales.team@zomato.co.in or reach out directly to rudrapatil2986@healthora.org for inquiries."
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(email_pattern, text)

print("Found Email Addresses:")
for email in emails:
    print(f"- {email}")