from django.contrib import admin

from hi.models import Visitors


@admin.register(Visitors)
class VisitorsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "time_registration",
    )
    list_display_links = ("last_name",)
    search_fields = (
        "last_name",
        "first_name",
        "time_registration",
    )
    list_filter = ("time_registration",)
    save_on_top = True


admin.site.site_title = "Админ-панель сайта регистрации поситителей"
admin.site.site_header = "Список зарегистрировавшихся"
