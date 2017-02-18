# -*- coding: utf-8 -*-
import qgis

def createPipeSymbols():
    # Setting up marker for pump
    pump_marker_layer = QgsSvgMarkerSymbolLayerV2('./Pump.svg')
    pump_marker_layer.setSize(20)
    pump_marker_layer.setOutlineWidth(1)
    pump_marker_layer.setScaleMethod(QgsSymbolV2.ScaleArea)
    # Setting up simple symbol layer
    simple_marker_layer = QgsSimpleMarkerSymbolLayerV2()
    simple_marker_layer.setScaleMethod(QgsSymbolV2.ScaleArea)
    # Not verified marker
    not_verified_marker = simple_marker_layer.clone()
    not_verified_marker.setColor(QColor(5,76,152))
    # Good marker
    ok_marker = simple_marker_layer.clone()
    ok_marker.setColor(QColor(91,137,56))
    # Bad marker
    bad_marker = simple_marker_layer.clone()
    bad_marker.setSize(4)
    bad_marker.setColor(QColor(237,0,8))
    # Rules data
    pipe_rules = (('Szivattyu', '"tipus" = \'Szivattyu\'', pump_marker_layer),
                  ('Halozat nem ellenorzott', '"assoc_err" = 0', not_verified_marker),
                  ('Halozat OK', '"assoc_err" = 2', ok_marker),
                  ('Halozat hiba', '"assoc_err" = 1', bad_marker),
    )
    # Create renderer
    symbol = QgsSymbolV2.defaultSymbol(layer.geometryType())
    renderer = QgsRuleBasedRendererV2(symbol)
    
    root_rule = renderer.rootRule()
    # We add out own rules
    for label, expression, layer in root_rule:
        rule = root_rule.children()[0].clone()
        rule.setLabel(label)
        rule.setFilterExpression(expression)
        rule.symbol().changeSymbolLayer(0, layer)
def setPipeRenderer(iface, layerName, renderer):
    pipeLayer = QgsMapLayerRegistry.instance().mapLayersByName(layerName)
    pipeLayer.setRendererV2(createPipeSymbols())
