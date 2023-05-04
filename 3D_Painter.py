import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
import PoseGet
import csv
datas,frameNums =PoseGet.GetPoseDataFromVideo("skating.gif")
#print(datas[-1])
'''
datas: visibility,x,y,z
'''

pair_list = [
    (0,1),
    (0,4),
    (1,3),
    (4,6),
    (3,7),
    (6,8),
    (9,10),
    (12,14),
    (14,16),
    (12,11),
    (11,13),
    (13,15),
    (12,24),
    (11,23),
    (24,23),
    (24,26),
    (26,28),
    (23,25),
    (25,27),
]
    
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))

def PaintLine(pointsData):
    for index1,index2 in pair_list:
        ax.plot([pointsData[index1].x,pointsData[index2].x],[pointsData[index1].z,pointsData[index2].z],[-pointsData[index1].y,-pointsData[index2].y], c = 'r', linewidth=1, marker=".", markeredgecolor='b', markerfacecolor='b')
#print(datas)
print(frameNums)
csv_file = open("3D_pose.csv",'w')
writer = csv.writer(csv_file)
while True:
    tmpData = None
    for i in range(frameNums):
        plt.cla()
        ax.set_title('Relative Coordinates')
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.set_xlim(-1, 1) 
        ax.set_ylim(-1, 1)
        ax.set_zlim(-1, 1)
        
        # ax.plot([datas[i][0].x,datas[i][1].x],[datas[i][0].y,datas[i][1].y],[datas[i][0].z,datas[i][1].z], c = 'r', linewidth=1, marker=".", markeredgecolor='b', markerfacecolor='b')
        try:
            PaintLine(datas[i])
            tmpData = datas[i]
            
        except:
            PaintLine(tmpData)
            
        one_data = [] 
        print(i)
        for j in range(33):
            one_data.append([tmpData[j].x,tmpData[j].z,-tmpData[j].y])
        writer.writerow(one_data)
        plt.pause(0.1)
    break
csv_file.close()
plt.show()

