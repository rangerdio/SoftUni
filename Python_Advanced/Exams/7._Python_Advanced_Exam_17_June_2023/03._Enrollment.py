def gather_credits(credits_needed, *course_info):
    current_credits = 0
    my_courses = {}
    for course_name, course_credits in course_info:
        if current_credits < credits_needed and course_name not in my_courses:
            current_credits += course_credits
            my_courses[course_name] = course_credits

    result = ''
    my_courses_sorted = sorted(my_courses.keys(), key=lambda x: x)
    if current_credits >= credits_needed:
        result += (f'Enrollment finished! Maximum credits: {current_credits}.\n'
                   f'Courses: {", ".join(x for x in my_courses_sorted)}')
    else:
        result += (f'You need to enroll in more courses! '
                   f'You have to gather {credits_needed - current_credits} credits more.')
    return result


print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
