import graphene

from graphene_django.types import DjangoObjectType

from social_network.facebook.models import FacebookUser, Videos, Photos


class FacebookUserType(DjangoObjectType):
    class Meta:
        model = FacebookUser


class VideosType(DjangoObjectType):
    class Meta:
        model = Videos


class PhotosType(DjangoObjectType):
    class Meta:
        model = Photos


class Query(object):
    all_users = graphene.List(FacebookUserType)
    all_photos = graphene.List(PhotosType)
    all_videos = graphene.List(VideosType)

    def resolve_all_users(self, info, **kwargs):
        return FacebookUser.objects.all()

    def resolve_all_photos(self, info, **kwargs):
        return Photos.objects.all()

    def resolve_all_videos(self, info, **kwargs):
        return Videos.objects.all()


class CreateFacebookUser(graphene.Mutation):
    name = graphene.String()
    age = graphene.Int()
    email = graphene.String()

    # 2
    class Arguments:
        name = graphene.String()
        age = graphene.Int()
        email = graphene.String()
        friends = graphene.List(graphene.Int)

    # 3
    def mutate(self, info, name, age, email, friends):
        user = FacebookUser(name=name, email=email, age=age)
        user.save()
        user.friends.set(friends)

        return CreateFacebookUser(
            name=user.name, email=user.email, age=user.age
        )


class Mutation(graphene.ObjectType):
    create_user = CreateFacebookUser.Field()
