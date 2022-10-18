# def solution(today, terms, privacies):
#     answer = []
#     today_list = list(map(int,today.split('.')))
#     # 약관 정보 딕셔너리
#     terms_dict = dict()
#     # 약관 정보 담기
#     for term in terms:
#         # 종류, 지속 월
#         kind, month_length = term.split()
#         terms_dict[kind] = int(month_length)
#     # 모든 privacy 탐색
#     for idx in range(len(privacies)):
#         privacy = privacies[idx]
#         day, privacy_kind = privacy.split()
#         day_list = list(map(int, day.split('.')))
#         # 날짜, 약관종류, 약관에 따른 계산 정보
#         day_list[1] += terms_dict[privacy_kind]
#         day_list[0] += day_list[1] // 12
#         day_list[1] = day_list[1] % 12
#         if day_list[0] <= today_list[0]:
#             if day_list[0] < today_list[0]:
#                 answer.append(idx+1)
#             elif day_list[1] < today_list[1]:
#                 answer.append(idx+1)
#             elif day_list[1] == today_list[1]:
#                 if day_list[2] <= today_list[2]:
#                     answer.append(idx+1)
#     print(answer)
#     return answer
# solution('2022.05.19', ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])


# def solution(cap, n, deliveries, pickups):
#     answer = 0
#     # 현재 배송, 픽업의 idx
#     d_idx = n-1
#     p_idx = n-1
#     # 배송, 회수가 끝날 때까지 진행
#     while d_idx >= 0 or p_idx >= 0:
#         d_cnt = 0
#         p_cnt = 0
#         # 현재 이동 간에 가장 먼 거리 계산
#         max_d_length = 0
#         max_p_length = 0
#         # 배송 가능한 상황 계산
#         while d_cnt < cap and d_idx >= 0:
#             if deliveries[d_idx]:
#                 max_d_length = max(max_d_length, d_idx+1)
#                 # 현재 배송 지역이 완료 덜 됐을 때
#                 if deliveries[d_idx] > cap - d_cnt:
#                     deliveries[d_idx] -= cap - d_cnt
#                     d_cnt = cap
#                 # 현재 배송 지역 완료 시
#                 else:
#                     d_cnt += deliveries[d_idx]
#                     deliveries[d_idx] = 0
#                     d_idx -= 1
#             # 배송 필요가 0일 때
#             else:
#                 d_idx -= 1
#         # 픽업 가능한 상황 계산
#         while p_cnt < cap and p_idx >= 0:
#             if pickups[p_idx]:
#                 max_p_length = max(max_p_length, p_idx+1)
#                 # 현재 픽업 지역이 완료 덜 됐을 때
#                 if pickups[p_idx] > cap - p_cnt:
#                     pickups[p_idx] -= cap - p_cnt
#                     p_cnt = cap
#                 # 현재 픽업 지역 완료 시
#                 else:
#                     p_cnt += pickups[p_idx]
#                     pickups[p_idx] = 0
#                     p_idx -= 1
#             # 픽업 필요가 0일 때
#             else:
#                 p_idx -= 1
#         # 가장 먼 거리 왕복 값 더하기
#         answer += max(max_d_length, max_p_length) * 2
#
#     return answer
# solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])

# def search(now, step, tree_num, post_result):
#     if step == 0:
#         if post_result == '0' and tree_num[now] == '1':
#             return False
#         return True
#     if post_result == '0' and tree_num[now] == '1':
#         return False
#     if not search(now - step, step // 2, tree_num, tree_num[now]):
#         return False
#     elif not search(now + step, step // 2, tree_num, tree_num[now]):
#         return False
#     else:
#         return True
#
#
#
# def solution(numbers):
#     answer = []
#     for idx in range(len(numbers)):
#         number = numbers[idx]
#         bin_num = ''
#         while number > 0:
#             if number % 2:
#                 bin_num += '1'
#             else:
#                 bin_num += '0'
#             number //= 2
#         bin_num = bin_num[::-1]
#         value = 1
#         while value - 1 < len(bin_num):
#             value *= 2
#         tree_num = '0' * (value - len(bin_num)) + bin_num
#         if tree_num[len(tree_num) // 2] == '0':
#             answer.append(0)
#         elif search(len(tree_num) // 2, len(tree_num) // 4, tree_num, 1):
#             answer.append(1)
#         else:
#             answer.append(0)
#     print(answer)
#     return answer
# solution([63, 111, 95])


def is_parent_exist(r, c, parent):
    if parent[r][c] == [2]:
        return r, c
    if len(parent[r][c]) == 2:
        p_r, p_c = parent[r][c]
        if parent[p_r][p_c] == [2]:
            return p_r, p_c
        elif len(parent[p_r][p_c]) == 2:
            return is_parent_exist(p_r,p_c, parent)
    return -1, -1


def solution(commands):
    answer = []
    graph = [[''] * 51 for _ in range(51)]
    parent = [[[] for _ in range(51)] for __ in range(51)]
    for command in commands:
        command_list = list(command.split())
        # 업데이트 명령
        if command_list[0] == 'UPDATE':
            # row, col 값 찾기
            if len(command_list) == 4:
                r, c, value = command_list[1:]
                r, c = int(r), int(c)
                # 부모와 병합 상태일 때
                p_r, p_c = is_parent_exist(r, c, parent)
                if p_r != -1:
                    graph[p_r][p_c] = value
                    continue
                else:
                    # 부모 초기화
                    parent[r][c] = []
                # 부모와 병합이 해제된 상태거나 병합 안 되어 있을 때
                graph[r][c] = value
            # value 값 찾기
            else:
                value1, value2 = command_list[1:]
                # value 완전 탐색 후 변경
                for row in range(1, 51):
                    for col in range(1, 51):
                        if graph[row][col] == value1:
                            graph[row][col] = value2
        # 셀 병합
        elif command_list[0] == 'MERGE':
            r1, c1, r2, c2 = map(int,command_list[1:])
            p_r1, p_c1 = is_parent_exist(r1,c1,parent)
            p_r2, p_c2 = is_parent_exist(r2,c2,parent)
            # r1이 부모가 없고 graph 값이 있을 때
            if graph[r1][c1]:
                # r2이 부모가 있을 때
                parent[r1][c1] = [2]
                if p_r2 != -1:
                    parent[p_r2][p_c2] = [r1, c1]
                    graph[p_r2][p_c2] = ''
                # r2이 부모가 없을 때
                else:
                    parent[r2][c2] = [r1,c1]
                    graph[r2][c2] = ''
            # r1의 부모가 있고 값이 있을 때
            elif p_r1 != -1 and graph[p_r1][p_c1]:
                # r2이 부모가 있을 때
                if p_r2 != -1:
                    parent[p_r2][p_c2] = [p_r1,p_c1]
                    graph[p_r2][p_c2] = ''
                # r2이 부모가 없을 때
                else:
                    parent[r2][c2] = [p_r1,p_c1]
                    graph[r2][c2] = ''
            # r2이 부모가 없고 graph 값이 있을 때
            elif graph[r2][c2]:
                parent[r2][c2] = [2]
                # r1이 부모가 있을 때
                if p_r1 != -1:
                    parent[p_r1][p_c1] = [r2, c2]
                    graph[p_r1][p_c1] = ''
                # r1이 부모가 없을 때
                else:
                    parent[r1][c1] = [r2,c2]
                    graph[r1][c1] = ''
            # r2의 부모가 있고 값이 있을 때
            elif p_r2 != -1 and graph[p_r2][p_c2]:
                # r1이 부모가 있을 때
                if p_r1 != -1:
                    parent[p_r1][p_c1] = [p_r2,p_c2]
                    graph[p_r1][p_c1] = ''
                # r1이 부모가 없을 때
                else:
                    parent[r1][c1] = [p_r2,p_c2]
                    graph[r1][c1] = ''
            else:
                if p_r1 != -1:
                    # r2이 부모가 있을 때
                    if p_r2 != -1:
                        parent[p_r2][p_c2] = [p_r1, p_c1]
                    # r2이 부모가 없을 때
                    else:
                        parent[r2][c2] = [p_r1, p_c1]
                else:
                    parent[r1][c1] = [2]
                    if p_r2 != -1:
                        parent[p_r2][p_c2] = [r1, c1]
                    # r2이 부모가 없을 때
                    else:
                        parent[r2][c2] = [r1, c1]
        # 셀 병합 해제
        elif command_list[0] == 'UNMERGE':
            r, c = command_list[1:]
            r, c = int(r), int(c)
            # 병합 상태 일 때
            p_r, p_c = is_parent_exist(r, c, parent)
            if p_r != -1:
                parent[p_r][p_c] = []
                graph[r][c] = graph[p_r][p_c]
                if r != p_r or c != p_c:
                    graph[p_r][p_c] = ''
                # 부모 초기화
            parent[r][c] = []
        # 프린트
        else:
            r, c = command_list[1:]
            r, c = int(r), int(c)
            p_r, p_c = is_parent_exist(r, c, parent)
            if p_r != -1:
                if graph[p_r][p_c]:
                    answer.append(graph[p_r][p_c])
                else:
                    answer.append('EMPTY')
            else:
                if graph[r][c]:
                    answer.append(graph[r][c])
                else:
                    answer.append('EMPTY')
    print(answer)
    return answer
solution(
["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "UPDATE d D","PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"])