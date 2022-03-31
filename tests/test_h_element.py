from elinon import make_h_element

def test_h_element():
  assert make_h_element("# Hello world", 1) == "<h1 class=\"markdown\">Hello world</h1>"

def test_empty_h_element():
  assert make_h_element("#### ", 4) == "<h4 class=\"markdown\"></h4>"
