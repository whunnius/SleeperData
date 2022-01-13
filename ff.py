from sleeper_wrapper import League
import csv

league_id2021 = "650024576553668608"
league_id2020 = "568559799207018496"
league = League(league_id2021)

users = league.get_users() 
rosters = league.get_rosters()
#these values need to change if more years are added.
leagueArr = [League(league_id2020),League(league_id2021)]
standingsArr = [league.get_standings(leagueArr[0].get_rosters(),users),league.get_standings(leagueArr[1].get_rosters(),users)]
print(standingsArr)
yearArr = ["2020","2021"]
usersARR = [1,3,8,2,4,5,7,6]
username = []
finalData = []
contestants = []
ryansum = []
billysum = []
shawnsum = []
calsum = []
natesum = []
keegansum = []
tommysum = []
blakesum = []
counter = 0
lst = len(username)
header = ["Year","Week","Team 1", "Team 1 Score","Team 2", "Team 2 Score"]
header2 = ["Player","Total Wins","Total Losses", "Total Points For","Total Points Against"]

#creates username arr
for event in users:

    username.append(event['display_name'])

#makes username arr a list of tuples
for i in range(len(username)):
    username[i]=(username[i],usersARR[i])

#this sorts username from 1-8
for i in range(0, lst): 
    for j in range(0, lst-i-1): 
        if (username[j][1] > username[j + 1][1]): 
            temp = username[j] 
            username[j]= username[j + 1] 
            username[j + 1]= temp 

#makes contestants
for year in leagueArr:
    for i in range (1,15):
        matchup = League.get_matchups(year,week=i)
        for event in matchup:
            contestants.append((event['roster_id'],event['matchup_id'],event['points'],i,yearArr[counter]))
    counter+=1

# 224 = 14 weeks * 8 players * 2 years added. if more years added change this value.
for i in range (0,224,1):
    for j in range(i+1):
        #if the matchup number is the same and the week is the same and year is the same
        if(contestants[i][1]==contestants[j][1] and contestants[i][3]==contestants[j][3] and i!=j and contestants[i][4]==contestants[j][4]):
            finalData.append((contestants[i][3],username[contestants[i][0]-1][0],contestants[i][2],username[contestants[j][0]-1][0],contestants[j][2],contestants[i][4]))
print(contestants)
# Writes to csv file
with open("/Users/willt/OneDrive/Desktop/Fantasy_Football/test.csv", 'w',newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    for event in finalData:
        #year, week, player 1, player 1 score, player 2, player 2 score
        data = [event[5],event[0],event[1],event[2],event[3],event[4]]
        writer.writerow(data)



for event in standingsArr:
    for event2 in event:
        if(event2[0]=='Groot Ninjas'):        
             
             if(not ryansum):
                ryansum.append('ryan2summ')
                ryansum.append(event2[1])
                ryansum.append(event2[2])
                ryansum.append(event2[3])
             else:
                 ryansum[1] = int(ryansum[1]) + int(event2[1])
                 ryansum[2] = int(ryansum[2]) + int(event2[2])
                 ryansum[3] = int(ryansum[3]) + int(event2[3]) + 1
        if(event2[0]=='Billy’s Bills'):        
             
             if(not billysum):
                billysum.append('billyellinghaus7')
                billysum.append(event2[1])
                billysum.append(event2[2])
                billysum.append(event2[3])
             else:
                 billysum[1] = int(billysum[1]) + int(event2[1])
                 billysum[2] = int(billysum[2]) + int(event2[2])
                 billysum[3] = int(billysum[3]) + int(event2[3]) + 1
        if(event2[0]=='Ghengis Swans'):        
             
             if(not shawnsum):
                shawnsum.append('GhengisSwans')
                shawnsum.append(event2[1])
                shawnsum.append(event2[2])
                shawnsum.append(event2[3])
             else:
                 shawnsum[1] = int(shawnsum[1]) + int(event2[1])
                 shawnsum[2] = int(shawnsum[2]) + int(event2[2])
                 shawnsum[3] = int(shawnsum[3]) + int(event2[3]) + 1
        if(event2[0]=='The Goffather'):        
             
             if(not calsum):
                calsum.append('calcangilla')
                calsum.append(event2[1])
                calsum.append(event2[2])
                calsum.append(event2[3])
             else:
                 calsum[1] = int(calsum[1]) + int(event2[1])
                 calsum[2] = int(calsum[2]) + int(event2[2])
                 calsum[3] = int(calsum[3]) + int(event2[3]) + 1
        if(event2[0]=='NateKirberg'):        
             
             if(not natesum):
                natesum.append('NateKirberg')
                natesum.append(event2[1])
                natesum.append(event2[2])
                natesum.append(event2[3])
             else:
                 natesum[1] = int(natesum[1]) + int(event2[1])
                 natesum[2] = int(natesum[2]) + int(event2[2])
                 natesum[3] = int(natesum[3]) + int(event2[3]) + 1
        if(event2[0]=='keeganbates'):        
             
             if(not keegansum):
                keegansum.append('keeganbates')
                keegansum.append(event2[1])
                keegansum.append(event2[2])
                keegansum.append(event2[3])
             else:
                 keegansum[1] = int(keegansum[1]) + int(event2[1])
                 keegansum[2] = int(keegansum[2]) + int(event2[2])
                 keegansum[3] = int(keegansum[3]) + int(event2[3]) + 1
        if(event2[0]=='Fighting Snails'):        
             
             if(not tommysum):
                tommysum.append('FightingSnails')
                tommysum.append(event2[1])
                tommysum.append(event2[2])
                tommysum.append(event2[3])
             else:
                 tommysum[1] = int(tommysum[1]) + int(event2[1])
                 tommysum[2] = int(tommysum[2]) + int(event2[2])
                 tommysum[3] = int(tommysum[3]) + int(event2[3]) + 1
        if(event2[0]=='blakeunderdog'):        
             
             if(not blakesum):
                blakesum.append('blakeunderdog')
                blakesum.append(event2[1])
                blakesum.append(event2[2])
                blakesum.append(event2[3])
             else:
                 blakesum[1] = int(blakesum[1]) + int(event2[1])
                 blakesum[2] = int(blakesum[2]) + int(event2[2])
                 blakesum[3] = int(blakesum[3]) + int(event2[3]) + 1

totalSum = [ryansum,billysum,shawnsum,calsum,natesum,keegansum,tommysum,blakesum]
for event in totalSum:
    print (event)


#next up: get total points scored 

#next up: make win loss ratio of every player
#next up: get everyones specific win/loss ratio against every other player



            

