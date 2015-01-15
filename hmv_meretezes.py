# -*- coding: utf-8 -*-
import qgis
import logging
import math
from string import Template
from pipesys_objects import *


class NetworkEnvironment(object):
  """Object to create environment to run calculation"""
  def __init__(self):
    super(NetworkEnvironment, self).__init__()
    self.registry = qgis.core.QgsMapLayerRegistry.instance()
    self._createLayers()
    self._createFeatureIterators()
    self.nodesList = []
    self.pipesList = []
    self._createObjects()
    self._createNodePipeRelations()
    self.pipeSizeSet = [10, 12.5, 16, 19, 25, 32, 40] # Set of available pipe diameters in mm
    # Constants to indicate the association state of elements
    self.ASSOC_NOCHECK = 0
    self.ASSOC_ERR = 1
    self.ASSOC_OK = 2
    # Stores validation status
    self.validationStats = { 'overallStatus': "Nem ellenőrzött",
                              'allElementsCount': 0,
                              'errElementsCount': 0,
                              'errElements': []}
    self.statusCodes = { 0: 'Nem ellenőrzött', 1: 'Hibás!', 2: 'OK'}
    # Default settings
    self.sizes = [10, 12, 16, 19, 25, 32, 40]
    self.density = 983.2 # kg/m3
    self.specificHeat = 4200.0 # J/kgK
    self.deltaTheta = 2.0 # K
    self.pipeSpeedLimit = 1 # m/s
    # Total heatloss of flow network
    self.totalNetworkHeatloss = None
    self.pumpFlow = None
    # Flow path matrix
    self.pathMatrix = []
    # Pressure loss for each path in the matrix
    self.pathPressureLoss = []
    # Reference pressure = max(path pressure loss) + 3000 Pa
    self.referencePathPressure = None
    # Choke pressure loss for each path in the matrix
    self.chokePressureLoss = []
    # Choke kv value for each path in the matrix
    self.chokeKv = []
  def _createLayers(self):
    # Load *node* layer
    self.nodesLayer = self.registry.mapLayersByName('elemek')[0]
    # Load *pipes* layer
    self.pipesLayer = self.registry.mapLayersByName('szakaszok')[0]
  def _createFeatureIterators(self):
    # Get layer features (elements)
    self.nodeIterator = self.nodesLayer.getFeatures()
    # Get layer features (pipes)
    self.pipeIterator = self.pipesLayer.getFeatures()
  def _createObjects(self):
    for node in self._getNodeIterator():
      self.nodesList.append(NodeObject(node, self._getNodesLayer()))
    for pipe in self._getPipeIterator():
      self.pipesList.append(PipeObject(pipe, self._getPipesLayer()))
  def _createNodePipeRelations(self):
    for node in self.nodesList:
      for pipe in self.pipesList:
        if node.connectsStart(pipe):
          node.outPipes.append(pipe)
          pipe.connectsStartNode = node
          msg = Template('Adding pipe $pipe to the list of pipes running OUT of node $node')
          logging.debug(msg.substitute(pipe=pipe.getId(), node=node.getId()))
        elif node.connectsEnd(pipe):
          msg = Template('Adding pipe $pipe to the list of pipes coming IN to node $node')
          logging.debug(msg.substitute(pipe=pipe.getId(), node=node.getId()))
          node.inPipes.append(pipe)
          pipe.connectsEndNode = node
  def _organizeVectors(self, nextNode=None, currentInPipe=None, firstRun=False):
    """Iterate through the whole nextwork to make sure
    that the pipe vectors point to the right direction.
    This is required for later stage calculations. It
    basically indicates the direction of the water flow."""
    if firstRun == True:
      # First we look for the starting point we can iterate from
      for node in self.nodesList:
        if node.getAttribute('tipus') == 'MTB':
          # Once found, that is our starting point
          startNode = node
          break
      # Make sure, that only one pipe goes out of the pump
      # (which should be the case)
      if len(startNode.outPipes) == 1:
        nextNode = startNode.outPipes[0].connectsEndNode

    # GENERIC PART starts gere

    # If only one pipe comes in, we are OK
    if len(nextNode.inPipes) == 1:
      pass
    # If there are other pipes, we need to flip 'em
    else:
      for pipe in nextNode.inPipes:
        # We only need to flip the incoming pipes
        # that are not the one we are coming from
        if pipe != currentInPipe:
          pipe.flipDirection()
        else:
          pass
    # If there are is a pipe going further from this node
    if len(nextNode.outPipes) > 0:
      for pipe in nextNode.outPipes:
        self._organizeVectors(nextNode=pipe.connectsEndNode, currentInPipe=pipe)
  def resetValidationStatus(self):
    """Resets validation stat dictionary to initial values"""
    self.validationStats = { 'overallStatus': 0,
                              'allElementsCount': len(self.pipesList) + len(self.nodesList),
                              'errElementsCount': 0,
                              'errElements': []}
  def addValidationErr(self, element):
    # Constructing element data for error list
    # Tuple: (layer's name, id, )
    msg = [element.qgisLayer.name(), element.getId(), element.getAttribute('tipus')]
    self.validationStats['overallStatus'] = 1
    self.validationStats['errElementsCount'] += 1
    self.validationStats['errElements'].append(msg)
  def verifyObjectConnections(self):
    # We reset the status
    self.resetValidationStatus()
    # Verify the all pipes have a node connected on both ends
    for pipe in self.pipesList:
      if pipe.connectsStartNode == None or pipe.connectsEndNode == None:
        pipe.setAttribute('assoc_err', self.ASSOC_ERR)
        self.addValidationErr(pipe)
      else:
        pipe.setAttribute('assoc_err', self.ASSOC_OK)
    for node in self.nodesList:
      if node.getType() == u'Csapoló':
        # If we are at a tap it should have one pipe coming in
        # and NO pipe going out.
        if len(node.inPipes) != 1 or len(node.outPipes) != 0:
          node.setAttribute('assoc_err', self.ASSOC_ERR)
          self.addValidationErr(node)
        else:
          node.setAttribute('assoc_err', self.ASSOC_OK)
      elif node.getType() == 'MTB':
        # If we are at the pump it should have one pipe going out
        # and NO pipe coming in.
        if len(node.inPipes) != 0 or len(node.outPipes) != 1:
          node.setAttribute('assoc_err', self.ASSOC_ERR)
          self.addValidationErr(node)
        else:
          node.setAttribute('assoc_err', self.ASSOC_OK)
      else:
        # For all other nodes, they should have exactly on pipe
        # coming in and at least one pipe going out.
        if len(node.inPipes) != 1 or len(node.outPipes) < 1:
          node.setAttribute('assoc_err', self.ASSOC_ERR)
          self.addValidationErr(node)
        else:
          node.setAttribute('assoc_err', self.ASSOC_OK)
    if self.validationStats['overallStatus'] == 0:
      self.validationStats['overallStatus'] = 2
    return self.validationStats
  def _getNodesLayer(self):
    return self.nodesLayer
  def _getPipesLayer(self):
    return self.pipesLayer
  def _getNodeIterator(self):
    return self.nodeIterator
  def _getPipeIterator(self):
    return self.pipeIterator
  def rebuildObjects(self):
    self.nodesList = []
    self.pipesList = []
    self._createObjects()
    self._createNodePipeRelations()
  def generateResults(self):
    """Creates a 2D matrix that can be consumed by a QTableView object model"""
    resultsMatrix = []
    for pipe in self.pipesList:
      resultsMatrix.append([pipe.getId(),
                            pipe.getAttribute('hoatbocs'),
                            pipe.getAttribute('holeadas'),
                            pipe.getAttribute('hovesztes'),
                            pipe.getAttribute('terfaram'), # 'terfaram' in dm3/h
                            pipe.getAttribute('vissza_atm'),
                            pipe.getAttribute('reynolds'),
                            pipe.getAttribute('cso_surl'),
                            pipe.getAttribute('nyomas_es')])
    return resultsMatrix
  def generatePressureResults(self):
    """Creates a 2D matrix of pressure data that can be used by a QTableView object model"""
    pressureResultsMatrix = []
    path = 0
    for pLoss, chokeLoss, chokeKv in zip(self.pathPressureLoss, self.chokePressureLoss, self.chokeKv):
      pressureResultsMatrix.append([path, pLoss, chokeLoss, chokeKv])
      path += 1
    return pressureResultsMatrix
  def generateFlowGraphResults(self):
    """Creates a list of pipe flow value for each pipe before the tap"""
    flowsList = []
    for path in self.pathMatrix:
      # We extract the flow value from the second item in the path, which is the
      # first pipe after the tap, this is what we need.
      flowsList.append(path[1].getAttribute('terfaram'))
    return flowsList
    
class AnalyzeHeatLoss(object):
  """Carries out heat loss analysis of a pipe network"""
  def __init__(self, NetworkEnvironment):
    super(AnalyzeHeatLoss, self).__init__()
    self.env = NetworkEnvironment
    self.nextNodes = []
  def _calculatePipeHeatloss(self):
    for pipe in self.env.pipesList:
      pipe.calculateHeatloss()
  def analyzeNextNodes(self):
    nextNodeCache = []
    for node in self.nextNodes:
      for pipe in node.inPipes:
          logging.debug('Adding network heatloss coming in from pipe %s to node %s',
                          pipe.getId(), pipe.connectsStartNode.getId())
          if pipe.connectsStartNode.calculateNetworkHeatloss(pipe, False) == True:
            logging.debug('Network heatloss is completely calculated for node %s',
                          pipe.connectsStartNode.getId())
            if pipe.connectsStartNode.getType() != 'MTB':
              logging.debug('The node on the other end of pipe %s is not' \
                            ' a storage tank, will calculate node %s next round',
                            pipe.getId(), pipe.connectsStartNode.getId())
              nextNodeCache.append(pipe.connectsStartNode)
            else:
              self.env.totalNetworkHeatloss = pipe.connectsStartNode.getAttribute('rendsz_hov') # W
              self.env.pumpFlow = self.env.totalNetworkHeatloss / ( self.env.density * self.env.specificHeat * self.env.deltaTheta ) * 3.6e6# dm3/h

    if len(nextNodeCache) > 0:
      self.nextNodes = nextNodeCache
      self.analyzeNextNodes()
      
  def doAnalyze(self):
    self._calculatePipeHeatloss()

    for node in self.env.nodesList:
      if node.getType() == u'Csapoló':
        logging.debug('Checking tap id: %s', node.getId())
        for pipe in node.inPipes:
          logging.debug('Analyzing pipe %s id coming IN to tap', pipe.getId())
          if pipe.connectsStartNode.calculateNetworkHeatloss(pipe, True) == True:
            logging.debug('Network heatloss is completely calculated for node %s',
                            pipe.connectsStartNode.getId())
            self.nextNodes.append(pipe.connectsStartNode)

class AnalyzeFlowRate(object):
  """Calculates the volume flow rate based on remaining network heat
  loss of a branch."""
  def __init__(self, NetworkEnvironment):
    super(AnalyzeFlowRate, self).__init__()
    self.env = NetworkEnvironment
    self.nextNodes = []
  def doAnalyze(self):
    for node in self.env.nodesList:
      if node.getType() == 'MTB':
        startNode = node # The pump
        break
    if len(startNode.outPipes) == 1:
      startPipe = startNode.outPipes[0] # Pipe going out from the pump
      # The flow rate of the first pipe the same as the pump's
      startPipe.setAttribute('terfaram', self.env.pumpFlow)
      self.nextNodes.append(startPipe.connectsEndNode)
    else:
      logging.error('Multiple pipes from pump!')
  def analyzeNextNodes(self):
    nextNodeCache = []
    logging.debug('Starting flow analysis for next node group.')
    for node in self.nextNodes:
      logging.debug('Flow analysis at node id %s', node.getId())
      inPipeFlow = 0
      inPipeHeatloss = 0
      for inPipe in node.inPipes:
        # We calculate the sum of incoming flow
        inPipeFlow += inPipe.getAttribute('terfaram')
        # We calculate the heatloss on incoming pipe(s)
        inPipeHeatloss += inPipe.getAttribute('hovesztes')
      logging.debug('Sum of incoming flow is %s and heatloss is %s.', inPipeFlow, inPipeHeatloss)

      for pipe in node.outPipes:
        logging.debug('Calculating flow at pipe id %s.', pipe.getId())
        if pipe.connectsEndNode.getType() != u'Csapoló':
          # The system heatloss on this branch from this node on
          heatlossTillPipe = pipe.connectsEndNode.getAttribute('rendsz_hov') + pipe.getAttribute('hovesztes')
        else:
          heatlossTillPipe = pipe.getAttribute('hovesztes')
        # Calculating the flow on outgoing branch
        pipeFlow = inPipeFlow * ( heatlossTillPipe / node.getAttribute('rendsz_hov'))
        # Setting result
        logging.debug('Calculated flow for pipe id %s is %s.', pipe.getId(), pipeFlow)
        pipe.setAttribute('terfaram', pipeFlow)
        # We need to check if we reached the pump
        if pipe.connectsEndNode.getType() != u'Csapoló':
          # Adding our next node to analyze
          nextNodeCache.append(pipe.connectsEndNode)
    if len(nextNodeCache) > 0:
      self.nextNodes = nextNodeCache
      self.analyzeNextNodes()

class AnalyzePipeDiameter(object):
  """Calculates the diameter of return flow pipes based on flow rate
  and target flow speed"""
  def __init__(self, NetworkEnvironment):
    super(AnalyzePipeDiameter, self).__init__()
    self.env = NetworkEnvironment
  def doAnalyze(self):
    for pipe in self.env.pipesList:
      logging.debug('Calculating return pipe diameter for pipe id %s.', pipe.getId())
      # Flow pipe calculated flow
      pipeFlow = pipe.getAttribute('terfaram')
      for diameter in self.env.sizes:
        logging.debug('Checking if pipe diameter of %smm is good.', diameter)
        # We need to divide the pipe flow 3.6e6 because it is in dm3/h
        flowSpeed = 4 * (pipeFlow / 3.6e6) / ( pow((diameter / 1000.0), 2) * math.pi )
        logging.debug('Flow speed is %sm/s.', flowSpeed)
        if flowSpeed < self.env.pipeSpeedLimit:
          logging.debug('Flow speed is between 0.2-1.0 m/s we use this diameter.')
          pipe.setAttribute('vissza_atm', diameter)
          pipe.setAttribute('aram_seb', flowSpeed)
          break

class AnalyzePipeDrag(object):
  """Calculates the drag effect of the pipe"""
  def __init__(self, NetworkEnvironment):
    super(AnalyzePipeDrag, self).__init__()
    self.env = NetworkEnvironment
    self.KINEMATICAL_VISCOSITY = 5e-7
    # Lambda zero
    self.DRAG_INITIAL = 0.02
  def calculateReynoldsNumber(self, flowSpeed, diameter):
    return flowSpeed * ( diameter / 1000.0 ) / self.KINEMATICAL_VISCOSITY
  def doAnalyze(self):
    for pipe in self.env.pipesList:
      re = self.calculateReynoldsNumber(
              pipe.getAttribute('aram_seb'), # m/s
              pipe.getAttribute('vissza_atm')) # mm
      pipe.setAttribute('reynolds', re)
      # IF the flow is laminar
      if re <= 2300:
        drag = 64 / re
      # IF the flow is non-laminar
      elif re > 2300:
        drag = self._calcNLDrag(re,
                              self.DRAG_INITIAL,
                              pipe.getAttribute('cso_erdess'),
                              pipe.getAttribute('vissza_atm'))
      pipe.setAttribute('cso_surl', drag)
  def _calcNLDrag(self, re, dragPrev, roughness, diameter):
    # Non-laminar drag calculation
    drag = 1 / pow((-2 * math.log10((2.51 / (re * math.sqrt(dragPrev))) + roughness / (3.71 * diameter) )), 2)
    # IF the difference between the previous and current drag calculation
    # is less than 0.001 we return the calculated drag
    if drag - dragPrev < 0.0001:
      return drag
    # Otherwise we continue the calculation recursively until we reach this goal
    else:
      return self._calcNLDrag(re, drag, roughness, diameter)
class AnalyzePressure(object):
  """Calculates the pressure loss on each circulation path"""
  def __init__(self, NetworkEnvironment):
    super(AnalyzePressure, self).__init__()
    self.env = NetworkEnvironment
  def doAnalyze(self):
    self._pressureLossOnPipe()
    self._createFlowPaths()
    self._pressureLossOnPaths()
    self._calculateReferencePathPressure()
    self._calculatePathChoke()
  def _pressureLossOnPipe(self):
    for pipe in self.env.pipesList:
      # We fetch the data required for the calculation
      Lm = pipe.getAttribute('hossz')
      lambdam = pipe.getAttribute('cso_surl')
      dm = pipe.getAttribute('vissza_atm')
      zetam = pipe.getAttribute('alaki_teny')
      wm = pipe.getAttribute('aram_seb')
      ro = self.env.density
      Vm = pipe.getAttribute('terfaram')
      kvm = pipe.getAttribute('szerelveny')

      deltapm = (Lm * (lambdam / dm) + zetam) * ((pow(wm, 2) * ro) / 2) + pow(Vm / kvm, 2)
      pipe.setAttribute('nyomas_es', deltapm)
  def _pressureLossOnPaths(self):
    self.env.pathPressureLoss = []
    for path in self.env.pathMatrix:
      pressureLoss = 0
      for item in path:
        if type(item) is PipeObject:
          pressureLoss += item.getAttribute('nyomas_es')
      self.env.pathPressureLoss.append(pressureLoss)
  def _createFlowPaths(self):
    """Creates a matrix of flow paths with their respective elements
    ATTENTION: pathMatrix is a mixed set of NodeObjects and PipeObjects!
    """
    self.env.pathMatrix = []
    for node in self.env.nodesList:
      if node.getType() == u'Csapoló':
        if len(self.env.pathMatrix) > 0:
          for idx, pathItem in enumerate(self.env.pathMatrix):
            if pathItem[0].getCoordinates().x() > node.getCoordinates().x():
              spaceIndex = idx
              break
            elif len(self.env.pathMatrix) == idx + 1:
              spaceIndex = idx + 1
        else:
          spaceIndex = 0
        pathCache = []
        pathCache.append(node)
        for pipe in node.inPipes:
          self._recursePath(pipe, pathCache)
        self.env.pathMatrix[spaceIndex:spaceIndex] = [pathCache]
    for idx, path in enumerate(self.env.pathMatrix):
      path[0].setAttribute('ag', idx)
  def _recursePath(self, nextPipe, pathCache):
    """Recurses through a path to add the elements to a list"""
    pathCache.append(nextPipe)
    pathCache.append(nextPipe.connectsStartNode)
    if nextPipe.connectsStartNode.getType() != 'MTB':
      for pipe in nextPipe.connectsStartNode.inPipes:
        self._recursePath(pipe, pathCache)
  def _calculateReferencePathPressure(self):
    self.env.referencePathPressure = max(self.env.pathPressureLoss) + 3000 # Pa
  def _calculatePathChoke(self):
    self.env.chokePressureLoss = []
    self.env.chokeKv = []
    for index, pathLoss in enumerate(self.env.pathPressureLoss):
      chokePrLoss = self.env.referencePathPressure - pathLoss
      self.env.chokePressureLoss.append(chokePrLoss)
      self.env.chokeKv.append(self.env.pathMatrix[index][1].getAttribute('terfaram') / math.sqrt(chokePrLoss))

