# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#import re
#from itemadapter import ItemAdapter
#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.preprocessing import StandardScaler
#nltk.download('all')
#import nltk
#from nltk.tokenize import word_tokenize
#from nltk.stem.lancaster import LancasterStemmer
##from nltk.tag import pos_tag
#!pip install nltk

#nltk.download('rslp')
#nltk.download('stopwords')
#from nltk.corpus import stopwords
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#from nltk.tokenize.treebank import TreebankWordDetokenizer


class G1CrawlerPipeline:
  # yield({'title':title, 'description':description, 'image_url':image_url, 'link':link,'categoria':cat})

    
    
    def process_item(self, item, spider):
        item['title'] = item['title'].lower()
        description = preparaTexto(item['description'].lower())
        item['categoria'] = item['categoria'].lower()
        print(item)
        line =  json.dumps(dict(item)) + '\n'
        self.file.write(line)
        return item
