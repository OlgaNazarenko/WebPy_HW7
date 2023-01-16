from sqlalchemy import desc, func, desc

from database.connect import session
from database.models import Group, Professor, Students, Marks, Disciplines


#найти 5 студентов с наибольшим средним баллом по всем предметам.
def select_1() -> list:
    print("Студенти з найвищим середнім балом: ")
    result = (
        session.query(Students.first_name, Students.last_name, func.round(func.avg(Marks.mark), 2).label('avg_grade'))\
        .select_from(Marks)
        .join(Students)
        .group_by(Students.id)
        .order_by(desc('avg_grade'))
        .limit(5)
        .all()
    )
    return result

# Найти студента с наивысшим средним баллом по определенному предмету.
def select_2() -> list:
    return(
        session.query(Disciplines.discipline, Students.last_name, func.round(func.avg(Marks.mark), 2).label("avg_mark"))
        .select_from(Marks)
        .join(Students, Disciplines)
        .group_by(Students.last_name, Disciplines.id, Disciplines)
        .order_by(Disciplines.discipline, desc("avg_mark"))
        .limit(1)
        .all()
    )


 #Найти средний балл в группах по определенному предмету.
def select_3() -> list:
    discipline_value: str = input("Choose the discipline (Python, Java, Korean, Japanese, QA):  ")
    return(
        session.query(Disciplines.discipline, Group.title, func.round(func.avg(Marks.mark), 2).label("avg_mark"))
        .select_from(Marks)
        .join(Students, Disciplines, Group)
        .filter(Disciplines.discipline == discipline_value)
        .order_by(Group.id, Group.title)
        .all()
    )


#Найти средний балл на потоке (по всей таблице оценок).
def select_4() -> list:
    return(
        session.query(func.round(func.avg(Marks.mark), 2).label("avg_mark"))
        .select_from(Marks)
        .order_by("avg_mark")
        .all()
    )


#Найти какие курсы читает определенный преподаватель.
def select_5() -> list:
    pr_id: str = input("Write the professor's ID:  ")
    return(
        session.query(Disciplines.discipline, Professor.last_name)
        .select_from(Disciplines)
        .join(Professor)
        .filter(Professor.id == pr_id)
        .all()
    )


#Найти список студентов в определенной группе.
def select_6() -> list:
    group_title: str = input("Write the group title (A, B, C, D):  ")

    return(
        session.query(Students.last_name, Group.title)
        .select_from(Students)
        .join(Group)
        .distinct()
        .filter(Group.title == group_title)
        .all()
    )


#Найти оценки студентов в отдельной группе по определенному предмету.
def select_7() -> list:
    group_title: str = input("Write the group title (A, B, C, D):  ")
    discipline_name: str = input("Choose the discipline (Python, Java, Korean, Japanese, QA):  ")

    return(
        session.query(Students.last_name, Students.group_id, Marks.mark, Disciplines.discipline)
        .select_from(Students)
        .join(Marks)
        .join(Group)
        .join(Disciplines)
        .distinct()
        .filter(Group.title == group_title, Disciplines.discipline == discipline_name)
        .order_by(desc(Marks.mark), Students.last_name)
        .all()
    )


#Найти средний балл, который ставит определенный преподаватель по своим предметам.
def select_8() -> list:
    pr_id: str = input("Write the professor's ID:  ")

    return(
        session.query(Professor.last_name, func.round(func.avg(Marks.mark), 2).label("avg_mark"))
        .select_from(Professor)
        .join(Marks)
        .filter(Professor.id == pr_id)
        .order_by(Professor.last_name, desc("avg_mark"))
        .all()
    )


#Найти список курсов, которые посещает определенный студент.
def select_9() -> list:
    st_id: str = input("Write the student's ID:  ")

    return(
        session.query(Students.last_name, Disciplines.discipline)
        .select_from(Marks)
        .join(Disciplines, Students)
        .filter(Marks.students_id == st_id)
        .group_by(Students.last_name)
        .order_by(Disciplines.discipline)
        .distinct()
        .all()
    )


#Список курсов, которые определенному студенту читает определенный преподаватель.
def select_10() -> list:
    st_id: str = input("Write the student's ID:  ")
    pr_id: str = input("Write the teacher's ID:  ")

    return(
        session.query(Students.last_name, Professor.last_name, Disciplines.discipline)
        .select_from(Students)
        .join(Marks)
        .join(Disciplines)
        .join(Professor)
        .distinct()
        .filter(Students.id == st_id, Professor.id == pr_id)
        .order_by(Professor.last_name, Disciplines.discipline)
        .all()
    )


if __name__ == '__main__':
    print(f"{select_10()}")
