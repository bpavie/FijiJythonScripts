import os

from ij import ImagePlus, IJ

from java.awt import Color, Rectangle
from java.io import File, FileOutputStream, OutputStreamWriter

from org.jfree.chart import ChartFactory
from org.jfree.chart.axis import NumberAxis
from org.jfree.chart.plot import PlotOrientation
from org.jfree.chart.renderer.category import StandardBarPainter, BarRenderer
from org.jfree.data.category import DefaultCategoryDataset
from org.jfree.chart.labels import StandardCategoryItemLabelGenerator, ItemLabelPosition, ItemLabelAnchor
from org.jfree.ui import RectangleInsets, TextAnchor

from org.apache.batik.dom import GenericDOMImplementation
from org.apache.batik.svggen import SVGGraphics2D


#Define the dataset
dataset = DefaultCategoryDataset()
dataset.addValue(25, 'S1', 'Slide XXX')#Value, serie name, X label
dataset.addValue(40, 'S1', 'Slide YYY')
dataset.addValue(60, 'S1', 'Slide ZZZ')

##############
# Plot Chart #
##############
#chart = ChartFactory.createLineChart(None,'Slide','% Brown Area',dataset,PlotOrientation.VERTICAL,False,True,False)
chart = ChartFactory.createBarChart("% Brown Area per Slide", 'Slide', '% Brown Area', dataset, PlotOrientation.VERTICAL, False,True,False)
# set the background color for the chart...
chart.setBackgroundPaint(Color.WHITE)

plot = chart.getPlot()
plot.setBackgroundPaint(Color.WHITE)
plot.setRangeGridlinesVisible(False)
plot.setAxisOffset(RectangleInsets.ZERO_INSETS)

#customise the range axis...
rangeAxis = plot.getRangeAxis()
rangeAxis.setStandardTickUnits(NumberAxis.createIntegerTickUnits())
rangeAxis.setAutoRangeIncludesZero(True)
#Set the Min Max value of the y axis
rangeAxis.setRange(0, 100)
#Create a custom BarRenderer
barRenderer = BarRenderer()
#Add a label in the middle of the histogram bar showing the % value
barRenderer.setBaseItemLabelGenerator(StandardCategoryItemLabelGenerator())
barRenderer.setBaseItemLabelsVisible(True)
#For parameters
#See http://www.jfree.org/jfreechart/api/javadoc/org/jfree/chart/labels/ItemLabelAnchor.html
#See http://www.jfree.org/jcommon/api/org/jfree/ui/TextAnchor.html and 
itemlabelposition = ItemLabelPosition(ItemLabelAnchor.OUTSIDE12, TextAnchor.BOTTOM_CENTER, TextAnchor.BOTTOM_CENTER, 0.00)
barRenderer.setBasePositiveItemLabelPosition(itemlabelposition)
#Customize the bar's color so they will be gray with a black outline and no shadow
barRenderer.setBarPainter(StandardBarPainter())#Use StandardBarPainter to avoid the color gradient inside the bar
barRenderer.setSeriesOutlinePaint(0, Color.BLACK)
barRenderer.setSeriesPaint(0, Color.GRAY)
barRenderer.setItemMargin(0.0)
barRenderer.setShadowVisible(False)
#Apply the renderer for the plot
plot.setRenderer(0,barRenderer)
barRenderer.setDrawBarOutline(True)

bi = chart.createBufferedImage(600, 400)

imp = ImagePlus('My Plot Title', bi)
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
chart.draw(svgGenerator, bounds)
#4-Select a folder to save the SVG
dir = IJ.getDirectory('Where should the svg file be saved?')
#5-Write the SVG file
svgFile = File(dir + 'test.svg')
outputStream = FileOutputStream(svgFile)
out = OutputStreamWriter(outputStream, 'UTF-8')
svgGenerator.stream(out, True)
outputStream.flush()
outputStream.close()

print 'Saved in %s' % (os.path.join(dir,'test.svg'))
