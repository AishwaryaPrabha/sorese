from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    herobanner_heading=models.CharField(max_length=100, blank=True)
    herobanner_description=RichTextField(
    	blank=True, 
    	verbose_name='Bottom Description')

    herobanner_button=models.URLField(max_length=100, db_index=True, unique=True, blank=True)