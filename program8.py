from pay_stub import Pay_Stub

def main():
    name = input("Enter employee name: ")
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter pay rate: "))

    stub = Pay_Stub(name, hours, rate)
    print(stub)
    print(Pay_Stub.summary())

if __name__ == "__main__":
    # Run 3 times for testing
    for _ in range(3):
        main()
