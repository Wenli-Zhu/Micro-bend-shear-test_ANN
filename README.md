# Micro bend-shear test
This is a guide for FEM database building, input-output data processing, and ANN training required in the using of the Micro bend-shear Test.
## Generate the tensile true stress-true plastic strain data using Ludwik-Hollomon relation 
Open the `Ludwik_Hollomon.m` and run this code. 
You may need to modify this line for changing the direction of the abaqus data file which will need to use for abaqus FEM generation.
```
writematrix(abaqus_input,'e:/ABAQUS/double hole/Abaqussnew.csv')
```
Also, if you want to change the different increment of the yield stress, the strength coefficient, and working hardening rate. Just change this part.
```
for d = 0.3:0.05:0.5
    for sigma_y= 200:25:450
        for K = 600:150:1650
            for n = 0.1:0.05:0.5
```
If the tested material mechanical properties satisfy other types of relationsip,  you also can easily modify this part.
```
sigma_true = sigma_y + K*epsilong_ln_pl.^(n);
```
## Generate FEM using Abaqus/Python
Open the file `Abaqus_buildModels.py`
Change this line for your own working directory:
```
os.chdir(r"D:\temp_abaqus")
```
Change this direction which is the direction you use to generate the `Abaqussnew.csv` file using `Ludwik_Hollomon.m`.
```
file='e:/ABAQUS/double hole/Abaqussnew.csv'
```
For computers with different configurations, you need to modify the abaqus job according to your own configuration. 
```
        mdb.Job(name='model'+ str(num), model='model'+ str(num), description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
        numGPUs=0)
```
For example, if your cpu has more cores, you can just change the parameter for the numCpus.
Then, unzip the `Abaqus_baseModels.rar`.
Open the cae file and choose `File--Run Script`. Choose the file `Abaqus_buildModels.py `.
## Run the simulation and Output generation
You may use the `Abaqus_run.py` to run all the jobs using Parallel computing. The number for each group of jobs need to be set for your own computer configuration.
`waitForCompletion` has added. So after Abaqus finish running a group of jobs you specified, Abaqus immediately submit the next set of jobs.
At least 100GB of hard disk space for the working directory to save all the OBD data files.
Use `Abaqus_curves.py` for generating excel file for the load-displacement curves. Also, the following lines need to be changed based on your own directory.
```
os.chdir(r"D:\temp_abaqus")
o3 = session.openOdb(name='d:/temp_abaqus/model'+str(n)+'.odb')#
```
Save the xlsx file in the working directory your matlab will use. 
## Using ANN with Matlab
Open and run the file `Ann_new.m` with Matlab.
Be sure your xlsx file name and directory are consistent with the Matlab code.
```
filename = 'database.xlsx';
```

