#from math import *
#previous line imports all functions from amth library
#import math as m
#.m for functions

#n#movies={"movie name":[year,IMDB,director,cast,genre,time,rotten tomatoes]}
movies={"Inception":[2010,9,"Christopher_Nolan",["Leonardo_Dicaprio","Cillian_Murphy","Tom_Hardy"],["action","sci-fi"],148,87],
        "The_dark_knight":[2008,9,"Christopher_Nolan",["Christian_Bale","Heath_Ledger","Gary_Oldman"],["action","crime"],152,84],
        "Interstellar":[2014,9,"Christopher_Nolan",["Matthew_McConaughey","Jessica_Chastain","Anne_Hathaway"],["Adventure","sci-fi"],168,73],
        "Arrival":[2016,8,"Denis_Villeleuve",["Jeremy_Rennner","Amy_Adams","Michael_Stuhlbarg"],["mystery","sci-fi"],116,94],
        "Little_women":[2019,8,"Greta_Gerwig",["Saoirse_Ronan","Timothee_Challamet","Florance_Pugh","Emma_Watson"],["romance","drama"],135,95]}
#series={"movie name":[year,IMDB,director,cast,genre,time,rotten tomatoes]}
series={"Harry_Potter":[2001,8,"Chris_Columbus",["Daniel_Radcliffe","Emma_Watson","Rupert_Grint"],["fantasy","drama"],1172,84]}

print("\n")
print("\t\t**********Welcome to movie club!**********")
print("\t\t------------------------------------------")
print("\t\t\t  Press any key to continue...")
input()
#creat profile
profile = {}

#get information 
profile['Name'] = input(" What is your name? : ")
profile['LastName'] = input(" What is your LastName? : ")
profile['Age'] = input(" How old are you? : ")
profile['Email'] = input(" What is your email? : ")
profile['PhoneNumber'] = input ("What is your phone number? :")
#print profile
print("\n your profile:")
for key, value in profile.items():
    print(f"{key}: {value}")

#verify information
    confirmation = input("press v to verify your information: ")
    if confirmation.lower() == 'v':
        print("\n your profile:")
        for key, value in profile.items():
            print(f"{key}: {value}")
        break

#confrim information
    confirmation = input("Is it true?(Yes/No)")
    if confirmation.lower() == 'Yes':
        break

#names={"a":"reza"}
#print(names["a"])

#fake comment to check github
#second fake comment