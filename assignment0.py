
#validation
import re

def home(option=None):
    print("Welcome, please select an option")
    option = input(" a) Login \n b) Register \n c) forget password \n")
    if option=="a":
      login()
    elif option=="b":
      register()
    elif option=="c":
      forgetPassword()

def login():
  email=input("Enter Email ")
  password=input("password ")
  regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
  if(re.fullmatch(regex, email)):
    if(len(password)>=5):
       db = open("database.txt", "r")
       d = []
       f = []
       for i in db:
        #  print(i)
         a,b = i.split(",")
         d.append(a)
         f.append(b)
         data = dict(zip(d, f))
        #  print(data)
       if email in data:
          #  print(email)
           hash=data[email].replace('\n','')
          #  print(hash +" "+password)
           if password==hash:
             print("Login Success")
           else:
             print("Invalid password")
       else:
           print("User not exist")
           print("Please choose a register option")
           home()
  else:
    print("InValid Email")


def register():
  email=input("Enter Email ")
  password=input("Enter Password ")
  regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
  if(re.fullmatch(regex, email)):
    if validPassword(password):
      save=open("database.txt","a")
      save.write(email+","+password+"\n")
      print("Successfully registred")
    else:
      print("""Not a Valid Password 
      Must have minimum one special character,
      one digit,
      one uppercase, 
      one lowercase character """)
  else:
    print("InValid Email")

def forgetPassword():
  email=input("Enter Email ")
  regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
  if(re.fullmatch(regex, email)):
       db = open("database.txt", "r")
       d = []
       f = []
       for i in db:
         a,b = i.split(",")
         d.append(a)
         f.append(b)
         data = dict(zip(d, f))
       if email in data:
           hash=data[email].replace('\n','')
           print("Current password : "+hash)
           
       else:
           print("User not exist")
           print("Please choose a register option")
  else:
    print("InValid Email")


def validPassword(password):
  flag = True
  while True:  
      if (len(password)<5):
          flag = False
          break
      elif not re.search("[a-z]", password):
          flag = False
          break
      elif not re.search("[A-Z]", password):
          flag = False
          break
      elif not re.search("[0-9]", password):
          flag = False
          break
      elif not re.search("[_@$*&#!]", password):
          flag = False
          break
      elif re.search("\s", password):
          flag = False
          break
      else:
          flag = True
          # print("Valid Password")
          break
    
  # if not flag:
  #     print("Not a Valid Password")
  return flag

home()