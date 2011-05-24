"""
This file is part of openexp.

openexp is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

openexp is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with openexp.  If not, see <http://www.gnu.org/licenses/>.
"""

import pygame
import math
import openexp._canvas.legacy
import openexp.exceptions
from psychopy import core, visual
from PIL import Image

class psycho(openexp._canvas.legacy.legacy):

	"""
	This is a canvas backend which uses PsychoPy (with Pyglet).
	"""
	
	def __init__(self, experiment, bgcolor = "black", fgcolor = "white"):
		
		"""
		Initializes the canvas. The specified colors should be used as a 
		default for subsequent drawing operations.
		
		Arguments:
		experiment -- an instance of libopensesame.experiment.experiment
		
		Keyword arguments:
		bgcolor -- a human-readable background color (default = "black")
		fgcolor -- a human-readable foreground color (default = "white")
		"""
		
		self.experiment = experiment
		self.min_penwidth = 1
		self.set_fgcolor(fgcolor)
		self.set_bgcolor(bgcolor)
		self.set_penwidth(1)
		self.clear()
				
	def color(self, color):
	
		"""
		Transforms a "human readable" color into the format that
		is used by the back-end (e.g., a PyGame color).
		
		Arguments:
		color -- A color in one the following formats (by example):
			255, 255, 255 (rgb)
			255, 255, 255, 255 (rgba)
			#f57900 (case-insensitive html)
			100 (integer intensity value 0 .. 255, for gray-scale)
			0.1 (float intensity value 0 .. 1.0, for gray-scale)
		
		Returns:
		A color in the back-end format
		"""
	
		return color
		
	def flip(self, x = True, y = False):
		
		"""
		Flips the canvas along the x- and/ or y-axis. Note: This does not refresh the display,
		like e.g., pygame.display.flip(), which is handled by show().
		
		Keyword arguments:
		x -- A boolean indicating whether the canvas should be flipped horizontally (default = True)
		y -- A boolean indicating whether the canvas should be flipped vertically (default = False)
		"""
		
		# TODO
		raise openexp.exceptions.canvas_error("openexp._canvas.psycho.flip(): not implemented!")		
		
	def copy(self, canvas):
	
		"""
		Turn the current canvas into a copy of the passed canvas.
		
		Arguments:
		canvas -- The canvas to copy.
		"""
		
		self.stim_list = canvas.stim_list
		self.bgcolor = canvas.bgcolor
		self.fgcolor = canvas.fgcolor
		self.penwidth = canvas.penwidth
		
	def xcenter(self):
		
		"""
		Returns:
		The center X coordinate in pixels.
		"""
		
		return self.experiment.resolution[0] / 2
	
	def ycenter(self):
		
		"""
		Returns:
		The center Y coordinate in pixels.
		"""
		
		return self.experiment.resolution[1] / 2	
		
	def show(self):
		
		"""
		Puts the canvas onto the screen.
		
		Returns:
		A timestamp containing the time at which the canvas actually appeared
		on the screen (or a best guess).
		"""
		
		for stim in self.stim_list:
			stim.draw()
		self.experiment.window.flip(clearBuffer = True)
		return 1000.0 * self.experiment.clock.getTime()
		
	def clear(self, color = None):
		
		"""
		Clears the canvas with the current background color.
		
		Keyword arguments:
		color -- A custom background color to be used. This does not affect the
				 default background color as set by set_bgcolor().
				 (Default = None)
		"""
		
		self.stim_list = []
		if color != None:
			color = self.color(color)
		else:
			color = self.bgcolor
		# The background is simply a rectangle, because of the awkward double flip required by set_color()			
		self.rect(0, 0, self.experiment.width, self.experiment.height, color = color, fill = True)
		
	def set_penwidth(self, penwidth):
		
		"""
		Sets the pen width for subsequent drawing operations.
		
		Arguments:
		penwidth -- A pen width in pixels
		"""
		
		self.penwidth = max(self.min_penwidth, penwidth)
		
	def set_fgcolor(self, color):
		
		"""
		Sets the foreground color for subsequent drawing operations.
		
		Arguments:
		color -- A human readable color
		"""
		
		self.fgcolor = color
		
	def set_bgcolor(self, color):
		
		"""
		Sets the background color for subsequent drawing operations.
		
		Arguments:
		color -- A human readable color
		"""

		self.bgcolor = color
		
	def set_font(self, style, size):
	
		"""
		Sets the font for subsequent drawing operations.
		
		Arguments:
		style -- A font located in the resources folder (without the .ttf extension)
		size -- A font size in pixels		
		"""
		
		self.font_style = style
		self.font_size = size
		
	def fixdot(self, x = None, y = None, color = None):
		
		"""
		Draws a standard fixation dot, which is a big circle (r = 8px) with the
		foreground color and a smaller circle (r = 2px) of the background color.
		
		Keyword arguments:
		x -- The center X coordinate. None = center (default = None)
		y -- The center Y coordinate. None = center (default = None)
		color -- A custom human readable foreground color. This does not affect the
				 default foreground color as set by set_fgcolor(). (Default = None)
		"""
		
		if x == None:
			x = self.xcenter()
		if y == None:
			y = self.ycenter()
		
		self.ellipse(x-8, y-8, 16, 16, fill = True, color = color)
		self.ellipse(x-2, y-2, 4, 4, fill = True, color = self.bgcolor)
		
	def circle(self, x, y, r, fill = False, color = None):
		
		"""
		Draws a circle.
		
		Arguments:
		x -- The center X coordinate
		y -- The center Y coordinate
		r -- The radius
		
		Keyword arguments:
		fill -- A boolean indicating whether the circle is outlined (False) or filled (True)
		color -- A custom human readable foreground color. This does not affect the
				 default foreground color as set by set_fgcolor(). (Default = None)
		"""
						
		self.ellipse(x-r, y-r, 2*r, 2*r, fill = fill, color = color)

	def line(self, sx, sy, ex, ey, color = None):
		
		"""
		Draws a line. Should accept parameters where sx > ex or sy > ey as well.
		
		Arguments:
		sx -- The left coordinate
		sy -- The top coordinate
		ex -- The right coordinate
		ey -- The bottom coordinate
		
		Keyword arguments:
		color -- A custom human readable foreground color. This does not affect the
				 default foreground color as set by set_fgcolor(). (Default = None)		
		"""
		
		if color == None:
			color = self.fgcolor
		self.shapestim( [[sx, sy], [ex, ey]], color = color)
		
	def arrow(self, sx, sy, ex, ey, arrow_size = 5, color = None):
		
		"""
		Draws an arrow. An arrow is a line, with an arrowhead at (ex, ey). The angle between
		the arrowhead lines and the arrow line is 45 degrees.
		
		Arguments:
		sx -- The left coordinate
		sy -- The top coordinate
		ex -- The right coordinate
		ey -- The bottom coordinate
		
		Keyword arguments:
		arrow_size -- The length of the arrowhead lines (default = 5)
		color -- A custom human readable foreground color. This does not affect the
				 default foreground color as set by set_fgcolor(). (Default = None)		
		"""
		
		if color != None:
			color = self.color(color)
		else:
			color = self.fgcolor		
		
		self.line(sx, sy, ex, ey, color = color)
		a = math.atan2(ey - sy, ex - sx)		
		_sx = ex + arrow_size * math.cos(a + math.radians(135))
		_sy = ey + arrow_size * math.sin(a + math.radians(135))
		self.line(_sx, _sy, ex, ey, color = color)		
		_sx = ex + arrow_size * math.cos(a + math.radians(225))
		_sy = ey + arrow_size * math.sin(a + math.radians(225))
		self.line(_sx, _sy, ex, ey, color = color)		
		
	def rect(self, x, y, w, h, fill = False, color = None):
		
		"""
		Draws a rectangle. Should accept parameters where w < 0 or h < 0 as well.
		
		Arguments:
		x -- The left X coordinate.
		y -- The top Y coordinate.
		w -- The width.
		h -- The height.
				
		Keyword arguments:
		fill -- A boolean indicating whether the rectangle is outlined (False) or filled (True)
		color -- A custom human readable foreground color. This does not affect the
				 default foreground color as set by set_fgcolor(). (Default = None)		
		"""
		
		if color == None:
			color = self.fgcolor		
		else:
			color = self.color(color)
			
		if not fill:			
			self.shapestim( [[x, y], [x+w, y], [x+w, y+h], [x, y+h]], color, close = True)
		else:
			pos = x + w/2 - self.xcenter(), self.ycenter() - y - h/2
			stim = visual.PatchStim(win = self.experiment.window, pos = pos, size = [w, h], color = color, tex = None, interpolate = False)
			self.stim_list.append(stim)
			
	def ellipse(self, x, y, w, h, fill = False, color = None):
		
		"""
		Draws an ellipse. Should accept parameters where w < 0 or h < 0 as well.
		
		Arguments:
		x -- The left X coordinate.
		y -- The top Y coordinate.
		w -- The width.
		h -- The height.
				
		Keyword arguments:
		fill -- A boolean indicating whether the ellipse is outlined (False) or filled (True)
		color -- A custom human readable foreground color. This does not affect the
				 default foreground color as set by set_fgcolor(). (Default = None)		
		"""
		
		if color != None:
			color = self.color(color)
		else:
			color = self.fgcolor
			
		pos = x - self.xcenter() + w/2, self.ycenter() - y - h/2

		stim = visual.PatchStim(win = self.experiment.window, mask = "circle", pos = pos, size = [w, h], color = color, tex = None, interpolate = True)
		self.stim_list.append(stim)
		
		if not fill:
			stim = visual.PatchStim(win = self.experiment.window, mask = "circle", pos = pos, size = [w-2*self.penwidth, h-2*self.penwidth], color = self.bgcolor, tex = None, interpolate = True)
			self.stim_list.append(stim)			
			
	def text_size(self, text):
	
		"""
		Determines the size of a text string in pixels.
		
		Arguments:
		text -- The text string
		
		Returns:
		A (width, height) tuple containing the dimensions of the text string
		"""
		
		# TODO
		raise openexp.exceptions.canvas_error("openexp._canvas.psycho.text_size(): not implemented!")
		
	def text(self, text, center = True, x = None, y = None, color = None):
		
		"""
		Draws text.
		
		Arguments:
		text -- The text string
		
		Keyword arguments:
		center -- A boolean indicating whether the coordinates reflect the center (True)
				  or top-left (default = True)
		x -- The X coordinate. None = center. (default = None)
		y -- The Y coordinate. None = center. (default = None)
		color -- A custom human readable foreground color. This does not affect the
				 default foreground color as set by set_fdcolor(). (Default = None)		
		"""
		
		if center:
			halign = "center"
			valign = "center"
		else:
			halign = "left"
			valign = "top"
			
		if color == None:
			color = self.fgcolor
		else:
			color = self.color(color)
			
		pos = x - self.xcenter(), self.ycenter() - y		
		stim = visual.TextStim(win = self.experiment.window, text = text, alignHoriz = halign, alignVert = valign, pos = pos, color = color)
		self.stim_list.append(stim)
		
	def textline(self, text, line, color = None):
		
		"""
		A convenience function that draws a line of text based on a 
		line number. The text strings are centered on the X-axis and
		vertically spaced with 1.5 the line height as determined by
		text_size().
		
		Arguments:
		text -- The text string
		line -- A line number, where 0 is the center and > 0 is below the center.
		color -- A custom human readable foreground color. This does not affect the
				 default foreground color as set by set_fdcolor(). (Default = None)		
		"""
		
		# TODO
		raise openexp.exceptions.canvas_error("openexp._canvas.psycho.textline(): not implemented!")
		
	def image(self, fname, center = True, x = None, y = None, scale = None):
		
		"""
		Draws an image from file. This function does not look in the file
		pool, but takes an absolute path.
		
		Arguments:
		fname -- The path of the file
		
		Keyword arguments:
		center -- A boolean indicating whether the given coordinates reflect the
				  center (True) or the top-left (False) of the image. (default = True)
		x -- The X coordinate. None = center. (default = None)
		y -- The Y coordinate. None = center. (default = None)
		scale -- The scaling factor of the image. 1.0 or None = no scaling, 2.0 = twice as large, etc. (default = None)
		"""
		
		im = Image.open(fname)
				
		w, h = im.size				
		if scale != None:
			im = im.resize( (w * scale, h * scale), Image.ANTIALIAS)		
		w, h = im.size
		
		# Calculate the position			
		if x == None:
			x = self.xcenter()
		if y == None:
			y = self.ycenter()			
		if not center:
			x -= w/2
			y -= h/2			
		pos = x - self.xcenter(), self.ycenter() - y
				
		stim = visual.SimpleImageStim(win = self.experiment.window, image = im, pos = pos)
		self.stim_list.append(stim)
					
	def gabor(self, x, y, orient, freq, env = "gaussian", size = 96, stdev = 12, phase = 0, col1 = "white", col2 = "black", bgmode = "avg"):
	
		"""
		Draws a Gabor patch. This function is derived from the online Gabor patch generator
		<http://www.cogsci.nl/software/online-gabor-patch-generator>	
		
		Arguments:
		x -- The center X coordinate
		y -- The center Y coordinate
		orient -- Orientation in degrees [0 .. 360]
		freq -- Frequency in cycles/px of the sinusoid
		
		Keyword arguments:	
		env -- Any of the following: "gaussian", "linear", "circular", "rectangle" (default = "gaussian")
		size -- Size in pixels (default = 96)
		stdev -- Standard deviation in pixels of the gaussian. Only applicable if env = "gaussian". (default = 12)
		phase -- Phase of the sinusoid [0.0 .. 1.0] (default = 0)
		col1 -- Human readable color for the tops (default = "white")
		col2 -- Human readable color for the troughs (default = "black")
		bgmode -- Specifies whether the background is the average of col1 and col2 (bgmode = "avg", a typical Gabor patch)
				  or equal to col2 ("col2"), useful for blending into the background. (default = "avg")
		"""	
	
		pos = x - self.xcenter(), self.ycenter() - y		
		surface = openexp._canvas.legacy._gabor(orient, freq, env, size, stdev, phase, col1, col2, bgmode)
		string = pygame.image.tostring(surface, "RGB")
		pil_img = Image.fromstring("RGB", (surface.get_width(), surface.get_height()), string)
		stim = visual.SimpleImageStim(win = self.experiment.window, image = pil_img, pos = pos)
		self.stim_list.append(stim)
		
	def noise_patch(self, x, y, env = "gaussian", size = 96, stdev = 12, col1 = "white", col2 = "black", bgmode = "avg"):
	
		"""
		Draws a patch of noise, with an envelope.
		
		Arguments:
		x -- The center X coordinate
		y -- The center Y coordinate
		
		Keyword arguments:	
		env -- Any of the following: "gaussian", "linear", "circular", "rectangle" (default = "gaussian")
		size -- Size in pixels (default = 96)
		stdev -- Standard deviation in pixels of the gaussian. Only applicable if env = "gaussian". (default = 12)
		phase -- Phase of the sinusoid [0.0 .. 1.0] (default = 0)
		col1 -- Human readable color for the tops (default = "white")
		col2 -- Human readable color for the troughs (default = "black")
		bgmode -- Specifies whether the background is the average of col1 and col2 (bgmode = "avg", a typical Gabor patch)
				  or equal to col2 ("col2"), useful for blending into the background. (default = "avg")
		"""	
		
		pos = x - self.xcenter(), self.ycenter() - y		
		surface = openexp._canvas.legacy._noise_patch(env, size, stdev, col1, col2, bgmode)
		string = pygame.image.tostring(surface, "RGB")
		pil_img = Image.fromstring("RGB", (surface.get_width(), surface.get_height()), string)
		stim = visual.SimpleImageStim(win = self.experiment.window, image = pil_img, pos = pos)
		self.stim_list.append(stim)
		
	def shapestim(self, vertices, color = None, fill = False, fix_coor = True, close = False):
	
		"""
		* Note: Specific to the PsychoPy backend, primarily intended for internal use. Using this function
				directly will break your experiment when switching backends.
				
		Draws a stimulus definied by a list of vertices
		
		Arguments:
		vertices: A list of lists, like [[0,0],[10,10]] containing the vertices of the shape
		
		Keyword arguments:
		color: the color of the shape
		fill: a boolean indicating wether the shape should be filles
		fix_coor: a boolean indicating whether the vertices are in OpenSesame or PsychoPy format
		"""
		
		if fix_coor:
			# Convert the coordinates into the PsychoPy format, in which 0,0 is the center of the screen
			# and negative y-coordinates are down.
			_vertices = []
			for x, y in vertices:
				_vertices.append( [x - self.xcenter(), self.ycenter() - y] )
		else:
			_vertices = vertices
			
		if color == None:
			color = self.fgcolor			
		if fill:
			fill = color
		else:
			fill = None		
			
		stim = visual.ShapeStim(self.experiment.window, units = "pix", lineWidth = self.penwidth, vertices = _vertices, lineColor = color, closeShape = close, fillColor = fill, interpolate = False)
		self.stim_list.append(stim)

"""
Static methods
"""

# Store the experiment as a singleton, to be used in the _time() function
_experiment = None

def init_display(experiment):

	"""
	Initialize the display before the experiment begins.
		
	Arguments:
	experiment -- An instance of libopensesame.experiment.experiment. The following properties are
				  of particular importance: experimnent.fullscreen (bool), experiment.width (int) and
				  experiment.height (int). The experiment also contains default font settings as
				  experriment.font_family (str) and experiment.font_size (int).
	"""
	
	global _experiment
	_experiment = experiment	
	
	# Set the PsychoPy monitor, default to testMonitor
	if experiment.has("psychopy_monitor"):
		monitor = experiment.get("psychopy_monitor")
	else:
		monitor = "testMonitor"
		
	# Set the PsychoPy wintype, default to PyGlet
	if experiment.has("psychopy_wintype"):
		wintype = experiment.get("psychopy_wintype")
	else:
		wintype = "pyglet"
		
	# Set the PsychoPy waitblanking option, default to True
	if experiment.has("psychopy_waitblanking") and experiment.get("psychopy_waitblanking") == "no":
		waitblanking = False
	else:
		waitblanking = True
			
	experiment.window = visual.Window( [experiment.width, experiment.height], waitBlanking = waitblanking, fullscr = experiment.fullscreen, monitor = monitor, units = "pix", winType = "pyglet")		
	experiment.clock = core.Clock()	
	experiment._time_func = _time

	# If pyglet is being used, change the window caption. Don't know how to do this for pygame (regular set_caption() is ineffective)
	if wintype == "pyglet":
		experiment.window.winHandle.set_caption("OpenSesame (PsychoPy backend)")
		
	pygame.mixer.init()	
				
def close_display(experiment):

	"""
	Close the display after the experiment is finished.
	
	Arguments:
	experiment -- An instance of libopensesame.experiment.experiment	
	"""
	
	experiment.window.close()	
	
def _time():

	"""
	Returns a psychopy timestamp converted to milliseconds. This function is not
	to be called directly, but is used by openexp.experiment.time()
	"""

	global _experiment
	return 1000.0 * _experiment.clock.getTime()