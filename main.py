from agents.tutor_agent import TutorAgent

def main():
    agent = TutorAgent()

    while True:
        query = input("\nAsk your question (type 'exit' to quit): ")
        if query.lower() == 'exit':
            break

        response = agent.generate_response(query)
        print("Response:", response)

if __name__ == "__main__":
    main()
