from tap import Tap
import re

def make_p_element(contents):
	return '<p class="markdown">{}</p>'.format(contents)

def make_h_element(contents, level):
	contents = contents.strip("# \t")
	return '<h{} class="markdown">{}</h{}>'.format(str(level), contents, str(level))

def get_h_level(element):
	level = 0
	for char in element:
		if char == "#":
			level += 1
		else:
			return level

def make_bulleted_list(element):
	bullets = 0
	newlines = 0
	for char in element.strip():
		if char == "*":
			bullets += 1
		
		if char == "\n":
			newlines += 1
	
	if bullets == len(element.strip()) - newlines:
		return ""
	
	elements = element.split("\n")
	final_list = '<ul class="markdown">\n'
	for el in elements:
		el = el.strip("* \t")
		final_list += '<li class="markdown">{}</li>\n'.format(el)
	
	final_list += '</ul>\n'
	return final_list

def txt_to_html(filename="test.txt"):
	html = "<!DOCTYPE html>\n<html>\n"
	html += "<head>\n<link rel='stylesheet' href='style.css'>\n</head>\n"
	html += "<body>\n<div class='outer-div'>\n"
	
	contents = open(filename, "r").read()
	contents = contents.split("\n\n")
	contents = list(map(str.strip, contents))
	
	for i in range(len(contents)):
		el = contents[i]
		if el.startswith("#"):
			level = get_h_level(el)
			html += make_h_element(el, level) + "\n"
			continue
		elif el.startswith("*"):
			html += make_bulleted_list(el)
			continue
		html += make_p_element(el) + "\n"
	
	html += "</div>\n</body>\n</html>"
	return html

def make_style_css():
	style_css = """
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
	return style_css

def main():
	class ArgParser(Tap):
		filename: str
		out: str = "out.html"

		def configure(self):
			self.add_argument("filename")
			self.add_argument("-o", "--out")
    
	args = ArgParser().parse_args()
	html = txt_to_html(args.filename)
	css = make_style_css()
	
	outhtml = open(args.out, "w")
	outhtml.write(html)
	
	outcss = open("style.css", "w")
	outcss.write(css)

if __name__ == "__main__":
	main()
