from elinon import txt_to_html

def test_txt_to_html():
  print(txt_to_html("test.txt"))
  assert txt_to_html("test.txt") == """<!DOCTYPE html>
<html>
<head>
<link rel='stylesheet' href='style.css'>
</head>
<body>
<div class='outer-div'>
<h1 class="markdown">This is an h1</h1>
<p class="markdown">This is a p element.</p>
<h3 class="markdown">This is an h3</h3>
</div>
</body>
</html>"""
