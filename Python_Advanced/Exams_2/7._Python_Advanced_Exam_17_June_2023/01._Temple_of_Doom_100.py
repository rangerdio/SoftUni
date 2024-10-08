from collections import deque
tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]


while challenges and tools and substances:
    current_tool = tools.popleft()
    current_substance = substances.pop()
    action_result = current_tool * current_substance
    if action_result in challenges:
        challenges.remove(action_result)
    else:
        current_tool += 1
        tools.append(current_tool)
        current_substance -= 1
        if current_substance > 0:
            substances.append(current_substance)

if not challenges:
    print('Harry found an ostracon, which is dated to the 6th century BCE.')
else:
    print('Harry is lost in the temple. Oblivion awaits him.')

if tools:
    print(f'Tools: {", ".join(map(str, tools))}')
if substances:
    print(f"Substances: {', '.join([str(x) for x in substances])}")
if challenges:
    print(f"Challenges: {', '.join([str(x) for x in challenges])}")
