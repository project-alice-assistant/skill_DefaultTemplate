import sqlite3

from core.base.model.Widget import Widget
from core.base.model.WidgetSizes import WidgetSizes


class Template(Widget):

	SIZE = WidgetSizes.w
	OPTIONS: dict = dict()

	def __init__(self, data: sqlite3.Row):
		super().__init__(data)
