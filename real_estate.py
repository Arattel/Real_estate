class Property:
    """
    This class represents a real estate propety
    """
    def __init__(self, square_feet='', beds='',
                 baths='', **kwargs):
        """
        (Property, str, str, str) -> None
        This method initializes a Property instance
        """
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        (Property) -> None
        This method displays a Property object details
        """
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        """
        (None) -> (dict)
        This static method inputs all properties needed to initialize a Property object
        """
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)


def get_valid_input(input_string, valid_options):
    """
    (str, tuple) -> (str)
    This function inputs a input string an valid options and inputs data until it`s valid
    """
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Apartment:
    """
    This class represents an Apartment as a part of real estate
    """
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        """
        (Apartment, str, str, str, str, str) -> None
        This method initializes an Apartment instance
        """
        self.property = Property(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        (Apartment) -> None
        This method displays an Apartment object details
        """
        self.property.display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    def prompt_init():
        """
        (None) -> (dict)
        This static method inputs all properties needed to initialize an Apartment object
        """
        parent_init = Property.prompt_init()
        laundry = get_valid_input(
            "What laundry facilities does "
            "the property have? ",
            Apartment.valid_laundries)
        balcony = get_valid_input(
            "Does the property have a balcony? ",
            Apartment.valid_balconies)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)


class House:
    """
    This class represents a house as a part of real estate
    """
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='',
                 garage='', fenced='', **kwargs):
        """
        (House, str, str, str, str, str, str) -> None
        This method initializes a House instance
        """
        self.property = Property(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """
        (House) -> None
        This method displays a House object details
        """
        self.property.display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        """
        (None) -> (dict)
        This static method inputs all properties needed to initialize a House object
        """
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
                                 House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
                                 House.valid_garage)
        num_stories = input("How many stories? ")
        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Purchase:
    """
    This class represents a purchase
    """
    def __init__(self, price='', taxes='', **kwargs):
        """
        (Purchase, str, str) -> None
        This method initializes a Purchase instance
        """
        self.price = price
        self.taxes = taxes

    def display(self):
        """
        (Purchase) -> None
        This method displays a Purchase object details
        """
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        """
        (None) -> (dict)
        This static method inputs all properties needed to initialize a Purchase object
        """
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are the estimated taxes? "))

    prompt_init = staticmethod(prompt_init)


class Rental:
    """
    This class represents a rental
    """
    def __init__(self, furnished='', utilities='',
                 rent='', **kwargs):
        """
        (Rental, str, str, str) -> None
        This method initializes a Rental instance
        """
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """
        (Rental) -> None
        This method displays a Rental object details
        """
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(
            self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        """
        (None) -> (dict)
        This static method inputs all properties needed to initialize a Rental object
        """
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input(
                "What are the estimated utilities? "),
            furnished=get_valid_input(
                "Is the property furnished? ",
                ("yes", "no")))

    prompt_init = staticmethod(prompt_init)


class HouseRental:
    """
    This class represents a house rental
    """
    def __init__(self, furnished = '', utilities = '', rent = '', **kwargs):
        """
        (HouseRental, str, str, str, **kwargs) -> None
        Initializes a HouseRental instance
        """
        self.rental = Rental(furnished = furnished,utilities = utilities, rent=rent)
        self.house = House(**kwargs)

    def display(self):
        """
        (HouseRental) -> None
        Displays a HouseRental details
        """
        self.rental.display()
        self.house.display()

    def prompt_init():
        """
        (None) -> (dict)
        This static method inputs all properties needed to initialize a HouseRental object
        """
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentRental:
    """
    This class represents an apratment rental
    """
    def __init__(self, furnished = '', utilities = '', rent = '', **kwargs):
        """
        (HouseRental, str, str, str, **kwargs) -> None
        Initializes an ApartmentRental instance
        """
        self.rental = Rental(furnished = furnished,utilities = utilities, rent=rent)
        self.apartment = Apartment(**kwargs)

    def display(self):
        """
        (HouseRental) -> None
        Displays a HouseRental details
        """
        self.rental.display()
        self.apartment.display()

    def prompt_init():
        """
        (None) -> (dict)
        This static method inputs all properties needed to initialize an ApartmentRental object
        """
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase:
    """
    This class represents an apartment purchase
    """

    def __init__(self, price='', taxes='', **kwargs):
        """
        (ApartmentPurchase, str, str, str, **kwargs) -> None
        Initializes an ApartmentPurchase instance
        """
        self.purchase = Purchase(price = price, taxes = taxes)
        self.apartment = Apartment(**kwargs)

    def display(self):
        """
        (ApartmentPurchase) -> None
        Displays a ApartmentPurchase details
        """
        self.purchase.display()
        self.apartment.display()


    def prompt_init():
        """
        (None) -> (dict)
        This static method inputs all properties needed to initialize an ApartmentPurchase object
        """
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    """
    This class represents a house prurchase
    """
    def __init__(self, price='', taxes='', **kwargs):
        """
        (HousePurchase, str, str, **kwargs) -> None
        Initializes a HouseRental instance
        """
        self.purchase = Purchase(price = price, taxes = taxes)
        self.house = House(**kwargs)

    def display(self):
        """
        (HousePurchase) -> None
        Displays a HouseRental details
        """
        self.purchase.display()
        self.house.display()
    def prompt_init():
        """
        (None) -> (dict)
        This static method inputs all properties needed to initialize a HousePurchase object
        """
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class Agent:
    """
    This class represents a real estate agent with data about properties
    """
    def __init__(self):
        """
        (Agent) -> None
        Initializes an Agent object instance
        """
        self.property_list = []

    def display_properties(self):
        """
        (Agent) -> None
        Prints all properties from properties list
        """
        for property in self.property_list:
            property.display()

    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def add_property(self):
        """
        (Agent) -> None
        Inputs a data for property instance and adds a property to property list
        """
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")).lower()
        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")).lower()
        PropertyClass = self.type_map[
            (property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))

    def display_biggest_rental(self):
        """
        (Agent) -> None
        Displays a property with biggest rental
        """
        rentals = []
        for i in self.property_list:
            if isinstance(i, HouseRental) or isinstance(i, ApartmentRental):
                rentals.append(i)
        for i, j in enumerate(rentals):
            rentals[i].rental.rent = float(rentals[i].rental.rent)
        max(rentals, key=lambda x: x.rental.rent).display()

    def display_biggest_purchase(self):
        """
        (Agent) -> None
        Displays a property with biggest price
        """
        purchases = []
        for i in self.property_list:
            if isinstance(i, HousePurchase) or isinstance(i, ApartmentPurchase):
                purchases.append(i)
        if not purchases: print("None of them")
        for i, j in enumerate(purchases):
            purchases[i].purchase.price = float(purchases[i].purchase.price)
        max(purchases, key=lambda x: x.purchase.price).display()