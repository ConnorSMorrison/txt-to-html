from elinon import make_bulleted_list, txt_to_html

def test_bulleted_list():
  assert make_bulleted_list("* Hello world\n * Hi there!") == '<ul class="markdown">\n<li class="markdown">Hello world</li>\n<li class="markdown">Hi there!</li>\n</ul>\n'

def test_empty_bulleted_list():
  assert make_bulleted_list("*\n*") == ""
  assert make_bulleted_list("*") == ""

def test_make_bulleted_list():
  assert txt_to_html("bulleted-list.txt") == """<!DOCTYPE html>
<html>
<head>
<link rel='stylesheet' href='style.css'>
</head>
<body>
<div class='outer-div'>
<ul class="markdown">
<li class="markdown">Hello</li>
<li class="markdown">World</li>
</ul>
<ul class="markdown">
<li class="markdown">Hello World</li>
</ul>
<ul class="markdown">
<li class="markdown">How goes it?</li>
<li class="markdown">I'm good</li>
<li class="markdown">How bout you?</li>
</ul>
</div>
</body>
</html>"""
