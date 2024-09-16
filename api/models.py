from django.db import models
from .constants import TEXT_CONSTRAINTS, COURSE_CATEGORIES

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = TEXT_CONSTRAINTS['SINGLE_NAME_LEN'], choices = COURSE_CATEGORIES, unique = True)
    outline = models.CharField(max_length = TEXT_CONSTRAINTS['OUTLINE_LEN'])
    thumbnail = models.FileField(blank = True, null = True)

class Author(models.Model):
    name = models.CharField(max_length = TEXT_CONSTRAINTS['TITLE_LEN'], unique = True)
    thumbnail = models.FileField(blank = True, null = True)
    linkedInUrl = models.URLField()
    outline = models.CharField(max_length = TEXT_CONSTRAINTS['OUTLINE_LEN'])

class Course(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    title = models.CharField(max_length = TEXT_CONSTRAINTS['TITLE_LEN'], unique = True)
    outline = models.CharField(max_length = TEXT_CONSTRAINTS['OUTLINE_LEN'])
    short_description = models.CharField(max_length = TEXT_CONSTRAINTS['SHORT_DESCRIPTION_LEN'])
    thumbnail = models.FileField(blank = True, null = True)
    author = models.ForeignKey(Author, on_delete = models.DO_NOTHING)
    image = models.FileField(blank = True, null = True)
    created_at = models.DateField(null = True)

class Session(models.Model):
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    title = models.CharField(max_length = TEXT_CONSTRAINTS['TITLE_LEN'], unique = True)
    outline = models.CharField(max_length = TEXT_CONSTRAINTS['OUTLINE_LEN'])
    thumbnail = models.FileField(blank = True, null = True)
    author = models.ForeignKey(Author, on_delete = models.DO_NOTHING, null = True)
    created_at = models.DateField(null = True)


class Concept(models.Model):
    session = models.ForeignKey(Session, on_delete = models.DO_NOTHING)
    title = models.CharField(max_length = TEXT_CONSTRAINTS['TITLE_LEN'])
    image = models.FileField(blank = True, null = True)
    description = models.CharField(max_length = TEXT_CONSTRAINTS['DESCRIPTION_LEN'])
