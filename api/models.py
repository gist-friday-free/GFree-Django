from enum import Enum

from django.db import models
from django.db.models import CASCADE


class SemesterChoices(Enum):
    First = 1
    Second = 2


class GradeChoices(Enum):
    Zero = 0
    One = 1
    Two = 2
    Three = 3
    Four = 4


class WeekChoices(Enum):
    Monday = 'mon'
    Tuesday = 'tue'
    Wednesday = 'wed'
    Thursday = 'thu'
    Friday = 'fri'
    Saturday = 'sat'
    Sunday = 'sun'


class EditType(Enum):
    ADD = "ADD"
    REMOVE = "REMOVE"

    CODE = "CODE"
    NAME = "NAME"
    GRADE = "GRADE"
    PROFESSOR = "PROFESSOR"
    PLACE = "PLACE"
    SIZE = "SIZE"

    TIMEADD = "TIMEADD"
    TIMEREMOVE = "TIMEREMOVE"


class Class(models.Model):
    year = models.IntegerField()
    semester = models.IntegerField(choices=[(semester.value, semester.name) for semester in SemesterChoices])
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20)
    professor = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    size = models.IntegerField()

    grade = models.IntegerField(choices=[(grade.value, grade.name) for grade in GradeChoices])

    start1 = models.TimeField(null=True, blank=True)
    end1 = models.TimeField(null=True, blank=True)
    week1 = models.CharField(max_length=20, choices=[(week.value, week.name) for week in WeekChoices], null=True,
                             blank=True)

    start2 = models.TimeField(null=True, blank=True)
    end2 = models.TimeField(null=True, blank=True)
    week2 = models.CharField(max_length=20, choices=[(week.value, week.name) for week in WeekChoices], null=True,
                             blank=True)

    start3 = models.TimeField(null=True, blank=True)
    end3 = models.TimeField(null=True, blank=True)
    week3 = models.CharField(max_length=20, choices=[(week.value, week.name) for week in WeekChoices], null=True,
                             blank=True)

    start4 = models.TimeField(null=True, blank=True)
    end4 = models.TimeField(null=True, blank=True)
    week4 = models.CharField(max_length=20, choices=[(week.value, week.name) for week in WeekChoices], null=True,
                             blank=True)

    start5 = models.TimeField(null=True, blank=True)
    end5 = models.TimeField(null=True, blank=True)
    week5 = models.CharField(max_length=20, choices=[(week.value, week.name) for week in WeekChoices], null=True,
                             blank=True)

    def __str__(self):
        return self.name

class ClassTemp(models.Model):
    year = models.IntegerField()
    semester = models.IntegerField(choices=[(semester.value, semester.name) for semester in SemesterChoices])
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20)
    professor = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    size = models.IntegerField()

    grade = models.IntegerField(choices=[(grade.value, grade.name) for grade in GradeChoices])

    start1 = models.TimeField(null=True, blank=True)
    end1 = models.TimeField(null=True, blank=True)
    week1 = models.CharField(max_length=20, choices=[(week.value, week.name) for week in WeekChoices], null=True,
                             blank=True)

    start2 = models.TimeField(null=True, blank=True)
    end2 = models.TimeField(null=True, blank=True)
    week2 = models.CharField(max_length=20, choices=[(week.value, week.name) for week in WeekChoices], null=True,
                             blank=True)

    start3 = models.TimeField(null=True, blank=True)
    end3 = models.TimeField(null=True, blank=True)
    week3 = models.CharField(max_length=20, choices=[(week.value, week.name) for week in WeekChoices], null=True,
                             blank=True)

    start4 = models.TimeField(null=True, blank=True)
    end4 = models.TimeField(null=True, blank=True)
    week4 = models.CharField(max_length=20, choices=[(week.value, week.name) for week in WeekChoices], null=True,
                             blank=True)

    start5 = models.TimeField(null=True, blank=True)
    end5 = models.TimeField(null=True, blank=True)
    week5 = models.CharField(max_length=20, choices=[(week.value, week.name) for week in WeekChoices], null=True,
                             blank=True)

    def __str__(self):
        return self.name


class User(models.Model):
    uid = models.CharField(max_length=100, primary_key=True)
    email = models.EmailField()
    majorCode = models.CharField(max_length=50)
    studentId = models.IntegerField()
    sex = models.IntegerField()
    age = models.IntegerField()
    classes = models.ManyToManyField(Class)

    def __str__(self):
        return self.email + ", uid = " + str(self.uid)


class Notice(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    writer = models.CharField(max_length=50)

    def __str__(self):
        return self.title + ", time = " + str(self.created)


class Review(models.Model):
    reviewClass = models.ForeignKey("Class", on_delete=CASCADE)
    writer = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reviewClass.name + ", writer : " + self.writer


class Edit(models.Model):
    year = models.IntegerField()
    semester = models.IntegerField(choices=[(semester.value, semester.name) for semester in SemesterChoices])
    editClass = models.ForeignKey("Class", on_delete=CASCADE)
    writer = models.EmailField()

    created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=20, choices=[(type.value, type.name) for type in EditType])
    value = models.CharField(max_length=100,blank=True)

    star = models.ManyToManyField(to="User",default=[],blank=True)

    def __str__(self):
        return 'Request : '+str(self.editClass)+' Type : '+str(self.type)

    class Meta:
        ordering = ['-created']


class PlayStoreInfo(models.Model):
    versionName = models.CharField(max_length=50)
    versionCode = models.IntegerField()

    def __str__(self):
        return self.versionName + "(" + str(self.versionCode) + ")"
