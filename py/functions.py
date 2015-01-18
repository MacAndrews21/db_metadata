import cv2
import glob
import os
import sys
import gdal
from gdalconst import *
import postgres as po

##metaData = os.popen('gdalinfo -stats -nomd -norat -noct -nofl ' + filePath + fileName)
def getResolution (filePath, fileName):
    dataset = gdal.Open(filePath + fileName, GA_ReadOnly)
    width = dataset.RasterXSize
    height = dataset.RasterYSize
    #print 'Projection:', dataset.GetProjection()
    
    geotrans = dataset.GetGeoTransform()
    if not geotrans is None:
        pixelSize = geotrans[1]
    
    return width, height, pixelSize

def createFileNameList(folderPath):
    
    ''' create List of file names in folder '''
    fileNameList = []
    
    
    
    for fileData in glob.glob(os.path.join(folderPath, '*.tif')):
        ''' create temporary dictionary '''
        namesDictionary = {}
        
        ''' seperate filename '''
        startIndex = fileData.rfind('/') + 1
        fileName = fileData[startIndex:]
        #print fileName
        
        width, height, pixelSize = getResolution(folderPath, fileName)

        
        ''' get kb id '''        
        kb = fileName[:4]
        
        ''' get kb year '''        
        end = fileName.rfind('.')
        year = fileName[5:end]
        
        ''' put fileName, id and year into temporary dictionary '''
        namesDictionary["name"] = fileName
        namesDictionary["id"] = kb
        namesDictionary["year"] = year
        namesDictionary["width"] = width
        namesDictionary["height"] = height
        namesDictionary["pixelSize"] = pixelSize

        ''' add filename to list '''
        fileNameList.append(namesDictionary)
        
        
    return fileNameList
