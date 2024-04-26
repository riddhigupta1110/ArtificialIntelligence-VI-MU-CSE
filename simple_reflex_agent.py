A_state = input("Enter initial state for A room (clean/dirty): ").lower()
B_state = input("Enter initial state for B room (clean/dirty): ").lower()
agent_location = input("Enter initial location for agent (A/B): ").upper()

def simple_reflex_agent():
    global A_state, B_state, agent_location
    action = ""
   
    print(f"Current Environment Status: A: {A_state}, B: {B_state}, Agent Location: {agent_location}")

    percept = A_state if agent_location == "A" else B_state
    if percept == "dirty":
        action = "suck"
        print(f"Action: {action}")

    if agent_location == "A":
        A_state = "clean"
        action = "move to B"
        agent_location = "B"
    else:
        B_state = "clean"
        action = "move to A"
        agent_location == "A"

    print(f"Action: {action}")
    print(f"Updated Environment Status: A: {A_state}, B: {B_state}, Agent Location: {agent_location}")

def main():
    while True:
        simple_reflex_agent()
        if A_state == "clean" and B_state == "clean":
            break

    print("Action: No Operation")
    print("Agent has finished cleaning.")

if __name__ == "__main__":
    main()