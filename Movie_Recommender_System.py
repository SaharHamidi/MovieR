

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
    input("\t\t\t  Press enter to continue...")

def create_profile(p={}):
    
    profile['Name'] = input(" What is your name? : ")
    while (type(profile['Name'])!=str or profile['Name'].isalpha()==False):
        profile['Name'] = input(" Please enter a valid name : ")

    profile['LastName'] = input(" What is your Last name? : ")
    while (type(profile['LastName'])!=str or profile['LastName'].isalpha()==False):
        profile['LastName'] = input(" Please enter a valid last name : ")

    profile['Age'] = input(" How old are you? : ")
    while (profile['Age'].isnumeric()==False or int(profile['Age'])>125):
        profile['Age'] = input(" Please enter a valid number : ")
    
    profile['Email'] = input(" What is your email? : ")
    #while (profile['Email'].endswith('@gmail.com',-10,-1)==False or profile['Email'].endswith('@yahoo.com',-10,-1)==False):
        #profile['Email'] = input(" Please enter a valid email ending with @gmail.com or @yahoo.com : ")
    #install re module 
    profile['PhoneNumber'] = input (" What is your phone number? : ")
    while (profile['PhoneNumber'].isnumeric()==False or len(profile['PhoneNumber'])>15):
        profile['PhoneNumber'] = input(" Please enter a valid phone number : ")
    
def show_profile():
    print("\n Your profile:")
    for key, value in profile.items():
        print(f"{key}: {value}")

def confirmation():
    confirm = input("Is the information correct?(yes/no)") 
    if confirm.lower() == 'no':
        profile={}
        create_profile(profile)
        show_profile()
        confirmation()
    elif confirm.lower() == 'yes':
        questionnaire()
    else:
        confirmation()
        
        
def verify_information():
    confirm = input("press v to verify your information or press s to skip:")
    if confirm.lower() == 'v':
        show_profile()
        confirmation()
    elif confirm.lower() == 's':
        questionnaire()
    else:
        verify_information()

def questionnaire():
    print("\nLet's find out what your preferences are.")
    print("Please answer the next 10 questions by choosing an option or typing out your answer.\n")
    #question 1
    print("1) Do you prefer popular movies or indie films?\na)very popular shows\nb)indie movies\nc)doesn't matter to me\n")
    #question 2
    print("2) What is the last series you watched that you really liked?\n")
    #question 3
    print("3) Choose two of the genres below that you enjoy the most:\na)comedy\nb)action\nc)drama\nd)horror\n")
    #question 4
    print("4) What is your favourite animation ever?(if you don't have one write:I don't watch animations)\n")
    #question 5
    print("5) What experience are you looking for when watching a movie?\na)a relaxing time\nb)a new concept to think about\nc)to learn about people and life\nd)excitement or fun\n")
    #question 6
    print("6) Who is your favorite actor or actresse?(Name one only.)\n")
    #question 7
    print("7) Which one of the directors below would you want to meet in real life?\na)Steven Spielberg\nb)Martin Scorsese\nc)Quentin Tarantino\nd)Christopher Nolan\n")
    #question 8
    print("8) What is your preferred movie length?\na)a shorter film(~90 minutes)\nb)average length(~1.5 to 2 hours)\nc)a long movie(~2.5 hours or more)\n")
    #question 9
    print("9) Are you in the mood for something light-hearted or serious?\na)light-hearted\nb)serious\n")
    #question 10
    print("10) I want to watch a movie from ...?\na)this year\nb)the past 2 years\nc)the past 5 years\nd)the past 10 years\n")

profile = {}
welcome_page()
create_profile(profile)
show_profile()
verify_information()

    

