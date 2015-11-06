from org.jfree.chart import ChartFactory
from org.jfree.chart.plot import PlotOrientation
from org.jfree.chart.axis import NumberAxis
from org.jfree.data.statistics import DefaultStatisticalCategoryDataset
#from org.jfree.chart.encoders import *
from org.jfree.chart.renderer.category import StatisticalBarRenderer

from java.awt import Color
from java.awt.geom import *
from java.io import *

from org.jfree.ui import RectangleInsets
from org.jfree.data.category import *
from org.jfree.data.statistics import *


#from org.apache.batik.dom import *
#from org.apache.batik.svggen import *

from ij import ImagePlus
 
dataset = DefaultStatisticalCategoryDataset()
 
# dataset.add(Mean, StdDev, "Series", "Condition")
dataset.add(15.0, 2.4, "Row 1", "Column 1")
dataset.add(15.0, 4.4, "Row 1", "Column 2")
dataset.add(13.0, 2.1, "Row 1", "Column 3")
dataset.add(7.0, 1.3, "Row 1", "Column 4")
dataset.add(2.0, 2.4, "Row 2", "Column 1")
dataset.add(18.0, 4.4, "Row 2", "Column 2")
dataset.add(28.0, 2.1, "Row 2", "Column 3")
dataset.add(17.0, 1.3, "Row 2", "Column 4")
 
chart = ChartFactory.createLineChart(None,'Treatment','Measurement',dataset,PlotOrientation.VERTICAL,False,True,False)
# set the background color for the chart...
chart.setBackgroundPaint(Color.white)
 
plot = chart.getPlot()
plot.setBackgroundPaint(Color.white)
plot.setRangeGridlinesVisible(False)
plot.setAxisOffset(RectangleInsets.ZERO_INSETS)
 
#customise the range axis...
rangeAxis = plot.getRangeAxis()
rangeAxis.setStandardTickUnits(NumberAxis.createIntegerTickUnits())
rangeAxis.setAutoRangeIncludesZero(True)
rangeAxis.setRange(0, 40)
 
#customise the renderer...
renderer = StatisticalBarRenderer();
renderer.setErrorIndicatorPaint(Color.black);
renderer.setSeriesOutlinePaint(0,Color.black);
renderer.setSeriesOutlinePaint(1,Color.black);
renderer.setSeriesPaint(0,Color.black);
renderer.setSeriesPaint(1,Color.white);
renderer.setItemMargin(0.0);
plot.setRenderer(0,renderer);
 
renderer.setDrawBarOutline(True);
 
bi = chart.createBufferedImage(600, 400);
 
imp = ImagePlus("Chart Test", bi);
imp.show();
