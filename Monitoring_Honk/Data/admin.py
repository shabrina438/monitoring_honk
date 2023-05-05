from django.contrib import admin


# Register your models here.
#from django.contrib import admin
from .models import Horn, Gyro, Location, SensorData, VehicleData

admin.site.register(Horn)
#admin.site.register(Gyro)
#admin.site.register(Location)
#admin.site.register(SensorData)

'''''
class HornAdmin(admin.ModelAdmin):
    #date_hierarchy = 'created_date'
    list_display = ('horn_status')
admin.site.register(Horn, HornAdmin)'''



class GyroAdmin(admin.ModelAdmin):
    #date_hierarchy = 'created_date'
    list_display = ('x', 'y', 'z')
admin.site.register(Gyro, GyroAdmin) 

class LocationAdmin(admin.ModelAdmin):
    #date_hierarchy = 'created_date'
    list_display = ('latitude','longitude')
admin.site.register(Location, LocationAdmin)

class SensorDataAdmin(admin.ModelAdmin):
    #date_hierarchy = 'created_date'
    list_display = ('ru_id','horn','gyro','date','timestamp','location')
admin.site.register(SensorData, SensorDataAdmin) 




class VehicleDataAdmin(admin.ModelAdmin):
    #date_hierarchy = 'created_date'
    list_display = ('time','horn','gyro','gps')
admin.site.register(VehicleData, VehicleDataAdmin) 