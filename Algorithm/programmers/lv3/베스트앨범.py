def solution(genres, plays):
    answer = []
    # 장르별 재생 수 총합
    genres_total_cnt = dict()
    # 장르별 최고 재생 수 두가지 노래
    genres_each_top2 = dict()
    for i in range(len(genres)):
        if genres[i] not in genres_total_cnt:
            genres_total_cnt[genres[i]] = plays[i]
            genres_each_top2[genres[i]] = [[plays[i], i]]
        else:
            genres_total_cnt[genres[i]] += plays[i]
            genres_each_top2[genres[i]].append([plays[i], i])
            genres_each_top2[genres[i]].sort(key=lambda x: (-x[0], x[1]))
            if len(genres_each_top2[genres[i]]) > 2:
                genres_each_top2[genres[i]].pop()
    sorted_genres_dict = sorted(genres_total_cnt.items(),key=lambda x: -x[1])
    for now_genre, value in sorted_genres_dict:
        for cnt, idx in genres_each_top2[now_genre]:
            answer.append(idx)
    print(answer)
    return answer