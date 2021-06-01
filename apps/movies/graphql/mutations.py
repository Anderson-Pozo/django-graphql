import graphene
from .queries import ActorType, MovieType
from ..models import Actor, Movie


class ActorInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    nationality = graphene.String()
    age = graphene.String()


class MovieInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    synopsis = graphene.String()
    actor = graphene.Field(ActorInput)
    published_date = graphene.Date()


class CreateActor(graphene.Mutation):
    class Arguments:
        input = ActorInput(required=True)

    actor = graphene.Field(ActorType)

    @staticmethod
    def mutate(root, info, input=None):
        actor_instance = Actor(
            name=input.name,
            nationality=input.nationality,
            age=input.age
        )
        actor_instance.save()
        return CreateActor(actor=actor_instance)


class UpdateActor(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = ActorInput(required=True)

    actor = graphene.Field(ActorType)

    @staticmethod
    def mutate(root, info, id, input=None):
        actor_instance = Actor.objects.get(pk=id)
        if actor_instance:
            actor_instance.name = input.name
            actor_instance.nationality = input.nationality
            actor_instance.age = input.age
            actor_instance.save()
            return UpdateActor(actor=actor_instance)
        return UpdateActor(actor=None)


class DeleteActor(graphene.Mutation):
    response = graphene.String()

    class Arguments:
        id = graphene.Int(required=True)

    @staticmethod
    def mutate(root, info, id):
        actor_instance = Actor.objects.get(pk=id)
        if actor_instance:
            actor_instance.delete()
            return DeleteActor(response='Actor deleted')


class CreateMovie(graphene.Mutation):
    class Arguments:
        input = MovieInput(required=True)

    movie = graphene.Field(MovieType)

    @staticmethod
    def mutate(root, info, input=None):
        actor = Actor.objects.get(pk=input.actor.id)
        movie_instance = Movie(
            title=input.title,
            synopsis=input.synopsis,
            actor=actor,
            published_date=input.published_date
        )

        movie_instance.save()
        return CreateMovie(movie=movie_instance)


class UpdateMovie(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = MovieInput(required=True)

    movie = graphene.Field(MovieType)

    @staticmethod
    def mutate(root, info, id, input=None):
        movie_instance = Movie.objects.get(pk=id)
        actor = Actor.objects.get(pk=input.actor.id)
        if movie_instance:
            movie_instance.title = input.title
            movie_instance.synopsis = input.synopsis
            movie_instance.published_date = input.published_date
            movie_instance.actor = actor
            movie_instance.save()
            return UpdateMovie(movie=movie_instance)
        return UpdateMovie(movie=None)


class DeleteMovie(graphene.Mutation):
    response = graphene.String()

    class Arguments:
        id = graphene.Int(required=True)

    @staticmethod
    def mutate(root, info, id):
        movie_instance = Movie.objects.get(pk=id)
        if movie_instance:
            movie_instance.delete()
            return DeleteMovie(response='Movie deleted')


class Mutation(graphene.ObjectType):
    create_actor = CreateActor.Field()
    update_actor = UpdateActor.Field()
    delete_actor = DeleteActor.Field()
    create_movie = CreateMovie.Field()
    update_movie = UpdateMovie.Field()
    delete_movie = DeleteMovie.Field()
