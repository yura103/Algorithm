def solution(info, n, m):
    cases = {(0, 0)}

    for a_trace, b_trace in info:
        next_cases = set()

        for a, b in cases:
            # A가 훔치는 경우
            if a + a_trace < n:
                next_cases.add((a + a_trace, b))

            # B가 훔치는 경우
            if b + b_trace < m:
                next_cases.add((a, b + b_trace))

        cases = next_cases

        if not cases:
            return -1

    answer = n

    for a, b in cases:
        if a < answer:
            answer = a

    return answer