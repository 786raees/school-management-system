from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Section(models.Model):

    name = models.CharField(_("Section name"), max_length=50)
    school = models.ForeignKey("configurations.SchoolInfo", verbose_name=_("school name"), on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = _("section")
        verbose_name_plural = _("sections")

    def __str__(self):
        return self.name

    def get_delete_url(self):
        return reverse('academics:delete_section', kwargs={'pk': self.pk})

    def get_change_url(self):
        return reverse('academics:change_section', kwargs={'pk': self.pk})



class Classes(models.Model):

    classes = models.CharField(_("Class Name"), max_length=50)
    section = models.ManyToManyField("academics.Section", verbose_name=_("Section"))
    school = models.ForeignKey("configurations.SchoolInfo", verbose_name=_("school name"), on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = _("Class")
        verbose_name_plural = _("Classes")

    def __str__(self):
        return f"{self.classes}"

    def get_delete_url(self):
        return reverse('academics:delete_class', kwargs={'pk': self.pk})

    def get_change_url(self):
        return reverse('academics:change_class', kwargs={'pk': self.pk})




class Subject(models.Model):
    class SubjectType(models.TextChoices):
        Theory = 'Theory','Theory'
        Practical = 'Practical','Practical'
    subject_name = models.CharField(_("subject Name"), max_length=50)
    subject_type = models.CharField(_("subject Type"), max_length=9, choices=SubjectType.choices,default=SubjectType.Theory)
    subject_code = models.CharField(_("subject Code"), max_length=50, blank=True, null=True)
    school = models.ForeignKey("configurations.SchoolInfo", verbose_name=_("school name"), on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = _("Subject")
        verbose_name_plural = _("Subjects")
        unique_together = (('subject_name','school'),)


    def __str__(self):
        return f"{self.subject_name}"

    def get_delete_url(self):
        return reverse('academics:delete_subject', kwargs={'pk': self.pk})

    def get_change_url(self):
        return reverse('academics:change_subject', kwargs={'pk': self.pk})




class SubjectGroup(models.Model):
    name = models.CharField(_("name"), max_length=50)
    class_name = models.ForeignKey("academics.Classes", verbose_name=_("class"), on_delete=models.CASCADE)
    section = models.ManyToManyField(Section,)
    subject = models.ManyToManyField("academics.Subject", verbose_name=_("subject"))
    description = models.TextField(_("description"), null=True, blank=True)
    school = models.ForeignKey("configurations.SchoolInfo", verbose_name=_("school name"), on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = _("Subject Group")
        verbose_name_plural = _("Subject Groups")


    def __str__(self):
        return f"{self.name}"

    def get_delete_url(self):
        return reverse('academics:delete_subject_group', kwargs={'pk': self.pk})

    def get_change_url(self):
        return reverse('academics:change_subject_group', kwargs={'pk': self.pk})



class Designation(models.Model):
    name = models.CharField(_("name"), max_length=50)
    school = models.ForeignKey("configurations.SchoolInfo", verbose_name=_("school name"), on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = _("Designation")
        verbose_name_plural = _("Designations")


    def __str__(self):
        return f"{self.name}"

    def get_delete_url(self):
        return reverse('academics:delete_designation', kwargs={'pk': self.pk})

    def get_change_url(self):
        return reverse('academics:change_designation', kwargs={'pk': self.pk})



class Department(models.Model):
    name = models.CharField(_("name"), max_length=50)
    school = models.ForeignKey("configurations.SchoolInfo", verbose_name=_("school name"), on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")


    def __str__(self):
        return f"{self.name}"

    def get_delete_url(self):
        return reverse('academics:delete_department', kwargs={'pk': self.pk})

    def get_change_url(self):
        return reverse('academics:change_department', kwargs={'pk': self.pk})



class AssignClassTeacher(models.Model):
    class_name = models.ForeignKey("academics.Classes", verbose_name=_("class"), on_delete=models.CASCADE)
    section = models.ForeignKey("academics.Section", verbose_name=_("section"), on_delete=models.CASCADE)
    teacher = models.ManyToManyField("users.Teacher", verbose_name=_("teachers"))
    school = models.ForeignKey("configurations.SchoolInfo", verbose_name=_("school name"), on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = _("Assign Class Teacher")
        verbose_name_plural = _("Assign Class Teachers")
        unique_together = (('class_name','section','school'),)

    def __str__(self):
        return f"{self.class_name}-{self.section}"

    def get_delete_url(self):
        return reverse('academics:delete_assign_class_teacher', kwargs={'pk': self.pk})

    def get_change_url(self):
        return reverse('academics:change_assign_class_teacher', kwargs={'pk': self.pk})
