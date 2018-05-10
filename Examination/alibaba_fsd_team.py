#!/bin/python


def fsd_team(staff_info):
    staff_list = []
    job_dict = {"java": [], "web": [], "data": [], "dm": []}
    for staff in staff_info:
        temp = staff.split(",")
        temp_dict = {"n": temp[0], "j": temp[1], "count": 0}
        staff_list.append(temp_dict)
        job_dict[temp[1]].append(temp[0])
    web_groups = []
    java_groups = []
    for staff in staff_list:
        if len(web_groups) == 0 or len(web_groups[len(web_groups)-1]) >= 3:
            web_groups.append([])
        if len(java_groups) == 0 or len(java_groups[len(java_groups) - 1]) >= 3:
            java_groups.append([])
        if staff["j"] == "web" or staff["j"] == "java":
            if staff["count"] >= 2:
                continue
            if staff["n"] not in web_groups[len(web_groups)-1]:
                web_groups[len(web_groups) - 1].append(staff["n"])
        if staff["j"] == "data" or staff["j"] == "java" or staff["j"] == "dm":
            if staff["count"] >= 2:
                continue
            if staff["n"] not in java_groups[len(java_groups)-1]:
                java_groups[len(java_groups) - 1].append(staff["n"])
    res = ""
    for g in web_groups:
        res += ",".join(g)
        res += "\n"
    for g in java_groups:
        res += ",".join(g)
        res += "\n"
    return res
    
    

_staff_info = ["10001,java", "10002,web", "10003,data", "10004,dm"]

res = fsd_team(_staff_info)

print(res)
