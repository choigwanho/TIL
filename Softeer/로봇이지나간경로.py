from collections import deque
import sys
si = sys.stdin.readline

h,w = map(int,si().split()) # 처음 로봇의 위치 -> 행 h, 열 w
graph = list(list(map(si().strip()))) # 지도 -> 방문 '#', 미방문 '.'

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def l(d,x,y):
    return d, x, y

def r(d,x,y):
    return d, x, y

def a(d,x,y):
    return d, x, y