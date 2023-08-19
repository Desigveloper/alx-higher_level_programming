#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    score_aggr = 0
    weight_aggr = 0

    for score, weight in my_list:
        score_aggr += score * weight
        weight_aggr += weight

    weighted_average = score_aggr / weight_aggr

    return weighted_average
