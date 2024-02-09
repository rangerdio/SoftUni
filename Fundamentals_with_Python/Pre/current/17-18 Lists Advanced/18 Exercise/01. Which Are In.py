todo_notes = ["2-Walk", "1-Drink", "6-Dinner", "5-Work"]

# todo_notes = []
# while True:
#     note = input()
#     if note == "End":
#         break
#     todo_notes.append(note)
#
sorted_notes = sorted(todo_notes, key=lambda x: int(x.split("-")[0]))
print(sorted_notes)
sorted_notes = [note.split("-")[1] for note in sorted_notes]
print(sorted_notes)
