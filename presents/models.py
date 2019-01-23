from django.db import models
from wagtail.core.models import Page
from django.db.models import TextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from django.conf import settings
from django.dispatch import receiver
import os

class GiftPage(Page):
    short_description = TextField(blank=False, help_text='Gift summary')
    full_description = TextField(blank=False, help_text='Complete gift information')
    icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    icon_url = TextField(blank=True)

    content_panels = [
        MultiFieldPanel(Page.content_panels + [
            FieldPanel('short_description'),
            FieldPanel('full_description'),
            ImageChooserPanel('icon')
        ])
    ]
@receiver(models.signals.post_save, sender=GiftPage)
def post_save(sender, instance, **kwargs):
    icon_name = instance.icon.filename
    new_icon_name = ''.join([os.path.splitext(icon_name)[0], '.original', os.path.splitext(icon_name)[1]])
    instance.icon_url = ''.join([settings.BASE_URL, settings.MEDIA_URL, 'images/', new_icon_name])

class GiftsPage(Page):
    content_panels = [MultiFieldPanel(Page.content_panels)]
