from elinon import get_h_level

def test_get_h_level():
  assert get_h_level("## Hello world") == 2
