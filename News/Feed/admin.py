from django.contrib import admin
from .models import Campuslogin, Newslogin, Register, Adminnewsmodel, Admincampusmodel, Newscomement, Campuscomement

admin.site.register(Campuslogin)
admin.site.register(Newslogin)
admin.site.register(Register)
admin.site.register(Adminnewsmodel)
admin.site.register(Admincampusmodel)
admin.site.register(Newscomement)
admin.site.register(Campuscomement)