from elinon import make_style_css

def test_make_css():
  assert make_style_css() == """
.outer-div {
	background-color: #211e1e;
	height: 100%;
	width: 40%;
	margin: 0 auto;
}

.markdown {
	font-family: Courier, monospace;
	color: #bfb2b2;
	text-align: center;
}"""
