def add_comment(comment_: str):
    return f"<div>\n    {comment_}\n</div>"


title = input()
content = input()
comments = []
while True:
    comment = input()
    if comment == "end of comments":
        break
    comments.append(comment)

print(f"<h1>\n    {title}\n</h1>")
print(f"<article>\n    {content}\n</article>")
for comment in comments:
    print(add_comment(comment))
