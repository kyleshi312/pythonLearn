has_ticket = True

knife_len = 30

if has_ticket:
    print('ticket check pass, prepare to safety check')
    # 1
    if knife_len > 20:
        print('the knife is too long, is %d long' % knife_len)
        print('get track is denied')
    # 2
    else:
        print('pass')
    # 3
else:
    print('brother please buy ticket')