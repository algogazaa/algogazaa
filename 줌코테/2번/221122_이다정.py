data1 = [[1,0,5],[2,2,2],[3,3,1],[4,4,1],[5,10,2]]
data2 = [[1,0,3],[2,1,3],[3,3,2],[4,9,1],[5,10,2]]
data3 = [[1,2,10],[2,5,8],[3,6,9],[4,20,6],[5,25,5]]

w_list=[]
result=[]

def solution(data):
    while len(data) > 0 or len(w_list) > 0:
        if len(w_list) == 0:
            w_list.append(data.pop(0))
            time = w_list[0][1]

        result.append(w_list[0][0])
        time += w_list.pop(0)[2]
        data = put_w_list(data, time)
        w_list.sort(key=lambda x:(x[2]))

    return result

def put_w_list(data, time):
    while len(data) > 0:
        if data[0][1] <= time:
            w_list.append(data.pop(0))
        else:
            break
    return data


print(solution(data3))
