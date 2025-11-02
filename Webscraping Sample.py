from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/118.0.0.0 Safari/537.36"
}

url = "https://www.imdb.com/chart/top/"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

rating = soup.find_all(class_="ipc-rating-star--rating")

ratings =[]
for score in rating:
    ratings.append(float(score.text))


titles = []
title = (soup.find_all("h3", class_="ipc-title__text ipc-title__text--reduced"))
for title in title:
    if title != "IMDb Charts":
        titles.append(title.text)

highest_score = (max(ratings))
index_numbr1 = (ratings.index(highest_score))

print(f"The best movie is: {titles[index_numbr1]} with the score of {ratings[index_numbr1]}\n")

print(f"Here are the top 10 Best Movies Of All Time:")
for top10 in range(0,10):
    print(titles[top10])