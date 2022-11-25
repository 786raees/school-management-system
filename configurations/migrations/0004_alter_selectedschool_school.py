# Generated by Django 4.1.3 on 2022-11-20 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("configurations", "0003_alter_schoolinfo_options_alter_selectedschool_school"),
    ]

    operations = [
        migrations.AlterField(
            model_name="selectedschool",
            name="school",
            field=models.OneToOneField(
                help_text="<p class='ml-2'><small>Select Your Current School That You Want To Work On.</small></p>",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="configurations.schoolinfo",
                verbose_name="Selected School",
            ),
        ),
    ]