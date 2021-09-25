import math


def cal_100m_score(t_old,wind_speed,altitude):
    return (1.028-0.028*math.exp(-0.000125*altitude)*(1.0-wind_speed*t_old/100)**2)*t_old