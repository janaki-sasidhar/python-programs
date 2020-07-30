#Address book using dictionary
class AddressClass:
    emp_count=0
    address_book={}
    def __init__(self,id,first_name,last_name,email_id,phone_number):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.email_id=email_id
        self.phone_number=phone_number
        if self.id in AddressClass.address_book:
            print("ID already exists ")
        else:
            AddressClass.address_book[self.id]=[self.first_name,self.last_name,self.email_id,self.phone_number]
            AddressClass.emp_count+=1
    
    def fullname(self):
        return f'{AddressClass.address_book[self.id][0]} {AddressClass.address_book[self.id][1]}'


    def update_firstname(self,new):
        self.first_name=new
        AddressClass.address_book[self.id][0]=new


    def update_lastname(self,new):
        self.last_name=new
        AddressClass.address_book[self.id][1]=new
    

    def update_email(self,new):
        self.email_id=new
        AddressClass.address_book[self.id][2]=new


    def update_phone(self,new):
        self.phone_number=new
        AddressClass.address_book[self.id][3]=new
    
    
    

def main():
    num=int(input("How many number of contacts you wanna create?"))
    id_list=[]
    print("Enter the instances you wanna create ")
    instances_list=[input() for i in range(num)]
    for i in range(num):
        id=int(input("Enter your contact id   "))
        first_name=input("Enter the first name   ").capitalize()
        last_name=input("Enter the last name   ").capitalize()
        mail_id=input("Enter the mail id   ").capitalize()
        phone_number=int(input("Enter the phone number   "))
        if id in id_list:
            print("ID already exists   ")
            continue
        else:
            instances_list[i]=AddressClass(id,first_name,last_name,mail_id,phone_number)
            id_list.append(id)
    print("The total count of addresss book is  ",AddressClass.emp_count)
    wanna_print=input("Do you wanna print address book dictionary ? (y/n").lower()
    if wanna_print=='y' or wanna_print=='yes' :
        print(AddressClass.address_book)
if __name__ == "__main__":
    main()
