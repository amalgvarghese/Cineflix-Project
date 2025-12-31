from django.shortcuts import render,redirect

from django.views import View

from . forms import MovieForm

from . models import Movie,IndustryChoices,GenreChoices,ArtistChoices,LanguageChoices,CertificationChoices

from django.db.models import Q

from django.utils.decorators import method_decorator

from authentication.permissions import permitted_user_roles

# from cineflix.utils import get_recommended_movies

from subscriptions.models import UserSubscriptions

from django.contrib import messages

# Create your views here.

class HomeView(View):

    template = 'home.html'

    def get(self,request,*args,**kwargs):

        data = {'page':'Home'}

        return render(request,self.template,context=data)
    
class MoviesListView(View):

    templates = 'movies/movie-list.html'

    def get(self,request,*args,**kwargs):

        query = request.GET.get('query')

        movies = Movie.objects.filter(active_status = True )

        if query :

            movies = movies.filter(Q(name__icontains=query)|
                                   Q(description__contains = query)|
                                   Q(industry_name_contains = query)|
                                   Q(genre_name_contains = query)|
                                   Q(artists_name_contains = query)| 
                                   Q(Languages_name_contains = query)
                                    ).distinct()

                                   


        data = {'page':'movies','movies':movies,'query':query}

        return render(request,self.templates,context=data)
    
#     ---------------------------------------------------------normal way--------------------------------------------------------------
    
# class MovieCreateView(View):

#     def get(self,request,args,*kwargs):

#         industry_choices = IndustryChoices

#         genreChoices = GenreChoices

#         artistchoices = ArtistChoices

#         languageChoices = LanguageChoices

#         certificationChoices = CertificationChoices



#         data = {'page':'Create Movie',
#                 'industry_choices':IndustryChoices,
#                 'genre_choices':GenreChoices,
#                 'artist_choices':ArtistChoices,
#                 'language_choices':languageChoices,
#                 'certification_choices':CertificationChoices}

#         return render(request,'movies/movie-create.html',context=data)
    
#     def post(self,request,args,*kwargs):

#         Movie_Data = request.POST

#         name = Movie_Data.get('name')

#         photo = request.FILES.get('photo')

#         description = Movie_Data.get('description')

#         release_date = Movie_Data.get('release_date')

#         runtime = Movie_Data.get('runtime')

#         certification = Movie_Data.get('certification')

#         industry = Movie_Data.get('industry')

#         languages = Movie_Data.get('languages')

#         genre = Movie_Data.get('genre')
        
#         artists = Movie_Data.get('artists')
        
#         video = Movie_Data.get('video')

#         tags = Movie_Data.get('tags')

#         Movie.objects.create(name=name,
#                              description=description,
#                              release_year= release_date,
#                              industry=industry,
#                              runtime=runtime,
#                              certification=certification,
#                              genre=genre,
#                              artists=artists,
#                              photo=photo,
#                              video=video,
#                              tags=tags,
#                              Languages=languages)

#         return redirect('movie-list')
    

    





# ==============================================================FORM WAY===================================================================================

@method_decorator(permitted_user_roles(['Admin']),name='dispatch')
class MovieCreateView(View):

    form_class =MovieForm

    template = 'movies/movie-create.html'

    def get(self,request,*args,**kwargs):

        form = self.form_class()

        data = {'page':'Create Movie',
                'form' : form,'page':'Create Movie'}

        return render(request,self.template,context=data)
    
    def post(self,request,*args,**kwargs):

        form =  self.form_class(request.POST,request.FILES)

        if form.is_valid():

            form.save()

            messages.success(request,'movie created succesfully')

            return redirect('movie-list')
        
        data = {'form':form}

        messages.error(request,'movie creation failed')


        return render(request,self.template,context=data)
    
class MovieDetailsView(View):

    template = 'movies/movie-details.html'

    def get(self,request,*args,**kwargs):

        uuid =  kwargs.get('uuid')

        movie = Movie.objects.get(uuid=uuid)

        # recommended_movies = get_recommended_movies(movie)

        data = {'movie':movie,'page':movie.name}
        
        return render(request,self.template,context=data)



@method_decorator(permitted_user_roles(['Admin']),name='dispatch')   
class MovieEditView(View):

    form_class = MovieForm

    template = 'movies/movie-edit.html'

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        movie = Movie.objects.get(uuid=uuid)

        form = self.form_class(instance=movie)

        data = {'form':form,'page':movie.name}

        return render(request,self.template,context=data)

    def post(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        movie = Movie.objects.get(uuid=uuid)

        form = self.form_class(request.POST,request.FILES,instance=movie)

        if form.is_valid():

            form.save()

            return redirect('movie-details',uuid=uuid)
        
        data = {'form':form,'page':movie.name}

        return render(request,self.template,context=data)


@method_decorator(permitted_user_roles(['Admin']),name='dispatch')   
class MovieDeleteView(View):

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        movie = Movie.objects.get(uuid=uuid)

        # movie.delete()

        movie.active_status = False

        movie.save()

        messages.success(request,'movie deleted succesfully')

        return redirect('movie-list')
    


@method_decorator(permitted_user_roles(['User']),name='dispatch') 

class PlayMovie(View):

    template = 'movies/movie-play.html'

    def get(self,request,*args,**kwargs):

        user = request.user

        plan = None

        try :
            
            plan = UserSubscriptions.objects.filter(profile=user,active=True).latest('created_at')
        
        except :

            pass

        if plan:

            uuid = kwargs.get('uuid')

            movie = Movie.objects.get(uuid=uuid)

            data = {'movie':movie,'page':movie.name}

            return render(request,self.template,context=data)
        
        else:

            messages.error(request,'you must subscribe a plan before watching')

            return redirect('subscription-list')

