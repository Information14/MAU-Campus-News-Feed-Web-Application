from django.shortcuts import render, redirect, get_object_or_404
from .forms import Campusloginform, Newsloginform, RegisterForm, Adminnewsform, Admincampusform, Campuscommentform, Newscommentform
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView 
from .models import Adminnewsmodel, Admincampusmodel, Campuscomement, Newscomement
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse
from django.http import HttpResponseRedirect

class IndexView(ListView):
    template_name = "index.html"
    model = Adminnewsmodel
    context_object_name = 'posts'

    def get_queryset(self):
        return Adminnewsmodel.objects.all().order_by('-created_at')[:3]


class NewsView(FormView, ListView):
    template_name = 'news.html'
    form_class = Newsloginform
    model = Adminnewsmodel
    context_object_name = 'posts'
    

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_at')
        return queryset

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)
            messages.success(self.request, 'Login successful!')
            return JsonResponse({'success': True, 'redirect_url': 'adminnews'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid username or password. Please try again.'})


    def form_invalid(self, form):
        return JsonResponse({'success': False, 'message': 'Form submission failed. Please check your input.'})

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        posts = self.get_queryset()
        paginator = Paginator(posts, 10)
        page = request.GET.get('page')
        paginated_posts = paginator.get_page(page)
        nums = "a" * paginated_posts.paginator.num_pages 
        return render(request, self.template_name, {'form': form, 'posts': posts, 'paginated_posts': paginated_posts, 'nums': nums})


class AdminNewsCreateView(LoginRequiredMixin, CreateView):
    template_name = 'adminnews.html'
    form_class = Adminnewsform
    success_url = reverse_lazy('adminnews')
    login_url = 'news'
    redirect_field_name = 'adminnews'

    def form_valid(self, form):
        title = form.cleaned_data.get('title')
        blog = form.cleaned_data.get('blog')
        person = form.cleaned_data.get('person')
        content = form.cleaned_data.get('content')
        main = form.cleaned_data.get('main')
        author = form.cleaned_data.get('author')
        created_at = form.cleaned_data.get('created_at')

        form.save()

        return super().form_valid(form)
 
def logout_news(request):
    logout(request)
    return redirect('news')


class Newsdetail(DetailView):
    model = Adminnewsmodel 
    template_name = 'detailnews.html'
    form_class = Newscommentform
    success_url = reverse_lazy('detailnews')

    def form_valid(self, form):
        post = get_object_or_404(Adminnewsmodel, pk=self.kwargs.get('pk'))
        form.instance.post = post  
        form.save()
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        post_id = self.kwargs.get('pk')

        posts = get_object_or_404(Adminnewsmodel, pk=post_id)


        news = self.get_object()

        curated = Adminnewsmodel.objects.all().order_by('-created_at')[:3]

        comments = Newscomement.objects.filter(post=news)

        form = self.form_class()

        context = {
            'posts': posts,
            'news': news,
            'curated': curated,
            'comments': comments,
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        news = self.get_object()

        form = self.form_class(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = news
            comment.save()

            return HttpResponseRedirect(reverse('detailnews', kwargs={'pk': news.pk}))
                
        post_id = self.kwargs.get('pk')

        posts = get_object_or_404(Adminnewsmodel, pk=post_id)

        curated = Adminnewsmodel.objects.all().order_by('-created_at')[:3]
        comments = Newscomement.objects.filter(post=news)

        context = {
            'posts': posts,
            'news': news,
            'curated': curated,
            'comments': comments,
            'form': form
        }

        return render(request, self.template_name, context)
    
    


class CampusView(FormView, ListView):
    template_name = 'campus.html'
    form_class = Campusloginform
    model = Admincampusmodel
    context_object_name = 'posts'
    

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_at')
        return queryset

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)
            messages.success(self.request, 'Login successful!')
            return JsonResponse({'success': True, 'redirect_url': 'admincampus'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid username or password. Please try again.'})

    def form_invalid(self, form):
        return JsonResponse({'success': False, 'message': 'Form submission failed. Please check your input.'})

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        posts = self.get_queryset()
        paginator = Paginator(posts, 10)
        page = request.GET.get('page')
        paginated_posts = paginator.get_page(page)
        nums = "a" * paginated_posts.paginator.num_pages 
        return render(request, self.template_name, {'form': form, 'posts': posts, 'paginated_posts': paginated_posts, 'nums': nums})


class AdminCampusCreateView(LoginRequiredMixin, CreateView):
    template_name = 'admincampus.html'
    form_class = Admincampusform
    success_url = reverse_lazy('admincampus')
    login_url = 'campus'
    redirect_field_name = 'admincampus'

    def form_valid(self, form):
        title = form.cleaned_data.get('title')
        blog = form.cleaned_data.get('blog')
        person = form.cleaned_data.get('person')
        content = form.cleaned_data.get('content')
        main = form.cleaned_data.get('main')
        author = form.cleaned_data.get('author')
        created_at = form.cleaned_data.get('created_at')

        form.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
 
def logout_campus(request):
    logout(request)
    return redirect('campus')



class Campusdetail(DetailView):
    model = Admincampusmodel
    template_name = 'detailcampus.html'
    form_class = Campuscommentform
    success_url = reverse_lazy('detailcampus')
     

    def form_valid(self, form):
        post = get_object_or_404(Admincampusmodel, pk=self.kwargs.get('pk'))
        form.instance.post = post  
        form.save()
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        post_id = self.kwargs.get('pk')

        posts = get_object_or_404(Admincampusmodel, pk=post_id)


        news = self.get_object()

        curated = Admincampusmodel.objects.all().order_by('-created_at')[:3]

        comments = Campuscomement.objects.filter(post=news)

        form = self.form_class()

        context = {
            'posts': posts,
            'news': news,
            'curated': curated,
            'comments': comments,
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        news = self.get_object()

        form = self.form_class(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = news
            comment.save()

            return HttpResponseRedirect(reverse('detailcampus', kwargs={'pk': news.pk}))
        
        post_id = self.kwargs.get('pk')

        posts = get_object_or_404(Admincampusmodel, pk=post_id)

        curated = Admincampusmodel.objects.all().order_by('-created_at')[:3]
        comments = Campuscomement.objects.filter(post=news)

        context = {
            'posts': posts,
            'news': news,
            'curated': curated,
            'comments': comments,
            'form': form
        }

        return render(request, self.template_name, context)
    
    


class RegisterView(FormView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('success') 

    def form_valid(self, form):
        form.save()  
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = "success.html" 


  
    