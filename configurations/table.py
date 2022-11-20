import django_tables2 as table
from django.utils.html import format_html
from django.urls import reverse
from .models import SchoolInfo

class ActionColumn(table.Column):
    def render(self, record):
        url = reverse('confurations:delete_school_view', kwargs={'id': record.id})
        return format_html(
            f"""<a role='button' class='btn btn-danger' href='{url}' hx-boost='true' hx-confirm='Are you sure you want to delete {record.school_name}'>
                    <i class="fas fa-trash p-0"></i>
                </a>""")


class SchoolInfoTable(table.Table):
    actions = ActionColumn(empty_values=())
    class Meta:
        model = SchoolInfo
        template_name = "django_tables2/bootstrap-responsive.html"

        exclude = (
            "school_short_name",
            "school_code",
            "session",
            "address",
            "user",
        )
