import bs4 as bs
import urllib

import pandas as pd

source = urllib.urlopen('https://www.yelp.com/search?find_desc=Restaurants&find_loc=Nashville%2C+TN&ns=1').read()
page_soup = bs.BeautifulSoup(source, 'html.parser')
mains = page_soup.find_all("div", {"class": "lemon--div__373c0__1mboc border-color--default__373c0__2oFDT"})
main = mains[0]  # First item of mains

# Empty list for main list items

Bizname = []
ratings = []
price = []

# Get Main attributes (name, ratings, noreviews, price)

for main in mains:
    try:
        Bizname.append(main.find("a", {"class": "lemon--a__374c0__IEZFH link__373c0__29943 "
                                                "link-color--blue-dark__373c0__1mhJo "
                                                "link-size--inherit__373c0__2JXk5"}).text)
    except:
        Bizname.append("None")
    try:
        ratings.append(main.find("div", {"class": "lemon--div__373c0__1mboc"}).div.get('aria-label'))
    except:
        ratings.append("None")

    try:
        price.append(main.find("span", {
            "class": "lemon--span__373c0__3997G text__373c0__2pB8f priceRange__373c0__2DY87 text-color--normal__373c0__K_MKN text-align--left__373c0__2pnx_ text-bullet--after__373c0__1ZHaA"}).text)
    except:
        price.append("None")

secondarys = page_soup.find_all("div", {"class": "lemon--div__373c0__1mboc secondaryAttributes__373c0__7bA0w "
                                                 "arrange-unit__373c0__1piwO border-color--default__373c0__2oFDT"})
sec = secondarys[0]
add = []

for sec in secondarys:
    try:
        add.append(sec.address.find("span", {"class": "lemon--span__373c0__3997G"}).text)
    except:
        add.append("None")

print(Bizname)
print(ratings)
print(price)
print(add)

# data = {}
# a = {'Rest_name': Bizname, 'Rest_ratings': ratings, 'Rest_price': price, 'Rest_add': add}
# orient = 'index'
# rest = pd.DataFrame.from_dict(a, orient)
# rest.transpose()
# rest = pd.DataFrame(data)
# columns = ('Rest_name', 'Rest_ratings', 'Rest_price', 'Rest_add')
# rest.to_csv('Output.csv', columns)
