#from Rake import rake
#from newsapi import NewsApiClient

'''
api = NewsApiClient(api_key='8e7caac0fb8c4c2ba9f3324db7ed392d')
category_1_first_tier = api.get_top_headlines(sources='associated-press, bbc-news, reuters, bloomberg, cbs-news, abc-news, nbc-news', q='trump')
category_1_second_tier = api.get_everything(sources='associated-press, bbc-news, reuters, bloomberg, cbs-news, abc-news, nbc-news', q='trump')
category_2_first_tier = api.get_top_headlines(sources='usa-today, the-hindu, politico, axios, the-wall-street-journal', q='trump')
category_2_second_tier = api.get_everything(sources='usa-today, the-hindu, politico, axios, the-wall-street-journal', q='trump')
category_3_first_tier = api.get_top_headlines(sources='time, the-washington-post, the-hill, msnbc, national-review, the-washington-times', q='trump')
category_3_second_tier = api.get_everything(sources='time, the-washington-post, the-hill, msnbc, national-review, the-washington-times', q='trump')
'''

'''
News in descending order of importance:
A does X1
C does Z1
A does X2
B does Y1
C does Z2
'''

people =[
					{
						"name": "A",
						"threshold": 10
					},
					{
						"name": "B",
						"threshold": 10
					},
					{
						"name": "C",
						"threshold": 10
					},
				]
category_1_first_tier = [
                          {
                            "name": "A",
                            "headline": "A does X1",
                            "content": "",
                            "keywords": ['A', 'X1', 'February 31', 'Greendale', 'election', 'desecration', 'graverobbing', 'blackout', 'murder', 'arson'],
                            "source": "1",
                          },
                          {
                            "name": "C",
                            "headline": "C does Z1",
                            "content": "",
                            "keywords": ['C', 'Z1', 'March 32', 'City', 'election', 'blackjack', 'hookers', 'space station', 'bender', 'clover'],
                            "source": "2",
                          },
                          {
                            "name": "A",
                            "headline": "A does X2",
                            "content": "",
                            "keywords": ['A', 'X2', 'Febtember 0', 'Planet Express', 'Fry', 'Six', 'Seasons', 'and', 'a', 'movie'],
                            "source": "3",
                          },
                        ]
category_1_second_tier =[
                          {
                            "name": "C",
                            "headline": "C does Z1",
                            "content": "",
                            "keywords": ['C', 'Z1', 'March 32', 'City', 'election', 'blackjack', 'hookers', 'space station', 'bender', 'clover'],
                            "source": "1",
                          },
                          {
                            "name": "A",
                            "headline": "A does X1",
                            "content": "",
                            "keywords": ['A', 'X1', 'February 31', 'Greendale', 'desecration', 'breaking-in', 'bender', 'murder', 'arson', 'poker'],
                            "source": "2",
                          },
                          {
                            "name": "A",
                            "headline": "A does X2",
                            "content": "",
                            "keywords": ['A', 'X2', 'Febtember 0', 'Planet Express', 'Fry', 'Six', 'Seasons', 'and', 'a', 'movie'],
                            "source": "2",
                          },
                          {
                            "name": "B",
                            "headline": "B does Y1",
                            "content": "",
                            "keywords": ['B', 'Y1', 'Hollywoob', 'Erika', 'Fring', 'Salamanca', 'Westeros', 'Red Wedding', 'Prostitutes', 'Dead'],
                            "source": "2",
                          },
                          {
                            "name": "C",
                            "headline": "C does Z2",
                            "content": "",
                            "keywords": ['C', 'Z2', 'Quasar 2000', 'Kane', 'Corleone', 'Wayne', 'Skywalker', 'HPMOR', 'Assbutt', 'San Junipero'],
                            "source": "2",
                          },
                          {
                            "name": "A",
                            "headline": "A does X1",
                            "content": "",
                            "keywords": ['A', 'X1', 'February 31', 'college', 'desecration', 'graverobbing', 'bender', 'murder', 'arson', 'cards'],
                            "source": "3",
                          },
                          {
                            "name": "C",
                            "headline": "C does Z1",
                            "content": "",
                            "keywords": ['C', 'Z1', 'March 32', 'City', 'election', 'blackjack', 'hookers', 'space station', 'bender', 'clover'],
                            "source": "3",
                          },
                        ]
category_2_first_tier = [
                          {
                            "name": "A",
                            "headline": "A does X1",
                            "content": "",
                            "keywords": ['A', 'X1', 'February 31', 'Greendale', 'election', 'desecration', 'graverobbing', 'blackout', 'murder', 'arson'],
                            "source": "4",
                          },
                          {
                            "name": "C",
                            "headline": "C does Z1",
                            "content": "",
                            "keywords": ['C', 'Z1', 'March 32', 'City', 'election', 'blackjack', 'hookers', 'space station', 'bender', 'clover'],
                            "source": "4",
                          },
                          {
                            "name": "C",
                            "headline": "C does Z1",
                            "content": "",
                            "keywords": ['C', 'Z1', 'March 32', 'City', 'election', 'blackjack', 'hookers', 'space station', 'bender', 'clover'],
                            "source": "5",
                          },
                        ]
category_2_second_tier =[
                          {
                            "name": "C",
                            "headline": "C does Z2",
                            "content": "",
                            "keywords": ['C', 'Z2', 'Quasar 2000', 'Kane', 'Corleone', 'Wayne', 'Skywalker', 'HPMOR', 'Assbutt', 'San Junipero'],
                            "source": "4",
                          },
                          {
                            "name": "A",
                            "headline": "A does X2",
                            "content": "",
                            "keywords": ['A', 'X2', 'Febtember 0', 'Planet Express', 'Fry', 'Six', 'Seasons', 'and', 'a', 'movie'],
                            "source": "4",
                          },
                          {
                            "name": "B",
                            "headline": "B does Y1",
                            "content": "",
                            "keywords": ['B', 'Y1', 'Hollywoob', 'Erika', 'Fring', 'Salamanca', 'Westeros', 'Red Wedding', 'Prostitutes', 'Dead'],
                            "source": "4",
                          },
                          {
                            "name": "A",
                            "headline": "A does X1",
                            "content": "",
                            "keywords": ['A', 'X1', 'February 31', 'Greendale', 'election', 'desecration', 'graverobbing', 'blackout', 'murder', 'arson'],
                            "source": "5",
                          },
                          {
                            "name": "A",
                            "headline": "A does X1",
                            "content": "",
                            "keywords": ['A', 'X1', 'February 31', 'Greendale', 'election', 'desecration', 'graverobbing', 'blackout', 'murder', 'arson'],
                            "source": "6",
                          },
                          {
                            "name": "A",
                            "headline": "A does X2",
                            "content": "",
                            "keywords": ['A', 'X2', 'Febtember 0', 'Planet Express', 'Fry', 'Six', 'Seasons', 'and', 'a', 'movie'],
                            "source": "6",
                          },
                        ]
category_3_first_tier = [
                          {
                            "name": "A",
                            "headline": "A does X1",
                            "content": "",
                            "keywords": ['A', 'X1', 'February 31', 'Greendale', 'election', 'desecration', 'graverobbing', 'blackout', 'murder', 'arson'],
                            "source": "7",
                          },
                          {
                            "name": "C",
                            "headline": "C does Z1",
                            "content": "",
                            "keywords": ['C', 'Z1', 'March 32', 'City', 'election', 'blackjack', 'hookers', 'space station', 'bender', 'clover'],
                            "source": "8",
                          },
                          {
                            "name": "B",
                            "headline": "B does Y1",
                            "content": "",
                            "keywords": ['B', 'Y1', 'Hollywoob', 'Erika', 'Fring', 'Salamanca', 'Westeros', 'Red Wedding', 'Prostitutes', 'Dead'],
                            "source": "9",
                          },
                        ]
category_3_second_tier =[
                          {
                            "name": "A",
                            "headline": "A does X2",
                            "content": "",
                            "keywords": ['A', 'X2', 'Febtember 0', 'Planet Express', 'Fry', 'Six', 'Seasons', 'and', 'a', 'movie'],
                            "source": "7",
                          },
                          {
                            "name": "C",
                            "headline": "C does Z1",
                            "content": "",
                            "keywords": ['C', 'Z1', 'March 32', 'City', 'election', 'blackjack', 'hookers', 'space station', 'bender', 'clover'],
                            "source": "7",
                          },
                          {
                            "name": "A",
                            "headline": "A does X1",
                            "content": "",
                            "keywords": ['A', 'X1', 'February 31', 'Greendale', 'election', 'desecration', 'graverobbing', 'blackout', 'murder', 'arson'],
                            "source": "8",
                          },
                          {
                            "name": "C",
                            "headline": "C does Z2",
                            "content": "",
                            "keywords": ['C', 'Z2', 'Quasar 2000', 'Kane', 'Corleone', 'Wayne', 'Skywalker', 'HPMOR', 'Assbutt', 'San Junipero'],
                            "source": "8",
                          },
                          {
                            "name": "B",
                            "headline": "B does Y1",
                            "content": "",
                            "keywords": ['B', 'Y1', 'Hollywoob', 'Erika', 'Fring', 'Salamanca', 'Westeros', 'Red Wedding', 'Prostitutes', 'Dead'],
                            "source": "8",
                          },
                          {
                            "name": "A does X1",
                            "headline": "",
                            "content": "",
                            "keywords": ['A', 'X1', 'February 31', 'Greendale', 'election', 'desecration', 'graverobbing', 'blackout', 'murder', 'arson'],
                            "source": "9",
                          },
                          {
                            "name": "C",
                            "headline": "C does Z1",
                            "content": "",
                            "keywords": ['C', 'Z1', 'March 32', 'City', 'election', 'blackjack', 'hookers', 'space station', 'bender', 'clover'],
                            "source": "9",
                          },
                        ]
news_items = []


#The following for loops extract the keywords of each article
'''
temp = []
for i in category_1_first_tier:
  text = i["content"]
  rake_object = rake.Rake("Rake/data/stoplists/SmartStoplist.txt", 5, 2, 1)
  keywords = rake_object.run(text)
  index = 1
  keywords_ten = [] 
  for j in keywords:
    if index > 10:
      break
    keywords_ten.append(j[0])
    index = index + 1
  i["keywords"] = keywords_ten
  temp.append(i)
category_1_first_tier = temp
temp = []
for i in category_1_second_tier:
  text = i["content"]
  rake_object = rake.Rake("Rake/data/stoplists/SmartStoplist.txt", 5, 2, 1)
  keywords = rake_object.run(text)
  index = 1
  keywords_ten = [] 
  for j in keywords:
    if index > 10:
      break
    keywords_ten.append(j[0])
    index = index + 1
  i["keywords"] = keywords_ten
  temp.append(i)
category_1_second_tier = temp
temp = []
for i in category_2_first_tier:
  text = i["content"]
  rake_object = rake.Rake("Rake/data/stoplists/SmartStoplist.txt", 5, 2, 1)
  keywords = rake_object.run(text)
  index = 1
  keywords_ten = [] 
  for j in keywords:
    if index > 10:
      break
    keywords_ten.append(j[0])
    index = index + 1
  i["keywords"] = keywords_ten
  temp.append(i)
category_2_first_tier = temp
temp = []
for i in category_2_second_tier:
  text = i["content"]
  rake_object = rake.Rake("Rake/data/stoplists/SmartStoplist.txt", 5, 2, 1)
  keywords = rake_object.run(text)
  index = 1
  keywords_ten = [] 
  for j in keywords:
    if index > 10:
      break
    keywords_ten.append(j[0])
    index = index + 1
  i["keywords"] = keywords_ten
  temp.append(i)
category_2_second_tier = temp
temp = []
for i in category_3_first_tier:
  text = i["content"]
  rake_object = rake.Rake("Rake/data/stoplists/SmartStoplist.txt", 5, 2, 1)
  keywords = rake_object.run(text)
  index = 1
  keywords_ten = [] 
  for j in keywords:
    if index > 10:
      break
    keywords_ten.append(j[0])
    index = index + 1
  i["keywords"] = keywords_ten
  temp.append(i)
category_3_first_tier = temp
temp = []
for i in category_3_second_tier:
  text = i["content"]
  rake_object = rake.Rake("Rake/data/stoplists/SmartStoplist.txt", 5, 2, 1)
  keywords = rake_object.run(text)
  index = 1
  keywords_ten = [] 
  for j in keywords:
    if index > 10:
      break
    keywords_ten.append(j[0])
    index = index + 1
  i["keywords"] = keywords_ten
  temp.append(i)
category_3_second_tier = temp
'''

#The following for loops find unique news items among the articles, and calculates percentages and prominences

while len(category_1_first_tier) > 0:
  i = category_1_first_tier[0]
  keywords = i["keywords"]
  equal = 0
  item = {"name": i["name"], "headline": i["headline"], "content": i["content"], "ppeo": 0, "speo": 0, "tpeo": 0, "ppro": 0, "spro": 0, "tpro": 0, 
  				"primary_percentage": 0, "secondary_percentage": 0, "tertiary_percentage": 0, "primary_prominence": 0, "secondary_prominence": 0, 
  				"tertiary_prominence": 0, "importance": 10, "primary_sources": [], "secondary_sources": [], "tertiary_sources": []}

  temp = category_1_first_tier[:]
  for j in category_1_first_tier:
    no = len(set(keywords).intersection(set(j["keywords"])))
    if no > 6:
      item["ppeo"] = item["ppeo"] + 1.0
      item["ppro"] = item["ppro"] + 2.0
      item["primary_sources"].append(j["source"])
      temp.remove(j)
  category_1_first_tier = temp[:]
  temp = category_1_second_tier[:]
  for j in category_1_second_tier:
    no = len(set(keywords).intersection(set(j["keywords"])))
    if no > 6 and j["source"] not in item["primary_sources"]:
      item["ppeo"] = item["ppeo"] + 1.0
      item["ppro"] = item["ppro"] + 1.0
      item["primary_sources"].append(j["source"])
      temp.remove(j)
  category_1_second_tier = temp
  item["primary_percentage"] = item["ppeo"]/3
  item["primary_prominence"] = item["ppro"]/len(item["primary_sources"])

  temp = category_2_first_tier[:]
  for j in category_2_first_tier:
    no = len(set(keywords).intersection(set(j["keywords"])))
    if no > 6:
      item["speo"] = item["speo"] + 1.0
      item["spro"] = item["spro"] + 2.0
      item["secondary_sources"].append(j["source"])
      temp.remove(j)
  category_2_first_tier = temp[:]
  temp = category_2_second_tier[:]
  for j in category_2_second_tier:
    no = len(set(keywords).intersection(set(j["keywords"])))
    if no > 6 and j["source"] not in item["secondary_sources"]:
      item["speo"] = item["speo"] + 1.0
      item["spro"] = item["spro"] + 1.0
      item["secondary_sources"].append(j["source"])
      temp.remove(j)
  category_2_second_tier = temp[:]
  item["secondary_percentage"] = item["speo"]/3
  if len(item["secondary_sources"]) != 0:
  	item["secondary_prominence"] = item["spro"]/len(item["secondary_sources"])

  temp = category_3_first_tier[:]
  for j in category_3_first_tier:
    no = len(set(keywords).intersection(set(j["keywords"])))
    if no > 6:
      item["tpeo"] = item["tpeo"] + 1.0
      item["tpro"] = item["tpro"] + 2.0
      item["tertiary_sources"].append(j["source"])
      temp.remove(j)
  category_3_first_tier = temp[:]
  temp = category_3_second_tier[:]
  for j in category_3_second_tier:
    no = len(set(keywords).intersection(set(j["keywords"])))
    if no > 6 and j["source"] not in item["tertiary_sources"]:
      item["tpeo"] = item["tpeo"] + 1.0
      item["tpro"] = item["tpro"] + 1.0
      item["tertiary_sources"].append(j["source"])
      temp.remove(j)
  category_3_second_tier = temp[:]
  item["tertiary_percentage"] = item["tpeo"]/3
  if len(item["tertiary_sources"]) != 0:
  	item["tertiary_prominence"] = item["tpro"]/len(item["tertiary_sources"])

  del item["ppeo"]
  del item["ppro"]
  del item["speo"]
  del item["spro"]
  del item["tpeo"]
  del item["tpro"]

  news_items.append(item)

while len(category_1_second_tier) > 0:
  i = category_1_second_tier[0]
  keywords = i["keywords"]
  equal = 0
  item = {"name": i["name"], "headline": i["headline"], "content": i["content"], "ppeo": 0, "speo": 0, "tpeo": 0, "ppro": 0, "spro": 0, "tpro": 0, 
  				"primary_percentage": 0, "secondary_percentage": 0, "tertiary_percentage": 0, "primary_prominence": 0, "secondary_prominence": 0, 
  				"tertiary_prominence": 0, "importance": 10, "primary_sources": [], "secondary_sources": [], "tertiary_sources": []}

  temp = category_1_second_tier[:]
  for j in category_1_second_tier:
    no = len(set(keywords).intersection(set(j["keywords"])))
    if no > 6:
      item["ppeo"] = item["ppeo"] + 1.0
      item["ppro"] = item["ppro"] + 1.0
      item["primary_sources"].append(j["source"])
      temp.remove(j)
  category_1_second_tier = temp[:]
  item["primary_percentage"] = item["ppeo"]/3
  item["primary_prominence"] = item["ppro"]/len(item["primary_sources"])

  temp = category_2_first_tier[:]
  for j in category_2_first_tier:
    no = len(set(keywords).intersection(set(j["keywords"])))
    if no > 6:
      item["speo"] = item["speo"] + 1.0
      item["spro"] = item["spro"] + 2.0
      item["secondary_sources"].append(j["source"])
      temp.remove(j)
  category_2_first_tier = temp[:]
  temp = category_2_second_tier[:]
  for j in category_2_second_tier:
    no = len(set(keywords).intersection(set(j["keywords"])))
    if no > 6 and j["source"] not in item["secondary_sources"]:
      item["speo"] = item["speo"] + 1.0
      item["spro"] = item["spro"] + 1.0
      item["secondary_sources"].append(j["source"])
      temp.remove(j)
  category_2_second_tier = temp[:]
  item["secondary_percentage"] = item["speo"]/3
  if len(item["secondary_sources"]) != 0:
  	item["secondary_prominence"] = item["spro"]/len(item["secondary_sources"])

  temp = category_3_first_tier[:]
  for j in category_3_first_tier:
    no = len(set(keywords).intersection(set(j["keywords"])))
    if no > 6:
      item["tpeo"] = item["tpeo"] + 1.0
      item["tpro"] = item["tpro"] + 2.0
      item["tertiary_sources"].append(j["source"])
      temp.remove(j)
  category_3_first_tier = temp[:]
  temp = category_3_second_tier[:]
  for j in category_3_second_tier:
    no = len(set(keywords).intersection(set(j["keywords"])))
    if no > 6 and j["source"] not in item["tertiary_sources"]:
      item["tpeo"] = item["tpeo"] + 1.0
      item["tpro"] = item["tpro"] + 1.0
      item["tertiary_sources"].append(j["source"])
      temp.remove(j)
  category_3_second_tier = temp[:]
  item["tertiary_percentage"] = item["tpeo"]/3
  if len(item["tertiary_sources"]) != 0:
  	item["tertiary_prominence"] = item["tpro"]/len(item["tertiary_sources"])

  del item["ppeo"]
  del item["ppro"]
  del item["speo"]
  del item["spro"]
  del item["tpeo"]
  del item["tpro"]

  news_items.append(item)

while len(category_2_first_tier) > 0:
  i = category_2_first_tier[0]
  keywords = i["keywords"]
  equal = 0
  item = {"name": i["name"], "headline": i["headline"], "content": i["content"], "ppeo": 0, "speo": 0, "tpeo": 0, "ppro": 0, "spro": 0, "tpro": 0, 
  				"primary_percentage": 0, "secondary_percentage": 0, "tertiary_percentage": 0, "primary_prominence": 0, "secondary_prominence": 0, 
  				"tertiary_prominence": 0, "importance": 10, "primary_sources": [], "secondary_sources": [], "tertiary_sources": []}

  temp = category_2_first_tier[:]
  for j in category_2_first_tier:
    no = len(set(keywords).intersection(set(j["keywords"])))
    if no > 6:
      item["speo"] = item["speo"] + 1.0
      item["spro"] = item["spro"] + 2.0
      item["secondary_sources"].append(j["source"])
      temp.remove(j)
  category_2_first_tier = temp[:]
  temp = category_2_second_tier[:]
  for j in category_2_second_tier:
    no = len(set(keywords).intersection(set(j["keywords"])))
    if no > 6 and j["source"] not in item["secondary_sources"]:
      item["speo"] = item["speo"] + 1.0
      item["spro"] = item["spro"] + 1.0
      item["secondary_sources"].append(j["source"])
      temp.remove(j)
  category_2_second_tier = temp[:]
  item["secondary_percentage"] = item["speo"]/3
  if len(item["secondary_sources"]) != 0:
  	item["secondary_prominence"] = item["spro"]/len(item["secondary_sources"])

  temp = category_3_first_tier[:]
  for j in category_3_first_tier:
    no = len(set(keywords).intersection(set(j["keywords"])))
    if no > 6:
      item["tpeo"] = item["tpeo"] + 1.0
      item["tpro"] = item["tpro"] + 2.0
      item["tertiary_sources"].append(j["source"])
      temp.remove(j)
  category_3_first_tier = temp[:]
  temp = category_3_second_tier[:]
  for j in category_3_second_tier:
    no = len(set(keywords).intersection(set(j["keywords"])))
    if no > 6 and j["source"] not in item["tertiary_sources"]:
      item["tpeo"] = item["tpeo"] + 1.0
      item["tpro"] = item["tpro"] + 1.0
      item["tertiary_sources"].append(j["source"])
      temp.remove(j)
  category_3_second_tier = temp[:]
  item["tertiary_percentage"] = item["tpeo"]/3
  if len(item["tertiary_sources"]) != 0:
  	item["tertiary_prominence"] = item["tpro"]/len(item["tertiary_sources"])

  del item["ppeo"]
  del item["ppro"]
  del item["speo"]
  del item["spro"]
  del item["tpeo"]
  del item["tpro"]

  news_items.append(item)

while len(category_2_second_tier) > 0:
  i = category_2_second_tier[0]
  keywords = i["keywords"]
  equal = 0
  item = {"name": i["name"], "headline": i["headline"], "content": i["content"], "ppeo": 0, "speo": 0, "tpeo": 0, "ppro": 0, "spro": 0, "tpro": 0, 
  				"primary_percentage": 0, "secondary_percentage": 0, "tertiary_percentage": 0, "primary_prominence": 0, "secondary_prominence": 0, 
  				"tertiary_prominence": 0, "importance": 10, "primary_sources": [], "secondary_sources": [], "tertiary_sources": []}

  temp = category_2_second_tier[:]
  for j in category_2_second_tier:
    no = len(set(keywords).intersection(set(j["keywords"])))
    if no > 6 and j["source"] not in item["secondary_sources"]:
      item["speo"] = item["speo"] + 1.0
      item["spro"] = item["spro"] + 1.0
      item["secondary_sources"].append(j["source"])
      temp.remove(j)
  category_2_second_tier = temp[:]
  item["secondary_percentage"] = item["speo"]/3
  if len(item["secondary_sources"]) != 0:
  	item["secondary_prominence"] = item["spro"]/len(item["secondary_sources"])

  temp = category_3_first_tier[:]
  for j in category_3_first_tier:
    no = len(set(keywords).intersection(set(j["keywords"])))
    if no > 6:
      item["tpeo"] = item["tpeo"] + 1.0
      item["tpro"] = item["tpro"] + 2.0
      item["tertiary_sources"].append(j["source"])
      temp.remove(j)
  category_3_first_tier = temp[:]
  temp = category_3_second_tier[:]
  for j in category_3_second_tier:
    no = len(set(keywords).intersection(set(j["keywords"])))
    if no > 6 and j["source"] not in item["tertiary_sources"]:
      item["tpeo"] = item["tpeo"] + 1.0
      item["tpro"] = item["tpro"] + 1.0
      item["tertiary_sources"].append(j["source"])
      temp.remove(j)
  category_3_second_tier = temp[:]
  item["tertiary_percentage"] = item["tpeo"]/3
  if len(item["tertiary_sources"]) != 0:
  	item["tertiary_prominence"] = item["tpro"]/len(item["tertiary_sources"])

  del item["ppeo"]
  del item["ppro"]
  del item["speo"]
  del item["spro"]
  del item["tpeo"]
  del item["tpro"]

  news_items.append(item)

while len(category_3_first_tier) > 0:
  i = category_3_first_tier[0]
  keywords = i["keywords"]
  equal = 0
  item = {"name": i["name"], "headline": i["headline"], "content": i["content"], "ppeo": 0, "speo": 0, "tpeo": 0, "ppro": 0, "spro": 0, "tpro": 0, 
  				"primary_percentage": 0, "secondary_percentage": 0, "tertiary_percentage": 0, "primary_prominence": 0, "secondary_prominence": 0, 
  				"tertiary_prominence": 0, "importance": 10, "primary_sources": [], "secondary_sources": [], "tertiary_sources": []}

  temp = category_3_first_tier[:]
  for j in category_3_first_tier:
    no = len(set(keywords).intersection(set(j["keywords"])))
    if no > 6:
      item["tpeo"] = item["tpeo"] + 1.0
      item["tpro"] = item["tpro"] + 2.0
      item["tertiary_sources"].append(j["source"])
      temp.remove(j)
  category_3_first_tier = temp[:]
  temp = category_3_second_tier[:]
  for j in category_3_second_tier:
    no = len(set(keywords).intersection(set(j["keywords"])))
    if no > 6 and j["source"] not in item["tertiary_sources"]:
      item["tpeo"] = item["tpeo"] + 1.0
      item["tpro"] = item["tpro"] + 1.0
      item["tertiary_sources"].append(j["source"])
      temp.remove(j)
  category_3_second_tier = temp[:]
  item["tertiary_percentage"] = item["tpeo"]/3
  if len(item["tertiary_sources"]) != 0:
  	item["tertiary_prominence"] = item["tpro"]/len(item["tertiary_sources"])

  del item["ppeo"]
  del item["ppro"]
  del item["speo"]
  del item["spro"]
  del item["tpeo"]
  del item["tpro"]

  news_items.append(item)

while len(category_3_second_tier) > 0:
  i = category_3_second_tier[0]
  keywords = i["keywords"]
  equal = 0
  item = {"name": i["name"], "headline": i["headline"], "content": i["content"], "ppeo": 0, "speo": 0, "tpeo": 0, "ppro": 0, "spro": 0, "tpro": 0, 
  				"primary_percentage": 0, "secondary_percentage": 0, "tertiary_percentage": 0, "primary_prominence": 0, "secondary_prominence": 0, 
  				"tertiary_prominence": 0, "importance": 10, "primary_sources": [], "secondary_sources": [], "tertiary_sources": []}

  temp = category_3_second_tier[:]
  for j in category_3_second_tier:
    no = len(set(keywords).intersection(set(j["keywords"])))
    if no > 6 and j["source"] not in item["tertiary_sources"]:
      item["tpeo"] = item["tpeo"] + 1.0
      item["tpro"] = item["tpro"] + 1.0
      item["tertiary_sources"].append(j["source"])
      temp.remove(j)
  category_3_second_tier = temp[:]
  item["tertiary_percentage"] = item["tpeo"]/3
  if len(item["tertiary_sources"]) != 0:
  	item["tertiary_prominence"] = item["tpro"]/len(item["tertiary_sources"])

  del item["ppeo"]
  del item["ppro"]
  del item["speo"]
  del item["spro"]
  del item["tpeo"]
  del item["tpro"]

  news_items.append(item)


output = [] # Ordered by lowest importance factor. Each entry contains name, headline, and importance.
remove = [] # Used to remove news items from the list after added to output.

def update(): # Updates every second

  for i in news_items: # Calculating importance of news items
    primary_percentage = i["primary_percentage"]
    secondary_percentage = i["secondary_percentage"]
    tertiary_percentage = i["tertiary_percentage"]
    l = [4 * primary_percentage, 2 * secondary_percentage, tertiary_percentage]
    max_l = max(l)
    if max_l == 4 * primary_percentage:
      category = 5
      prominence = i["primary_prominence"]
      if primary_percentage * category * prominence != 0:
        i["importance"] = i["importance"] / (primary_percentage * category * prominence)
    elif max_l == 2 * secondary_percentage:
      category = 3
      prominence = i["secondary_prominence"]
      if secondary_percentage * category * prominence != 0:
        i["importance"] = i["importance"] / (secondary_percentage * category * prominence)
    else:
      category = 1
      prominence = i["tertiary_prominence"]
      if tertiary_percentage * category * prominence != 0:
        i["importance"] = i["importance"] / (tertiary_percentage * category * prominence)

  news_items.sort(key = lambda x: x["importance"])

  for i in news_items: # Creating output
    name = i["name"]
    importance = i["importance"]
    new = {"name": name, "headline": i["headline"], "importance": importance}
    index = 0
    for j in people:
      if j["name"] == name:
        person = j
        threshold = j["threshold"]
        break
      index = index + 1
    if importance < threshold:
      output.append(new)
      people[index]["threshold"] = threshold/importance
      remove.append(i) 

  for i in remove:
    news_items.remove(i)

  for i in people:
    i["threshold"] = i["threshold"] * 1.0000046929
  
  print(output)

update()