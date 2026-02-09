from django.contrib import admin
from .models import dailyadd,Monthlyadd
class dailyaddadmin(admin.ModelAdmin):
    data=('grocery','onlinepayment','datetime','total')
admin.site.register(dailyadd,dailyaddadmin)

class monthlyaddadmin(admin.ModelAdmin):
    data2=('income','fixed_expenses','varaiable_expenses','saving','sessional','month')
admin.site.register(Monthlyadd,monthlyaddadmin)

# Register your models here.
