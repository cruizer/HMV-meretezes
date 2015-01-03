# This is general boilerplate code that QGIS can use to start the plugin
def classFactory(iface):
  from hmv_meretezes_plugin import HmvPlugin
  # We instantiate our plugin object and pass the QGIS interface object
  return HmvPlugin(iface)