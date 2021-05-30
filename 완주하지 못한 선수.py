def solution(participant, completion):
    answer = ''

    completion = {p: p for p in completion}
    print(participant)
    for i in range(len(participant)):
        comp = completion.get(participant[i])
        print(participant)
        if comp is None:
            answer = comp
    return answer

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

result = solution(participant, completion)
print(result)