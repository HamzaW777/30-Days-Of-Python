def q1():
    dog={'name': 'Buddy', 'age': 5, 'breed': 'Golden Retriever'}
    student={'name': 'Alice',
        'age': 20,
        'major': 'Computer Science',
        'skills': ['Python', 'Java', 'C++']}
      # print(len(student))
      # print(student['skills'])
      # print(type(student['skills']))
    student['skills'].append(['JavaScript','DevOps'])
    keys=list(student.keys())
      #print(keys)
      #values=list(student.values())
      #print(values)
    student_items=student.items()
    print(student_items)
    student.pop('age')
    del dog
q1()

