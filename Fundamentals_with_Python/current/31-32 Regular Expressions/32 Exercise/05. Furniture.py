import re


def extract_emails(text):
    # Regex pattern for extracting email addresses
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Find all matches in the text
    emails = re.findall(pattern, text)

    # Print the extracted email addresses on separate lines
    for email in emails:
        print(email)


# Test the function
text = "Valid emails: info@softuni-bulgaria.org, kiki@hotmail.co.uk, no-reply@github.com, s.peterson@mail.uu.net, info-bg@software-university.software.academy. Invalid emails: --123@gmail.com, …@mail.bg, .info@info.info, _steve@yahoo.cn, mike@helloworld, mike@.unknown.soft., s.johnson@invalid-"
extract_emails(text)
