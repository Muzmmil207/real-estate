from base import Agent


def main(agent: Agent) -> None:
    while 1:
        print(
            "- for displaying all the properties enter (1)\n"
            "- for add new property enter (2)\n"
            "- for closing the program enter (3)"
        )
        choice = input("enter a number: ")
        if choice == "1":
            agent.display_properties()
        elif choice == "2":
            agent.add_property()
        elif choice == "3":
            break
        else:
            print("Please enter correct nomber")


if __name__ == "__main__":
    agent = Agent()

    main(agent)
