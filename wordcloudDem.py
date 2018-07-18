from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud

d = path.dirname(__file__)

# Read the whole text.
text = open('tweet_dem2text.txt').read()
wordcloud = WordCloud().generate(text)
wordcloud.to_file("democratic.png")
# Open a plot of the generated image.
#plt.imshow(wordcloud)
#plt.axis("off")
#plt.show()

