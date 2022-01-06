from bs4 import BeautifulSoup

with open('website.html', encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

# print(soup.prettify())

# getting all anchor tags
all_anchor_tags = soup.find_all(name='a')
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.get_text())
    print(tag.get('href'))


heading = soup.find(name='h1', id='name')
print(heading)

# finding using class
class_is_heading = soup.find_all(class_='heading')
print(class_is_heading)

heading_h3 = soup.find_all('h3', class_='heading')
print(heading_h3)

# selecting using selector
# select one selects the first element
company_url = soup.select_one(selector='p a')
print(company_url)

# selecting using id
name = soup.select_one(selector='#name')
print(name)

# selecting using class
headings = soup.select_one('.heading')
print(headings)

