from django.contrib import admin

# Register your models here.
# from django.contrib import admin
# from .models import KitchenLunch, KitchenLate, TerminalLunch, TerminalLate
#
# admin.site.register(KitchenLunch)
# admin.site.register(KitchenLate)
# admin.site.register(TerminalLunch)
# admin.site.register(TerminalLate)
from django.contrib import admin
from .models import KitchenLunch, KitchenLate, TerminalLunch, TerminalLate, KitchenSpecialcleaningMonday, \
    DryStorageCleaning, WednesdayCleaning, ApartmentCleaning, KitchenLunchTask, KitchenLateTask


@admin.register(KitchenLunch)
class KitchenLunchAdmin(admin.ModelAdmin):
    list_display = ('date', 'location','name', 'balls_amount', 'today_balls_total', 'yesterday_balls_total')
from django.contrib import admin
from .models import KitchenLunch

@admin.register(KitchenLate)
class KitchenLateAdmin(admin.ModelAdmin):
    list_display = ('date', 'location','name', 'balls_amount', 'pizza_grade','tomorrow_balls_total','old_balls_total','balls_broken_today','pizzas_broken_today')
@admin.register(TerminalLunch)
class TerminalLunchAdmin(admin.ModelAdmin):
    list_display = ('date','location','name')
@admin.register(TerminalLate)
class TerminalLateAdmin(admin.ModelAdmin):
    list_display = ('date','location','name')
@admin.register(KitchenSpecialcleaningMonday)
class KitchenSpecialCleaningMondayAdmin(admin.ModelAdmin):
    list_display = ('date','location','name')
@admin.register(DryStorageCleaning)
class DryStorageCleaningAdmin(admin.ModelAdmin):
    list_display = ('date','location','name')

@admin.register(WednesdayCleaning)
class DryStorageCleaningAdmin(admin.ModelAdmin):
    list_display = ('date','location','name')

@admin.register(ApartmentCleaning)
class ApartmentCleaningAdmin(admin.ModelAdmin):
    list_display = ('date','location','name')
@admin.register(KitchenLunchTask)
class KitchenLunchTaskAdmin(admin.ModelAdmin):
    list_display = ('date','location','name')
@admin.register(KitchenLateTask)
class KitchenLateTaskAdmin(admin.ModelAdmin):
    list_display = ('date','location','name')