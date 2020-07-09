from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from app.models import *
import django_filters
import graphql_jwt
import graphene
from graphene import relay
from graphql_relay.node.node import from_global_id

class PackageNode(DjangoObjectType):
    class Meta:
        model = Package
        filter_fields = ()
        interfaces = (relay.Node,)




class Query(graphene.AbstractType):
    packages = DjangoFilterConnectionField(PackageNode)