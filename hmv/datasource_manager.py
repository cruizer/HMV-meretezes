import ogr
import os.path
from PyQt4.QtGui import QMessageBox


def createLayer(layerName, fileName, workingDir, layerType):
    """Create a new layer in a new datasource"""
    driver = ogr.GetDriverByName('SQLite')

    if os.path.isdir(workingDir):
        layerFilePath = os.path.join(workingDir, fileName)
    else:
        raise OSError("Working directory {} doesn't exist.".format(workingDir))

    if os.path.exists(layerFilePath):
        if askUseExistingFile() == False:
            # User doesn't want to use existing file
            return None
        else:
            # OK, use existing file as a datasource
            datasource = driver.Open(layerFilePath)

    else:
        datasource = driver.CreateDataSource(layerFilePath, options=['SPATIALITE=YES'])
    # Create the type of layer needed
    if layerType == 'szakaszok':
        layer = datasource.CreateLayer(layerName.encode('utf-8'), geom_type=ogr.wkbLineString)
    elif layerType == 'elemek':
        layer = datasource.CreateLayer(layerName.encode('utf-8'), geom_type=ogr.wkbPoint)
    else:
        return None

    addLayerAttributes(layer, layerType)
    return layerFilePath
        

def askUseExistingFile():
    """Ask if the existing file should be used as a datasource for the change"""
    existsQuestionBox = QMessageBox()
    existsQuestionBox.setText('The configured datasource file already exists.')
    existsQuestionBox.setInformativeText('Is this an existing data source you want to add the new layer to?')
    existsQuestionBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    userAnswer = existsQuestionBox.exec_()
    if userAnswer == QMessageBox.Yes:
        return True
    else:
        return False


def addLayerAttributes(layer, kind):
    # Attributes
    # pipes
    pipeAttributes = {'hossz': {'type': ogr.OFTReal, 'width': 19, 'precision': 2},
                       'csoviz_hom': {'type': ogr.OFTReal, 'width': 19, 'precision': 2},
                       'helyiseg_h': {'type': ogr.OFTReal, 'width': 19, 'precision': 2},
                       'szig_hovez': {'type': ogr.OFTReal, 'width': 19, 'precision': 2},
                       'atmero_szi': {'type': ogr.OFTReal, 'width': 19, 'precision': 2},
                       'atmero_cso': {'type': ogr.OFTReal, 'width': 19, 'precision': 2},
                       'hoatadas': {'type': ogr.OFTReal, 'width': 19, 'precision': 2},
                       'cso_erdess': {'type': ogr.OFTReal, 'width': 19, 'precision': 2},
                       'szerelveny': {'type': ogr.OFTReal, 'width': 19, 'precision': 2},
                       'alaki_teny': {'type': ogr.OFTReal, 'width': 19, 'precision': 2},
                       'hovesztes': {'type': ogr.OFTReal, 'width': 19, 'precision': 2},
                       'hoatbocs': {'type': ogr.OFTReal, 'width': 19, 'precision': 2},
                       'holeadas': {'type': ogr.OFTReal, 'width': 19, 'precision': 2},
                       'aram_seb': {'type': ogr.OFTReal, 'width': 4, 'precision': 2},
                       'vissza_atm': {'type': ogr.OFTInteger, 'width': 3, 'precision': 0},
                       'terfaram': {'type': ogr.OFTReal, 'width': 7, 'precision': 2},
                       'assoc_err': {'type': ogr.OFTInteger, 'width': 1, 'precision': 0},
                       'cso_surl': {'type': ogr.OFTReal, 'width': 4, 'precision': 2},
                       'nyomas_es': {'type': ogr.OFTReal, 'width': 6, 'precision': 2},
                       'reynolds': {'type': ogr.OFTReal, 'width': 6, 'precision': 2},
                       'fajl_nyom': {'type': ogr.OFTReal, 'width': 9, 'precision': 2}
    }
    # nodes
    nodeAttributes = {'tipus': {'type': ogr.OFTString, 'width': 80, 'precision': 0},
                       'fojtas': {'type': ogr.OFTReal, 'width': 14, 'precision': 2},
                       'rendsz_hov': {'type': ogr.OFTReal, 'width': 9, 'precision': 2},
                       'assoc_err': {'type': ogr.OFTInteger, 'width': 1, 'precision': 0},
                       'ag': {'type': ogr.OFTInteger, 'width': 2, 'precision': 0}
    }
    if kind == 'szakaszok':
        layerAttributes = pipeAttributes
    elif kind == 'elemek':
        layerAttributes = nodeAttributes
    # Create attributes
    for attrName, config in layerAttributes.items():
        field = ogr.FieldDefn(attrName, config['type'])
        field.SetWidth(config['width'])
        field.SetPrecision(config['precision'])
        layer.CreateField(field)
