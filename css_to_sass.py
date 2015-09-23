import sublime, sublime_plugin
import re

class CssToSass(sublime_plugin.TextCommand):
  def run(self, edit):
    if self.view.file_name() and self.view.file_name().endswith(".sass"):
      self.convert(sublime.get_clipboard())
    else:
      self.view.run_command('paste')


  def convert(self, text):
      if (";" in text):
        self.clean()
        self.view.run_command('paste')
      else:
        self.view.run_command('paste')

  def clean(self):
    text = sublime.get_clipboard()
    text = re.sub("(;|{|})", "", text)
    sublime.set_clipboard(text)