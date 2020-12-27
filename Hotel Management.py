import pandas as pd

#DECLARING VARIABLES
rooms=[]
occupied = []
unoccupied = []
staying_customers = []
customers = []
ph_no = []

#CREATING CLASSES AND RELATED METHODS

class Room(object):
    def __init__(self, number, type, status):
        self.number = number
        self.type = type
        self.status = status

        if self.status == "unoccupied":
            unoccupied.append(self.number)

    def checkin(self, status):
         self.status= status

         if self.number in unoccupied:
             unoccupied.remove(self.number)
             occupied.append(self.number)

         else:
             print("Room is already occupied")


    def checkout(self, status):
         self.status= status
         if self.number in occupied:
            unoccupied.append(self.number)
            occupied.remove(self.number)
         else:
            print("Room is unoccupied")

#INITIALIZING ROOMS
for i in range(100):
    if i%3==1:
        rooms.append(Room(i,"single","unoccupied"))
    if i%3==2:
        rooms.append(Room(i, "deluxe", "unoccupied"))
    if i%3==0:
        rooms.append(Room(i, "suite", "unoccupied"))

#DEFINING FUNCTION FOR DISPLAYING OCCUPIED AND UNOCCUPIED ROOMS

def available_rooms():
    unoccupied.sort()
    print("Unnocupied Rooms :")
    print(unoccupied)
    print("Occupied Rooms :")
    print(occupied)


def available_single_rooms():
    single_rooms=[]
    for i in unoccupied:
        if (i)%3==1:
            single_rooms.append(i)
    single_rooms.sort()
    print(single_rooms)

def available_deluxe_rooms():
    deluxe_rooms=[]
    for i in unoccupied:
        if (i)%3==2:
            deluxe_rooms.append(i)
    deluxe_rooms.sort()
    print(deluxe_rooms)

def available_suite_rooms():
    suite_rooms=[]
    for i in unoccupied:
        if (i)%3==0:
            suite_rooms.append(i)
    suite_rooms.sort()
    print(suite_rooms)

#CREATING CLASS FOR ALL CUSTOMERS
class Customer:
    def __init__(self, id, name, phone_number, membership):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.membership = membership    # None, Silver, Gold or Platinum
        customers.append(self)

def add_customer():
    id = len(customers)+1
    print("ID =")
    print(id)
    name = input("Name : ")
    ph_number = int(input("Phone Number : "))
    print("Press s for Silver")
    print("Press g for Gold (access to pool facilities and 20% special discount)")
    print("Press p for Platinum(access to pool facilities, complementary breakfast and 20% special discount)")
    mem = input()
    if mem == "s":
        membership = "Silver"
    elif mem == "g":
        membership = "Gold"
    elif mem == "p":
        membership = "Platinum"
    else:
        print("Undefined input. Try again!")

    Customer(id, name, ph_number, membership)

#CREATING CLASS FOR CUSTOMERS CURRENTLY STAYING
class stay_customer:
   def __init__(self, id ,checkin_date, checkout_date, room_number, number_of_days, number_of_nights):
    self.id = id
    self.checkin_date = checkin_date
    self.checkout_date = checkout_date
    self.room_number = room_number
    self.number_of_days = number_of_days
    self.number_of_nights = number_of_nights
    staying_customers.append(self)

#DEFINING CHECK-IN AND CHECK-OUT FUNCTIONS
def check_in():
    id = int(input("Enter Customer ID : "))
    checkin_date = input("Enter check-in date : ")
    checkout_date = input("Enter check-out date : ")
    room_num = int(input("Check in to room number : "))
    nod = int(input("number of days : "))
    non = int(input("number of nights : "))
    stay_customer(id, checkin_date, checkout_date, room_num, nod, non)

    for i in range(len(rooms)):
        if rooms[i].number == room_num:
            rooms[i].checkin("occupied")
            break

def check_out():
     room_num = int(input("Enter room number : "))

#CHECK-OUT AND BILL CALCULATION
     for i in rooms:
             if i.number == room_num:
                 room_type = i.type
                 if room_type == "single":
                     x_d = 500
                     x_n = 1000

                 elif room_type == "deluxe":
                     x_d = 750
                     x_n = 1250

                 elif room_type == "suite":
                     x_d = 1000
                     x_n = 1500

                 i.checkout("unoccupied")

                 for i in staying_customers:
                   if i.room_number == room_num:
                    bill = i.number_of_days*x_d + i.number_of_nights*x_n
                    print(bill)
                    id_ = i.id

                    for customer in customers:
                       if customer.id == id_:
                         if customer.membership == "Silver":
                           print(bill)
                         elif customer.membership == "Gold":
                           print("special discount for Gold members = 20%")
                           print(80*bill/100)
                         elif customer.membership == "Platinum":
                           print("special discount for Gold members = 30%")
                           print(70*bill/100)


#INITIAL CUSTOMERS
Customer(1,"A",9030095595,"Gold")
Customer(2,"B",9948295888,"Silver")

for i in customers:
    ph_no.append(i.phone_number)

#CREATING WHILE LOOP
while True:
 print("For list of rooms, press 0")
 print("For list of staying customers, press 1")
 print("For checkin, press 2")
 print("For checkout, press 3")
 print("For list of all customers, press 4")
 start = int(input())

#DISPLAYS ALL OCCUPIED AND UNOCCUPIED ROOMS
 if start == 0:
     available_rooms()

# DISPLAYS ALL CURRENT CUSTOMERS
 elif start == 1:
     for i in range(len(staying_customers)):
         print(staying_customers[i].__dict__)

#CHECKING IN
 #DISPPLAYING AVAILABLE ROOMS IN DIFFERENT TYPES
 elif start == 2:
    print("Press 1 for Single rooms")
    print("Press 2 for Deluxe rooms")
    print("Press 3 for Suite rooms")

    a= int(input())
    if a ==1:
       available_single_rooms()
    elif a ==2:
       available_deluxe_rooms()
    elif a ==3:
       available_suite_rooms()
    else:
        print("Undefined input. Try again!")
        print()
        continue

#CHECKING IF CUSTOMER IS NEW OR EXISTING
    member_confirmation =input("Already a member? (y/n)")

    if member_confirmation == "y":
        phone_no = int(input("Enter phone number : "))
        customer_present = 0
        for i in range(len(customers)):
           if customers[i].phone_number == phone_no:
              print(customers[i].__dict__)
              customer_present = 1
              break
        if (customer_present == 0):
            print("Not a member")
            continue

#ADD NEW CUSTOMER
    elif member_confirmation == "n":
       add_customer()
       phone_no = int(input("Enter phone number : "))
       for i in range(len(customers)):
         if customers[i].phone_number == phone_no:
            print(customers[i].__dict__)


    else:
        print("Undefined input. Try again!")
        print()
        continue
#CHECK IN
    check_in()

#CHECKING OUT and BILLING
 elif start == 3:
     check_out()

#DISPLAYING ALL MEMBERS/CUSTOMERS
 elif start == 4:
     id = []
     name = []
     phone_num = []
     membership = []

     for i in customers:
        id.append(i.id)
        name.append(i.name)
        phone_num.append(i.phone_number)
        membership.append(i.membership)

     CV = pd.DataFrame(
     {
         'ID': id,
         'Name': name,
         'PhoneNumber': phone_num,
         'Membership': membership,

      })

     print(CV)
     CV.to_csv('customers.csv')
     print()

 else:
     print("Undefined input. Try again!")
     print()
