from school import School, PrimarySchool, HighSchool


def main():
    a = School("Codecademy", "high", 100)
    print(a)
    print(a.name)
    print(a.level)
    a.numberOfStudents = 200
    print(a.numberOfStudents)

    b = PrimarySchool("Codecademy", 300, "Pickup Allowed")
    print(b.pickupPolicy)
    print(b)

    c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
    print(c.sportTeams)
    print(c)

if __name__ == "__main__":
    main()