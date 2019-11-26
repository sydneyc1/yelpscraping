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
        Bizname.append(main.address.find("a", {"class": "lemon--a__373c0__IEZFH link__373c0__29943 "
                                                       "link-color--blue-dark__373c0__1mhJo "
                                                       "link-size--inherit__373c0__2JXk5"}).text)
    except:
        Bizname.append("None")
    try:
        ratings.append(main.find("div", {"class": "lemon--div__373c0__1mboc i-stars__373c0__Y2F3O "
                                                  "i-stars--regular-4-half__373c0__3VLp8 "
                                                  "border-color--default__373c0__2oFDT "
                                                  "overflow--hidden__373c0__8Jq2I"}).div.get('aria-label'))
    except:
        ratings.append("None")

    try:
        price.append(main.find("span", {"class": "lemon--span__373c0__3997G text__373c0__2pB8f "
                                                 "priceRange__373c0__2DY87 text-color--normal__373c0__K_MKN "
                                                 "text-align--left__373c0__2pnx_ "
                                                 "text-bullet--after__373c0__1ZHaA"}).text)
    except:
        price.append("None")

secondarys = page_soup.find_all("div", {"class": "lemon--div__373c0__1mboc secondaryAttributes__373c0__7bA0w "
                                                 "arrange-unit__373c0__1piwO border-color--default__373c0__2oFDT"})
sec = secondarys[0]

# Empty list for secondary list items

add = []
tel = []

# Get Secondary attributes (add, tel)

for sec in secondarys:
    try:
        add.append(sec.address.find("span", {"class": "lemon--span__373c0__3997G"}).text)
    except:
        add.append("None")
    try:
        tel.append(sec.div.div.text)
    except:
        tel.append("None")

# Replace any non-telephone numbers with "None"

# new_tel = [x if (bool(re.search(r'[(]\d\d[)].\d{4}.\d{4}|[(]\d\d[)].\d{4}.\d{3}|\d{4}.\d{3}.\d{3}', x)) == True) else "None" for x in tel]


data = {}
a = {'Rest_name': Bizname, 'Rest_ratings': ratings, 'Rest_price': price, 'Rest_add': add}
rest = pd.DataFrame.from_dict(a, orient='index')
rest.transpose()
rest = pd.DataFrame(data)
rest.to_csv('Output.csv', columns=('Rest_name', 'Rest_ratings', 'Rest_price', 'Rest_add'))
