import json
import pandas as pd
import matpolotlib.pylot as plt


data_path = 'result.txt'

data = []
filect= open(data_path, "r")
for line in filect:
    try:
        tweet = json.loads(line)
        data.append(tweet)
    except:
        continue
    
    
print len(data)

tweets = pd.DataFrame()

tweets['text'] = map(lambda tweet: tweet['text'], data)
tweets['lang'] = map(lambda tweet: tweet['lang'], data)
tweets['county'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, data)


tweets_by_lang = tweets['lang'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10) 
ax.set_xlabel('Languages', fontsize=15) 
ax.set_ylabel('Number of tweets' , fontsize=15) 
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold') 
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')