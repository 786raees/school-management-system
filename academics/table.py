import django_tables2 as table
from django.utils.html import format_html
from django.urls import reverse
from .models import Section,Classes

class SectionActionColumn(table.Column):
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
    actions = SectionActionColumn(empty_values=())
    class Meta:
        model = Section
        template_name = "django_tables2/bootstrap-responsive.html"

        exclude = (
            "id",
            "school",
        )

class ClassActionColumn(table.Column):
    def render(self, record):
        delete_class_url = reverse('academics:delete_class', kwargs={'pk': record.id})
        update_class_url = reverse('academics:update_class', kwargs={'pk': record.id})
        return format_html(
            f"""<a role='button' class='btn btn-sm btn-danger' href='{delete_class_url}' hx-boost='true' hx-confirm='Are you sure you want to delete {record.classes} class'>
                    <i class="fas fa-trash p-0"></i>
                </a>
                <a role='button' class='btn btn-sm btn-warning' href='{update_class_url}' hx-boost='true'>
                    <i class="fas fa-edit p-0"></i>
                </a>
                """)


class ClassTable(table.Table):
    actions = ClassActionColumn(empty_values=())
    class Meta:
        model = Classes
        template_name = "django_tables2/bootstrap-responsive.html"

        exclude = (
            "id",
            "school",
        )
