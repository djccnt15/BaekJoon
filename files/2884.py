# 2884
h, m = map(int, input().split())
alarm = h * 60 + m - 45
if alarm < 0: alarm = 23 * 60 + 60 + alarm

alarm_h = alarm // 60
alarm_m = alarm % 60

print('%s %s' %(alarm_h, alarm_m))
