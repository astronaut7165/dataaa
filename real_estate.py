import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url_base = "http://apis.data.go.kr/1613000/RTMSDataSvcAptTradeDev/getRTMSDataSvcAptTradeDev"
key = "DGLcc6tpjDBTdqj5r4S0zDznFf5MC99GPSY6YSY%2F1hAUt8iDWSNPO3hLA1juvYs%2BSxG%2Bl%2FiNHvGRWQgy7Pc8mQ%3D%3D"
val_lawd_cd = 11110
val_deal_ymd = 202501
url = f"{url_base}?serviceKey={key}&LAWD_CD={val_lawd_cd}&DEAL_YMD={val_deal_ymd}&pageNo=1&numOfRows=10"
res = requests.get(url)
bs_res = bs(res.content, features = "xml")

# print(bs_res.prettify())
items = bs_res.find_all("item")
print(f"✅ 총 {len(items)}개의 거래 데이터가 있습니다.")


for i, item in enumerate(items):
    print(f"--- 거래 {i+1} ---")
    for tag in item.find_all():
        print(f"{tag.name}: {tag.text}")


data = []
for item in items:
    row = {}
    for tag in item.find_all():
        row[tag.name] = tag.text
    data.append(row)

df = pd.DataFrame(data)
print(df.head())

df.to_csv("real_estate.csv", index=False, encoding="utf-8-sig")
print("✅ CSV 저장 완료: real_estate_.csv")