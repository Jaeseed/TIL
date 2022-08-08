import math
def time_calculation(i, o):
    o_hours = o[:2]
    i_hours = i[:2]
    o_minutes = o[3:]
    i_minutes = i[3:]
    ret = (int(o_hours) - int(i_hours)) * 60
    ret += int(o_minutes) - int(i_minutes)
    return ret

def price_calculation(all_time, fee_info):
    min_minutes, min_price, unit_minutes, unit_price = fee_info
    if all_time <= min_minutes:
        return min_price
    # if all_time % unit_minutes:
    #     all_time += unit_minutes - all_time % unit_minutes
    return min_price + math.ceil((all_time - min_minutes) / unit_minutes) * unit_price

def solution(fees, records):
    answer = []
    info_dict = dict()
    for record in records:
        time, car_num, state = record.split()
        if state == 'IN':
            if car_num not in info_dict:
                info_dict[car_num] = [time, 0]
            else:
                info_dict[car_num][0] = time
        else:
            info_dict[car_num][1] += time_calculation(info_dict[car_num][0],time)
            info_dict[car_num][0] = 0
    for key, value in info_dict.items():
        if value[0] != 0:
            info_dict[key][1] += time_calculation(value[0],'23:59')
    tong = []
    for key, value in info_dict.items():
        tong.append([int(key), value[1]])
    tong.sort()
    for to in tong:
        price = to[1]
        answer.append(price_calculation(price,fees))
    return answer