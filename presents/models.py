from django.db import models
from wagtail.core.models import Page
from django.db.models import TextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel


class GiftPage(Page):
    short_description = TextField(blank=False, help_text='Gift summary')
    full_description = TextField(blank=False, help_text='Complete gift information')
    icon_front = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    icon_back = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = [
        MultiFieldPanel(Page.content_panels + [
            FieldPanel('short_description'),
            FieldPanel('full_description'),
            ImageChooserPanel('icon_front'),
            ImageChooserPanel('icon_back')
        ])
    ]

class GiftsPage(Page):
    content_panels = [MultiFieldPanel(Page.content_panels)]
