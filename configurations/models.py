from django.db import models
from django.utils.translation import gettext_lazy as _


class SchoolInfo(models.Model):

    management_name = models.CharField(max_length=200, default='Management Name')
    school_name = models.CharField(max_length=200, default='Your School Name')
    school_short_name = models.CharField(max_length=200, default='R.G.S')
    school_code = models.CharField(max_length=200, default='Your School Code')
    address = models.CharField(max_length=200, default='Your School Address')
    phone = models.CharField(max_length=200, default='Your School Phone')
    email = models.EmailField(max_length=200, default='yourschoolemail@domain.com')
    # Session
    Session_Choices = [(f'20{year}-{year+1}',f'20{year}-{year+1}') for year in range(10,31) ]
    session = models.CharField(_("Session "), max_length=10, choices=Session_Choices, null=True)
    user = models.ForeignKey('users.SuperAdmin', verbose_name=_("User"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("school info")
        verbose_name_plural = _("school info")

    def __str__(self):
        return f"{self.school_name}"


class SelectedSchool(models.Model):
    user = models.OneToOneField('users.SuperAdmin', verbose_name=_("User"), on_delete=models.CASCADE)
    school = models.OneToOneField('SchoolInfo', verbose_name=_("Selected School"), on_delete=models.CASCADE,
                                  help_text="<p class='ml-2'><small>Select Your Current School That You Want To Work On.</small></p>", null=True)
    def __str__(self):
        return f"{self.user} | {self.school}"

