""" 
The code is about checking if a person getting prizes for some
olympiad based on their category their rank falls into. The olympiad will
gives prizes according to this convention

Cash prize: 1 - 10
Gold: 10 - 50
Silver: 50 - 250
Bronze: 250 - 500
Merit Certificate: 500 - 1000
Participation Certificate: 1000 and above

Lets say person A gets a rank of 693, he/she will get a Merit Certificate and Participation
Certificate.

"""
# Try-Except statement to block text data from causing errors
try:
    rank = int(input("Your Rank: ")) # The input rank can be received in various methods, like from a database, input is used here as a place holder
except:
    print("Invalid input")
    exit()

# The Prizes

Medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
Certificates = ["Merit Certificate", "Participation Certificate"]

#Constants
CASH_PRIZE = 1
GOLD_MEDAL = 2
SILVER_MEDAL = 3
BRONZE_MEDAL = 4
MERIT_CERTIFICATE = 5
PARTICIPATION_CERTIFICATE = 6

#Outputs
attachedRank = 0
gainedPrizes = [] # The Output Array Containing the prizes gained

#The Given function
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False

#Checks wheter the person falls into the certain category. This function uses the binary_search function.
def checkRankCategory (rank, upperBound, lowerBound) :
    search_Array = list(range(upperBound, lowerBound+1))

    if binary_search(search_Array, rank):
        return True
    else:
        return False

# Adds them to a certain rank category using checkRankCategory
def attachRankCategory():
    global attachedRank
    if checkRankCategory(rank, 1, 10):
        attachedRank = CASH_PRIZE
    elif checkRankCategory(rank, 11, 50):
        attachedRank = GOLD_MEDAL
    elif checkRankCategory(rank, 51, 250):
        attachedRank = SILVER_MEDAL
    elif checkRankCategory(rank, 251, 500):
        attachedRank = BRONZE_MEDAL
    elif checkRankCategory(rank, 501, 1000):
        attachedRank = MERIT_CERTIFICATE
    elif rank > 1000:
        attachedRank = PARTICIPATION_CERTIFICATE
    else:
        print("This rank dosen't exist")
        exit()

# Attaches the prizes
def attachPrizes(prizes):
    for i in prizes:
        gainedPrizes.append(i)

# It uses the attachPrizes function according to their rank
def sortAndAddPrizes():
    match attachedRank:
        case 1:
            attachPrizes(["Cash Prize", Medals[0], Certificates[0], Certificates[1]])

        case 2:
            attachPrizes([Medals[0], Certificates[0], Certificates[1]])

        case 3:
            attachPrizes([Medals[1], Certificates[0], Certificates[1]])

        case 4:
            attachPrizes([Medals[2], Certificates[0], Certificates[1]])
        
        case 5:
            attachPrizes([Certificates[0], Certificates[1]])

        case 6:
            attachPrizes([Certificates[1],])

        case _:
            print("Error: Can't Add Prizes")
            exit()
        
# The output function can vary based on use. For example, send it to the client from a server etc.
def output ():
    print("The prizes gained are: ")
    for x in gainedPrizes:
        print(f"-> {x}")


# Calling the functions
attachRankCategory()
sortAndAddPrizes()
output()



    


    


