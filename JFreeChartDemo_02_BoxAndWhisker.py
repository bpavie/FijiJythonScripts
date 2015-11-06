import os

from java.awt import Color, Dimension, Rectangle
from java.io import File, FileOutputStream, OutputStreamWriter
from java.lang import Math, Double
from java.util import ArrayList, List
from javax.swing import JPanel

from org.jfree.chart import ChartFactory, ChartPanel, JFreeChart
from org.jfree.chart.axis import NumberAxis
from org.jfree.chart.plot import CategoryPlot
from org.jfree.data.statistics import BoxAndWhiskerCategoryDataset, DefaultBoxAndWhiskerCategoryDataset
from org.jfree.ui import ApplicationFrame, RefineryUtilities

from ij import ImagePlus, IJ

from org.apache.batik.dom import GenericDOMImplementation
from org.apache.batik.svggen import SVGGraphics2D

#Fill a arraylist of random values constrain on some limits
def createValueList(d, d1, i):
  arraylist = ArrayList()
  for j in range(0, i):#Generate 20 values for each serie
    d2 = d + Math.random() * (d1 - d)
    arraylist.add(Double(d2))
  return arraylist

#Create te default dataset for the BoxAndWhisker
def createDataSet():
  dataset = DefaultBoxAndWhiskerCategoryDataset()
  for i in range(0, 3):#Generate 3 series for each category
    for j in range(0,5):#Generate 5 Categories
      list = createValueList(0.0, 20.0, 20)
      dataset.add(list, "Series " + str(i), "Category " + str(j))#Add a list of value for 1 rowKey (Serie), 1 columnKey (Category)
  return dataset

boxandwhiskercategorydataset=createDataSet()
jfreechart = ChartFactory.createBoxAndWhiskerChart('Box and Whisker Chart Demo 1', 'Category', 'Value', boxandwhiskercategorydataset, True)
categoryplot = jfreechart.getPlot()
jfreechart.setBackgroundPaint(Color.white)
categoryplot.setBackgroundPaint(Color.lightGray)
categoryplot.setDomainGridlinePaint(Color.white)
categoryplot.setDomainGridlinesVisible(True)
categoryplot.setRangeGridlinePaint(Color.white)
numberaxis = categoryplot.getRangeAxis()
numberaxis.setStandardTickUnits(NumberAxis.createIntegerTickUnits())

#Plot the Chart into an ImagePlus
bi = jfreechart.createBufferedImage(600, 400)
imp = ImagePlus('Chart Test', bi)
imp.show()


####################
# Create SVG image #
####################

#Could be open using inkscape, see https://inkscape.org
#1- Get a DOMImplementation and create an XML document
domImpl = GenericDOMImplementation.getDOMImplementation()
document = domImpl.createDocument(None, 'svg', None)
#2-Create an instance of the SVG Generator
svgGenerator = SVGGraphics2D(document)
#3-Draw the chart in the SVG generator
bounds = Rectangle(600, 400)
jfreechart.draw(svgGenerator, bounds)
#4-Select a folder to save the SVG
dir = IJ.getDirectory('Where should the svg file be saved?')
#5-Write the SVG file
svgFile = File(dir + 'test.svg')
outputStream = FileOutputStream(svgFile)
out = OutputStreamWriter(outputStream, 'UTF-8')
svgGenerator.stream(out, True)
outputStream.flush()
outputStream.close()


