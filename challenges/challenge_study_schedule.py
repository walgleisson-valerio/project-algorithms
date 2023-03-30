def study_schedule(permanence_period, target_time):
    students_present = 0

    try:
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                students_present += 1
        return students_present

    except TypeError:
        return None
