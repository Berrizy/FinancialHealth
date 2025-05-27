def get_user_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def calculate_financial_health(income, expenses, savings_goal):
    surplus = income - expenses
    savings_percentage = (savings_goal / income) * 100 if income else 0

    if surplus > 500:
        rating = "Excellent"
    elif surplus > 0:
        rating = "Good"
    elif surplus == 0:
        rating = "Neutral"
    else:
        rating = "Needs Improvement"

    advice = ""
    if surplus < 0:
        advice = "You're spending more than you earn. Consider cutting non-essential expenses."
    elif savings_percentage < 20:
        advice = "Try to save at least 20% of your income if possible."
    else:
        advice = "You're on track! Keep it up."

    return surplus, rating, savings_percentage, advice

def main():
    print(" Welcome to the Financial Health Checker!\n")
    income = get_user_input("Enter your monthly income ($): ")
    expenses = get_user_input("Enter your monthly expenses ($): ")
    savings_goal = get_user_input("How much would you like to save this month? ($): ")

    surplus, rating, savings_pct, advice = calculate_financial_health(income, expenses, savings_goal)

    print("\n Results:")
    print(f"→ Monthly Surplus/Deficit: ${surplus:.2f}")
    print(f"→ Financial Health Rating: {rating}")
    print(f"→ Savings Goal: {savings_pct:.1f}% of income")
    print(f"→ Advice: {advice}")

if __name__ == "__main__":
    main()
