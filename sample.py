import time

def print_header(title):
    print("\n" + "="*len(title))
    print(title)
    print("="*len(title))

def pause():
    input("\nPress Enter to continue...")

def day_1():
    print_header("Day 1: Platform Familiarization & Basic Testing")
    input("✅ Visit URL and describe the homepage layout: ") #replace URL with your platform link
    input("✅ Visit docs and list main key points: ") #replace docs with your platform docs/blog
    input("✅ What categories are available? List 3 examples: ")
    input("✅ Switch between languages Arabic and English. Any localization issues? (Y/N, describe): ")
    input("✅ Try registering or logging in. Describe the user flow: ")
    input("✅ Explore the application submission flow. What steps did you observe? ")
    input("✅ List any UI/UX issues or bugs you found so far: ")
    pause()

def day_2():
    print_header("Day 2: Test Case Writing & Hands-On Testing")
    input("✅ Write 2–3 test cases for user registration. Briefly summarize one: ")
    input("✅ Write test cases for CRUD operations (e.g., attachments, dropdowns): ")
    input("✅ Perform manual testing. Did any test cases fail? List failures if any: ")
    input("✅ Upload a file (PDF, image). Did the validation behave correctly? ")
    input("✅ Are the field validations working (e.g., required fields, formats)? ")
    input("✅ List any bugs or defects you encountered today: ")
    pause()

def day_3():
    print_header("Day 3: Deep Dive & Reporting")
    input("✅ Open portal on mobile and desktop. Did you notice any responsive layout issues? ")
    input("✅ Toggle language mid-process. Any breakage in flow or UI? ")
    input("✅ Estimate page load times (slow/acceptable/fast): ")
    input("✅ Try using the 'Ask Abdea' form or FAQ. How clear and helpful is it? ")
    input("✅ Review your test cases. Can you add 1–2 negative or edge test cases? ")
    input("✅ What reporting format will you use for bugs and test results (e.g., Excel, Jira)? ")
    input("✅ Final thoughts: what do you feel confident about and where do you need support? ")
    pause()

def main():
    print_header("🚀 3-Day QC Onboarding Program")

    while True:
        print("\nChoose a day to begin or review:")
        print("1. Day 1 - Familiarization")
        print("2. Day 2 - Test Case Writing")
        print("3. Day 3 - Deep Dive")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            day_1()
        elif choice == '2':
            day_2()
        elif choice == '3':
            day_3()
        elif choice == '4':
            print("🎉 Good luck with your QC journey!")
            break
        else:
            print("❌ Invalid input. Please select 1-4.")

if __name__ == "__main__":
    main()
