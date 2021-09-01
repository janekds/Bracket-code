
import csv
import os
import random
names = []
userhome = os.path.expanduser('~')
csvfile = userhome + r'/Desktop/uni_spread.csv'
with open(csvfile, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)


bracket1 = []
bracket2 = []
lenx = len(data)
lenx = int(lenx/2)

reshuffle = True
shuffleCount = 0

while (reshuffle == True) and (shuffleCount <= 100):
    random.shuffle(data)
    

    bracket1 = data[0:lenx]
    bracket2 = data[lenx:]


    for i in range((lenx-1)):
        uni1 = str(bracket1[i])
        uni2 = str(bracket2[i])
        uni1,team1 = uni1.split('#')
        uni2,team2 = uni2.split('#')
        if uni1 == uni2:
            reshuffle = True
            break
        reshuffle = False
    shuffleCount +=1



print('final shuffle')
print("""
""")

if len(bracket1) != len(bracket2):
    print('uneven teams, walkover granted to:  ')
    print(bracket1[(len(bracket1)-1)])

print("""

team matchup

""")
for i in range(lenx):
        uni1 = str(bracket1[i])
        uni2 = str(bracket2[i])
        uni1,team1 = uni1.split('#')
        uni2,team2 = uni2.split('#')
        print( uni1, '', team1 , ' VS ', uni2, '', team2)
   

print('shuffle count is ', shuffleCount)

        

    
