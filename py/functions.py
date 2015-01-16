import cv2
import glob
import os
import sys
import gdal
from gdalconst import *

dataset =gdal.Open("/home/andreas/Projekte/test-data/1012_1955.tif", GA_ReadOnly)
width = dataset.RasterXSize
height = dataset.RasterYSize
#print 'Projection:', dataset.GetProjection()

geotrans = dataset.GetGeoTransform()
if not geotrans is None:
    pixelSize = geotrans[1]
    
    
res = width * pixelSize
resres = height * pixelSize
print res, resres



##def getResolution (filePath, fileName):
    ##metaData = os.popen('gdalinfo -stats -nomd -norat -noct -nofl ' + filePath + fileName)
    ##data = metaData.readlines()
    ##metaData.close()
    
    ##def getBrackets(currentLine):
        ##''' Select brackets '''
        ##startBracket = currentLine.index("(") + 1
        ##endBracket = currentLine.index(")", startBracket)            
        ##brackets = currentLine[startBracket:endBracket]       
        
        ##''' get all before the comma and remove whitespace with .strip()'''
        ##comma = brackets.index(",")
        ##X = float(brackets[:comma].strip())
        ##Y = float(brackets[comma + 1:].strip())
        
        ##''' return first and second value of the brackets'''
        ##return X, Y
    
    
    ##cornerCoordinates = {}
    ###print data
    ##for lines in range(len(data)):
        ##line = data[lines]
        ##if 'Pixel Size' in line:
            ##pxSize, negPxSize = getBrackets(line)
            ###pixelSize['positiv'] = pxSize
            ###pixelSize['negativ'] = negPxSize
            ##cornerCoordinates['pixelSize'] = pxSize
            
        ##if 'Size is' in line:
            ##midle = line.rfind(',')
            ##w = midle - 4
            ##width = line[w:midle]
            ##hs = midle + 2
            ##h = hs + 4
            ##height = line[hs:h]
            ##print width, height
            ###pixelSize['positiv'] = pxSize
            ###pixelSize['negativ'] = negPxSize
            ##cornerCoordinates['width'] = width
            ##cornerCoordinates['height'] = height
    ###print cornerCoordinates
    ##test = float(cornerCoordinates['width']) / float(cornerCoordinates['pixelSize'])
    ##print test
    ##return cornerCoordinates





def createFileNameList(folderPath):
    
    ''' create List of file names in folder '''
    fileNameList = []
    
    
    
    for filename in glob.glob(os.path.join(folderPath, '*.tif')):
        ''' create temporary dictionary '''
        namesDictionary = {}
        
        ''' seperate filename '''
        startIndex = filename.rfind('/') + 1
        name = filename[startIndex:]

        
        ''' get kb id '''        
        kb = name[:4]
        
        ''' get kb year '''        
        end = name.rfind('.')
        year = name[5:end]
        
        ''' put name, id and year into temporary dictionary '''
        namesDictionary["name"] = name
        namesDictionary["id"] = kb
        namesDictionary["year"] = year

        ''' add filename to list '''
        fileNameList.append(namesDictionary)
    return fileNameList
