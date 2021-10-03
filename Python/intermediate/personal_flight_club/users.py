import requests

USER_SHEET_ENDPOINT = "https://api.sheety.co/340901e51ddc58930c91a4d2b7f54662/flightDeals/users"

class Users:

    def get_user_data(self):
        response = requests.get(USER_SHEET_ENDPOINT)
        user_data = response.json()["users"]
        return user_data


    def firststep(self):

        user_data = self.get_user_data()       

        print("Welcome to the Flight Club.\nWefind the best flight deals and email you\n\n")

        first_name = input("What's your FIRST name?\n")
        last_name = input("What's your LAST name?\n")
        email = input("What's your Email?\n")
        check_email = input("Type your Email again\n")

        if email != check_email:
            print("please make sure that you typed your email correctly.")

        else:
            already = False

            for row in user_data:
                
                if row["email"] == check_email:
                    already = True
                    

            else:

                if already:
                    print("You're already in the club.\n\n")

                elif not already:
                    new_data = {
                        "user":{
                            "firstName" : first_name,
                            "lastName" : last_name,
                            "email" : check_email
                        }
                    }

                    response2 = requests.post(USER_SHEET_ENDPOINT, json=new_data)
                    print(f"Hey! {first_name} {last_name} Welcome in Our flight club!\n\n")





