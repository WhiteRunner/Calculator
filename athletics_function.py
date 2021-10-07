import math


def cal_score(t_origin, wind_speed, altitude, length, lane_num=0, gender='men'):
    if length <= 100:
        # 100m成绩修正与性别道次无关
        return (1.028 - 0.028 * math.exp(-0.000125 * altitude) * (1.0 - wind_speed * t_origin / length) ** 2) * t_origin
    # 不能传参，因为会丢失精度
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
            elif lane_num == 4:
                return t_origin - (.5849876305e-2 * wind_speed ** 2 - .6855952381e-1 * wind_speed - .5205524601e-2 + (
                        -.6920222619e-6 * wind_speed ** 2 + .7647619043e-5 * wind_speed - .9491032781e-4) * altitude)
            elif lane_num == 5:
                return t_origin - (.5727788093e-2 * wind_speed ** 2 - .7192698412e-1 * wind_speed - .4418058132e-2 + (
                        -.6745825703e-6 * wind_speed ** 2 + .8003809515e-5 * wind_speed - .9506468759e-4) * altitude)
            elif lane_num == 6:
                return t_origin - (.5635281356e-2 * wind_speed ** 2 - .7525793651e-1 * wind_speed - .4965367685e-2 + (
                        -.6675324621e-6 * wind_speed ** 2 + .8375238100e-5 * wind_speed - .9518787886e-4) * altitude)
            elif lane_num == 7:
                return t_origin - (.5562976702e-2 * wind_speed ** 2 - .7846031747e-1 * wind_speed - .4763760038e-2 + (
                        -.6695732846e-6 * wind_speed ** 2 + .8730476192e-5 * wind_speed - .9523141616e-4) * altitude)
            elif lane_num == 8:
                return t_origin - (.5497165554e-2 * wind_speed ** 2 - .8159285713e-1 * wind_speed - .5002267739e-2 + (
                        -.6547309794e-6 * wind_speed ** 2 + .9080952375e-5 * wind_speed - .9529226969e-4) * altitude)
        else:
            if lane_num == 1:
                return t_origin - (.8164192923e-2 * wind_speed ** 2 - .7134126985e-1 * wind_speed - .5253349577e-2 + (
                        -.9581941721e-6 * wind_speed ** 2 + .7988571428e-5 * wind_speed - .1015294992e-3) * altitude)
            elif lane_num == 2:
                return t_origin - (.8012420137e-2 * wind_speed ** 2 - .7549761905e-1 * wind_speed - .5664811539e-2 + (
                        -.9247990043e-6 * wind_speed ** 2 + .8438095233e-5 * wind_speed - .1016949907e-3) * altitude)
            elif lane_num == 3:
                return t_origin - (.7904916485e-2 * wind_speed ** 2 - .7968492063e-1 * wind_speed - .5239125688e-2 + (
                        -.9269635173e-6 * wind_speed ** 2 + .8905714292e-5 * wind_speed - .1016551638e-3) * altitude)
            elif lane_num == 4:
                return t_origin - (.8307720076e-2 * wind_speed ** 2 - .8214841271e-1 * wind_speed - .5935065061e-2 + (
                        -.1204329010e-5 * wind_speed ** 2 + .8447619050e-5 * wind_speed - .1016346319e-3) * altitude)
            elif lane_num == 5:
                return t_origin - (.7666048256e-2 * wind_speed ** 2 - .8769523808e-1 * wind_speed - .5233972510e-2 + (
                        -.9012368561e-6 * wind_speed ** 2 + .9736190467e-5 * wind_speed - .1018901670e-3) * altitude)
            elif lane_num == 6:
                return t_origin - (.7537878777e-2 * wind_speed ** 2 - .9157222225e-1 * wind_speed - .4871572736e-2 + (
                        -.8844155844e-6 * wind_speed ** 2 + .1013999999e-4 * wind_speed - .1020086579e-3) * altitude)
            elif lane_num == 7:
                return t_origin - (.7438260160e-2 * wind_speed ** 2 - .9541269842e-1 * wind_speed - .4911152390e-2 + (
                        -.8664811526e-6 * wind_speed ** 2 + .1057238095e-4 * wind_speed - .1021726653e-3) * altitude)
            elif lane_num == 8:
                return t_origin - (.7340342199e-2 * wind_speed ** 2 - .9905396825e-1 * wind_speed - .5168418916e-2 + (
                        -.8719851461e-6 * wind_speed ** 2 + .1096761904e-4 * wind_speed - .1021486705e-3) * altitude)
    elif length == 400:
        return t_origin + ((-0.00001335714286 * altitude ** 2 + 0.25196428571429 * altitude + 0.82142857142857) * 1e-3)


def cal_points(event_name, gender, seconds_or_meter, minutes=0):
    points = 0
    if event_name == '100m':
        points = 290.52712 * (100 / seconds_or_meter) - 1953.2266
    elif event_name == '200m':
        points = 267.75893 * (200 / seconds_or_meter) - 1703.6447
    elif event_name == '400m':
        points = 262.37121 * (400 / seconds_or_meter) - 1402.7708
    elif event_name == '800m':
        points = 302.9089 * (800 / ((60 * minutes) + seconds_or_meter)) - 1377.5673
    elif event_name == '1000m':
        points = 313.6503268 * (1000 / ((60 * minutes) + seconds_or_meter)) - 1374.25166
    elif event_name == '100mH':
        return 245.697911 * (100 / seconds_or_meter) - 974.427319
    elif event_name == '110mH':
        return 232.393146 * (110 / seconds_or_meter) - 977.72885
    elif event_name == "highJump":
        points = 2227.8560 * seconds_or_meter ** 0.5 - 2447.9277
    elif event_name == "longJump":
        points = 1065.6947 * seconds_or_meter ** 0.5 - 2120.1067
    elif event_name == "tripleJump":  # 三级跳
        points = 717.9505 * seconds_or_meter ** 0.5 - 2042.6637
    elif event_name == "poleVault":  # 撑杆跳
        points = 839.81066 * seconds_or_meter ** 0.5 - 1065.4477
    elif event_name == "Javelin":  # 标枪
        return 170.11116 * seconds_or_meter ** 0.5 - 417.375499 if gender == 'women' \
            else 168.13381 * seconds_or_meter ** 0.5 - 601.71996
    elif event_name == "shotPut":  # 铅球
        return 326.4432919 * seconds_or_meter ** 0.5 - 474.3020648 if gender == 'women' \
            else 363.768931 * seconds_or_meter ** 0.5 - 701.8195151
    else:
        return 0

    if gender == 'women':
        points = (points + 370.23683) / 1.10218405
    return points


def cal_points2score(race_name, gender, points):
    old_points=points
    if gender == 'women':
        points = 1.10218405 * points - 370.23683

    if race_name == '100m':
        return 100 / (0.003439 * points + 6.72526)
    elif race_name == '200m':
        return 200/(0.003734*points+6.36315)
    elif race_name == '400m':
        return 400/(0.0038105*points+5.34719)
    elif race_name == '800m':
        return 800/(0.003300*points+4.54844)
    elif race_name == '1000m':
        return 1000/(0.00318746*points+4.382052887)
    elif race_name == '100mH':
        return 100/(0.00406955*old_points+3.9663329)
    elif race_name == '110mH':
        return 110/(0.00430147*old_points+4.2084435)
    elif race_name == "highJump":
        return math.pow(0.00044878*points+1.098838,2)
    elif race_name == "longJump":
        return math.pow(0.0009379*points+1.9897558,2)
    elif race_name == "tripleJump":  # 三级跳
        return math.pow(0.0013899*points+2.8472750,2)
    elif race_name == "poleVault":  # 撑杆跳
        return math.pow(0.0011566*points+1.293145,2)
    elif race_name == "Javelin":  # 标枪
        return math.pow(0.0058689*old_points+2.4609307,2) if gender=='women' \
            else math.pow(0.0059368*old_points+3.5872388,2)
    elif race_name == "shotPut":  # 铅球
        return math.pow(0.003061312*old_points+1.454488154,2) if gender=='women' \
                else math.pow(0.002747525 * old_points + 1.930440381, 2)
    else:
        return 0


if __name__ == '__main__':
    # print(cal_points('shotPut', 'men', 10))
    print(cal_points2score('shotPut', 'women', 1578.6))
