#!/usr/bin/python
# Author: Savitaa Venkateswaran
# Problem statement: https://www.hackerrank.com/challenges/saveprincess/problem
# Difficulty: Easy

def displayPathtoPrincess(n,grid):
#print all the moves here
    grid1 = grid[0].split('-')
    grid1 = list(grid1)
    gridn = grid[n-1].split('-')
    gridn = list(gridn)
    
    if str(grid1[0]) == 'p':
        princess = [0, 0]
    elif str(grid1[n-1]) == 'p':
        princess = [0, n-1]
    elif str(gridn[0]) == 'p':
        princess = [n-1, 0]
    elif str(gridn[n-1]) == 'p':
        princess = [n-1, n-1]
    
    if n % 2 == 0:
        mid = n/2 - 1
        midplu = n/2
        gridm1 = grid[mid].split('-')
        gridm1 = list(gridm1)
        gridm2 = grid[midplu].split('-')
        gridm2 = list(gridm2)
        if str(gridm1[mid]) == 'm':
            mypos = [mid, mid]
        elif str(gridm1[midplu]) == 'm':
            mypos = [mid, midplu]
        elif str(gridm2[mid]) == 'm':
            mypos = [midplu, mid]
        elif str(gridm2[midplu]) == 'm':
            mypos = [midplu, midplu]
    else:
        mid = int(n/2)
        gridm = grid[mid].split('-')
        gridm = list(gridm)
        if str(gridm[mid]) == 'm':
            mypos = [mid, mid]
        else:
            print('pos not center..')
            
    # print(mypos, princess)
    
    # calc distance and print moves..
    trajectory = [mypos[0]-princess[0], mypos[1]-princess[1]]
    
    # print(trajectory)
    
    if trajectory[0] > 0:
        for i in range(trajectory[0]):
            print('UP')
    elif trajectory[0] < 0:
        for j in range(abs(trajectory[0])):
            print('DOWN')
    if trajectory[1] > 0:
        for k in range(trajectory[1]):
            print('LEFT')
    elif trajectory[1] < 0:
        for h in range(abs(trajectory[1])):
            print('RIGHT')

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
