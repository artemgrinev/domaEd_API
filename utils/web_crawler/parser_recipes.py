import requests
from bs4 import BeautifulSoup


class GetRecipes:
    def __int__(self, url: str):
        self.url = url

    def start_parser(self):
        domain = self.url.split("/")
        if domain[2] == "eda.ru":
            return self._get_ingredients_eda_ru(self.url)
        elif domain[0] == "eda.ru":
            link = "https://" + self.url
            return self._get_ingredients_eda_ru(link)

    def _get_ingredients_eda_ru(self, url: str) -> dict:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        recipes_name = soup.select('span[itemprop = "name"] > h1')[0].text
        ingredients = soup.find_all('div', class_="emotion-ydhjlb")
        data = {}
        ingredients_list = []
        for i in ingredients:
            name = i.find('span', itemprop='recipeIngredient')
            info = i.find('span', class_='emotion-15im4d2')
            if name and info:
                ing = {"name": name.text,
                       "amount": info.text.split()[0],
                       "measure": info.text.split()[1],
                       }
                ingredients_list.append(ing)

        data.update({
            "name": recipes_name,
            "resource": "eda.ru",
            "url": url,
            "ingredients": ingredients_list})

        return data

