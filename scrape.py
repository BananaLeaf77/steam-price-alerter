import requests
import bs4

ITEM = "Chef d'Escadron Rouchard | Gendarmerie Nationale"


def scrape(s_url, cur_url):
    # STEAM SCRAPE
    s_response = requests.get(url=s_url)
    # print(f"STEAN WEB : {s_response.raise_for_status}")
    s_data = s_response.text
    steam_soup = bs4.BeautifulSoup(s_data, "html.parser")

    select = steam_soup.find(name="span", class_="normal_price")
    if select:
        text = select.getText()
        price = float(text.split('$')[1].split()[0])

    # CURRENCY SCRAPE
    c_response = requests.get(url=cur_url)
    # print(f"CURRENCY WEB : {c_response.raise_for_status}")
    c_data = c_response.text

    currency_soup = bs4.BeautifulSoup(c_data, "html.parser")

    cur_select = currency_soup.find(name="strong")
    if cur_select:
        text = cur_select.getText()
        format1 = "".join(text.split()[3].split(".")[0:1])
        current_value = float(format1.replace(",", "."))
    else:
        print("not found")

    idr_result = price * current_value
    rounded_result = round(idr_result, 3)

    body = f"""({ITEM}) value :
          USD = ${price}
          IDR = Rp.{rounded_result}
          """
    return body
