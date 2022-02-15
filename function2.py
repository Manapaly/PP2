import random  
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
movie = random.choice(movies)

def true_imdb(movie):
    if movie['imdb'] >= 5.5: print(movie['name'] + ' imdb more than 5.5')
    else: print(movie['name'] + ' imdb less than 5.5')
# true_imdb(movie)

def popular_movie(movies):
    result = []
    for i in movies:
        if i['imdb']>=5.5: result.append(i['name'])
    return result
# print(popular_movie(movies))

def category_list(s):
    result = [] 
    for i in movies:
        if i['category'] == s : result.append(i['name'])
    return result
# print(category_list('Romance'))

def average(movies):
    cnt = 0
    total_imdb = 0
    for i in movies:
        cnt += 1
        total_imdb += i['imdb']
    return total_imdb/cnt
# print(average(movies))

def average_of_category(category):
    res = []
    for i in movies:
        if i['category']==category: res.append(i)
    return average(res)
# print(average_of_category('Romance'))