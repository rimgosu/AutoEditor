def who(video):
    user_list = ['rimgosu', 'matsuri', 'beterbabbit', 'xqn']
    user = 'Default'

    r1 = video.find('rim')
    r2 = video.find('gosu')
    r3 = video.find('rimgosu')
    r4 = video.find('RIM')
    r5 = video.find('GOSU')
    r6 = video.find('RIMGOSU')
    m1 = video.find('mat')
    m2 = video.find('suri')
    m3 = video.find('matsuri')
    m4 = video.find('MAT')
    m5 = video.find('SURI')
    m6 = video.find('MATSURI')
    b1 = video.find('beter')
    b2 = video.find('babbit')
    b3 = video.find('beterbabbit')
    b4 = video.find('BETER')
    b5 = video.find('BABBIT')
    b6 = video.find('BETERBABBIT')
    x1 = video.find('xq')
    x2 = video.find('xqn')
    x3 = video.find('XQ')
    x4 = video.find('XQN')

    rimgosu_list = [r1, r2, r3, r4, r5, r6]
    matsuri_list = [m1, m2, m3, m4, m5, m6]
    beterbabbit_list = [b1, b2, b3, b4, b5, b6]
    xqn_list = [x1, x2, x3, x4]
    for i in rimgosu_list:
        if i != -1:
            user = user_list[0]
    for i in matsuri_list:
        if i != -1:
            user = user_list[1]
    for i in beterbabbit_list:
        if i != -1:
            user = user_list[2]
    for i in xqn_list:
        if i != -1:
            user = user_list[3]

    return user

if __name__ == "__main__":
    user = who('RIMGOSU.mp4')
    print(user)