import random

def summation_vote(students):
    num_vote = num_notvote = 0
    for student in students:
        if student == 0:
            num_notvote += 1
        else:
            num_vote += 1
    return num_vote, num_notvote

def result_vote(students, max_chairman):
    votes = [0] * (max_chairman + 1)
    for student in students:
        votes[student] += 1
    return votes

def report(votes, percents, max_chairman, num_vote):
    print("Result of election chairman\n---------------------------")
    print("| No. | Votes | Percent(%)|\n---------------------------")
    for n in range(1, max_chairman + 1, 1):
        print(f"| {n:2}. | {votes[n]:5} | {percents[n]:9.2f} |")
    print("---------------------------")
    print(f"|Total| {num_vote:5} |    100.00 |")

MAX = 500
students = []
max_chairman = 0

random.seed()
max_chairman = int(input("Enter number of student chairmen: "))
if max_chairman > 0:
    for n in range(MAX):
        students.append(random.randint(0, max_chairman))

    num_vote, num_notvote = summation_vote(students)

    percent_vote = (num_vote * 100.0) / MAX
    percent_notvote = (num_notvote * 100.0) / MAX

    print(f"Number of students: {MAX}")
    print(f"Number of votes: {num_vote} = {percent_vote:.2f}%")
    print(f"Number of not votes: {num_notvote} = {percent_notvote:.2f}%")

    votes = result_vote(students, max_chairman)
    percents = [(votes[i] * 100.0) / num_vote for i in range(max_chairman + 1)]
    report(votes, percents, max_chairman, num_vote)
