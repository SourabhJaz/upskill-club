from django.db import models
from .constants import TEXT_CONSTRAINTS, COURSE_CATEGORIES

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = TEXT_CONSTRAINTS['SINGLE_NAME_LEN'], choices = COURSE_CATEGORIES, unique = True)
    outline = models.CharField(max_length = TEXT_CONSTRAINTS['OUTLINE_LEN'])
    thumbnail = models.FileField(blank = True, null = True)

class Author(models.Model):
    name = models.CharField(max_length = TEXT_CONSTRAINTS['TITLE_LEN'], unique = True)
    image_url = models.URLField(blank = True, null = True)
    linkedin_url = models.URLField(blank = True, null = True, max_length=1000)
    outline = models.CharField(max_length = TEXT_CONSTRAINTS['OUTLINE_LEN'])

class Course(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    title = models.CharField(max_length = TEXT_CONSTRAINTS['TITLE_LEN'], unique = True)
    outline = models.CharField(max_length = TEXT_CONSTRAINTS['OUTLINE_LEN'])
    short_description = models.CharField(max_length = TEXT_CONSTRAINTS['SHORT_DESCRIPTION_LEN'])
    author = models.ForeignKey(Author, on_delete = models.DO_NOTHING)
    image_url = models.URLField(blank = True, null = True, max_length=1000)
    created_at = models.DateField(null = True)

class Session(models.Model):
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    title = models.CharField(max_length = TEXT_CONSTRAINTS['TITLE_LEN'])
    outline = models.CharField(max_length = TEXT_CONSTRAINTS['OUTLINE_LEN'])
    image_url = models.URLField(blank = True, null = True, max_length=1000)
    author = models.ForeignKey(Author, on_delete = models.DO_NOTHING, null = True)
    created_at = models.DateField(null = True)


class Concept(models.Model):
    session = models.ForeignKey(Session, on_delete = models.DO_NOTHING)
    title = models.CharField(max_length = TEXT_CONSTRAINTS['TITLE_LEN'], blank = True, null = True)
    image_url = models.URLField(blank = True, null = True, max_length=1000)
    description = models.CharField(max_length = TEXT_CONSTRAINTS['DESCRIPTION_LEN'])
