import math


def cal_score(t_origin, wind_speed, altitude, length, lane_num=0, gender='men'):
    if length <= 100:
        # 100m成绩修正与性别道次无关
        return (1.028 - 0.028 * math.exp(-0.000125 * altitude) * (1.0 - wind_speed * t_origin / length) ** 2) * t_origin
    elif length == 200:
        if gender == "men" and t_origin < 21.5:
            if lane_num == 1:
                return t_origin - (.6823850739e-2 * wind_speed ** 2 - .6261746031e-1 * wind_speed + .6769739610e-3 + (
                        - .8533086093e-6 * wind_speed ** 2 + .7409523797e-5 * wind_speed - .9576524416e-4) * altitude)
            elif lane_num == 2:
                return t_origin - (.6037981841e-2 * wind_speed ** 2 - .6160238093e-1 * wind_speed - .5337868373e-2 + (
                        - .7012368506e-6 * wind_speed ** 2 + .6901904772e-5 * wind_speed - .9484254800e-4) * altitude)
            elif lane_num == 3:
                return t_origin - (.5937950920e-2 * wind_speed ** 2 - .6508253968e-1 * wind_speed - .4702741522e-2 + (
                        - .7021645076e-6 * wind_speed ** 2 + .7283809515e-5 * wind_speed - .9485541123e-4) * altitude)
            if lane_num == 4:
                return t_origin - (.5849876305e-2 * wind_speed ** 2 - .6855952381e-1 * wind_speed - .5205524601e-2 + (
                        -.6920222619e-6 * wind_speed ** 2 + .7647619043e-5 * wind_speed - .9491032781e-4) * altitude)
            if lane_num == 5:
                return t_origin - (.5727788093e-2 * wind_speed ** 2 - .7192698412e-1 * wind_speed - .4418058132e-2 + (
                        -.6745825703e-6 * wind_speed ** 2 + .8003809515e-5 * wind_speed - .9506468759e-4) * altitude)
            if lane_num == 6:
                return t_origin - (.5635281356e-2 * wind_speed ** 2 - .7525793651e-1 * wind_speed - .4965367685e-2 + (
                        -.6675324621e-6 * wind_speed ** 2 + .8375238100e-5 * wind_speed - .9518787886e-4) * altitude)

            if lane_num == 7:
                return t_origin - (.5562976702e-2 * wind_speed ** 2 - .7846031747e-1 * wind_speed - .4763760038e-2 + (
                        -.6695732846e-6 * wind_speed ** 2 + .8730476192e-5 * wind_speed - .9523141616e-4) * altitude)

            if lane_num == 8:
                return t_origin - (.5497165554e-2 * wind_speed ** 2 - .8159285713e-1 * wind_speed - .5002267739e-2 + (
                            -.6547309794e-6 * wind_speed ** 2 + .9080952375e-5 * wind_speed - .9529226969e-4) * altitude)
        else:
            pass


def cal_50m_score(t_origin, wind_speed, altitude):
    return cal_score(t_origin, wind_speed, altitude, 50)


def cal_60m_score(t_origin, wind_speed, altitude):
    return cal_score(t_origin, wind_speed, altitude, 60)


def cal_100m_score(t_origin, wind_speed, altitude):
    return cal_score(t_origin, wind_speed, altitude, 100)


def cal_200m_score(t_origin, wind_speed, altitude, lane_num, gender):
    return cal_score(t_origin, wind_speed, altitude, 200, lane_num, gender)
