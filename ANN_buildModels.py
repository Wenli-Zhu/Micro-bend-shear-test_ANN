from abaqus import *
from abaqusConstants import *
import csv
import os
import numpy as np
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
    
#openMdb(pathName='E:/ABAQUS/double hole/doubleholetestANN_new.cae')
os.chdir(r"D:\temp_abaqus")


name = ['Modela','Modelb','Modelc','Modeld','Modele']

file='e:/ABAQUS/double hole/Abaqussnew.csv' # Abaqus_input


ANN = []
with open(file) as csvfile:
    csv_reader = csv.reader(csvfile)    
    for row in csv_reader:  
        ANN.append(row)
        
stress = []
strain = []
for i in range(3960):#900 number of samples
    stress.append([])
    for j in range(50): # epsilong_ln_pl = linspace(0,0.3,50);
        stress[i].append(0)
        
for i in range(3960):#900 number of samples
    strain.append([])
    for j in range(50): # epsilong_ln_pl = linspace(0,0.3,50);
        strain[i].append(0)
        
num =1      
c = range(5)  #5  number of different thickness    
a = range(792)# number of samples/ number of different thickness
b = range(50)
for z in c:
    for x in a:
        for y in b:
       
         stress[x][y] = float(ANN[y+1][792*2*z+2*x])# number of samples in each thickness 792
         strain[x][y] = float(ANN[y+1][792*2*z+2*x+1])# number of samples in each thickness 792
        
        mdb.Model(name= 'model'+ str(num), objectToCopy=mdb.models[name[z]])
        mdb.models['model'+ str(num)].materials['Material-1'].plastic.setValues(table=((
        stress[x][0], strain[x][0]), (stress[x][1], strain[x][1]), (stress[x][2], strain[x][2]), 
        (stress[x][3], strain[x][3]), (stress[x][4], strain[x][4]), (stress[x][5], 
        strain[x][5]), (stress[x][6], strain[x][6]), (stress[x][7], strain[x][7]), (
        stress[x][8], strain[x][8]), (stress[x][9], strain[x][9]), (stress[x][10], 
        strain[x][10]), (stress[x][11], strain[x][11]), (stress[x][12], strain[x][12]), (
        stress[x][13], strain[x][13]), (stress[x][14], strain[x][14]), (stress[x][15], 
        strain[x][15]), (stress[x][16], strain[x][16]), (stress[x][17], strain[x][17]), (
        stress[x][18], strain[x][18]), (stress[x][19], strain[x][19]), (stress[x][20], 
        strain[x][20]), (stress[x][21], strain[x][21]), (stress[x][22], strain[x][22]), (
        stress[x][23], strain[x][23]), (stress[x][24], strain[x][24]), (stress[x][25], 
        strain[x][25]), (stress[x][26], strain[x][26]), (stress[x][27], strain[x][27]), (
        stress[x][28], strain[x][28]), (stress[x][29], strain[x][29]), (stress[x][30], 
        strain[x][30]), (stress[x][31], strain[x][31]), (stress[x][32], strain[x][32]), (
        stress[x][33], strain[x][33]), (stress[x][34], strain[x][34]), (stress[x][35], 
        strain[x][35]), (stress[x][36], strain[x][36]), (stress[x][37], strain[x][37]), (
        stress[x][38], strain[x][38]), (stress[x][39], strain[x][39]), (stress[x][40], 
        strain[x][40]), (stress[x][41], strain[x][41]), (stress[x][42], strain[x][42]), (
        stress[x][43], strain[x][43]), (stress[x][44], strain[x][44]), (stress[x][45], 
        strain[x][45]), (stress[x][46], strain[x][46]), (stress[x][47], strain[x][47]), (
        stress[x][48], strain[x][48]), (stress[x][49], strain[x][49])))
            
        mdb.Job(name='model'+ str(num), model='model'+ str(num), description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
        numGPUs=0)
        num = num+1


mdb.save()
    
    
    



     
     
    
     
     

    
    