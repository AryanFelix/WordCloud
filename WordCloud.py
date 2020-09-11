import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import random

df = pd.read_csv(r"text.txt", header = None, error_bad_lines = False, encoding = 'utf_8')
df= df.drop(0)
df.columns=['Date', 'Message']
Chat = df["Message"].str.split("-", n = 1, expand = True)
df["Time"] = Chat[0]
df["Content"] = Chat[1]
Texts = df["Content"].str.split(":", n = 1, expand = True)
df["Person"] = Texts[0]
df["Text"] = Texts[1]
df=df.drop(columns=["Date", "Time", "Content", "Person", "Message"])
df["Text"] = df["Text"].str.lower()
df["Text"] = df["Text"].str.replace("<media omitted>", "MediaShared")
df["Text"] = df["Text"].str.replace("this message was deleted", "DeletedMessage")
df["Text"] = df["Text"].str.replace("missed voice call", "")
df["Text"] = df["Text"].str.replace("missed video call", "")
df["Text"] = df["Text"].str.replace(".", "")
df["Text"] = df["Text"].str.replace("?", "")
df["Text"] = df["Text"].str.replace("!", "")
df["Text"] = df["Text"].str.replace(",", "")
for x in df["Text"].index:
    temp = str(df["Text"][x])
    if len(temp) > 4:
        if temp.find(" http") == -1:
            continue
        elif temp.find(" https"):
            df["Text"][x] = ""
        else:
            df["Text"][x] = ""
df.to_csv("Final.csv", index = False)
deletionlist = []
df = pd.read_csv("Final.csv")
words = df["Text"].to_string(index = False)
words = words.split()
unique = {}
for x in words:
    if x in unique:
        unique[x] += 1
    else:
        unique[x] = 1
sortVal = sorted(unique.items(), key=lambda x: x[1], reverse=True)
sortList = ["MediaShared", "DeletedMessage", ""]
for x in sortVal:
    sortList.append(x[0])
sortString = ""
for s in sortList:
    sortString = sortString + " " + str(s)
stopwords = STOPWORDS
stopwords.update(deletionlist)
mask = np.array(Image.open("Masks/Mask"+str(random.randrange(1,11))+".jpg"))
wordcloud = WordCloud(stopwords=stopwords, background_color="white", mode="RGBA", max_words=1000, mask=mask).generate(sortString)

image_colors = ImageColorGenerator(mask)
plt.figure(figsize=(24,14), dpi=800)
plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")

plt.savefig("Final.png", format="png")
plt.show()