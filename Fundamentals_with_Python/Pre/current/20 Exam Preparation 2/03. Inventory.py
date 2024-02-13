def gather(journal: list, command: list):

    return "123"


journal_list = input().split(", ")
result_journal = []

while True:
    cmd = input()
    if cmd == "Craft!":
        break
    command_list = cmd.split(" - ")
    result_journal = gather(journal_list, command_list)
    journal_list = result_journal

print(", ".join(result_journal))
