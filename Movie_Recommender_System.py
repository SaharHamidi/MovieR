
#movies={"movie name":[year,IMDB ratings,director,cast,genre,time,series or movies,rotten tomatoes]}
movies={"Inception":[2010,9,"Christopher Nolan",["Leonardo Dicaprio","Cillian Murphy","Tom Hardy"],["action","sci-fi"],148,'m',87],
        "The dark knight":[2008,9,"Christopher Nolan",["Christian Bale","Heath Ledger","Gary Oldman"],["action","crime"],152,'m',84],
        "Interstellar":[2014,9,"Christopher Nolan",["Matthew McConaughey","Jessica Chastain","Anne Hathaway"],["adventure","sci-fi"],168,'m',73],
        "Arrival":[2016,8,"Denis Villeleuve",["Jeremy Rennner","Amy Adams","Michael Stuhlbarg"],["mystery","sci-fi"],116,'m',94],
        "Little women":[2019,8,"Greta Gerwig",["Saoirse Ronan","Timothee Challamet","Florance Pugh","Emma Watson"],["romance","drama"],135,'m',95],
        "Harry Potter":[2001,8,"Chris Columbus",["Daniel Radcliffe","Emma Watson","Rupert Grint"],["fantasy","drama"],1172,'s',84]}


def welcome_page():
    print("\n")
    print("\t\t********** Welcome to movie club! **********")
    print("\t\t------------------------------------------")
    input("\t\t\t  Press enter to continue...\n")

def create_profile(profile={}):

    profile['Name'] = input("What is your first name?:")
    while (type(profile['Name'])!=str or profile['Name'].isalpha()==False):
        profile['Name'] = input("-Please enter a valid first name:")

    profile['LastName'] = input("What is your Last name?:")
    while (type(profile['LastName'])!=str or profile['LastName'].isalpha()==False):
        profile['LastName'] = input("-Please enter a valid last name:")

    profile['Age'] = input("How old are you?:")
    while (profile['Age'].isnumeric()==False or int(profile['Age'])>125 or int(profile['Age'])<1):
        profile['Age'] = input("-Please enter a valid number:")
    
    profile['Email'] = input("What is your email?:")
    #while (profile['Email'].endswith('@gmail.com',-10,-1)==False or profile['Email'].endswith('@yahoo.com',-10,-1)==False):
        #profile['Email'] = input(" Please enter a valid email ending with @gmail.com or @yahoo.com : ")
    #install re module 
    profile['PhoneNumber'] = input ("What is your phone number?:")
    while (profile['PhoneNumber'].isnumeric()==False or len(profile['PhoneNumber'])>15 or len(profile['PhoneNumber'])<6):
        profile['PhoneNumber'] = input("-Please enter a valid phone number:")
    
def show_profile(profile={}):
    print("\nYour profile:")
    for key, value in profile.items():
        print(f"{key}: {value}")

def confirmation(profile={},fav=[]):
    confirm = input("Is the information correct?(yes/no)") 
    if confirm.lower() == 'no':
        profile={}
        create_profile(profile)
        show_profile(profile)
        confirmation(profile,fav)
    elif confirm.lower() == 'yes':
        questionnaire(fav)
    else:
        confirmation(profile,fav)
        
        
def verify_information(profile={},fav=[]):
    confirm = input("Press v to verify your information or press s to skip:")
    if confirm.lower() == 'v':
        show_profile(profile)
        confirmation(profile,fav)
    elif confirm.lower() == 's':
        questionnaire(fav)
    else:
        verify_information(profile,fav)

def questionnaire(favourites=[]): 

    print("\nLet's find out what your preferences are.")
    print("Please answer the next 10 questions by choosing one of the options below.")
    print("(for example:a)\n")

    #question 1
    print("1)I want to watch a movie from ...?\na)this year\nb)the past 2 years\nc)the past 5 years\nd)the past 10 years\n")
    answer=(input("answer:"))
    while answer!='a' and answer!='b' and  answer!='c' and answer!='d' :
        answer=input("Please choose one of the options:\n") 
    if answer=='a':
        favourites.append("2024")
    elif answer=='b':
        favourites.append("2022")
    elif answer=='c':
        favourites.append("2019")
    else:
        favourites.append("2014")
    
    #question 2
    print("\n2)Which rating do you think is most valid?\na)IMDB\nb)Rotten Tomatos\nc)neither\nd)both\n")
    answer=(input("answer:"))
    while answer!='a' and answer!='b' and  answer!='c' and answer!='d':
        answer=input("Please choose one of the options:\n") 
    if answer=='a':
        favourites.append("IMDB")
    elif answer=='b':
        favourites.append("Rotten Tomatos")
    elif answer=='c':
        favourites.append("neither")
    else :
        favourites.append("both")
      
    #question 3
    print("\n3)Which one of the directors below would you want to meet in real life?")
    print("a)Steven Spielberg\nb)Martin Scorsese\nc)Quentin Tarantino\nd)Christopher Nolan\n")
    answer=(input("answer:"))
    while answer!='a' and answer!='b' and  answer!='c' and answer!='d' :
        answer=input("Please choose one of the options:\n")
    favourites.append(answer)
    
    #question 4
    print("\n4)Which one of these actors/actresses have you previously seen in a movie?\na)Tom Hanks\nb)Meryl Streep\nc)Leonardo Dicaprio\nd)none\n")
    answer=(input("answer:"))
    while answer!='a' and answer!='b' and  answer!='c' and answer!='d' :
        answer=input("Please choose one of the options:\n")
    favourites.append(answer)
    
    #question 5
    print("\n5)Choose two of the genres below that you enjoy the most:\na)comedy\nb)action\nc)drama\nd)horror\n")
    answer=(input("answer:"))
    while answer!='a' and answer!='b' and  answer!='c' and answer!='d' :
        answer=input("Please choose one of the options:\n")
    favourites.append(answer)

    #question 6
    print("\n6)What is your preferred movie length?\na)a shorter film(~90 minutes)\nb)average length(~1.5 to 2 hours)\nc)a long movie(~2.5 hours or more)\n")
    answer=(input("answer:"))
    while answer!='a' and answer!='b' and  answer!='c':
        answer=input("Please choose one of the options:\n") 
    if answer=='a':
        favourites.append(90)
    elif answer=='b':
        favourites.append(120)
    else:
        favourites.append(1000)
    
    #question 7
    print("\n7)Which one of these plots seems more interesting to you?\na)A mafia patriarch transfers control of his empire to his reluctant son")
    print("b)A tragic love stroy unfolds abroad the ill-fated Titanic ship")
    print("c)Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency")
    print("d)Genetically engineered dinosaurs wreak havoc after scaping in a theme park preview\n")
    answer=(input("answer:"))
    while answer!='a' and answer!='b' and  answer!='c' and answer!='d' :
        answer=input("Please choose one of the options:\n") 
    if answer=='a':
        favourites.append("Godfather")
    elif answer=='b':
        favourites.append("Titanic")
    elif answer=='c':
        favourites.append("Shawshank redemption")
    else :
        favourites.append("Jurassic park")

    #question 8
    print("\n8)What experience are you looking for when watching a movie?\na)a relaxing time\nb)a new concept to think about\nc)to learn about people and life")
    print("d)excitement or fun\n")
    answer=(input("answer:"))
    while answer!='a' and answer!='b' and  answer!='c' and answer!='d' :
        answer=input("Please choose one of the options:\n")
    if answer=='a':
        favourites.append(["romance","comedy"])
    elif answer=='b':
        favourites.append(["psychology"])
    elif answer=='c':
        favourites.append(["biography","drama"])
    else :
        favourites.append(["comedy","adventure","horror","sci-fi","crime","thriller"])

    #question 9
    print("\n9)Are you in the mood for something light-hearted or serious?\na)light-hearted\nb)serious\n")
    answer=(input("answer:"))
    while answer!='a' and answer!='b':
        answer=input("Please choose one of the options:\n") 
    if answer=='a':
        favourites.append(["romance","comedy","biography","adventure"])
    else :
        favourites.append(["horror","sci-fi","crime","thriller","sci-fi"])

    #question 10
    print("\n10) Do you prefer stand-alone movies or series?\na)films\nb)series\nc)neither\nd)both\n")
    answer=(input("answer:"))
    while answer!='a' and answer!='b' and  answer!='c' and answer!='d' :
        answer=input("Please choose one of the options:\n")
    if answer=='a':
        favourites.append('s')
    elif answer=='b':
        favourites.append('m')
    
def max_index(points=[]):
    max=0
    count=0
    for i in points:
        if i>=max:
            max=i
            index=count
        count+=1
    points.remove(max)
    return index

#ranking movies based on user's answers
def compare(movies=[],fav=[],points=[]):
    m_index=0 #index of each movie
    for i in movies:
        #year
        if int(movies[i][0])>=int(fav[0]):
            points[m_index]+=1
        #IMDB / RT / neither / both
        if fav[1]=="IMDB":
            if int(movies[i][1])>=8:
                points[m_index]+=1
        elif fav[1]=="Rotten Tomatos":
            if int(movies[i][7])>=80:
                points[m_index]+=1
        elif fav[1]=="both":
            if int(movies[i][1])>=8:
                points[m_index]+=1
            if int(movies[i][7])>=80:
                points[m_index]+=1
        #director
        if fav[2]==movies[i][2]:
            points[m_index]+=1
        #cast
        for j in range(len(movies[i][3])):
            if fav[3]==movies[i][3][j]:
                points[m_index]+=1
        #genre
        for j in range(len(movies[i][4])):
            if fav[4]==movies[i][4][j]:
                points[m_index]+=1
        #movie length
        if int(movies[i][5])<=int(fav[5]):
            points[m_index]+=1
        #plots
        if movies[i]==fav[6]:
            points[m_index]+=1
        #experience
        for j in range(len(movies[i][4])):
            for k in range(len(fav[7])):
                if movies[i][4][j]==fav[7][k]:
                    points[m_index]+=1
        #mood
        for j in range(len(movies[i][4])):
            for k in range(len(fav[8])):
                if movies[i][4][j]==fav[8][k]:
                    points[m_index]+=1
        #series or movies
        if movies[i][6]==fav[9]:
            points[m_index]+=1

        m_index+=1 #next movie

#starting,creating a profile,verifying the info,finding out the user's taste.
profile = {}
welcome_page()
create_profile(profile)
show_profile(profile)

favs=[] #list of user's favourites
verify_information(profile,favs)

#assigning points to each movie
points=[] 
#initial points = 0
for i in range(20):
    num=int(0)
    points.append(num)
    print("\ninitial points = ",points[i])

#assigning points:
compare(movies,favs,points)
        
#presenting top 5 movies
print("\n5 Movies that you might enjoy:")
for i in range(0,5):
    index=max_index(points) 
    print(index)
