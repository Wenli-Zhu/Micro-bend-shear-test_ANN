# -*- coding: mbcs -*-
# Internal Version: 2016_09_28-05.54.59 126836



from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup

import os
os.chdir(r"D:\temp_abaqus")

n = 1
a = range(3960)  #900
for x in a:

 o3 = session.openOdb(name='d:/temp_abaqus/model'+str(n)+'.odb')#

 session.viewports['Viewport: 1'].setValues(displayedObject=o3)
 odb = session.odbs['d:/temp_abaqus/model'+str(n)+'.odb']#
 xy0 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='CFNM: CFNM     ASSEMBLY__PICKEDSURF10/ASSEMBLY__PICKEDSURF21', 
    steps=('Step-1', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
 xy1 = abs(xy0)
 xy_result = session.XYData(
    name='CFNM     ASSEMBLY__PICKEDSURF10/ASSEMBLY__PICKEDSURF21-1', 
    objectToCopy=xy1, 
    sourceDescription='abs(CFNM     ASSEMBLY__PICKEDSURF10/ASSEMBLY__PICKEDSURF21-1)')
 del session.xyDataObjects[xy0.name]
 del session.xyDataObjects[xy1.name]
 c1 = session.Curve(xyData=xy_result)
 xyp = session.XYPlot('XYPlot-'+str(n)) #:~
 chartName = xyp.charts.keys()[0]
 chart = xyp.charts[chartName]
 chart.setValues(curvesToPlot=(c1, ), )
 session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
 odb = session.odbs['d:/temp_abaqus/model'+str(n)+'.odb']#
 session.viewports['Viewport: 1'].setValues(displayedObject=odb)
 session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
 session.viewports['Viewport: 1'].view.setValues(nearPlane=24.1433, 
    farPlane=44.041, width=20.922, height=10.1811, cameraPosition=(-12.5607, 
    43.3376, -12.7129), cameraUpVector=(0.179344, -0.697361, -0.693918), 
    cameraTarget=(5.43838, 17.3765, 1.40716))
 session.viewports['Viewport: 1'].view.setValues(nearPlane=25.0399, 
    farPlane=43.1443, width=14.4865, height=7.04941, viewOffsetX=0.156059, 
    viewOffsetY=0.612052)
 session.viewports['Viewport: 1'].view.setValues(nearPlane=26.1478, 
    farPlane=42.9578, width=15.1274, height=7.36132, cameraPosition=(17.8281, 
    44.5262, -16.1712), cameraUpVector=(-0.184879, -0.751693, -0.63307), 
    cameraTarget=(5.02848, 17.5732, 1.35087), viewOffsetX=0.162964, 
    viewOffsetY=0.639132)
 odb = session.odbs['d:/temp_abaqus/model'+str(n)+'.odb'] #
 session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('U', 
    NODAL, ((INVARIANT, 'Magnitude'), )), ), nodePick=(('PART-1-1', 1, (
    '[#0:10 #10000000 ]', )), ), )
 xy1 = session.xyDataObjects['U:Magnitude PI: PART-1-1 N: 349']
 xy2 = session.xyDataObjects['CFNM     ASSEMBLY__PICKEDSURF10/ASSEMBLY__PICKEDSURF21-1']
 xy3 = combine(xy1, xy2)
 xy3.setValues(
    sourceDescription='combine ( "U:Magnitude PI: PART-1-1 N: 349", "CFNM     ASSEMBLY__PICKEDSURF10/ASSEMBLY__PICKEDSURF21-1" )')
 tmpName = xy3.name
 session.xyDataObjects.changeKey(tmpName, 'XYData-'+str(n)) #:~
 xyp = session.xyPlots['XYPlot-'+str(n)] #:~
 chartName = xyp.charts.keys()[0]
 chart = xyp.charts[chartName]
 xy1 = session.xyDataObjects['XYData-'+str(n)] #:~
 c1 = session.Curve(xyData=xy1)
 chart.setValues(curvesToPlot=(c1, ), )
 session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
 n = n+1

name_final =''
num =1
b = range(3959)  #
for y in b: 
    name_temp = 'XYData-'+str(num)+','
    name_final = name_final + name_temp
    num = num +1

name_final = name_final + 'XYData-3960'




import sys
sys.path.insert(46, 
    r'c:/SIMULIA/EstProducts/2020/win_b64/code/python2.7/lib/abaqus_plugins/excelUtilities')
import abq_ExcelUtilities.excelUtilities
abq_ExcelUtilities.excelUtilities.XYtoExcel(
    xyDataNames=name_final, 
    trueName='From Current XY Plot')
#: Multiple XY Data are exported. No chart will be created.
#: XY Data sent to Excel
 
 
