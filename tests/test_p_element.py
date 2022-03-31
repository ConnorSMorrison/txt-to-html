from elinon import make_p_element

def test_p_element():
  assert make_p_element("Hello world") == "<p class=\"markdown\">Hello world</p>"

def test_empty_p_element():
  assert make_p_element("") == "<p class=\"markdown\"></p>"
