from django.db import models
# Create your models here.

class InstructorCategory(models.Model):
    instructor_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Catergories"

    def __str__(self):
        return self.instructor_category

class InstructorSeries(models.Model):
    instructor_series = models.CharField(max_length=200)
    instructor_category = models.ForeignKey(InstructorCategory, default=1,
                                            verbose_name="Catergory", on_delete=models.SET_DEFAULT)
    series_summaries = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.instructor_series

class Instructors(models.Model):
    instructor_name = models.CharField(max_length=200)
    instructor_age = models.SmallIntegerField()
    instructor_price = models.DecimalField(max_digits=6, decimal_places=2)
    instructor_image = models.ImageField(upload_to='static', blank=True)

    instructor_series = models.ForeignKey(InstructorSeries, default=1,
                                            verbose_name="Series", on_delete=models.SET_DEFAULT)
    instructor_slug = models.CharField(max_length=200, default=1)
    class Meta:
        verbose_name_plural = "Instructors"

    def __str__(self):
        return self.instructor_name
