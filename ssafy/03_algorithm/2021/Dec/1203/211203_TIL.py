import sys

sys.stdin = open('input.txt', 'r')

## SW 1865 동철이의 일 분배
# def dfs(step, percent):
#     global max_percent
#     if step == N:
#         if max_percent < percent:
#             max_percent = percent
#             return
#     if max_percent >= percent or percent == 0:
#         return
#     for i in range(N):
#         if visited[i] == 0:
#             visited[i] = 1
#             dfs(step+1, percent * MAP[step][i])
#             visited[i] = 0
#     return
#
# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     MAP = [list(map(lambda x:float(x) / 100,input().split())) for _ in range(N)]
#     max_percent = 0
#     visited = [0] * N
#     dfs(0,1)
#     ans = format(float(max_percent) * 100, ".6f")
#     print('#{} {}'.format(t,ans))


## SW 2383. [모의 SW 역량테스트] 점심 식사시간
# def find_exit():
#     for r in range(N):
#         for c in range(N):
#             if MAP[r][c] > 1:
#                 exit_tong.append((r, c, MAP[r][c]))
#
#
# def calcul_distance():
#     exit_r1, exit_c1 = exit_tong[0][0], exit_tong[0][1]
#     exit_r2, exit_c2 = exit_tong[1][0], exit_tong[1][1]
#     for r in range(N):
#         for c in range(N):
#             if MAP[r][c] == 1:
#                 distance1 = abs(r - exit_r1) + abs(c - exit_c1)
#                 distance2 = abs(r - exit_r2) + abs(c - exit_c2)
#                 distance_list.append([distance1, distance2])
#     cnt = len(distance_list)
#     return cnt
#
#
# def move_people():
#     global people_set
#     global min_minutes
#     this_minutes = [0,0]
#     for n in range(2):
#         people_units_cnt = len(people_set[n])
#         stepping_people = 0
#         complete_people = 0
#         steps = exit_tong[n][2]
#         while complete_people < people_units_cnt:
#             candidate = 0
#             for now in range(people_units_cnt):
#                 if people_set[n][now] > 0:
#                     people_set[n][now] -= 1
#                 elif people_set[n][now] == 0:
#                     if stepping_people < 3:
#                         stepping_people += 1
#                         people_set[n][now] -= 1
#                 elif people_set[n][now] + steps > 0:
#                     people_set[n][now] -= 1
#                     if people_set[n][now] + steps == 0:
#                         candidate += 1
#             complete_people += candidate
#             stepping_people -= candidate
#             this_minutes[n] += 1
#             if min_minutes <= this_minutes[n]:
#                 break
#     ret = max(this_minutes[0], this_minutes[1])
#     return ret
#
#
#
#
# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     MAP = [list(map(int, input().split())) for _ in range(N)]
#     exit_tong = []
#     distance_list = []
#     min_minutes = 2e29
#     find_exit()
#     people_cnt = calcul_distance()
#     for i in range(2 ** people_cnt):
#         all_people_set = [0] * people_cnt
#         people_set = [[],[]]
#         idx = people_cnt - 1
#         while i > 0:
#             if i % 2:
#                 all_people_set[idx] = 1
#             i //= 2
#             idx -= 1
#         for unit in range(len(all_people_set)):
#             if all_people_set[unit] == 0:
#                 people_set[0].append(distance_list[unit][0])
#             else:
#                 people_set[1].append(distance_list[unit][1])
#         min_minutes = min(move_people(), min_minutes)
#     print('#{} {}'.format(t, min_minutes+1))


## BJ 21608 상어 초등학교
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
#
# def make_arrange(stu):
#     global end_r
#     global end_c
#     max_adj_likes = 0
#     max_empty_space = 0
#     cr, cc = 0, 0
#     first_in = True
#     for r in range(N):
#         for c in range(N):
#             empty_space = 0
#             adj_likes = 0
#             if MAP[r][c]: continue
#             if first_in:
#                 first_in_axis = (r,c)
#                 first_in = False
#             for i in range(4):
#                 nr = r + dr[i]
#                 nc = c + dc[i]
#                 if 0 <= nr < N and 0 <= nc < N:
#                     if MAP[nr][nc] == 0:
#                         empty_space += 1
#                     elif MAP[nr][nc] in like_list[stu]:
#                         adj_likes += 1
#             if adj_likes == 4:
#                 MAP[r][c] = stu
#                 if r > end_r or (r == end_r and c > end_c):
#                     end_r, end_c = r, c
#                 return
#             if adj_likes > max_adj_likes or (adj_likes == max_adj_likes and empty_space > max_empty_space):
#                 max_adj_likes = adj_likes
#                 max_empty_space = empty_space
#                 cr, cc = r, c
#     if max_empty_space == 0 and max_adj_likes == 0:
#         cr, cc = first_in_axis
#     MAP[cr][cc] = stu
#     if cr > end_r or (cr == end_r and cc > end_c):
#         end_r, end_c = cr, cc
#     return
#
#
# def calculate_score():
#     satisfaction = 0
#     for r in range(N):
#         for c in range(N):
#             cnt = 0
#             now_student = MAP[r][c]
#             for i in range(4):
#                 nr = r + dr[i]
#                 nc = c + dc[i]
#                 if 0 <= nr < N and 0 <= nc < N and MAP[nr][nc] in like_list[now_student]:
#                     cnt += 1
#             if cnt > 0:
#                 satisfaction += 10 ** (cnt-1)
#     return satisfaction
#
# N = int(input())
# like_list = [[0, 0, 0, 0] for _ in range(N ** 2 + 1)]
# arrange_order = [0] * (N ** 2)
# MAP = [[0] * N for _ in range(N)]
# for n in range(N ** 2):
#     now, st1, st2, st3, st4 = map(int, input().split())
#     arrange_order[n] = now
#     like_list[now][0] = st1
#     like_list[now][1] = st2
#     like_list[now][2] = st3
#     like_list[now][3] = st4
# end_r, end_c = 1, 1
# for student in arrange_order:
#     make_arrange(student)
# ans = calculate_score()
# print(ans)

## BJ 14889 스타트와 링크
def dfs(members,idx,member_list):
    global min_gap
    if idx >= N: return
    if members == N // 2:
        gap = form_team(member_list)
        min_gap = min(min_gap,gap)
        return
    member_list.append(idx)
    dfs(members+1,idx+1,member_list)
    member_list.pop()
    dfs(members, idx+1, member_list)
    return


def form_team(team1):
    team2 = []
    for i in range(N):
        if i in team1: continue
        team2.append(i)
    team1_scores = calculate_synergy(team1)
    team2_scores = calculate_synergy(team2)
    return abs(team1_scores - team2_scores)


def calculate_synergy(team):
    team_scores = 0
    for i in range(len(team)):
        for j in range(i+1,len(team)):
            team_scores += MAP[team[i]][team[j]]
    return team_scores



N = int(input())
MAP = [list(map(int,input().split())) for _ in range(N)]
for r in range(N):
    for c in range(r+1,N):
        MAP[r][c] += MAP[c][r]
min_gap = 2e29
dfs(0,0,[])
print(min_gap)