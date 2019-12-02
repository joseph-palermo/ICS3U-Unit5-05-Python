#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: November 2019
# This program prints a Canada Post mailing address


def mailing_address(name, address, city,
                    province, postal_code, apartment=None):
    # this function puts the credentials into proper format

    # process
    if apartment is not None:
        post_address = name + "\n" + apartment + "-" + address + "\n" + \
                       city + " " + province + "  " + postal_code
    else:
        post_address = name + "\n" + address + "\n" + city + " " + province \
                    + "  " + postal_code

    return post_address


def main():
    # this function gets all mailing credentials and outputs them

    # variables
    apartment_number = None

    # input
    name = input("Enter your full name: ")
    address = input("Enter your address: ")
    question = input("Do you live in an apartment? (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        apartment_number = input("Enter your apartment number: ")
    city = input("Enter your city: ")
    province = input("Enter your abbreviated province or territory: ")
    postal_code = input("Enter your postal code: ")

    # process, addy means exact address
    if apartment_number is not None:
        addy = mailing_address(name, address, city, province, postal_code,
                               apartment_number)
    else:
        addy = mailing_address(name, address, city, province, postal_code,
                               apartment_number)

    # Output
    print("")
    print(addy)


if __name__ == "__main__":
    main()
