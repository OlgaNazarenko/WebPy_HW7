from sqlalchemy import Column, Integer, String, func, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from database.connect import engine

Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    title = Column(String(150))

    students = relationship("Students")
    discipline = relationship("Disciplines")


class Professor(Base):
    __tablename__ = "professors"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)

    discipline = relationship("Disciplines", back_populates="professor")
    mark = relationship("Marks", back_populates="professor")


class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id", ondelete="CASCADE"))

    mark = relationship("Marks")


class Disciplines(Base):
    __tablename__ = "disciplines"
    id = Column(Integer, primary_key=True)
    discipline = Column(String(150), nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id", ondelete = "CASCADE"))
    professor_id = Column(Integer, ForeignKey("professors.id", ondelete="CASCADE"))

    professor = relationship("Professor", back_populates="discipline")
    group = relationship("Group", back_populates="discipline")
    mark = relationship("Marks", back_populates="discipline")


class Marks(Base):
    __tablename__ = "marks"
    id = Column(Integer, primary_key=True)
    mark = Column(Integer)
    lesson_date = Column(Date, default=func.now())
    students_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"),
                         nullable=False)
    discipline_id = Column(Integer, ForeignKey("disciplines.id", ondelete="CASCADE"),
                           nullable=False)
    professor_id = Column(Integer, ForeignKey("professors.id", ondelete="CASCADE"),
                          nullable=False)

    discipline = relationship("Disciplines", back_populates="mark")
    student = relationship("Students", back_populates="mark")
    professor = relationship("Professor", back_populates="mark")


Base.metadata.create_all(engine)
Base.metadata.bind = engine
