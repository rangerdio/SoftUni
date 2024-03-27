import re
text = "Just send email to s.miller@mit.edu and j.hopking@york.ac.uk for more information."
pattern = r'\b[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
matches = re.findall(pattern, text)
for match in matches:
    print(match)
