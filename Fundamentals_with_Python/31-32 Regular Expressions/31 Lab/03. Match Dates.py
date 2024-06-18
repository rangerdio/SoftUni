import re
string = input()
pattern = r"\b\d{2}[//][A-Z][a-z]{2}[//]\d{4}\b|\b\d{2}[-][A-Z][a-z]{2}[-]\d{4}\b|\b\d{2}[/.][A-Z][a-z]{2}[/.]\d{4}\b"
result = re.findall(pattern, string)

for element in result:
    if "/" in element:
        day = element.split("/")[0]
        month = element.split("/")[1]
        year = element.split("/")[2]

    elif "-" in element:
        day = element.split("-")[0]
        month = element.split("-")[1]
        year = element.split("-")[2]
    elif "." in element:
        day = element.split(".")[0]
        month = element.split(".")[1]
        year = element.split(".")[2]
    print(f"Day: {day}, Month: {month}, Year: {year}")
