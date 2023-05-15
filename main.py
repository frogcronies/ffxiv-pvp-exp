level = [0, 0, 2000, 4000, 6000, 8000, 11000, 14000, 17000, 20000, 23000, 27000, 31000, 35000, 39000, 43000, 48500, 54000, 59500, 65000, 70500, 78000, 85500, 93000, 100500, 108000, 118000, 128000, 138000, 148000, 158000, 178000]
flexp = 1250
ccexp = 800

userlev = int(input('What PVP level are you? (max 30, default 1) ') or 1)
usergoal = int(input('What PVP level do you want to be? (no max, default 25)') or 25)
userexp = int(input('How much series EXP do you have? (0 if you don\'t know, default 0) ') or 0)

mathlev = int(level[userlev])

if usergoal > 30:
    excess = usergoal - 30
    mathgoal = 158000 + excess*20000
else: mathgoal = int(level[usergoal])
mathreq = mathgoal - mathlev - userexp

print('You need {reqexp} EXP to hit level {goal} from your current level {level}. \nIt will take {fl} Frontlines matches or {cc} rounds of CC.'.format(reqexp = mathreq, goal = usergoal, level = userlev, fl = round(mathreq/flexp+0.5), cc = round(mathreq/ccexp+0.5)))