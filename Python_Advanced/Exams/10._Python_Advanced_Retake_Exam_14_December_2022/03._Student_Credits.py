def students_credits(*args):
    total_credits = 0
    exam_results = {}
    for data in args:
        course_name, course_credit, max_points, exam_result = data.split("-")
        current_credits = int(exam_result) / int(max_points) * int(course_credit)
        exam_results[course_name] = current_credits
        total_credits += current_credits
    exam_results_sorted = sorted(exam_results.items(), key=lambda x: -x[1])
    result = ''
    if total_credits >= 240:
        result += f'Diyan gets a diploma with {total_credits:.1f} credits.'
    else:
        result += f'Diyan needs {240 - total_credits:.1f} credits more for a diploma.'
    for course_name, credits_achieved in exam_results_sorted:
        result += f'\n{course_name} - {credits_achieved:.1f}'
    return result


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)
print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
