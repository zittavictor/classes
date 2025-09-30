
def main():
    name = input("Enter walker’s name: ")
    steps = int(input("Enter number of steps: "))
    step_length = int(input("Enter length of step (inches): "))

    walker = Walk(name, steps, step_length)
    miles = walker.miles_walked()

    print(f"{walker.get_name()}'s walk with {walker.get_steps()} steps averaging "
          f"{walker.get_step_length()} inches per step equates to {miles:.2f} miles.")

if __name__ == "__main__":
    main()
