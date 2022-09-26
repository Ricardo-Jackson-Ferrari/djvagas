from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Application, Job, Salary, Schooling

admin.site.register(Salary)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'status']
    list_filter = ('status',)
    search_fields = ['title', 'company__email']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Schooling)
class SchoolingAdmin(admin.ModelAdmin):
    list_display = ['schooling', 'level']
    list_filter = ('schooling', 'level')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['get_job_title', 'candidate', 'status']
    list_filter = ('job__title', 'status')

    @admin.display(description=_('job'))
    def get_job_title(self, obj):
        return obj.job.title
