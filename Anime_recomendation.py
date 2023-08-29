import random
import pandas as pd
#List of animes
Series = pd.read_csv('C:/Users/gaspa/Desktop/Anime_recomendation/all_animes.csv')
GENRES = ["Thriller", "Supernatural", "Sports", "Slice of Life", "Shonen", "Shojo", "Seinen", "Sci-fi", "Romance", "Music","Post Apocalyptic", "Mistery", "Mecha", "Magical Girls", "Isekai", "Idols", "Historical", "Harem", "Fantasy", "Drama", "Comedy", "Adventure", "Action"]
expressions= [['idk','show','me','something'],['whatever'],['what','ever'],['i','dont','know'],['show','me','something']]
excluded_words= ['anime', 'animes']

#Ask to the user what do the user want to see
def Question():
    answer = ""
    while answer not in GENRES:
        if answer not in GENRES and answer != '':
            print("{} is an Invalid Option".format(answer))
        print("The Genere's are: Thriller, Supernatural, Sports, Slice Of Life, Shonen, Shojo, Seinen, Sci-fi, Romance, Music,""\n" "Post-Apocalyptic, Mistery,Mecha, Magical Girls, Isekai, Idols, Historical, Harem, Fantasy, Drama, Comedy,""\n"" Adventure, Action")
        answer = input("What do you want to watch? ")
        if answer in expressions:
            break
    return answer

def answer_filter(answer):
    answer= answer.split(" ")
    for item in answer:
        if item == "":
            answer.delete(item)
    if answer[1] in excluded_words:
        answer = answer[0]
        
    return answer

def selection(answer, GENRES, Series):
    recomendation = None
    if answer in GENRES:
        recomendation = Series[answer][pick_anime(answer)]
    elif answer in expressions:
        recomendation = Series[GENRES[random.randint(0,len(GENRES))]][pick_anime(answer)]
    return recomendation

#aswers corrections
def question_filter(answer):
    if answer == 'super natural':
        answer = 'supernatural'
    elif answer == 'post apocalyptic':
        answer = 'post-apocalyptic'

    elif answer == 'magical girl':
        answer = 'magical-girl'

    elif answer == 'sci fi':
        answer = 'sci-fi'
    else:
        answer= 'slice-of-life'
    return answer

#Pick an anime
def pick_anime(genre):
    return random.randint(0,len(genre))

#Show the data
def show_the_data(recomendation):
    print("The recomoendation is '{}', have {} and is {} ".format(recomendation[0],recomendation[2],recomendation[1]))
    input('Press enter to exit')



#choose the genre
answer = Question()
#selection
recomendation = selection(answer, GENRES, Series)

#Shows the Anime
show_the_data(recomendation)

