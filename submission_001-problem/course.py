

def create_outline():
    """
    TODO: implement your code here
    """
    course_topics = ["Introduction to Python","Tools of the Trade","How to make decisions","How to repeat code","How to structure data","Functions","Modules"]
    course_topics = set(course_topics)
    topics = list(set(course_topics))
    s_topics = sorted(topics)
    i = 0
    print("Course Topics:")
    for j in topics:
        print("* " + s_topics[i])
        i += 1

    j = 0
    
    print("Problems:")
    for k in topics:
        course_map = {topics[j]: ["Problem 1", "Problem 2", "Problem 3"]}
        for topic in course_map:
            print("* " + topic +" : ",end="")
            s = 0
            for problemo in course_map.get(topics[j]):
                if s > 0 and s < len(course_map.get(topics[j])):
                    print(", ",end="")
                print(problemo,end="")
                s += 1
        j += 1
        print()
    
    print("Student Progress:")
    count = 1
    student_progress = [
        ("Mzingaye", "Tools of the Trade", "Problem 2", "[STARTED]"),
        ("Isaya", "How to make decisions", "Problem 2", "[GRADED]"),
        ("Advocate", "Modules", "Problem 3", "[COMPLETED]")
    ]
    m = 0
    while m < len(student_progress):
        i = student_progress[m]
        print(str(m + 1) + ". "+i[0] + " - " + i[1] + " - " +i[2] + " " +i[3])
        m += 1    
    
if __name__ == "__main__":
    create_outline()
