import random

def ask_questions():
    # Original personal questions
    personal_questions = {
        "name": "What is your name? ",
        "age": "How old are you? ",
        "color": "What is your favorite color? ",
        "food": "What is your favorite food? ",
        "city": "Which city do you live in? ",
        "shs": "Which SHS did you attend? ",
        "team": "What is your favorite soccer team? ",
        "hobby": "What is one of your hobbies? ",
        "movie": "What is your favorite movie? ",
        "music": "What kind of music do you like? "
    }

    # New fun/personality-based questions
    fun_questions = {
        "superpower": "If you could have any superpower, what would it be? ",
        "dream_job": "What’s your dream job? ",
        "morning_night": "Are you more of a morning person or a night owl? ",
        "cant_live_without": "What’s one thing you can’t live without? ",
        "travel_place": "What’s the most interesting place you’ve ever visited? ",
        "live_anywhere": "If you could live anywhere in the world, where would it be? ",
        "adventure": "Have you ever tried something adventurous like skydiving or scuba diving? ",
        "game": "What’s your all-time favorite video game or board game? ",
        "new_hobby": "What’s a hobby you’ve always wanted to try but haven’t yet? ",
        "fictional_character": "Who’s your favorite fictional character? ",
        "learning": "What’s a skill you’re currently learning or want to learn? ",
        "advice": "What’s the best advice you’ve ever received? ",
        "books_docs": "Do you prefer reading books or watching documentaries? ",
        "animal": "If you were an animal, what would you be and why? ",
        "karaoke": "What’s your go-to karaoke song? ",
        "time_machine": "If you had a time machine, would you go to the past or the future? "
    }

    # Combine and randomly select 6 questions
    all_questions = {**personal_questions, **fun_questions}
    selected_keys = random.sample(list(all_questions.keys()), k=6)
    answers = {}

    for key in selected_keys:
        answers[key] = input(all_questions[key])

    return answers
def create_summary(answers):
    summary = f"\nHello, {answers.get('name', 'Friend')}!\n"
    for key, value in answers.items():
        if key != "name":
            summary += f"- {value}\n"
    return summary

def save_to_file(name, summary, rating):
    filename = f"{name}.txt"
    with open(filename, "w") as f:
        f.write(summary)
        f.write(f"\nUser Rating: {rating} stars\n")
    print(f"Summary saved to {filename}")

def main():
    while True:
        answers = ask_questions()
        summary = create_summary(answers)
        print("\n--- Your Personalized Summary ---")
        print(summary)

        save = input("Would you like to save this summary to a file? (yes/no): ").strip().lower()
        if save == "yes":
            rating = input("Please rate this assistant (1 to 5 stars): ").strip()
            save_to_file(answers.get("name", "user"), summary, rating)

        restart = input("Would you like to restart the process? (yes/no): ").strip().lower()
        if restart != "yes":
            print("Thank you for using the assistant. Goodbye!")
            break

if __name__ == "__main__":
    main()
