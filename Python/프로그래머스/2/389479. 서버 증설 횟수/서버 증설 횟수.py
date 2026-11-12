def solution(players, m, k):
    answer = 0
    server = [1] * len(players)

    for i in range(len(players)):
        n = players[i] // m

        if (n + 1) > server[i]:
            add = (n + 1) - server[i]
            answer += add

            for j in range(i, min(i + k, len(players))):
                server[j] += add

    return answer