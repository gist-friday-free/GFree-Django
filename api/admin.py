from django.contrib import admin

from api.models import Class, User, Notice, PlayStoreInfo, Edit


class UserInline(admin.StackedInline):
    model = User.classes.through

class ClassAdmin(admin.ModelAdmin):
    inlines = [UserInline]

admin.site.register(Class,ClassAdmin)
admin.site.register(User)
admin.site.register(Notice)
admin.site.register(PlayStoreInfo)
admin.site.register(Edit)