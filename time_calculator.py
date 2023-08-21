def add_time(start, duration, day=None):
    week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    dh, dm = [int(i) for i in duration.split(':')]
    sh, sm, when = int(start.split(':')[0]), int(start.split(':')[1].split()[0]), start.split(':')[1].split()[1]
    ###
    Days = dh
    if sm + dm >= 60: Days += 1
    Days = int(Days / 24)
    pad = 0
    if when == 'PM': pad += 12
    
    x = sh + pad + (dh-Days*24)
    if sm + dm >= 60: x += 1
    if x >= 24: Days+=1
    ###
    padding = 0
    if when == "AM": padding += 12
    if (sm + dm) >= 60: padding += 1
    totalh = padding + sh + dh
    days = int(totalh / 24)
    
    nd = ''
    if day:
        day = week.index(day.lower())
        nd = f', {week[(day+Days)%7].capitalize()}'
    
    if Days == 1: d_msg = ' (next day)'
    elif Days == 0: d_msg = ''
    else: d_msg = f' ({Days} days later)'
    nh_24 = totalh - (days * 24)
    
    if nh_24 == 0: nh = 12
    elif nh_24 > 12: nh = nh_24 % 12
    elif nh_24 == 12:nh = 12
    else: nh = nh_24
    
    if (sm + dm) >= 60: n = sh + dh +1
    else: n = sh + dh
    num = n // 24
    
    n = n - num * 24
    if 24 >= n >= 12:
        if when == 'AM': sys = 'PM'
        else: sys = 'AM'
    elif n <= 12: sys = when
    else:print("fuck")
    
    nm = int((sm+dm)%60)
    return f"{int(nh)}:{'0'*(2-len(nm.__str__()))}{nm} {sys}{nd}{d_msg}"
