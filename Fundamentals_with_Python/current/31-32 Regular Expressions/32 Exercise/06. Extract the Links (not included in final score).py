import re

while True:
    text = input()
    if not text:
        break
    pattern = r'www\.[a-zA-Z-0-9.]+\.[a-z]{2,}'
    sites = re.findall(pattern, text)
    for site in sites:
        print(site)
