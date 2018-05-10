#!/bin/python


def bike_plan(distance, speed):
    time = distance / speed
    ofo_distance = 1.5
    yong_per_min = 0.2
    hello_bike = [1, 3, 5, 8]
    cost = {
        "OFO小黄车": distance // ofo_distance if distance % ofo_distance == 0 else distance // ofo_distance + 1,
        "永安行":     time * yong_per_min if time == int(time) else time * yong_per_min + 1}
    if distance <= 2:
        cost["hellobike"] = hello_bike[0]
    elif distance <= 4:
        cost["hellobike"] = hello_bike[1]
    elif distance <= 8:
        cost["hellobike"] = hello_bike[2]
    else:
        cost["hellobike"] = hello_bike[3]
    min_cost = cost["OFO小黄车"]
    min_cost_bike = []
    for c in cost:
        if min_cost > cost[c]:
            min_cost = cost[c]
    for c in cost:
        if min_cost == cost[c]:
            min_cost_bike.append(c+"%0.1f（元）" % min_cost)
    return_str = "骑行距离"+str(distance)+"(千米)，匀速骑行速度"+str(speed)+"(千米/分钟)最省钱方案:\n"
    return_str += "和".join(min_cost_bike)
    return return_str

res = bike_plan(40, 1)

print(res)
