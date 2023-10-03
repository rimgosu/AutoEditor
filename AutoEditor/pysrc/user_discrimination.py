def who(video):
    user_list = ['rimgosu', 'matsuri', 'beterbabbit', 'shadybunny', 'duckdragon', 'zanyang', 'sunbacon']
    user = 'Default'

    r1 = video.find('rimgo')
    r2 = video.find('mgosu')
    r3 = video.find('rimgosu')
    r4 = video.find('RIMGO')
    r5 = video.find('MGOSU')
    r6 = video.find('RIMGOSU')
    m1 = video.find('matsu')
    m2 = video.find('tsuri')
    m3 = video.find('matsuri')
    m4 = video.find('MATSU')
    m5 = video.find('TSURI')
    m6 = video.find('MATSURI')
    b1 = video.find('beterbabbit')
    b2 = video.find('beterbabbit')
    b3 = video.find('beterbabbit')
    b4 = video.find('BETERBABBIT')
    b5 = video.find('BETERBABBIT')
    b6 = video.find('BETERBABBIT')
    sh1 = video.find('shadybunny')
    sh2 = video.find('shady')
    sh3 = video.find('bunny')
    sh4 = video.find('SHADYBUNNY')
    sh5 = video.find('SHADY')
    sh6 = video.find('BUNNY')
    d1 = video.find('duck')
    d2 = video.find('duckdragon')
    d3 = video.find('DUCK')
    d4 = video.find('DUCKDRAGON')
    z1 = video.find('zanyang')
    z2 = video.find('zanya')
    z3 = video.find('ZANYANG')
    z4 = video.find('ZANYA')
    s1 = video.find('sunbacon')
    s2 = video.find('sunba')
    s3 = video.find('SUNBACON')
    s4 = video.find('SUNBA')

    rimgosu_list = [r1, r2, r3, r4, r5, r6]
    matsuri_list = [m1, m2, m3, m4, m5, m6]
    beterbabbit_list = [b1, b2, b3, b4, b5, b6]
    shadybunny_list = [sh1, sh2, sh3, sh4, sh5, sh6]
    duckdragon_list = [d1, d2, d3, d4]
    zanyang_list = [z1, z2, z3, z4]
    sunbacon_list = [s1, s2, s3, s4]
    for i in rimgosu_list:
        if i != -1:
            user = user_list[0]
    for i in matsuri_list:
        if i != -1:
            user = user_list[1]
    for i in beterbabbit_list:
        if i != -1:
            user = user_list[2]
    for i in shadybunny_list:
        if i != -1:
            user = user_list[3]
    for i in duckdragon_list:
        if i != -1:
            user = user_list[4]
    for i in zanyang_list:
        if i != -1:
            user = user_list[5]
    for i in sunbacon_list:
        if i != -1:
            user = user_list[6]

    return user

def what_hero(hero_found):
    hero_list = ['_0_', '_1_', '_2_']
    hero = 'Default'

    _0_ = hero_found.find('0')
    _1_ = hero_found.find('1')
    _2_ = hero_found.find('2')

    _0_list = [_0_]
    _1_list = [_1_]
    _2_list = [_2_]
    for i in _0_list:
        if i != -1:
            hero = hero_list[0]
    for i in _1_list:
        if i != -1:
            hero = hero_list[1]
    for i in _2_list:
        if i != -1:
            hero = hero_list[2]

    return hero

if __name__ == "__main__":
    user = who('shadybunny elise.mp4')
    print(user)
    
    hero = what_hero('_0_dena')
    print(hero)
