import django_tables2 as table
from .models import SchoolInfo


class SchoolInfoTable(table.Table):
    class Meta:
        model = SchoolInfo
        template_name = "django_tables2/bootstrap.html"

        exclude = (
            "school_short_name",
            "school_code",
            "session",
            "address",
            "user",
        )
