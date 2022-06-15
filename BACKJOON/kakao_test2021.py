survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

def solution(survey, choices):
    answer = ''
    idx = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'M': 0,
        'J': 0,
        'A': 0,
        'N': 0,
    }
    idx_list = ['RT','CF','JM','AN']
    for i in range(len(survey)):
        if choices[i] > 4:
            idx[survey[i][1]] += abs(4-choices[i])
        elif choices[i] < 4:
            idx[survey[i][0]] += abs(4-choices[i])

    for i in idx_list:
        if idx[i[0]] > idx[i[1]]:
            answer += str(i[0])

        elif idx[i[0]] < idx[i[1]]:
            answer += str(i[1])
        else:
            answer += str(i[0])
    return answer


print(solution(survey, choices))