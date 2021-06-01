import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from django.db.models import Q
from ..models import Actor, Movie


# Definir automáticamente los campos GraphQL que corresponden
# a los campos en los modelos Django.
class ActorType(DjangoObjectType):
    class Meta:
        model = Actor


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie


class Query(ObjectType):
    actor = graphene.Field(ActorType, id=graphene.Int())
    movie = graphene.Field(MovieType, id=graphene.Int())
    actors = graphene.List(ActorType)
    movies = graphene.List(MovieType)
    actor_search = graphene.List(ActorType, string=graphene.String())
    movie_search = graphene.List(MovieType, string=graphene.String())

    def resolve_actor(self, info, id, **kwargs):
        if id is not None:
            return Actor.objects.get(pk=id)

        return None

    def resolve_movie(self, info, id,  **kwargs):
        if id is not None:
            return Movie.objects.get(pk=id)

        return None

    def resolve_actors(self, info, **kwargs):
        return Actor.objects.all()

    def resolve_movies(self, info, **kwargs):
        return Movie.objects.all()

    def resolve_actor_search(self, info, string,  **kwargs):
        return Actor.objects.filter(name__icontains=string)

    def resolve_movie_search(self, info, string, **kwargs):
        return Movie.objects.filter(
            Q(title__icontains=string) | Q(actor__name__icontains=string) |
            Q(synopsis__icontains=string)
        )[0:5]
