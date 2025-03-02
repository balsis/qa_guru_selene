from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import List


class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'


class Hobby(Enum):
    SPORTS = "Sports"
    READING = "Reading"
    MUSIC = "Music"


@dataclass
class User:
    firstname: str
    lastname: str
    email: str
    gender: str
    phone_number: str
    date_of_birth: date
    hobbies: List[str]
    subjects: List[str]
    picture: str
    current_address: str
    state: str
    city: str


def format_date(day: int, month: int, year: int) -> str:
    return date(year, month, day).strftime('%d %B,%Y')


user = User(
    firstname = "Ivan",
    lastname = "Ivanov",
    email = "test@test.com",
    gender = Gender.MALE.value,
    phone_number = "7911111111",
    date_of_birth = date(day = 11, month = 11, year = 2011),
    hobbies = [Hobby.SPORTS.value, Hobby.MUSIC.value],
    subjects = ["Maths", "History"],
    picture = "avatar.png",
    current_address = "Pushkina street, Kolotushkina house",
    state = "Haryana",
    city = "Panipat"
)
