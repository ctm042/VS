class Course:
    def __init__(self, name, hrs, prereq, coreq, passed):
        self.name = name
        self.hrs = hrs
        self.prereq = prereq
        self.coreq = coreq
        self.passed = passed

class Course2:
    def __init__(self, token, name, prereq, coreq, passed):
        self.token = token
        self.name = name
        self.prereq = [""]
        self.coreq = [""]
        self.passed = False

class Curiculm:
    def __init__(self, major, c):
        self.major = major
        self.c = c

        #append the obj courses named in c into a new list var

#Elective vars
FineArts = 1 #0
CSCElective = 3
MATHElective = 1
Concentration = 4
SocialScience = 2 #0

DEBUG = True

def elicheck(c):
    if not c.prereq == [""]:
        if not prereqcheck(c):
            return False
    if not c.coreq == [""]:
        if not coreqcheck(c):
            return False
    return True

def prereqcheck(c):
    #print(f"<PRC> {c.name} \tPrereqs = {c.prereq}")
    for prereq in c.prereq:
        for obj in courses:
            if obj.name == prereq:
                if not obj.passed:
                    #print(f"\t{prereq}: Passed = False")
                    return False
                #else: print(f"\t{prereq}: Passed = True")
    return True

def coreqcheck(c):
    #print(f"<CRC> {c.name} \tCoreqs =  {c.coreq}")
    for coreq in c.coreq:
        for obj in courses:
            if obj.name == coreq:
                if not obj.passed:
                    #print(f"\t{coreq}: Passed = False")
                    return elicheck(obj)
                #else: print(f"\t\t{coreq}: Passed = True")
    return True

def passed(name):
    for obj in courses:
        if obj.name == name:
            obj.passed = True



courses = [
    Course("CSC-130", 3, ["MATH-101"], [""], False),
    Course("CSC-131", 3, ["CSC-130"], [""], False),
    Course("CSC-132", 3, ["CSC-131"], [""], False),
    Course("CSC-220", 3, ["CSC-132"], ["MATH-240"], False),
    Course("CSC-222", 3, ["CSC-132"], ["MATH-240"], False),
    Course("CSC-265", 3, ["CSC-132"], [""], False),
    Course("CSC-310", 3, ["CSC-220", "MATH-311"], [""], False),
    Course("CSC-325", 3, ["CSC-220"], ["MATH-311"], False),
    Course("CSC-330", 3, ["CSC-325"], [""], False),
    Course("CSC-345", 3, ["CSC-222"], [""], False),
    Course("CSC-364", 3, ["CSC-265"], [""], False),
    Course("CSC-403", 3, ["CSC-325", "Senior-Standing"], [""], False),
    Course("CSC-405", 2, ["CSC-403"], [""], False),
    Course("CSC-406", 1, ["CSC-405"], [""], False),
    Course("CSC-430", 3, ["CSC-220"], [""], False),

    Course("BISC-130", 3, [""], [""], False),
    Course("BISC-131", 1, [""], ["BISC-130"], False),

    Course("COMM-101", 3, [""], [""], False),

    Course("ENGL-101", 3, [""], [""], False),
    Course("ENGL-102", 3, ["ENGL-101"], [""], False),
    Course("ENGL-210", 3, ["ENGL-102"], [""], False), #
    Course("ENGL-211", 3, ["ENGL-102"], [""], False),#
    Course("ENGL-212", 3, ["ENGL-102"], [""], False),#
    Course("ENGL-303", 3, ["ENGL-102"], [""], False),
    Course("ENGL-363", 3, ["ENGL-303"], [""], False),

    Course("MATH-240", 3, [""], [""], False),
    Course("MATH-241", 3, ["MATH-240"], [""], False),
    Course("MATH-242", 3, ["MATH-241"], [""], False),
    Course("MATH-311", 3, ["MATH-242"], [""], False),

    Course("PHYS-201", 3, ["MATH-241"], [""], False),
    Course("PHYS-202", 3, ["PHYS-201","MATH-242"], [""], False),
    Course("PHYS-261", 1, ["MATH-240"], [""], False),
    Course("PHYS-262", 1, ["PHYS-261"], [""], False),

    Course("STAT-405", 3, ["MATH-242"], [""], False)
]

#Transfer Credits
passed("ENGL-101")
passed("ENGL-102")

#Fall 2021
passed("COMM-101")
passed("CSC-130")
passed("FYE-100")
passed("MUEN-271")

#Winter 2022
passed("CSC-131")
passed("ENGR-120")
passed("MATH-240")
passed("MUGN-290")

#Spring 2022
passed("CSC-132")
passed("ENGR-121")
passed("MATH-241")

#Fall 2022
passed("CSC-220")
passed("ENGR-122")

#Winter 2023
passed("CSC-222")
passed("MATH-242")
passed("PHYS-201")
passed("SOC-201")

#Spring
passed("CSC-345")
passed("CSC-301")

#Summer 2023
passed("ENGL-303")

#Fall 2023
passed("BISC-130")
passed("CSC-265")
passed("ENGL-210") #
passed("ENGL-211") #
passed("ENGL-212") #
passed("GEOG-321")

#Winter 2024
passed("MATH-311")
passed("CSC-430")
passed("CSC-325")
passed("BISC-131")
passed("PHYS-261")

#Spring 2024
passed("CSC-330")
passed("PHYS-202")
passed("PHYS-262")
#CSC Directed Elective 1/2 (CSC-470) Game Design


#Summer 2024
passed("STAT-405")
passed("ENGL-363") # NOT AVAILABLE

#Fall 2024
passed("CSC-310")
passed("CSC-364")
passed("CSC-403")
#Minor/Concentration 1/4 (ELEN-242) Introduction to Microprocessors


#Winter 2025
passed("CSC-405")
#CSC Directed Elective 2/2 (CSC-450) Computer Networks
#Math elective 1/1 

#Minor/Concentration 2/4 (ELEN-333) Introduction to Digital Design

#Spring 2025
passed("CSC-406")
#Minor/Concentration 3/4 (ELEN-423) Embedded Systems
#Minor/Concentration 4/4 (ENGR-221) Electrical Engineering and Circuits 1

for c in courses:
    if not c.passed and elicheck(c): 
        print(c.name)
        #print(f"Eligible = {elicheck(c)}\n")

if "test" in ["hey", ["in", "here", "test"], "test"]: print("true")
