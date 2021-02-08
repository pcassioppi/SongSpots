import graphene
from graphene_django import DjangoObjectType

from .models import Song
from users.schema import UserType

class SongType(DjangoObjectType):
    class Meta:
        model = Song

# class SongListType(DjangoObjectType):
#     class Meta:
#         model = SongList

class Query(graphene.ObjectType):
    songs = graphene.List(SongType, search=graphene.String(),
     first=graphene.Int(),
     skip=graphene.Int(),
     )
    # votes = graphene.List(VoteType)

    def resolve_songs(self,info,search=None,first=None, skip=None, **kwargs):
        #retrieving all the links to paginate them
        all_songs = Song.objects.all()

        #if there is a search parameter, run this, else it will just return unfiltered links
        if search:
            filter = (
                Q(title__icontains=search) |
                Q(artist__icontains=search) 
                #should date be added in here??....

            )
            all_songs = all_songs.filter(filter)

        if skip:
            all_songs = all_songs[skip:]

        if first:
            all_songs = all_songs[:first]

        return all_songs
    
    # def resolve_votes(self, info, **kwargs):
    #     return Vote.objects.all()

class CreateSong(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    artist = graphene.String()
    latitude = graphene.String()
    longitude = graphene.String()
    date = graphene.Date()
    tagged_by = graphene.Field(UserType)

   
    class Arguments:
        title = graphene.String()
        artist = graphene.String()
        latitude = graphene.String()
        longitude = graphene.String()
        date = graphene.Date()

    
    def mutate(self, info, title, artist, latitude, longitude, date):
        user = info.context.user or None

        song = Song(title = title, artist=artist, latitude=latitude, longitude=longitude, date=date, tagged_by=user)
        song.save()

        return CreateSong(
            id=song.id,
            title=song.title,
            artist=song.artist,
            latitude=song.latitude,
            longitude=song.longitude,
            date=song.date,
            tagged_by=song.tagged_by,
        )


class Mutation(graphene.ObjectType):
    create_song = CreateSong.Field()