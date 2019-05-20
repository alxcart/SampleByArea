#CONSTANTS
from qgis.core import *
# Plano de amostragem
#Nivel_de_Inspecao = self.dlg.comboBoxLevel.currentIndex()
dicSampleLength={2:[2,2,3],9:[2,3,5],16:[3,5,8],26:[5,8,13],51:[5,13,20],91:[8,20,32],151:[13,32,50],281:[20,50,80],501:[32,80,125],1201:[50,125,200],3201:[80,200,315],10001:[125,315,500],35001:[200,500,800],150001:[315,800,1250],500001:[500,1250,2000]}



# Map Units
Meters                  = 0
Feet                    = 1
Degrees                 = 2
UnknownUnit             = 3
DecimalDegrees          = 4
DegreesMinutesSeconds   = 5
DegreesDecimalMinutes   = 6
NauticalMiles           = 7


uMeters                 = QgsUnitTypes.DistanceMeters 	        #Meters.
uKilometers             = QgsUnitTypes.DistanceKilometers 	    #Kilometers.
uImperialFeet           = QgsUnitTypes.DistanceFeet 	        #Imperial feet.
uNauticalMiles          = QgsUnitTypes.DistanceNauticalMiles 	#Nautical miles.
uImperialYards          = QgsUnitTypes.DistanceYards 	        #Imperial yards.
uTerrestrialMiles       = QgsUnitTypes.DistanceMiles 	        #Terrestrial miles.
uDegrees                = QgsUnitTypes.DistanceDegrees 	        #Degrees, for planar geographic CRS distance measurements.
uCentimeters            = QgsUnitTypes.DistanceCentimeters 	    #Centimeters.
uMillimeters            = QgsUnitTypes.DistanceMillimeters 	    #Millimeters.
uUnknownDistanceUnit    = QgsUnitTypes.DistanceUnknownUnit 	    #Unknown distance unit.

#Convert km to
#Meter
m = 1000

#Feet
ft = 3280.8398950131

#Degrees
dg = 1/111.320

#NauticalMiles
nm = 0.54

#UnknownUnit
uk = 1