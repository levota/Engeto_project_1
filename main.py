from task_template import TEXTS
from Users import users
import time

ODDELOVAC = "-"
uzivatel = str(input("Plese enter your user name: ")).lower()
heslo = str(input("Please insert your password: "))



if users.get(uzivatel) == heslo:
    print(f"""Welcome to the app, {uzivatel}
              We have 3 texts to be analyzed""")

else:
    print("User name or password is incorect")
    time.sleep(3)
    quit()




