import sublime, sublime_plugin
import re

class CssToSass(sublime_plugin.TextCommand):
  options = {
    'indent': 2,
    'openingBracket': '{',
    'closingBracket': '}',
    'semicolon': ':',
    'eol': ';',
    'unPrefix': False,
    'keepColons': False,
  }

  def run(self, edit):
    if self.view.file_name() and self.view.file_name().endswith(".sass"):
      self.convert(sublime.get_clipboard())
    else:
      self.view.run_command('paste')


  def convert(self, text):
      if (";" in text):
        self.process()
        self.view.run_command('paste_and_indent')
      else:
        self.view.run_command('paste')

  def process(self):
    text = sublime.get_clipboard()
    # text = re.sub("(;|{|})", "", text)
    # sublime.set_clipboard(text)
    
    tree = {'children': {}}
    # Remove comments
    text = re.sub("\/\*[\s\S]*?\*\/", "", text)
    # Process each css block
    for (selector, declaration) in re.findall("([^{]+)\{([^}]+)\}", text):
      selectors = []
      path = tree

      selector = selector.strip()
      if re.search(",", selector):
        self.addRule(path, selector)
      
 
  def addRule(self, path, selector):
    print(path)
    path['children'][selector] = path['children'][selector] | { children: 1, declarations: [] }
    print(path)


      