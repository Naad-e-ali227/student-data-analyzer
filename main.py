import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "students.csv"
SUBJECTS = ["Maths", "Physics", "ComputerScience"]


def load_data():
    return pd.read_csv(DATA_FILE)


def show_summary(data):
    print("\n===== Dataset Summary =====")
    print(f"Students analyzed: {len(data)}")
    print(f"Subjects analyzed: {len(SUBJECTS)}")

    print("\nAverage scores:")

    for subject in SUBJECTS:
        print(f"{subject}: {data[subject].mean():.1f}")


def show_extremes(data):
    print("\n===== Highest and Lowest Scores =====")

    for subject in SUBJECTS:
        highest = data.loc[data[subject].idxmax()]
        lowest = data.loc[data[subject].idxmin()]

        print(f"\n{subject}")
        print(f"Highest: {highest['Name']} - {highest[subject]}")
        print(f"Lowest: {lowest['Name']} - {lowest[subject]}")


def show_student_averages(data):
    data["Average"] = data[SUBJECTS].mean(axis=1)

    print("\n===== Student Averages =====")

    for _, student in data.iterrows():
        print(f"{student['Name']}: {student['Average']:.1f}")

    top_student = data.loc[data["Average"].idxmax()]

    print(
        f"\nTop student: {top_student['Name']} "
        f"({top_student['Average']:.1f} average)"
    )


def analyze_subject(data):
    print("\n===== Subject Analysis =====")

    for number, subject in enumerate(SUBJECTS, start=1):
        print(f"{number}. {subject}")

    choice = input("\nChoose a subject (1-3): ").strip()

    if not choice.isdigit() or not 1 <= int(choice) <= len(SUBJECTS):
        print("Invalid choice.")
        return

    subject = SUBJECTS[int(choice) - 1]

    average = data[subject].mean()
    highest = data.loc[data[subject].idxmax()]
    lowest = data.loc[data[subject].idxmin()]

    print(f"\n===== {subject} Analysis =====")
    print(f"Average: {average:.1f}")
    print(f"Highest: {highest['Name']} - {highest[subject]}")
    print(f"Lowest: {lowest['Name']} - {lowest[subject]}")


def create_average_chart(data):
    averages = data[SUBJECTS].mean()

    averages.plot(kind="bar")

    plt.title("Average Score by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Average Score")
    plt.ylim(0, 100)
    plt.tight_layout()

    plt.savefig("average_scores.png")
    plt.show()
    plt.close()


def create_student_chart(data):
    data.plot(
        x="Name",
        y=SUBJECTS,
        kind="bar",
        figsize=(10, 6)
    )

    plt.title("Student Scores by Subject")
    plt.xlabel("Student")
    plt.ylabel("Score")
    plt.ylim(0, 100)
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("student_scores.png")
    plt.show()
    plt.close()


def main():
    data = load_data()

    print("===== Student Data Analyzer =====")

    show_summary(data)
    show_extremes(data)
    show_student_averages(data)
    analyze_subject(data)

    print("\nCreating charts...")
    create_average_chart(data)
    create_student_chart(data)

    print("\nAnalysis complete!")


if __name__ == "__main__":
    main()