# -*- coding: utf-8 -*-
import qgis
from PyQt4 import QtGui

def createPipeSymbols(baseLayer):
    # Setting up simple line symbol layer
    simple_line_layer = qgis.core.QgsSimpleLineSymbolLayerV2()
    # Network failure line
    network_fail_line = simple_line_layer.clone()
    network_fail_line.setColor(QtGui.QColor(182, 67, 90))
    # Network OK line
    network_ok_line = simple_line_layer.clone()
    network_ok_line.setColor(QtGui.QColor(43, 176, 7))
    # Network not verified
    network_noverify_line = simple_line_layer.clone()
    network_noverify_line.setColor(QtGui.QColor(197, 185, 16))
    # Rules data
    pipe_rules = (('Hálózat hiba', '"assoc_err" = 1', network_fail_line),
                  ('Hálózat OK', '"assoc_err" = 2', network_ok_line),
                  ('Hálózat nem ellenőrzött', '"assoc_err" = 0', network_noverify_line)
    )
    # Create renderer
    symbol = qgis.core.QgsSymbolV2.defaultSymbol(baseLayer.geometryType())
    renderer = qgis.core.QgsRuleBasedRendererV2(symbol)
    
    root_rule = renderer.rootRule()
    # We add out own rules
    for label, expression, layer in pipe_rules:
        rule = root_rule.children()[0].clone()
        rule.setLabel(label)
        rule.setFilterExpression(expression)
        rule.symbol().changeSymbolLayer(0, layer)
        root_rule.appendChild(rule)

    return renderer


def createNodeSymbols(baseLayer):
    # Setting up marker for pump
    pump_marker_layer = qgis.core.QgsSvgMarkerSymbolLayerV2('./Pump.svg')
    pump_marker_layer.setSize(20)
    pump_marker_layer.setOutlineWidth(1)
    pump_marker_layer.setScaleMethod(qgis.core.QgsSymbolV2.ScaleArea)
    # Setting up simple symbol layer
    simple_marker_layer = qgis.core.QgsSimpleMarkerSymbolLayerV2()
    simple_marker_layer.setScaleMethod(qgis.core.QgsSymbolV2.ScaleArea)
    # Not verified marker
    not_verified_marker = simple_marker_layer.clone()
    not_verified_marker.setColor(QtGui.QColor(5, 76, 152))
    # Good marker
    ok_marker = simple_marker_layer.clone()
    ok_marker.setColor(QtGui.QColor(91, 137, 56))
    # Bad marker
    bad_marker = simple_marker_layer.clone()
    bad_marker.setSize(4)
    bad_marker.setColor(QtGui.QColor(237, 0, 8))
    # Rules data
    node_rules = (('Szivattyu', '"tipus" = \'Szivattyu\'', pump_marker_layer),
                  ('Halozat nem ellenorzott', '"assoc_err" = 0', not_verified_marker),
                  ('Halozat OK', '"assoc_err" = 2', ok_marker),
                  ('Halozat hiba', '"assoc_err" = 1', bad_marker)
    )
    # Create renderer
    symbol = qgis.core.QgsSymbolV2.defaultSymbol(baseLayer.geometryType())
    renderer = qgis.core.QgsRuleBasedRendererV2(symbol)
    
    root_rule = renderer.rootRule()
    # We add out own rules
    for label, expression, layer in node_rules:
        rule = root_rule.children()[0].clone()
        rule.setLabel(label)
        rule.setFilterExpression(expression)
        rule.symbol().changeSymbolLayer(0, layer)
        root_rule.appendChild(rule)

    return renderer


def setupNodeLayer(layerName):
    '''Add all formatting features to the node layer'''
    # Fetch the layer from the project
    nodeLayer = qgis.core.QgsMapLayerRegistry.instance().mapLayersByName(layerName)[0]
    # Set the UI file used to edit layer attributes
    nodeLayer.setEditForm('./elemek_form.ui')
    # Setup the renderer with symbols added
    nodeLayer.setRendererV2(createNodeSymbols(nodeLayer))
    # Node labels
    setNodeLabeling(nodeLayer)


def setupPipeLayer(layerName):
    '''Add all formatting features to the pipe layer'''
    # Fetch the layer from the project
    pipeLayer = qgis.core.QgsMapLayerRegistry.instance().mapLayersByName(layerName)[0]
    # Set the UI file used to edit layer attributes
    pipeLayer.setEditForm('./szakaszok_form.ui')
    # Setup the renderer with symbols added
    pipeLayer.setRendererV2(createPipeSymbols(pipeLayer))
    # Pipe labels
    setPipeLabeling(pipeLayer)


def setNodeLabeling(layer):
    '''Add labeling to node layer'''
    layer.setCustomProperty('labeling', 'pal')
    layer.setCustomProperty('labeling/enabled', True)
    layer.setCustomProperty('labeling/fieldName', 'CASE WHEN "ag" IS NOT NULL THEN \'F\' || ag '
                                                  '|| \'\n\' || tipus || \' (\' || $id || \')\''
                                                  'ELSE tipus || \' (\' || $id || \')\' END')
    layer.setCustomProperty('labeling/fontSize', 13)
    layer.setCustomProperty('labeling/fontFamily', 'Helvetica')


def setPipeLabeling(layer):
    '''Add labeling to pipe layer'''
    layer.setCustomProperty('labeling', 'pal')
    layer.setCustomProperty('labeling/enabled', True)
    layer.setCustomProperty('labeling/fieldName', '\'(\' || $id || \')\' || \'\n\' |'
                                                  '|\'Ø \'||atmero_cso || \'mm\'|| \'/\' '
                                                  '|| vissza_atm  || \'mm\' || \'\n\' || '
                                                  '\'Vm = \' || terfaram || \' dm3/h\'')
    layer.setCustomProperty('labeling/addDirectionSymbol', True)
    layer.setCustomProperty('labeling/fontSize', 13)
    layer.setCustomProperty('labeling/fontFamily', 'Helvetica')