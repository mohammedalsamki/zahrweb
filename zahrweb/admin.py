from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    InKindDonation,
    CashDonation,
    News,
    Volunteer,
    Events,
    poster,
    NumberOfAchivment,
    ExistingProjects,
    About,
)

# Register your models here.

# Register the Admin classes for Book using the decorator


class NewsAdmin(admin.ModelAdmin):
    list_display = ("Title", "Image", "Details")
    list_filter = ["date"]


# Register the Admin classes for Boo,kInstance using the decorator


class ExistingProjectsAdmin(admin.ModelAdmin):
    list_display = ("Image", "Name", "Details", "start_date")
    list_filter = ["start_date"]
    fields = ("Name", "start_date", "Details", "Image")


class VolunteersAdmin(admin.ModelAdmin):
    list_display = ("field_of_volunteers", "RegisterDate")
    fields = ("field_of_volunteers", "RegisterDate")


class InKindDonationAdmin(admin.ModelAdmin):
    pass


class CashDonationAdmin(admin.ModelAdmin):
    pass


class EventsAdmin(admin.ModelAdmin):
    pass


class posterAdmin(admin.ModelAdmin):
    pass


class AboutAdmin(admin.ModelAdmin):
    pass


class NumberOfAchivmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Volunteer, VolunteersAdmin)
admin.site.register(ExistingProjects, ExistingProjectsAdmin)
admin.site.register(InKindDonation, InKindDonationAdmin)
admin.site.register(CashDonation, CashDonationAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(poster, posterAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(NumberOfAchivment, NumberOfAchivmentAdmin)
