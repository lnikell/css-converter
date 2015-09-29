import sublime, sublime_plugin
import re

class CssToSass(sublime_plugin.TextCommand):
  options = {
    'indent': 2,
    'openingBracket': '',
    'closingBracket': '',
    'semicolon': ':',
    'eol': '',
    'unPrefix': False,
    'keepColons': False,
  }

  depth = 0
  def run(self, edit):
    if self.view.file_name() and self.view.file_name().endswith(".sass"):
      self.convert(sublime.get_clipboard())
    else:
      self.view.run_command('paste')


  def convert(self, text):
      if (";" in text):
        sublime.set_clipboard(self.process())
        self.view.run_command('paste_and_indent')
      else:
        self.view.run_command('paste')

  def process(self):
    text = sublime.get_clipboard()
        
    tree = {'children': {}}
    # Remove comments
    text = re.sub("\/\*[\s\S]*?\*\/", "", text)
    # Process each css block
    for (selector, declaration) in re.findall("([^{]+)\{([^}]+)\}", text):
      selectors = []
      path = tree

      selector = selector.strip()
      if re.search(",", selector):
        path = self.addRule(path, selector)
      else:
        selector = re.sub("\s*([>\+~])\s*", r' &\1' , selector)   
        selector = re.sub("(\w)([:\.])", r'\1 &\2' , selector)  
        selectors = re.split("[\s]+", selector)
        for item in selectors: 
          #fix back special chars
          _sel = re.sub("&(.)", r'& \1 ', item)
          _sel = re.sub("& ([:\.]) ", r'&\1', _sel)

          path = self.addRule(path, _sel)
      for (_property, value) in re.findall("([^:;]+):([^;]+)", declaration):
        obj = {
          "property": _property.strip(),
          "value": value.strip()
        }

        path['declarations'].append(obj)
    return self.generateOutput(tree)

      
 
  def addRule(self, path, selector):
    if selector in path['children']:
      path['children'][selector] = path['children'][selector] 
    else:
      path['children'][selector] = { 'children': {}, 'declarations': [] }
    return path['children'][selector]

  def generateOutput(self, tree):
    output = ''
    openingBracket = self.options['openingBracket']
    for key in tree['children']:
      sel = key
      output += self.getIndent() + sel + openingBracket + '\n'
      self.depth = self.depth + 1
      declarations = tree['children'][key]['declarations']
      for index, declaration in enumerate(declarations):
        output += self.getIndent() + declaration['property'] + self.options['semicolon'] + ' ' + declaration['value'] + self.options['eol'] + '\n'
      output += self.generateOutput(tree['children'][key])
      self.depth = self.depth - 1
      output += self.getIndent() + self.options['closingBracket'] + '\n' + ('$n' if self.depth == 0 else '')
    print(output)
    # output = output.replace(/^\s*$[\n\r]{1,}/gm, '').replace(//g, '\n')  
    output = re.sub('^\s*$[\n\r]{1,}', '', output)
    output = re.sub('\$n', '\n', output)
    print("=============")
    print(output)
    print("=============")
    return output
  def getIndent(self):
    return '  ' * (self.depth + 1)


          
