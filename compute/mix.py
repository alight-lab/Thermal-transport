def mixture(file1, file2):
    import os
    import sys
    import copy
    import numpy as np
    import shutil
    path1 = file1
    path2 = file2
    path_target = sys.path[0]
    path_target = path_target.replace('compute', 'data')
    path_target = path_target + '\\data\\file.data'
    shutil.copyfile(path1, path_target)

    with open(path_target, 'r+') as f:
        f.truncate(0)
        f.close()

    with open(path2) as f:
        data = f.readline()
        data = data.split()
        while 'atoms' not in data:
            data = f.readline()
            data = data.split()
        numbers_2 = data[0]
        while 'xlo' not in data:
            data = f.readline()
            data = data.split()
        x_2 = copy.deepcopy(data[0:2])
        data = f.readline()
        data = data.split()
        y_2 = copy.deepcopy(data[0:2])
        data = f.readline()
        data = data.split()
        z_2 = copy.deepcopy(data[0:2])
        mass_2 = []
        position_2 = []
        while 'Masses' not in data:
            data = f.readline()
            data = data.split()
        data = f.readline()
        data = data.split()
        while not data:
            data = f.readline()
            data = data.split()
        while data:
            mass_2.append(data[0:2])
            data = f.readline()
            data = data.split()
        while 'Atoms' not in data:
            data = f.readline()
            data = data.split()
        data = f.readline()
        data = data.split()
        while not data:
            data = f.readline()
            data = data.split()
        while data:
            position_2.append(data[1:5])
            data = f.readline()
            data = data.split()
        f.close()

        with open(file1) as f:
            data = f.readline()
            data = data.split()
            while 'atoms' not in data:
                data = f.readline()
                data = data.split()
            numbers_1 = copy.deepcopy(data[0])
            while 'xlo' not in data:
                data = f.readline()
                data = data.split()
            x_1 = copy.deepcopy(data[0:2])
            data = f.readline()
            data = data.split()
            y_1 = copy.deepcopy(data[0:2])
            data = f.readline()
            data = data.split()
            z_1 = copy.deepcopy(data[0:2])
            mass_1 = []
            position_1 = []
            while 'Masses' not in data:
                data = f.readline()
                data = data.split()
            data = f.readline()
            data = data.split()
            while not data:
                data = f.readline()
                data = data.split()
            while data:
                mass_1.append(data[0:2])
                data = f.readline()
                data = data.split()
            while 'Atoms' not in data:
                data = f.readline()
                data = data.split()
            data = f.readline()
            data = data.split()
            while not data:
                data = f.readline()
                data = data.split()
            while data:
                position_1.append(data[1:5])
                data = f.readline()
                data = data.split()
            f.close()

        numbers = str(int(numbers_1) + int(numbers_2))
        mass = copy.deepcopy(mass_1)
        for i in range(len(mass_2)):
            h = 0
            for j in range(len(mass)):
                if int(float(mass_2[i][1])) == int(float(mass[j][1])):
                    h = 1
            if h == 0:
                mass.append([len(mass) + 1, mass_2[i][1]])
        types = len(mass)
        x = copy.deepcopy(x_1)
        x[1] = str(float(x_1[1]) + float(x_2[1]))
        y = copy.deepcopy(y_1)
        if float(y_1[1]) > float(y_2[1]):
            y[1] = str(float(y_1[1]))
        else:
            y[1] = str(float(y_2[1]))
        z = copy.deepcopy(z_1)
        z[1] = str(float(z_1[1]) + float(z_2[1]))
        if float(z_1[1]) > float(z_2[1]):
            z[1] = str(float(z_1[1]))
        else:
            z[1] = str(float(z_2[1]))
        temp1 = copy.deepcopy(position_1)
        for i in range(len(position_1)):
            temp1[i].insert(0, str(i + 1))
        temp2 = copy.deepcopy(position_2)
        p = []
        m = []
        for k in range(len(position_1)):
                p.append(float(position_1[k][1]))
        max_value = max(p)
        for r in range(len(p)):
            if p[r] != max_value:
                m.append(p[r])
        max_value_2 = max(m)
        for i in range(len(position_2)):
            temp2[i].insert(0, str(i + 1 + int(numbers_1)))
            temp2[i][2] = str(float(temp2[i][2]) + max_value + max_value - max_value_2)
            for j in range(len(mass)):
                if int(float(mass_2[int(temp2[i][1]) - 1][1])) == int(float(mass[j][1])):
                    temp2[i][1] = str(j + 1)
        position = copy.deepcopy(temp1)
        position.extend(temp2)
    x_result = (max_value + max_value + max_value - max_value_2) / 2
    result0 = '\r'
    result1 = '         ' + str(numbers) + '  atoms\r'
    result2 = '           ' + str(types) + '  atom types\r\r'
    result3 = '\r'
    result4 = str(x[0]) + '      ' + str(x[1]) + '  xlo xhi\r'
    result5 = str(y[0]) + '      ' + str(y[1]) + '  ylo yhi\r'
    result6 = str(z[0]) + '      ' + str(z[1]) + '  zlo zhi\r'
    result7 = '\r'
    result8 = 'Masses\r'
    result9 = '\r'
    result10 = ''
    for i in range(len(mass)):
        result10 = result10 + '            ' + str(mass[i][0]) + '   ' + str(mass[i][1]) + '\r'
    result11 = '\r'
    result12 = 'Atoms  # atomic' + '\r'
    result13 = '\r'
    result14 = ''
    for i in range(len(temp1)):
        result14 = (result14 + '         ' + str(temp1[i][0]) + '    ' + str(temp1[i][1]) + '       ' + str(temp1[i][2]) + '       ' + str(
            temp1[i][3])
                    + '       ' + str(temp1[i][4]) + '\r')
    result15 = ''
    for i in range(len(temp2)):
        result15 = (result15 + '         ' + str(temp2[i][0]) + '    ' + str(temp2[i][1]) + '       ' + str(temp2[i][2]) + '       ' + str(
            temp2[i][3])
                    + '       ' + str(temp2[i][4]) + '\r')
    with open(path_target, 'w') as f:
        f.write(result0)
        f.write(result1)
        f.write(result2)
        f.write(result3)
        f.write(result4)
        f.write(result5)
        f.write(result6)
        f.write(result7)
        f.write(result8)
        f.write(result9)
        f.write(result10)
        f.write(result11)
        f.write(result12)
        f.write(result13)
        f.write(result14)
        f.write(result15)
    return x_result


if __name__ == '__main__':
    x = mixture('G:\\data\\app_v1\\data\\copper.lmp', 'G:\\data\\app_v1\\data\\iron.lmp')
    # x = mixture('Cu.data', 'Fe.data')
    print(x)
