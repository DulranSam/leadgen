import random
from openpyxl import Workbook


class LeadGenerationChatbot:
    def __init__(self, business_name):
        self.business_name = business_name
        self.leads = []

    def greet(self):
        greetings = ["Hello!", "Hi there!", "Welcome!", "Greetings!"]
        return random.choice(greetings)

    def introduce(self):
        return f"I am {self.business_name}, your personal AI assistant. How can I assist you today?"


    def collect_lead_info(self):
        print("To assist you better, could you please provide some information?")
        name = input("What is your name? ")
        email = input("What is your email address? ")
        phone = input("What is your phone number? ")
        interest = input("What are you interested in? ")
        lead_data = {"name": name, "email": email, "phone": phone, "interest": interest}
        self.leads.append(lead_data)
        print("Thank you! We will get back to you shortly.")

        # Save lead information to an Excel spreadsheet
        wb = Workbook()
        ws = wb.active
        ws.append(["Name", "Email", "Phone", "Interest"])
        ws.append([lead_data['name'], lead_data['email'], lead_data['phone'], lead_data['interest']])
        wb.save("leads.xlsx")

        

# Main function to interact with the chatbot
def main():
    business_name = "Veloxal"
    chatbot = LeadGenerationChatbot(business_name)
    
    print(chatbot.greet())
    print(chatbot.introduce())

    while True:
        print("\nWhat would you like to do?")
        print("1. Inquire about our services")
        print("2. Provide lead information")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            print("Our services include...")
            # Add information about services offered
        elif choice == '2':
            chatbot.collect_lead_info()
        elif choice == '3':
            print("Thank you for your interest. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
