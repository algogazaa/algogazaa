def solution(commands):
    answer = []
    table = [['EMPTY' for _ in range(50)] for _ in range(50)]
    connect = [[0 for _ in range(50)] for _ in range(50)]
    dic_connect = {}
    cnt = 1
    for i in commands:
        if 'UPDATE' in i:
            command = i.split()
            if len(command) == 4:
                a, b = int(command[1])-1, int(command[2])-1
                table[a][b] = command[3]
                if connect[a][b] != 0:
                    table = update(table, connect, command[3], a, b, dic_connect)
            elif len(command) == 3:
                for a in range(50):
                    for b in range(50):
                        if table[a][b] == command[1]:
                            table[a][b] = command[2]
                            if connect[a][b] != 0:
                                table = update(table, connect, command[2], a, b, dic_connect)

        elif 'UNMERGE' in i:
            command = i.split()
            a, b = int(command[1])-1, int(command[2])-1
            value = table[a][b]
            key = connect[a][b]
            for x, y in dic_connect[key]:
                table[x][y] = 'EMPTY'
                connect[x][y] = 0
            table[a][b] = value
            del dic_connect[key]

        elif 'MERGE' in i:
            command = i.split()
            a, b, c, d = int(command[1])-1, int(command[2])-1, int(command[3])-1, int(command[4])-1
            if connect[a][b] == 0 and connect[c][d] == 0:
                connect[a][b], connect[c][d] = cnt, cnt
                table[c][d] = table[a][b]
                dic_connect[cnt] = [[a, b], [c, d]]
                cnt += 1
            elif connect[a][b] != 0 and connect[c][d] != 0:
                key = connect[c][d]
                for x, y in dic_connect[connect[c][d]]:
                    connect[x][y] = connect[a][b]
                    table[x][y] = table[a][b]
                    dic_connect[connect[a][b]].append([x, y])
                del dic_connect[key]
            else:
                if connect[a][b] == 0:
                    connect[a][b] = connect[c][d]
                    table[a][b] = table[c][d]
                    dic_connect[connect[c][d]].append([a, b])
                else:
                    connect[c][d] = connect[a][b]
                    table[c][d] = table[a][b]
                    dic_connect[connect[a][b]].append([c, d])

        else:
            command = i.split()
            answer.append(table[int(command[1])-1][int(command[2])-1])

    return answer


def update(table, connect, value, x, y, dic):
    num = connect[x][y]
    for i in dic[num]:
        table[i[0]][i[1]] = value
    return table

print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap",
                "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean",
                "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian",
                "UPDATE 4 3  noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik",
                "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]), ["EMPTY", "group"])
print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d",
                "MERGE 1 1 1 2", "MERGE 2 2 2 1"," MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2",
                "PRINT 1 1"]), ["d", "EMPTY"])