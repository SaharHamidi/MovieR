
#movies={"movie name":[year,IMDB ratings,director,cast,genre,time,rotten tomatoes]}
movies={"Inception":[2010,9,"Christopher_Nolan",["Leonardo_Dicaprio","Cillian_Murphy","Tom_Hardy"],["action","sci-fi"],148,87],
        "The_dark_knight":[2008,9,"Christopher_Nolan",["Christian_Bale","Heath_Ledger","Gary_Oldman"],["action","crime"],152,84],
        "Interstellar":[2014,9,"Christopher_Nolan",["Matthew_McConaughey","Jessica_Chastain","Anne_Hathaway"],["Adventure","sci-fi"],168,73],
        "Arrival":[2016,8,"Denis_Villeleuve",["Jeremy_Rennner","Amy_Adams","Michael_Stuhlbarg"],["mystery","sci-fi"],116,94],
        "Little_women":[2019,8,"Greta_Gerwig",["Saoirse_Ronan","Timothee_Challamet","Florance_Pugh","Emma_Watson"],["romance","drama"],135,95]}
#series={"movie name":[year,IMDB,director,cast,genre,time,rotten tomatoes]}
series={"Harry_Potter":[2001,8,"Chris_Columbus",["Daniel_Radcliffe","Emma_Watson","Rupert_Grint"],["fantasy","drama"],1172,84]}


def welcome_page():
    print("\n")
    print("\t\t********** Welcome to movie club! **********")
    print("\t\t------------------------------------------")
    input("\t\t\t  Press enter to continue...\n")

def create_profile(profile={}):
    
    profile['Name'] = input("What is your name?:")
    while (type(profile['Name'])!=str or profile['Name'].isalpha()==False):
        profile['Name'] = input(" Please enter a valid name:")

    profile['LastName'] = input("What is your Last name?:")
    while (type(profile['LastName'])!=str or profile['LastName'].isalpha()==False):
        profile['LastName'] = input(" Please enter a valid last name:")

    profile['Age'] = input("How old are you?:")
    while (profile['Age'].isnumeric()==False or int(profile['Age'])>125 or int(profile['Age'])<1):
        profile['Age'] = input(" Please enter a valid number:")
    
    profile['Email'] = input("What is your email?:")
    #while (profile['Email'].endswith('@gmail.com',-10,-1)==False or profile['Email'].endswith('@yahoo.com',-10,-1)==False):
        #profile['Email'] = input(" Please enter a valid email ending with @gmail.com or @yahoo.com : ")
    #install re module 
    profile['PhoneNumber'] = input ("What is your phone number?:")
    while (profile['PhoneNumber'].isnumeric()==False or len(profile['PhoneNumber'])>15 or len(profile['PhoneNumber'])<11):
        profile['PhoneNumber'] = input(" Please enter a valid phone number:")
    
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
    confirm = input("press v to verify your information or press s to skip:")
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
        input("Please enter a valid choice:\n") 
    if answer=='a':
        favourites.append("2024")
    elif answer=='b':
        favourites.append("2022")
    elif answer=='c':
        favourites.append("2019")
    else :
        favourites.append("2014")
    

    #question 2
    print("\n2)Which rating do you think is most valid?\na)IMDB\nb)Rotten Tomatos\nc)neither\nd)both\n")
    answer=(input("answer:"))
    while answer!='a' and answer!='b' and  answer!='c' and answer!='d' :
        input("Please enter a valid choice:\n") 
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
    favourites.append(input("answer:"))
    
    
    #question 4
    print("\n4)Which one of these actors/actresses have you previously seen in a movie)Tom Hanks\nb)Meryl Streep\nc)Leonardo Dicaprio\nd)none\n")
    favourites.append(input("answer:"))
    
    #question 5
    print("\n5)Choose two of the genres below that you enjoy the most:\na)comedy\nb)action\nc)drama\nd)horror\n")
    favourites.append(input("answer:"))

    #question 6
    print("\n6)What is your preferred movie length?\na)a shorter film(~90 minutes)\nb)average length(~1.5 to 2 hours)\nc)a long movie(~2.5 hours or more)\n")
    answer=(input("answer:"))
    while answer!='a' and answer!='b' and  answer!='c':
        input("Please enter a valid choice:\n") 
    if answer=='a':
        favourites.append(90)
    elif answer=='b':
        favourites.append(120)
    else:
        favourites.append(1000)
    
    #question 7
    print("\n8)Which one of these plots seems more interesting to you?\na)A mafia patriarch transfers control of his empire to his reluctant son")
    print("b)A tragic love stroy unfolds abroad the ill-fated Titanic ship")
    print("c)Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency")
    print("d)Genetically engineered dinosaurs wreak havoc after scaping in a theme park preview\n")
    answer=(input("answer:"))
    while answer!='a' and answer!='b' and  answer!='c' and answer!='d' :
        input("Please enter a valid choice:\n") 
    if answer=='a':
        favourites.append("God father")
    elif answer=='b':
        favourites.append("Titanic")
    elif answer=='c':
        favourites.append("Shawshank redemption")
    else :
        favourites.append("jurassic park")

    #question 8
    print("\n9)What experience are you looking for when watching a movie?\na)a relaxing time\nb)a new concept to think about\nc)to learn about people and life")
    print("d)excitement or fun\n")
    answer=(input("answer:"))
    while answer!='a' and answer!='b' and  answer!='c' and answer!='d' :
        input("Please enter a valid choice:\n") 
    if answer=='a':
        favourites.append(["romance","comedy"])
    elif answer=='b':
        favourites.append(["psychology"])
    elif answer=='c':
        favourites.append(["biography","drama"])
    else :
        favourites.append(["comedy","adventure","horror","sci-fi","crime","thriller"])

    #question 19
    print("\n10)Are you in the mood for something light-hearted or serious?\na)light-hearted\nb)serious\n")
    answer=(input("answer:"))
    while answer!='a' and answer!='b':
        input("Please enter a valid choice:\n") 
    if answer=='a':
        favourites.append(["romance","comedy","biography","adventure"])
    else :
        favourites.append(["horror","sci-fi","crime","thriller","sci-fi"])
    

#starting, creating a profile, verifying the info then finding what the user's taste is in movies.
p = {}
welcome_page()
create_profile(p)
show_profile(p)

#list of user's favourite things = f
f=[]
verify_information(p,f)
#suggesting top 5 movies for this user:

def compare(fav=[],movies=[]):
        print("something")
