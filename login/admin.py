from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import User



from login.models import Profile


class ProfileInline(admin.TabularInline):
    model = Profile


class UserAdmin(DjangoUserAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
