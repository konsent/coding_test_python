alp = 0
cop = 0
problems = [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]

def solution(alp, cop, problems):
    answer = 0
    listA = []
    listB = []
    for i in range(len(problems)):
        listA.append(problems[i][0])
        listB.append(problems[i][1])
    goal = [max(listA), max(listB)]
    success = []

    while alp < goal[0] or cop < goal[1]:
        for i in range(len(problems)):
            if alp >= problems[i][0] and cop >= problems[i][1]:
                success.append(problems[i]) # 문제를 풀 수 있는 경우 성공 리스트에 넘김
            else: # 문제를 못푸는 경우
                if len(success) > 0: # 이미 푼 문제가 있는 경우 일단 문제 품
                    listA = []
                    listB = []
                    for j in success:
                        listA.append(j[2])
                        listB.append(j[3])
                    alp_idx = listA.index(max(listA)) # 푼 문제 중에서 알고력을 가장 많이 올려주는 문제 인덱스
                    cop_idx = listB.index(max(listB)) # 푼 문제 중에서 코딩력을 가장 많이 올려주는 문제 인덱스

                    alp_gap = problems[i][0] - alp
                    cop_gap = problems[i][1] - cop

                    if alp_gap > cop_gap: # 목표까지 알고력이 더 부족한 경우
                        while True:
                            if problems[i][0] == alp:
                                break
                            if alp == (problems[i][0] - success[alp_idx][2] + 1):
                                alp += 1
                                answer += 1
                                break
                            alp += success[alp_idx][2]
                            cop += success[alp_idx][3]
                            answer += success[alp_idx][4]
                            while cop_gap2 != cop:
                                cop += 1
                                answer += 1
                            success.append(problems[i])
                        cop_gap2 = problems[i][1] - cop
                        while cop_gap2 != cop:
                            cop += 1
                            answer += 1
                        success.append(problems[i])

                    else:
                        while True:
                            if problems[i][0] == cop:
                                break
                            if cop == (problems[i][1] - success[cop_idx][2] + 1):
                                cop += 1
                                answer += 1
                                break
                            alp += success[cop_idx][2]
                            cop += success[cop_idx][3]
                            answer += success[cop_idx][4]
                            while cop_gap2 != cop:
                                cop += 1
                                answer += 1
                            success.append(problems[i])
                        alp_gap2 = problems[i][1] - cop
                        while alp_gap2 != alp:
                            alp += 1
                            answer += 1
                        success.append(problems[i])

                else: # 이미 푼 문제가 없는 경우 공부함
                    while problems[i][0] != alp:
                        alp += 1
                        answer += 1
                    while problems[i][1] != cop:
                        cop += 1
                        answer += 1
                    success.append(problems[i])
    return answer

print(solution(alp, cop, problems))