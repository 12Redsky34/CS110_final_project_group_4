# Class representing the attributes of a person's name
class Name:
    first = None
    last = None
    middle = None
    title = None
    suffix = None

    # Returns the string representation of this class
    def to_string(self):
        out_string = ""

        if self.title != None:
            out_string += self.title + " "
        if self.first != None:
            out_string += self.first + " "
        if self.middle != None:
            out_string += self.middle + " "
        if self.last != None:
            out_string += self.last + " "
        if self.suffix != None:
            out_string += self.suffix + " "
        
        return out_string.removesuffix(" ") # Remove trailing space

# Class representing the attributes of a person's address
class Address:
    street = None
    city = None
    state = None
    zip = None

    # Returns the string representation of this class
    def to_string(self):
        out_string = ""

        if self.street != None:
            out_string += "Street: " + self.street + "\n"
        if self.city != None:
            out_string += "City: " + self.city + "\n"
        if self.state != None:
            out_string += "State: " + self.state + "\n"
        if self.zip != None:
            out_string += "ZIP: " + self.zip + "\n"

        return out_string.removesuffix("\n") # Remove trailing newline

# Class representing the attributes of a person's contact information
class Contact:
    primary_phone = None
    secondary_phone = None
    email = None

    # Returns the string representation of this class
    def to_string(self):
        out_string = ""
        
        if self.primary_phone != None:
            out_string += "Phone: " + self.primary_phone + "\n"

            if self.secondary_phone != None:
                out_string += "Phone 2: " + self.secondary_phone + "\n"

        if self.email != None:
            out_string += "Email: " + self.email + "\n"

        return out_string.removesuffix("\n") # Remove trailing newline


# Class representing a list of strings, to be used for properties of the
# Applicant class (experience, education, skills)
class String_List:
    entries = None

    # Appends a new entry to the list
    def add_entry(self, entry):
        if self.entries == None:
            self.entries = list()
        
        self.entries.append(entry)

    # Removes a list entry at the specified index
    def remove_entry(self, index):
        self.entries.remove(index)

    # Returns the string representation of this class
    def to_string(self):
        out_string = ""

        if self.entries == None:
            return out_string
        
        for entry in self.entries:
            out_string += entry + "\n"
        
        return out_string.removesuffix("\n") # Remove trailing newline

# The primary class, representing an applicant's personal information.
# Contains behavior to initialize, modify, and display said information.
# I anticipate this class to be the foundation of the program; the GUI
# interfacing with it to handle the logic.
class Applicant:
    name = Name()
    address = Address()
    contact = Contact()
    experience = String_List()
    education = String_List()
    skills = String_List()

    # Name property setter methods
    def set_name_first(self, f):
        self.name.first = f
    def set_name_middle(self, m):
        self.name.middle = m
    def set_name_last(self, l):
        self.name.last = l
    def set_name_title(self, t):
        self.name.title = t
    def set_name_suffix(self, s):
        self.name.suffix = s
    
    # Address property setter methods
    def set_addr_street(self, street):
        self.address.street = street
    def set_addr_city(self, city):
        self.address.city = city
    def set_addr_state(self, state):
        self.address.state = state
    def set_addr_zip(self, zip):
        self.address.zip = zip
    
    # Contact property setter methods
    def set_contact_phone(self, phone):
        self.contact.primary_phone = phone
    def set_contact_phone_alt(self, phone):
        self.contact.secondary_phone = phone
    def set_contact_email(self, email):
        self.contact.email = email

    # Methods to add experience, education, or skill entries
    def add_experience(self, exp):
        self.experience.add_entry(exp)
    def add_education(self, edu):
        self.education.add_entry(edu)
    def add_skill(self, skill):
        self.skills.add_entry(skill)
    
    # Methods to clear one or all properties of the class, resetting
    # them to their defaults
    def clear_name(self):
        self.name = Name()
    def clear_address(self):
        self.address = Address()
    def clear_contact(self):
        self.contact = Contact()
    def clear_experience(self):
        self.experience = String_List()
    def clear_education(self):
        self.education = String_List()
    def clear_skills(self):
        self.skills = String_List()
    def clear(self):
        self.name = Name()
        self.address = Address()
        self.contact = Contact()
        self.experience = String_List()
        self.education = String_List()
        self.skills = String_List()

    # Returns the string representation of this class
    def to_string(self):
        out_string = self.name.to_string() + "\n\n"
        out_string += "Address:\n" + self.address.to_string() + "\n\n"
        out_string += "Contact:\n" + self.contact.to_string() + "\n\n"
        out_string += "Experience:\n" + self.experience.to_string() + "\n\n"
        out_string += "Education:\n" + self.education.to_string() + "\n\n"
        out_string += "Skills:\n" + self.skills.to_string() + "\n"

        return out_string
    
    # Prints the string representation of this class
    def print(self):
        print(self.to_string())

# Function that sets up an Applicant object for demonstration purposes
def demo():
    demo_applicant = Applicant()

    demo_applicant.set_name_title("Mr.")
    demo_applicant.set_name_first("John")
    demo_applicant.set_name_middle("J.")
    demo_applicant.set_name_last("Doe")

    demo_applicant.set_addr_street("123 Fake St")
    demo_applicant.set_addr_city("Bremerton")
    demo_applicant.set_addr_state("WA")
    demo_applicant.set_addr_zip("11235")

    demo_applicant.set_contact_phone("(360) 867-5309")
    demo_applicant.set_contact_phone_alt("(360) 112-5381")
    demo_applicant.set_contact_email("jdoe112@aol.com")
    
    experience = ["Accounting", "Banking", "Finance"]

    for exp in experience:
        demo_applicant.add_experience(exp)
    
    education = ["I'm", "Getting", "Tired", "Of", "Making", "Up", "Examples"]

    for edu in education:
        demo_applicant.add_education(edu)

    skills = ["Juggling", "Underwater Basket Weaving", "Ballet"]

    for skill in skills:
        demo_applicant.add_skill(skill)
    
    demo_applicant.print()

# Runs the demo function
#demo()
