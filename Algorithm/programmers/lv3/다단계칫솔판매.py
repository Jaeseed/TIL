def solution(enroll, referral, seller, amount):
    # 총 판매자 인원 수
    num_of_people = len(enroll)
    # 판매자 인덱스 저장용 딕셔너리
    idx_dict = dict()
    # 본인의 추천인 인덱스 리스트
    recommender_list = [-1] * num_of_people
    # 총 이익 리스트
    answer = [0] * num_of_people
    # 추천인 배분
    for rec_idx in range(num_of_people):
        idx_dict[enroll[rec_idx]] = rec_idx
        recommender = referral[rec_idx]
        if recommender != "-":
            recommender_list[rec_idx] = idx_dict[recommender]

    # 이익 더하기
    for pro_idx in range(len(seller)):
        now_idx = idx_dict[seller[pro_idx]]
        sales = amount[pro_idx] * 100
        answer[now_idx] += sales
        while True:
            recommender = recommender_list[now_idx]
            commission = sales // 10
            answer[now_idx] -= commission
            if recommender == -1 or commission == 0:
                break
            answer[recommender] += commission
            sales = commission
            now_idx = recommender
    return answer

solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10])