# -*- coding: utf-8 -*-
from PyQt4.QtCore import QObject, QFileInfo, QLocale

class Translator:
    def __init__(self, config, comboBox):
        self.config = config
        self.comboBox = comboBox
        self.translator = None
        self.defaultLanguage = "English"
        self.translationFilePaths = {}

    def loadConfig(self, translationsPath):
        _loadDefaultFromConfig(self.config)
        _scanTranslationFiles(translationsPath)
        
    def activate(self):
        _populateLanguageCombo()

    def bindConnection(self):
        QObject.connect(self.comboBox, SIGNAL("activated(QString)"), self._updateLanguage)
        
    def _updateLanguage(self, language):
        _setTranslator(self.translationFilePaths[language])
        _saveConfig(language)
        
    def _loadDefaultFromConfig(self):
        if config.has_option("hmv", "language"):
            self.defaultLanguage = self.config.get("hmv", "language")
        else:
            self.defaultLanguage = QLocale.languageToString(QLocale.system().language())
            
    def _scanTranslationFiles(self, translationsPath):
        for f in os.listdir(translationsPath):
            if fnmatch.fnmatch(f, "*.qm"):
                os.path.splitext(f)[0]
                locale = f[f.find("_") + 1:]
                language = QLocale.languageToString(QLocale(locale).language())
                self.translationFilePaths[language] = QFileInfo(f).path()

    def _populateLanguageCombo(self):
        self.comboBox.addItems(self.translationFilePaths.keys)
        self.comboBox.setCurrentIndex(self.comboBox.find(self.defaultLanguage))

    def _setTranslator(self, translationPath):
        if QFileInfo(self.localePath).exists():
            self.translator = QTranslator()
            self.translator.load(self.translationPath)
        if qVersion() > '4.3.3':
            QCoreApplication.installTranslator(self.translator)
            
    def _saveConfig(self, language):
        self.config.set("hmv", "language", language)
