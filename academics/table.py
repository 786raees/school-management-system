import django_tables2 as table
from django.utils.html import format_html
from django.urls import reverse
from .models import Section

class ActionColumn(table.Column):
    def render(self, record):
        delete_section_url = reverse('academics:delete_section', kwargs={'pk': record.id})
        update_section_url = reverse('academics:update_section', kwargs={'pk': record.id})
        return format_html(
            f"""<a role='button' class='btn btn-sm btn-danger' href='{delete_section_url}' hx-boost='true' hx-confirm='Are you sure you want to delete {record.name} section'>
                    <i class="fas fa-trash p-0"></i>
                </a>
                <a role='button' class='btn btn-sm btn-warning' href='{update_section_url}' hx-boost='true'>
                    <i class="fas fa-edit p-0"></i>
                </a>
                """)


class SectionTable(table.Table):
    actions = ActionColumn(empty_values=())
    class Meta:
        model = Section
        template_name = "django_tables2/bootstrap-responsive.html"

        exclude = (
            "school",
        )
