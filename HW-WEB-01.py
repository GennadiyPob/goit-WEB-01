from abc import ABC, abstractmethod

# Абстрактний базовий клас для користувальницьких уявлень

class UserInterface(ABC):
    @abstractmethod
    def display_contacts(self,contacts):
        pass

    @abstractmethod
    def display_notes(self, notes):
        pass

    @abstractmethod
    def display_commands(self):
        pass

# Клас консольного інтерфейсу, що успадковує абстрактний клас

class ConsoleUserInterface(UserInterface):
    def display_contacts(self, contacts):
        print("Contact List :")
        for contact in contacts:
            print(f'Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}, Birthday: {contact['birthday']}')

    def display_notes(self, notes):
        print('Notes:')
        for note in notes:
            print(note)

    def display_commands(self):
        print('------------------')
        print('Available Commands:')
        print('1. Show contacts')
        print('2. Show notes')
        print('3. Add contact')
        print('4. Add note')
        print('5. Exit')

# Клас додатку

class App:
    def __init__(self, user_interface):
        # self.contacts = []
        self.contacts = [
            {
                'name': 'Vitalii',
                'phone': '+38067-123-45-67',
                'email': 'abc@google.com',
                'address': 'Lisova 5',
                'birthday': '04.11.2000'
            }
        ]
        
        self.notes = ['Нотатка 1', 'Нотатка 2']

        self.user_interface = user_interface

    def run_app(self):
        while True:
            self.user_interface.display_commands()
            command = input('Enter command:')
            print('===============')

            if command == '1':
                self.user_interface.display_contacts(self.contacts)
            elif command == '2':
                self.user_interface.display_notes(self.notes)
            elif command == '3':
                self.add_contact()
            elif command == '4':
                self.add_notes()
            elif command == '5':
                break
            else:
                print("Not available command. Try again.")
            
    def add_contact(self):
        # Блок додавання контакту
        pass
               

    def add_note(self):
        # Блок додавання нотатки
        pass

# Приклад виконання програми

console_user_interface = ConsoleUserInterface()
app = App(console_user_interface)

app.run_app()