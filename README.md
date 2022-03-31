# Elinon

Converts simple text files to HTML and styles them with CSS

## Usage

```
usage: elinon.py [-o OUT] [-h] filename

positional arguments:
  filename           (str, default=None)

options:
  -o OUT, --out OUT  (str, default=out.html)
  -h, --help         show this help message and exit
```

## Examples

```
* Foo
* Bar
* Baz
```
will become
```
<ul class="markdown">
<li class="markdown">Foo</li>
<li class="markdown">Bar</li>
<li class="markdown">Baz</li>
</ul>
```

```
## Hello world

This is a p element
```
will become
```
<h2 class="markdown">Hello world</h2>
<p class="markdown">This is a p element</p>
```

## Tests

Run tests using pytest. `python3 -m pytest tests`
