import json
from prettytable import prettytable

#Reads the JSON file, extracts the team names and returns a list of the names
def getTeamNames():    
        with open('teamstats.json') as stats:
            
            statImport = json.load(stats)
            return(list(statImport.keys()))


#The index of a team is passed through this method and a list is returned of the amount of wins the team had against every other team        
def get_Team_Wins(team_num):
        
        list_of_wins = []
        with open('teamstats.json') as stats:
            
            statImport = json.load(stats)
        num_of_teams = len(getTeamNames())
        
        for i in range(1):
                all_wins_losses = list(statImport.values())[team_num]
                
                for j in range(num_of_teams - 1):
                        single_wins_losses = list(all_wins_losses.values())[j]
                        
                        for k in range(num_of_teams - 1):
                                single_win = list(single_wins_losses.values())
                        list_of_wins.append(single_win[0])
                        
        return(list_of_wins)                

#This method creates a 2d array. The first row, last row and first column are the team abbreviations. The rest of the rows are the win and loss data. The array is then returned.                           
def makeTable(teamNames):

        teamNames = getTeamNames()
        numTeams = len(teamNames)
        row, column = (numTeams + 2, numTeams + 1)
        arr = []
        header_footer = ["Tm "] + teamNames

        for i in range(row):
                col = []
                
                for j in range(column):
                        if i == 0 or i == column:
                                
                                col.append(header_footer[j])
                                
                        if i > 0 and i < row-1:
                                
                                if j == 0:
                                        col.append(teamNames[i-1])
                                        
                                if i == j:
                                        col.append('---')
                                        
                                if j > 0 and j < numTeams:
                                        win_list = get_Team_Wins(i-1)
                                        w = win_list[j-1]
                                        if w < 10:
                                                
                                                col.append(str(w)+'  ')
                                        else:
                                                col.append(str(w)+' ')
                arr.append(col)
                
        return(arr)        

#This method prints the array to the console. A nested for loop is used to print each line individually from a temporary array created in the method.
def printTable(table):
        
        teamNames = getTeamNames()
        numTeams = len(teamNames)
        row, column = (numTeams + 1, numTeams + 2)
        
        for i in range(column):
                holder = []
                for j in range(row):
                        holder.append(table[i][j])
                print(*holder, sep=' ')


printTable(makeTable(getTeamNames()))


        
