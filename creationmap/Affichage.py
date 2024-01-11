# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CreationMap
                                 A QGIS plugin
 Density population map creation by region
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2023-12-18
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Althéa Feuillet
        email                : althea.feuillet@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtGui import QColor
from qgis.PyQt.QtWidgets import QMessageBox
from qgis.core import (QgsCoordinateTransformContext, QgsVectorFileWriter, QgsProject, QgsVectorFileWriter,
                       QgsCoordinateReferenceSystem, QgsGraduatedSymbolRenderer, QgsRendererRange,
                       QgsRendererRange, QgsGraduatedSymbolRenderer, QgsGraduatedSymbolRenderer, QgsFillSymbol)

class Affichage:
    @staticmethod
    def applyGraduatedSymbology(layer):
        """
        Applique une symbologie graduée à la couche en fonction des plages de densité.

        :param layer: La couche à laquelle appliquer la symbologie graduée.
        :type layer: QgsVectorLayer

        Crée des plages de densité prédéfinies avec des couleurs spécifiques et applique une symbologie graduée à la couche en fonction de ces plages.
        """
        myRangeList = []

        ranges = []
        ranges.append((0, 100, "Densité Faible", QColor('#AAA039')))
        ranges.append((100, 200, "Densité Moyenne", QColor('#AA7B39')))
        ranges.append((200, 500, "Densité forte", QColor('#AA3F39')))

        for myMin, myMax, myLabel, myColor in ranges:
            mySymbol = QgsFillSymbol.createSimple({'color': myColor, 'style': 'solid'})
            myRange = QgsRendererRange(myMin, myMax, mySymbol, myLabel)
            myRangeList.append(myRange)

        myRenderer = QgsGraduatedSymbolRenderer('', myRangeList)
        myRenderer.setMode(QgsGraduatedSymbolRenderer.Quantile)
        myRenderer.setClassAttribute("densité")

        layer.setRenderer(myRenderer)

    @staticmethod
    def saveLayer(layer, name, path_save):
        """
        Enregistre la couche sous forme de fichier shapefile.

        :param layer: La couche à enregistrer.
        :type layer: QgsVectorLayer

        :param name: Le nom de la couche.
        :type name: str

        :param path_save: Le chemin de sauvegarde pour le fichier shapefile.
        :type path_save: str

        Ajoute la couche au projet QGIS, lui donne un nom, puis écrit la couche au format shapefile en utilisant les options spécifiées.
        """
        try:
            QgsProject.instance().addMapLayer(layer)
            layer.setName(name)

            options = QgsVectorFileWriter.SaveVectorOptions()
            options.driverName = 'ESRI Shapefile'
            options.fileEncoding = 'UTF-8'
            QgsVectorFileWriter.writeAsVectorFormatV3(layer, path_save, QgsCoordinateTransformContext(), options)

        except Exception as e:
            QMessageBox.critical(None, 'Erreur', f'Erreur lors de l\'enregistrement de la couche : {str(e)}')

    @staticmethod
    def changeCRS(layer):
        """
        Change la projection de la couche à EPSG:3857.

        :param layer: La couche dont la projection doit être modifiée.
        :type layer: QgsVectorLayer

        Modifie la projection de la couche à EPSG:3857 et actualise son affichage.
        """
        layer.setCrs(QgsCoordinateReferenceSystem('EPSG:3857'))
        layer.triggerRepaint()