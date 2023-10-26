from bs4 import BeautifulSoup

html = '''
<div id="fool" class="buzz">Hello</div> <div id="foo2">World<div>Test<p class="buzz"></p></div></div>

<div id="bar1">Example<div>Test</div></div>

<table name="fizz" class="buzz"> <tr>

<th>Letters</th>

<th>Numbers</th>

</tr>

<tr>

<td>A</td> <td>1</td>

</tr>

<tr>

<td>B</td> <td>2</td>

</tr>

<tr>

<td>C</td> <td>3</td>

</tr> </table>
'''

soup = BeautifulSoup(html, "html.parser")

p = soup.select_one("[id^=foo]")
print(p)

p = p.find_next_sibling("div")

print(p.contents)
print(p.children)
print(list(p.children))

print(p.attrs)
p["name"]="bar"

print(p.attrs)