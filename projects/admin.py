from django.contrib import admin

from django.db import models
from .models import Our_Project
from mdeditor.widgets import MDEditorWidget

class ExampleModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }

# Register your models here.
admin.site.register(Our_Project)