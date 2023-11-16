def solution(word):
    countr = 0
    for x in range(len(word)//2, 0, -1):
        if word[:x] == word[-x:]:
            countr += len(word[:x])
    return countr



print(solution("onaona"))