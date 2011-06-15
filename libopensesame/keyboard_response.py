"""
This file is part of OpenSesame.

OpenSesame is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OpenSesame is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OpenSesame.  If not, see <http://www.gnu.org/licenses/>.
"""

from libopensesame import item, exceptions, generic_response
import openexp.keyboard
import openexp.exceptions

class keyboard_response(item.item, generic_response.generic_response):

	def __init__(self, name, experiment, string = None):

		"""
		Initialize the loop
		"""

		self.flush = "yes"
		self.item_type = "keyboard_response"
		self.description = "Collects keyboard responses"
		self.timeout = "infinite"
		self.auto_response = 97 # 'a'
		self.duration = "keypress"

		item.item.__init__(self, name, experiment, string)

	def prepare(self):

		"""
		Prepare the keyboard response item
		"""

		item.item.prepare(self)
		generic_response.generic_response.prepare(self)
		return True

	def run(self):

		"""
		Run the keyboard response item
		"""

		# Record the onset of the current item
		self.set_item_onset()

		# Flush responses, to make sure that earlier responses
		# are not carried over
		if self.get("flush") == "yes":
			self._keyboard.flush()

		self.set_sri()
		self.process_response()

		# Report success
		return True

	def to_string(self):

		"""
		Encode the keyboard_response as string
		"""

		s = item.item.to_string(self, "keyboard_response")
		return s


