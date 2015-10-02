# CSS to SASS/Stylus converter for Sublime Text 3
**STOP WASTE YOUR TIME** removing brackets, semicolon and formating any css inserted from your browser to Sublime Text.

![Example usage]
(https://habrastorage.org/files/1cc/aa6/0bb/1ccaa60bb0924c8b8976b99acf0e5fd9.gif)

You could also copy something like this:
```css
{
  display: block;
  color: #ffffff;
}
```
And plugin will transform it to:
```css
display: block
color: #ffffff
```

### Features
- plugin works without any gems or npm packages
- support nested selectors
- unprefix(comming soon)

### Installation
#### via Package Control
- Open the Command Pallete (ctrl+shift+P or cmd+shift+P);
- Type "Add repository";
- Insert "https://github.com/lnikell/css-to-sass-converter.git"
- Open the Command Pallete (ctrl+shift+P or cmd+shift+P);
- Type "Install Package"
- Type "css to sass converter" and hit return.

### Configuration options
**css_converter_indent**

Number of spaces or tabs.
Default: 2.
Possible option "\t".

**css_converter_semicolon**

Default: ':'. If you want to convert css to stylus you need to change this option to ''.

**css_converter_eol**
End of line symbol. Default ''.

Default settings:
```json
{
  "css_converter_indent": 2,
  "css_converter_semicolon": ":",
  "css_converter_eol": "",
}
```

### Default key binding

```json
[
  { "keys": ["ctrl+v"], "command": "css_to_sass" },
]
```



