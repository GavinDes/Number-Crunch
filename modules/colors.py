"""
Module containing color escape sequences simplified by name.

Quick Tutorial:

style_sequence = Style.var_style
normal_color_sequence = Color.normal
dark_color_sequence = Color.dark
light_color_sequence = Color.light
normal_highlight_sequence = Color.h_normal
dark_highlight_sequence = Color.h_dark
normal_color = Color.text("foo")
light_color = Color.text("foo", "light")
dark_color = Color.text("foo", "dark")
highlighted_text = Color.highlight("foo")
dark_highlighted_text = Color.highlight("foo", "dark)
styled_text = Style.style("foo")

Order of Functions:

Color.text -> Color.highlight -> Style.style -> "bar"
Blue.text(Green.highlight(Style.blink("bar")))

OR

Color.text -> Style.style -> Color.highlight -> "bar"
Red.text(Style.crossed(Green.highlight("bar")))

A script that displays all the colors and styles can be found:
/usr/bin/colors_display.py
"""

normal_text = "\033[0m"


class Red:
   
   light = "\033[1;31m"
   dark = "\033[2;31m"
   normal = "\033[0;31m"
   h_dark = "\033[2;41m"
   h_normal = "\033[1;41m"
   def text(self, string, value = "0"):
      if value == "light": value = "1"
      elif value == "dark": value = "2"
      return "\033[{};31m{}\033[0m".format(value, string)
   def highlight(self, string, value = "1"):
      if value == "dark": value = "2"
      return "\033[{};41m{}\033[0m".format(value, string)

class Gray:
   
   light = "\033[1;30m"
   dark = "\033[2;30m"
   normal = "\033[0;30m"
   h_dark = "\033[2;47m"
   h_normal = "\033[1;47m"
   def text(self, string, value = "0"):
      if value == "dark": value = "2"
      elif value == "light": value = "1"
      return "\033[{};30m{}\033[0m".format(value, string)
   def highlight(self, string, value = "1"):
      if value == "dark": value = "2"
      return "\033[{};47m{}\033[0m".format(value, string)

class Green:
   
   light = "\033[1;32m"
   dark = "\033[2;32m"
   normal = "\033[0;32m"
   h_dark = "\033[2;42m"
   h_normal = "\033[1;42m"
   def text(self, string, value = "0"):
      if value == "light": value = "1"
      elif value == "dark": value = "2"
      return "\033[{};32m{}\033[0m".format(value, string)
   def highlight(self, string, value = "1"):
      if value == "dark": value = "2"
      return "\033[{};42m{}\033[0m".format(value, string)
   
class Yellow:
   
   light = "\033[1;33m"
   dark = "\033[2;33m"
   normal = "\033[0;33m"
   def text(self, string, value = "0"):
      if value == "light": value = "1"
      elif value == "dark": value = "2"
      return "\033[{};33m{}\033[0m".format(value, string)

class Blue:
   
   light = "\033[1;34m"
   dark = "\033[2;34m"
   normal = "\033[0;34m"
   h_dark = "\033[2;44m"
   h_normal = "\033[1;44m"
   def text(self, string, value = "0"):
      if value == "light": value = "1"
      elif value == "dark": value = "2"
      return "\033[{};34m{}\033[0m".format(value, string)
   def highlight(self, string, value = "1"):
      if value == "dark": value = "2"
      return "\033[{};44m{}\033[0m".format(value, string)


class Magenta:
   
   light = "\033[1;35m"
   dark = "\033[2;35m"
   normal = "\033[0;35m"
   h_dark = "\033[2;45m"
   h_normal = "\033[1;45m"
   def text(self, string, value = "0"):
      if value == "light": value = "1"
      elif value == "dark": value = "2"
      return "\033[{};35m{}\033[0m".format(value, string)
   def highlight(self, string, value = "1"):
      if value == "dark": value = "2"
      return "\033[{};45m{}\033[0m".format(value, string)
   
class Cyan:
   
   light = "\033[1;36m"
   dark = "\033[2;36m"
   normal = "\033[0;36m"
   h_dark = "\033[2;46m"
   h_normal = "\033[1;46m"
   def text(self, string, value = "0"):
      if value == "light": value = "1"
      elif value == "dark": value = "2"
      return "\033[{};36m{}\033[0m".format(value, string)
   def highlight(self, string, value = "1"):
      if value == "dark": value = "2"
      return "\033[{};46m{}\033[0m".format(value, string)
   
class White:
   
   light = "\033[1;37m"
   dark = "\033[2;37m"
   normal = "\033[0;37m"
   def text(self, string, value = "0"):
      if value == "light": value = "1"
      elif value == "dark": value = "2"
      return "\033[{};37m{}\033[0m".format(value, string)

class Brown:
   
   h_dark = "\033[2;43m"
   h_normal = "\033[1;43m"
   def highlight(self, string, value = "1"):
      if value == "dark": value = "2"
      return "\033[{};43m{}\033[0m".format(value, string)

class Style:

   var_underline = "\033[4m"
   var_italics = "\033[3m"
   var_blink = "\033[5m"
   var_crossed = "\033[9m"
   var_negative = "\033[7m"
   def underline(self, string):
      return "\033[4m{}\033[0m".format(string)
   def italics(self, string):
      return "\033[3m{}\033[0m".format(string)
   def blink(self, string):
      return "\033[5m{}\033[0m".format(string)
   def crossed(self, string):
      return "\033[9m{}\033[0m".format(string)
   def negative(self, string):
      return "\033[7m{}\033[0m".format(string)


# Class instances
Red = Red()
Gray = Gray()
Green = Green()
Yellow = Yellow()
Blue = Blue()
Magenta = Magenta()
Cyan = Cyan()
White = White()
Brown = Brown()
Style = Style()
