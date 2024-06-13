from django.db import models

class KitchenLunch(models.Model):
    date = models.DateField()
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES,default='JP23')
    balls_amount = models.IntegerField()
    today_balls_total = models.IntegerField()
    yesterday_balls_total = models.IntegerField()

    class Meta:
        verbose_name = "Kitchen Department Lunch Shift(Quantity)"
        verbose_name_plural = "Kitchen Department Lunch Shift(Quantity)"

class KitchenLate(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)
    balls_amount = models.IntegerField()
    pizza_grade = models.IntegerField()
    tomorrow_balls_total = models.IntegerField()
    old_balls_total = models.IntegerField()
    balls_broken_today = models.IntegerField()
    pizzas_broken_today = models.IntegerField()

    class Meta:
        verbose_name = "Kitchen Department Late Shift(Quantity)"
        verbose_name_plural = "Kitchen Department Late Shift(Quantity)"


from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100)

class TerminalLunch(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Terminal Department Lunch Shift"
        verbose_name_plural = "Terminal Department Lunch Shift"


class TerminalLate(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Terminal Department Late Shift"
        verbose_name_plural = "Terminal Department Late Shift"

class KitchenSpecialcleaningMonday(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Kitchen Department Specialcleaning(Monday)"
        verbose_name_plural = "Kitchen Department Specialcleaning(Monday)"

class DryStorageCleaning(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Dry Storage Cleaning(Wednesday)"
        verbose_name_plural = "Dry Storage Cleaning(Wednesday)"

class WednesdayCleaning(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Kitchen Special Cleaning(Wednesday)"
        verbose_name_plural = "Kitchen Special Cleaning(Wednesday)"

class ApartmentCleaning(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Apartment Cleaning(Wednesday)"
        verbose_name_plural = "Apartment Cleaning(Wednesday)"

class KitchenLunchTask(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Kitchen Department Lunch Shift(Task)"
        verbose_name_plural = "Kitchen Department Lunch Shift(Task)"

class KitchenLateTask(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Kitchen Department Late Shift(Task)"
        verbose_name_plural = "Kitchen Department Late Shift(Task)"
