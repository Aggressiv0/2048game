import random

ciag = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

g = 0

moves_count = 0
health = 3

while g == 0:
    c = 0
    while c == 0:
        random_num_1 = random.randrange(0, 4)
        random_num_2 = random.randrange(0, 4)
        if ciag[random_num_1][random_num_2] == 0:
            ciag[random_num_1][random_num_2] = 2
            c += 1

    for i in range(len(ciag)):
        print(ciag[i])

    print('Wykorzystane ruchy: ' + str(moves_count))
    print('Życia: ' + str(health))

    move = 0

    komenda = input('Type command: ')
    if komenda == 'd':
        for j in range(len(ciag)):
            for i in range(len(ciag[j]) - 2, -1, -1):
                print(i)
                con = 0
                for d in range(i, len(ciag) - 1):
                    if con == 0:
                        if ciag[j][d + 1] == 0 or ciag[j][d + 1] == ciag[j][d]:
                            move += 1
                            if ciag[j][d + 1] == ciag[j][d]:
                                con += 1
                            ciag[j][d + 1] = ciag[j][d + 1] + ciag[j][d]
                            ciag[j][d] = 0
                    else:
                        if ciag[j][d + 1] == 0:
                            ciag[j][d + 1] = ciag[j][d + 1] + ciag[j][d]
                            ciag[j][d] = 0
                print(con, 'con')
                print(ciag)
    elif komenda == 'a':
        for j in range(len(ciag)):
            for i in range(0, len(ciag[j])):
                con = 0
                for d in range(i, 0, -1):
                    if con == 0:
                        if ciag[j][d - 1] == 0 or ciag[j][d - 1] == ciag[j][d]:
                            move += 1
                            if ciag[j][d - 1] == ciag[j][d]:
                                con += 1
                                # ///
                            ciag[j][d - 1] = ciag[j][d - 1] + ciag[j][d]
                            ciag[j][d] = 0
                    else:
                        if ciag[j][d - 1] == 0:
                            ciag[j][d - 1] = ciag[j][d - 1] + ciag[j][d]
                            ciag[j][d] = 0
    elif komenda == 'w':
        for j in range(len(ciag)):
            for i in range(len(ciag)):
                print(ciag[i][j])
                con = 0
                for d in range(i, 0, -1):
                    if con == 0:
                        if ciag[d - 1][j] == 0 or ciag[d - 1][j] == ciag[d][j]:
                            move += 1
                            if ciag[d - 1][j] == ciag[d][j]:
                                con += 1
                            ciag[d - 1][j] = ciag[d - 1][j] + ciag[d][j]
                            ciag[d][j] = 0
                    else:
                        if ciag[d - 1][j] == 0:
                            ciag[d - 1][j] = ciag[d - 1][j] + ciag[d][j]
                            ciag[d][j] = 0
    elif komenda == 's':
        for j in range(len(ciag)):
            for i in range(len(ciag) - 1, -1, -1):
                print(ciag[i][j])
                con = 0
                for d in range(i, len(ciag) - 1):
                    if con == 0:
                        if ciag[d + 1][j] == 0 or ciag[d + 1][j] == ciag[d][j]:
                            move += 1
                            if ciag[d + 1][j] == ciag[d][j]:
                                con += 1
                            ciag[d + 1][j] = ciag[d + 1][j] + ciag[d][j]
                            ciag[d][j] = 0
                    else:
                        if ciag[d + 1][j] == 0:
                            ciag[d + 1][j] = ciag[d + 1][j] + ciag[d][j]
                            ciag[d][j] = 0

    if move > 0:
        moves_count += 1
    else:
        health -= 1

    if health == 0:
        g += 1

    for i in range(len(ciag)):
        for j in range(len(ciag)):
            if ciag[i][j] == 2048:
                g += 2

if g == 2:
    print('Congratulation you win!')
elif g == 1:
    print('No more moves you loose!')


# print(ciag[1][1])

# for j in range(len(ciag)):
#     for i in range(len(ciag) - 1, -1, -1):
#         print(ciag[i][j])
