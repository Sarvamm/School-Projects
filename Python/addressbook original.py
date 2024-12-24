import random
fnames = [
    "Liam", "Emma", "Noah", "Olivia", "William", "Ava", "James", "Sofia", "Lucas", "Mia",
    "Ethan", "Isabella", "Alexander", "Amelia", "Michael", "Charlotte", "Benjamin", "Harper",
    "Elijah", "Evelyn", "Mason", "Abigail", "Sebastian", "Emily", "Logan", "Ella", "Daniel", "Avery",
    "Matthew", "Scarlett", "Henry", "Grace", "Jackson", "Chloe", "Samuel", "Victoria", "David", "Lily",
    "Joseph", "Zoe", "Carter", "Hannah", "Owen", "Natalie", "Jack", "Addison", "Luke", "Aria", 
    "Gabriel", "Ellie", "Jayden", "Nora", "Isaac", "Stella", "Grayson", "Riley", "Levi", "Leah",
    "Dylan", "Hazel", "Mateo", "Violet", "Julian", "Aurora", "Wyatt", "Savannah", "Ryan", "Penelope",
    "Caleb", "Lillian", "Nathan", "Layla", "Isaiah", "Paisley", "Thomas", "Brooklyn", "Aarav", "Ananya",
    "Ishaan", "Aarohi", "Vihaan", "Saanvi", "Krishna", "Diya", "Arjun", "Riya", "Rohan", "Priya", 
    "Karan", "Neha", "Aditya", "Pooja", "Rahul", "Sneha", "Ayaan", "Kavya", "Vikram", "Tara",
    "Siddharth", "Meera", "Kabir", "Nisha", "Dev", "Isha"
]
lnames = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
    "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts",
    "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes",
    "Stewart", "Morris", "Morales", "Murphy", "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper",
    "Patel", "Gupta", "Khan", "Sharma", "Mehta", "Agarwal", "Jain", "Singh", "Bose", "Chopra",
    "Malik", "Desai", "Menon", "Pandey", "Reddy", "Iyer", "Nair", "Naidu", "Rao", "Bhatt", 
    "Verma", "Sinha", "Tripathi", "Thakur", "Yadav", "Mishra", "Kulkarni", "Chatterjee", "Banerjee", "Dutta",
    "Shah", "Rastogi", "Kapoor", "Bhatia", "Pillai", "Ghosh"
]
addresses = addresses = [
    "123 Maple Street\nApt 4B\nNew York, NY 10001",
    "456 Oak Avenue\nLos Angeles, CA 90011",
    "789 Pine Lane\nSuite 300\nChicago, IL 60622",
    "101 Cedar Drive\nSan Francisco, CA 94103",
    "12 Birch Road\nToronto, ON M4B 1B3\nCanada",
    "98 Elm Street\nApt 8C\nLondon, NW1 4DR\nUnited Kingdom",
    "654 Spruce Boulevard\nSydney, NSW 2000\nAustralia",
    "321 Walnut Court\nHouston, TX 77002",
    "567 Redwood Avenue\nMelbourne, VIC 3000\nAustralia",
    "444 Willow Street\nParis, 75001\nFrance",
    "808 Cypress Lane\nDubai, UAE 00000",
    "33 Palm Avenue\nApt 5A\nMiami, FL 33101",
    "89 Aspen Street\nVancouver, BC V5K 0A1\nCanada",
    "77 Magnolia Road\nBerlin, 10115\nGermany",
    "222 Maplewood Avenue\nApt 12\nBoston, MA 02118",
    "999 Oakwood Terrace\nMumbai, MH 400001\nIndia",
    "45 Cherry Blossom Lane\nTokyo, 100-0001\nJapan",
    "76 Olive Street\nApt 3B\nSeoul, 03185\nSouth Korea",
    "34 Poplar Avenue\nMexico City, 01000\nMexico",
    "567 Beech Street\nApt 7\nDublin, D02 YT21\nIreland",
    "292 Linden Drive\nSingapore 238164",
    "402 Sycamore Street\nApt 15B\nSan Diego, CA 92101",
    "18 Chestnut Boulevard\nRome, 00184\nItaly",
    "190 Silver Birch Lane\nJohannesburg, 2000\nSouth Africa",
    "50 Holly Road\nAuckland, 1010\nNew Zealand",
    "200 Alder Avenue\nApt 10F\nBoston, MA 02110",
    "34 Maple Terrace\nToronto, ON M5A 2A4\nCanada",
    "5 Ash Lane\nDubai, UAE 12345",
    "789 Redwood Road\nSingapore 123456",
    "123 Sequoia Court\nLondon, SE1 1AA\nUnited Kingdom",
    "11 Cedar Grove\nSuite 4A\nParis, 75002\nFrance",
    "99 Fir Lane\nApt 23\nChicago, IL 60614",
    "105 Pine Terrace\nTokyo, 150-0001\nJapan",
    "65 Elm Street\nMumbai, MH 400005\nIndia",
    "203 Maplewood Circle\nApt 7D\nLos Angeles, CA 90017",
    "88 Spruce Grove\nSydney, NSW 2010\nAustralia",
    "42 Sycamore Avenue\nApt 6F\nMelbourne, VIC 3001\nAustralia",
    "61 Chestnut Lane\nVancouver, BC V6B 2Z4\nCanada",
    "17 Beech Road\nSuite 202\nBerlin, 10117\nGermany",
    "300 Cedar Terrace\nNew York, NY 10002",
    "71 Aspen Street\nSan Francisco, CA 94105",
    "150 Pine Avenue\nHouston, TX 77004",
    "120 Redwood Street\nApt 8E\nToronto, ON M6J 1E9\nCanada",
    "36 Oak Drive\nSeoul, 04527\nSouth Korea",
    "110 Palm Boulevard\nDubai, UAE 98765",
    "50 Birch Terrace\nLondon, EC1A 1BB\nUnited Kingdom",
    "450 Willow Avenue\nDublin, D04 KX77\nIreland",
    "21 Ash Road\nParis, 75003\nFrance",
    "910 Walnut Street\nTokyo, 101-0051\nJapan"
]

address_book = {
    "names": [],
    "ages": [],
    "phones": [],
    "addresses": [],
}

def addRandomEntry(n):
    for i in range(n):
        name = random.choice(fnames) +" "+ random.choice(lnames)
        address = random.choice(addresses)
        phno = ""
        phno = phno + str(random.randint(6,9))
        for k in range(9):
            phno = phno + str(random.randint(0,9))
        age = random.randint(15,99)

        address_book["names"].append(name)
        address_book["ages"].append(age)
        address_book["phones"].append(phno)
        address_book["addresses"].append(address)

def manualEntry(n):
    for i in range(n):
        name = input("Enter name: ")
        address = input("Enter address")
        phno = int(input("Enter phone number (10 digits)"))
        age = int(input(("enter age (0-150)")))
        if (len(str(phno))==10) and (150 > age > 0):
            address_book["names"].append(name)
            address_book["ages"].append(age)
            address_book["phones"].append(phno)
            address_book["addresses"].append(address)
        else:
            print("Invalid phone number or age. Please try again.")

n = int(input("How many entries?"))
if n <= 0:
    print("Invalid number of entries. Please try again.")
else:
    ch = input("random entry or manual? (R/M)")
    if ch.lower() == "r":
        addRandomEntry(n)
    elif ch.lower() == "m":
        manualEntry(n)

from prettytable import PrettyTable

def print_address_book():
    table = PrettyTable()
    table.field_names = ["Name", "Age", "Phone", "Address"]

    if not address_book["names"]:
        print("Address book is empty.")
        return

    for i in range(len(address_book["names"])):
        table.add_row([
            address_book["names"][i],
            address_book["ages"][i],
            address_book["phones"][i],
            address_book["addresses"][i]
        ])
    print(table)
print_address_book()
