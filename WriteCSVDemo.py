import os
import re #Used to manipulate Regular Expression
from ij import IJ, ImagePlus, ImageStack
from ij.process import ImageProcessor, ByteProcessor, ColorProcessor
from ij.gui import Roi
from trainableSegmentation import WekaSegmentation
from ij.io import DirectoryChooser
from ij.measure import ResultsTable
from ij.plugin.frame import RoiManager
from ij.plugin.filter import ParticleAnalyzer
from ij.plugin import HyperStackConverter
from ij.measure import Measurements
from java.lang import Double
from ij.plugin.filter import ParticleAnalyzer as PA
from java.lang import Double
from java.io import FileWriter
from java.lang import String
from jarray import array as jarr
from util.opencsv import CSVWriter

writer = CSVWriter(FileWriter('C:\\test.csv'), ',')
row1 = ['Tumor Area', 'Total Area', 'Tumor Area Percentage','Blabla']
row2 = ['Tumor Area', 'Total Area', 'Tumor Area Percentage']
row3 = ['Tumor Area', 'Total Area', 'Tumor Area Percentage','Bliblib']
jrow1 = jarr(row1, String)
writer.writeNext(jrow1)
jrow2 = jarr(row2, String)
writer.writeNext(jrow2)
jrow3 = jarr(row3, String)
writer.writeNext(jrow3)
writer.close()
