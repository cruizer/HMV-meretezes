import math
import logging
from qgis.core import QGis

class NetworkObject(object):
    """BASE object representing a general
    object in the pipe network.
    """
    def __init__(self, qgisElement, qgisLayer):
        super(NetworkObject, self).__init__()
        self.qgisElement = qgisElement
        self.qgisLayer = qgisLayer
    def getId(self):
        return self.qgisElement.id()
    def getType(self):
        return self.qgisElement.attribute('tipus')
    def getGeometryType(self):
        return self.qgisElement.geometry().wkbType()
    def getAttribute(self, keyword):
        return self.qgisElement.attribute(keyword)
    def setAttribute(self, keyword, value):
        self.qgisLayer.startEditing()
        self.qgisElement.setAttribute(keyword, value)
        self.qgisLayer.updateFeature(self.qgisElement)
        self.qgisLayer.commitChanges()

class NodeObject(NetworkObject):
    """Wrapper object representing node like
    objects in the pipe network.
    """
    def __init__(self, qgisElement, qgisLayer):
        super(NodeObject, self).__init__(qgisElement, qgisLayer)
        if self.getGeometryType() != QGis.WKBPoint:
            # TODO: Raise exception
            return None
        # Pipes that flow water IN the node
        self.inPipes = []
        # Pipes that flow water OUT of the node
        self.outPipes = []
        # Cache variable for listing network heatloss
        self.heatlossCache = []
    def getCoordinates(self):
        return self.qgisElement.geometry().asPoint()
    def connects(self, otherFeature):
        if otherFeature.getGeometryType() == QGis.WKBLineString:
            if self.getCoordinates() == otherFeature.getCoordinates()[0] or \
                self.getCoordinates() == otherFeature.getCoordinates()[
                    len(otherFeature.getCoordinates()) - 1]:
                return True
            else:
                return False
        else:
            # TODO: Raise exception
            return None
    def connectsStart(self, otherFeature):
        if otherFeature.getGeometryType() == QGis.WKBLineString:
            if self.getCoordinates() == otherFeature.getCoordinates()[0]:
                return True
            else:
                return False
        else:
            # TODO: Raise exception
            return None
    def connectsEnd(self, otherFeature):
        if otherFeature.getGeometryType() == QGis.WKBLineString:
            if self.getCoordinates() == \
                otherFeature.getCoordinates()[len(otherFeature.getCoordinates()) - 1]:
                return True
            else:
                return False
        else:
            # TODO: Raise exception
            return None
    def calculateNetworkHeatloss(self, pipeObject, isFromTap):
        pipeHeatLoss = pipeObject.getAttribute('hovesztes')
        if isFromTap == True:
            networkHeatloss = pipeHeatLoss
        else:
            previousNodeHeatloss = pipeObject.connectsEndNode.getAttribute('rendsz_hov')
            networkHeatloss = pipeHeatLoss + previousNodeHeatloss

        self.heatlossCache.append(networkHeatloss)
        logging.debug('Number of outgoing pipes from node id %s is %s from this, we have %s added to the heatloss cache.',
                      self.getId(), len(self.outPipes), len(self.heatlossCache))
        if len(self.heatlossCache) == len(self.outPipes):
            self.saveHeatlossFromCache()
            return True
        else:
            return False
    def saveHeatlossFromCache(self):
        total = 0
        for item in self.heatlossCache:
            total += item
        self.qgisLayer.startEditing()
        self.setAttribute('rendsz_hov', total)
        self.qgisLayer.updateFeature(self.qgisElement)
        self.qgisLayer.commitChanges()

class PipeObject(NetworkObject):
    """Wrapper object representing pipes
    in the pipe network.
    """
    def __init__(self, qgisElement, qgisLayer):
        super(PipeObject, self).__init__(qgisElement, qgisLayer)
        if self.getGeometryType() != QGis.WKBLineString:
            # TODO: Raise exception
            pass
        # Node connecting the start of this pipe
        self.connectsStartNode = None
        # Node connection the end of this pipe
        self.connectsEndNode = None
    def getCoordinates(self):
        return self.qgisElement.geometry().asPolyline()
    def setCoordinates(self, newGeo):
        self.qgisElement.setGeometry(newGeo)
    def connects(self, otherFeature):
        if otherFeature.getGeometryType() == QGis.WKBPoint:
            if self.getCoordinates()[0] == otherFeature.getCoordinates() or \
                      self.getCoordinates()[len(self.getCoordinates()) - 1] == \
                      otherFeature.getCoordinates():
                return True
            else:
                return False
        else:
            # TODO: Raise exception
            return None
    def flipDirection(self):
        """We flip the direction of a pipe, which takes three steps:
        1. Reverse the coordinates
        2. Fix the in and out pipes references of connected nodes
        3. Fix the node references of the pipe (connectsEndNode / connectsStartNode)
        """
        # Open the layer for editing
        self.qgisLayer.startEditing()
        # We fetch the current coordinates and reverse them
        newCoordinates = self.getCoordinates().reverse()
        self.setCoordinates(newCoordinates)
        # Save the direction change of the vector
        self.qgisLayer.updateFeature(self.qgisElement)
        self.qgisLayer.commitChanges()
        # We fix the reference to this pipe on the
        # nodes that are connected
        oldEndNode = self.connectsEndNode
        oldStartNode = self.connectsStartNode
        # Fix node that used to be the end
        oldEndNode.inPipes.remove(self)
        oldEndNode.outPipes.append(self)
        # Fix node that used to be the start
        oldStartNode.outPipes.remove(self)
        oldStartNode.inPipes.append(self)
        # Finally, flip the references to the nodes on this pipe
        self.connectsStartNode = oldEndNode
        self.connectsEndNode = oldStartNode


    def calculateHeatloss(self):
        # Hoszigeteles hovezetesi tenyezoje
        lambdam = self.getAttribute('szig_hovez')
        # Hoszigetelessel egyutti csoatmero
        Dm = self.getAttribute('atmero_szi')
        # Hoszigeteles nelkuli csoatmero
        dm = self.getAttribute('atmero_cso')
        # Kulso oldali hoatadasi tenyezo 10W/(m2K)
        alfakm = self.getAttribute('hoatadas')
        # Helyiseg homerseklet
        Thely = self.getAttribute('helyiseg_h')
        # Csoben levo viz homerseklete
        Thmv = self.getAttribute('csoviz_hom')
        # Szakasz hossza
        Lm = self.getAttribute('hossz')
        # Hoatbocsatasi tenyezo
        heatTrans = math.pi / (
            (1.0 / (2.0 * lambdam)) * math.log(Dm / dm) + (1.0 / (alfakm * Dm / 1000.0)))
        self.setAttribute('hoatbocs', heatTrans)
        # Holeadas / m
        heatDissipation = heatTrans * (Thmv - Thely)
        self.setAttribute('holeadas', heatDissipation)
        # Hoveszteseg a szakaszra
        heatLoss = heatDissipation * Lm
        self.setAttribute('hovesztes', heatLoss)
        logging.debug('The heat loss on the pipe with id %s is %s .', self.getId(), heatLoss)
