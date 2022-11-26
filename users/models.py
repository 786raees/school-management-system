from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.dispatch import receiver
from django.core.files import File
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

from io import BytesIO
import barcode
from barcode.writer import ImageWriter

from configurations.models import SchoolInfo


def get_upload_to(instance, filename):
    return f"upload/{instance.username}/{filename}"


def get_barcode_upload_to(instance, filename):
    return f"barcodes/{instance.school}/{instance.username}-{filename}"


class AllUser(AbstractUser):
    registration_no = models.PositiveIntegerField(
        _("registration no"), null=True, blank=True
    )
    roll_no = models.PositiveIntegerField(_("roll no"), null=True, blank=True)
    class_name = models.ForeignKey(
        "academics.Classes",
        verbose_name=_("class name"),
        on_delete=models.PROTECT,
        null=True,
    )
    section = models.ForeignKey(
        "academics.Section",
        verbose_name=_("section"),
        on_delete=models.PROTECT,
        null=True,
    )
    first_name = models.CharField(_("first name"), max_length=150, null=True)
    religion = models.CharField(_("religion"), max_length=150, null=True, blank=True)
    caste = models.CharField(_("caste"), max_length=150, null=True, blank=True)
    school = models.ForeignKey(
        "configurations.SchoolInfo",
        verbose_name=_("school name"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class UserType(models.TextChoices):
        student = "student", "student"
        parent = "parent", "parent"
        teacher = "teacher", "teacher"
        admin = "admin", "admin"
        super_admin = "super admin", "super admin"

    user_type = models.CharField(
        max_length=11, choices=UserType.choices, default=UserType.super_admin
    )

    class GENDER(models.TextChoices):
        male = "male", "male"
        female = "female", "female"

    gender = models.CharField(max_length=6, choices=GENDER.choices, default=GENDER.male)
    date_of_birth = models.DateField(
        _("Date Of Birth"), auto_now=False, auto_now_add=False, null=True, default=now
    )
    father_name = models.CharField(
        _("father name"), max_length=150, null=True, blank=True
    )
    phone = models.CharField(_("phone"), max_length=150, null=True, blank=True)
    emergency_contact_number = models.CharField(
        _("Emergency Contact"), max_length=150, null=True, blank=True
    )
    mother_name = models.CharField(
        _("mother name"), max_length=150, null=True, blank=True
    )
    designation = models.ForeignKey(
        "academics.Designation",
        verbose_name=_("designation"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    department = models.ForeignKey(
        "academics.Department",
        verbose_name=_("department"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    date_of_joining = models.DateField(
        _("Date Of Joining"),
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True,
        default=now,
    )

    class MaritalStatus(models.TextChoices):
        Single = "Single", "Single"
        Married = "Married", "Married"
        Widowed = "Widowed", "Widowed"
        Separated = "Separated", "Separated"
        Not_Specified = "Not Specified", "Not Specified"

    marital_status = models.CharField(
        max_length=13,
        choices=MaritalStatus.choices,
        default=MaritalStatus.Not_Specified,
    )
    photo = models.ImageField(
        _("user dp"), upload_to="user_photo", default="user_default_pic.jpg"
    )
    current_address = models.TextField(_("current address"), null=True, blank=True)
    permanent_address = models.TextField(_("permanent address"), null=True, blank=True)
    qualification = models.TextField(_("qualification"), null=True, blank=True)
    work_experience = models.TextField(_("work experience"), null=True, blank=True)
    note = models.TextField(_("note"), null=True, blank=True)
    # Payroll
    epf_no = models.CharField(_("EPF No"), max_length=500, null=True, blank=True)

    class ContractType(models.TextChoices):
        Permanent = "Permanent", "Permanent"
        Probation = "Probation", "Probation"

    contract_type = models.CharField(
        max_length=9, choices=ContractType.choices, null=True, blank=True
    )
    basic_salary = models.PositiveIntegerField(_("Basic Salary"), blank=True, null=True)
    work_shift = models.CharField(
        _("Work Shift"), max_length=100, blank=True, null=True
    )
    location = models.CharField(_("Location"), max_length=100, blank=True, null=True)
    date_of_leaving = models.CharField(
        _("Date Of Leaving"), max_length=100, blank=True, null=True
    )
    # Bank Account Details
    account_title = models.CharField(
        _("Account Title"), max_length=100, blank=True, null=True
    )
    bank_account_number = models.CharField(
        _("Bank Account Number"), max_length=100, blank=True, null=True
    )
    bank_name = models.CharField(_("Bank Name"), max_length=100, blank=True, null=True)
    ifsc_code = models.CharField(_("IFSC Code"), max_length=100, blank=True, null=True)
    bank_branch_name = models.CharField(
        _("Bank Branch Name"), max_length=100, blank=True, null=True
    )
    # Social Media Link
    facebook_url = models.URLField(
        _("Facebook URL"), max_length=300, blank=True, null=True
    )
    twitter_url = models.URLField(
        _("Twitter URL"), max_length=300, blank=True, null=True
    )
    linkedin_url = models.URLField(
        _("Linkedin URL"), max_length=300, blank=True, null=True
    )
    instagram_url = models.URLField(
        _("Instagram URL"), max_length=300, blank=True, null=True
    )
    # Upload Documents
    resume = models.FileField(
        _("Resume"), upload_to=get_upload_to, blank=True, null=True
    )
    joining_letter = models.FileField(
        _("Joining Letter"), upload_to=get_upload_to, blank=True, null=True
    )
    resignation_letter = models.FileField(
        _("Resignation Letter"), upload_to=get_upload_to, blank=True, null=True
    )
    other_documents = models.FileField(
        _("Other Documents"), upload_to=get_upload_to, blank=True, null=True
    )
    barcode = models.ImageField(
        _("barcode"), upload_to=get_barcode_upload_to, blank=True, null=True
    )

    class Meta:
        verbose_name = _("All User")
        verbose_name_plural = _("All Users")
        unique_together = (
            ("school", "registration_no"),
            ("section", "roll_no", "school"),
        )


class StudentManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(user_type=AllUser.UserType.student)
        )


class Student(AllUser):
    objects = StudentManager()

    class Meta:
        proxy = True
        verbose_name = _("student")
        verbose_name_plural = _("students")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = AllUser.UserType.student
        return super().save(*args, **kwargs)


class ParentManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(user_type=AllUser.UserType.parent)
        )


class Parent(AllUser):
    objects = ParentManager()

    class Meta:
        proxy = True
        verbose_name = _("Parent")
        verbose_name_plural = _("Parents")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = AllUser.UserType.parent
        return super().save(*args, **kwargs)


class TeacherManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(user_type=AllUser.UserType.teacher)
        )


class Teacher(AllUser):
    objects = TeacherManager()

    class Meta:
        proxy = True
        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = AllUser.UserType.teacher
        return super().save(*args, **kwargs)


class AdminManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(user_type=AllUser.UserType.admin)
        )


class Admin(AllUser):
    objects = AdminManager()

    class Meta:
        proxy = True
        verbose_name = _("Admin")
        verbose_name_plural = _("Admins")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = AllUser.UserType.admin
        return super().save(*args, **kwargs)


class SuperAdminManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(user_type=AllUser.UserType.super_admin)
        )


class SuperAdmin(AllUser):
    objects = SuperAdminManager()

    class Meta:
        proxy = True
        verbose_name = _("Super Admin")
        verbose_name_plural = _("Super Admins")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = AllUser.UserType.super_admin
        return super().save(*args, **kwargs)


@receiver(post_save, sender=SuperAdmin)
def save_schoolinfo(sender, created, instance, **kwargs):
    if created:
        school = SchoolInfo(user=instance, management_name=instance.get_full_name())
        school.save()
        instance.school = school
        instance.save()


@receiver(pre_save, sender=Student)
@receiver(pre_save, sender=Teacher)
@receiver(pre_save, sender=Admin)
@receiver(pre_save, sender=SuperAdmin)
@receiver(pre_save, sender=AllUser)
def student_reg_no_increase_pre_save_receiver(sender, instance: AllUser, **kwargs):

    if not instance.registration_no:
        try:
            if last := instance.school.alluser_set.latest("registration_no"):  # type: ignore
                instance.registration_no = last.registration_no + 1

            else:
                instance.registration_no = 100
        except Exception:
            instance.registration_no = 100
    COD128 = barcode.get_barcode_class("code128")
    rv = BytesIO()
    barcode_num = "0"
    for _ in range(12 - len(str(instance.registration_no))):
        barcode_num += "0"

    barcode_num = barcode_num + str(instance.registration_no)
    code = COD128(f"{barcode_num}", writer=ImageWriter()).write(rv)
    instance.barcode.save(f"{instance.first_name}.png", File(rv), save=False)
