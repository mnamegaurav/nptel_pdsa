# Number of best-of-5 set matches won
# Number of best-of-3 set matches won
# Number of sets won
# Number of games won
# Number of sets lost
# Number of games lost
# Federer:Nadal:2-6,6-7,7-6,6-3,6-1

input_data = input()
output_data = {}
while input_data:
    (bestof5won, bestof3won) = (0,0)
    (sets_won,sets_lost) = (0,0)
    (games_won,games_lost) = (0,0)
    (winner,loser,sets) = input_data.split(':')     
    for scores in sets.split(','):
        scores = scores.split('-')
        scores[0],scores[1] = int(scores[0]),int(scores[1])
        if scores[0] > scores[1]:
            sets_won += 1
        else:
            sets_lost += 1
        games_won += scores[0]
        games_lost += scores[1]
    if sets_won >= 3:
        bestof5won += 1
    elif sets_won < 3:
        bestof3won += 1    
    
    for player in [winner,loser]:
        try:
            output_data[player]
        except:
            output_data[player] = [0,0,0,0,0,0]
            
        if player == winner:
            output_data[player][0] += bestof5won
            output_data[player][1] += bestof3won
            output_data[player][2] += sets_won
            output_data[player][3] += games_won
            output_data[player][4] += sets_lost
            output_data[player][5] += games_lost
        
        if player == loser:
            output_data[player][2] += sets_lost
            output_data[player][3] += games_lost
            output_data[player][4] += sets_won
            output_data[player][5] += games_won
            
    input_data = input()
            
output_data = sorted(output_data.items(),key = lambda t:t[1], reverse = True)

for values in output_data:
    print(values[0],values[1][0],values[1][1],values[1][2],values[1][3],values[1][4],values[1][5])