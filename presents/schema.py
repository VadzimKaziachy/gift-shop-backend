import graphene
from graphene_django.types import DjangoObjectType
from presents.models import GiftPage


class GiftType(DjangoObjectType):
    class Meta:
        model = GiftPage


class Query(object):
    all_gifts = graphene.List(GiftType)
    gift = graphene.Field(GiftType, id=graphene.Int())

    def resolve_all_gifts(self, info, **kwargs):
        return GiftPage.objects.all()

    def resolve_gift(self, info, **kwargs):
        id = kwargs.get('id')
        gift = None
        if id is not None and GiftPage.objects.filter(id=id).exists():
            gift = GiftPage.objects.get(id=id)
        return gift
