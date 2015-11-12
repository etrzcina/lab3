import numpy

#Wczytanie warstwy powiaty do QGIS
path_powiaty = "C:/Users/HP/Documents/Github/lab3/bdo/powiaty.shp"
powiaty = qgis.core.QgsVectorLayer(path_powiaty, "Powiaty", "ogr")
qgis.core.QgsMapLayerRegistry.instance().addMapLayer(powiaty)

#Obliczenie wspolczynnika korelacji pomiedzy populacja powiatow a ich powierzchnia
a = powiaty.getFeatures()
pop = []
pow = []
for i in a:
    pop.append(i.attributes()[4])
    pow.append(i.attributes()[6])
c_pop_pow = numpy.corrcoef(pop,pow)
print "Wspolczynnik korelacji pomiedzy populacja a powierzchnia powiatow:"
print c_pop_pow[0,1]