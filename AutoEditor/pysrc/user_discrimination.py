def who(video):
    user_list = ['rimgosu', 'matsuri', 'beterbabbit', 'xqn']
    user = 'Default'

    r1 = video.find('rim')
    r2 = video.find('gosu')
    r3 = video.find('rimgosu')
    m1 = video.find('mat')
    m2 = video.find('ma')
    m3 = video.find('suri')
    m4 = video.find('matsuri')
    b1 = video.find('beter')
    b2 = video.find('babbit')
    b3 = video.find('bet')
    b4 = video.find('beterbabbit')
    x1 = video.find('xq')
    x2 = video.find('xqn')

    rimgosu_list = [r1, r2, r3]
    matsuri_list = [m1, m2, m3, m4]
    beterbabbit_list = [b1, b2, b3, b4]
    xqn_list = [x1, x2]
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
    user = who('xqn.mp4')
    print(user)