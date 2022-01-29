def main():

    score = [
        [88, 64, 58, 63],
        [12, 34, 56, 78],
        [98, 87, 76, 65]
    ]

    total = 0
    totalsub = 0

    for student in score:
        subject_total = 0
        for subject in student:
            subject_total += subject
        
        subjects = len(student)
        print("총점 %d, 평균 %.2f" % (subject_total, subject_total/subjects))
        total += subject_total
        totalsub += subjects

    print("전체평균 %.2f" % (total/totalsub))
    
main()