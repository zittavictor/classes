from car_rental import Car_Rental

def main():
    customer = input("Enter the customer's name: ")
    start = int(input("Enter the beginning odometer reading: "))
    end = int(input("Enter the ending odometer reading: "))
    days = int(input("Enter the number of rental days: "))

    rental = Car_Rental(customer, start, end, days)
    print(rental)

if __name__ == "__main__":
    main()
