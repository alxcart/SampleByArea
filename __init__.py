# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Sample by Area
                                 A QGIS plugin
This plugin elaborates the area-oriented sampling plan, 
it is based on the ISO 2859 series of standards. 
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-03-21
        copyright            : (C) 2021 by Alex Santos
        email                : alxcart@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SampleByArea class from file SampleByArea.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .SampleByArea import SampleByArea
    return SampleByArea(iface)
