from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Researcher, Project, Publication
from .forms import ResearcherForm, ProjectForm, PublicationForm, SignUpForm, UserLoginForm

# Authentication Views


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # Redirige vers la page souhaitée après inscription
            return redirect('researcher_list')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirige vers la page souhaitée après connexion
                return redirect('researcher_list')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('researcher_list')

# Researchers Views


def researcher_list(request):
    researchers = Researcher.objects.all()
    return render(request, 'researcher_list.html', {'researchers': researchers})


def researcher_detail(request, pk):
    researcher = get_object_or_404(Researcher, pk=pk)
    return render(request, 'researcher_detail.html', {'researcher': researcher})


@login_required
def researcher_create(request):
    if request.method == "POST":
        form = ResearcherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('researcher_list')
    else:
        form = ResearcherForm()
    return render(request, 'researcher_form.html', {'form': form})


@login_required
def researcher_update(request, pk):
    researcher = get_object_or_404(Researcher, pk=pk)
    if request.method == "POST":
        form = ResearcherForm(request.POST, instance=researcher)
        if form.is_valid():
            form.save()
            return redirect('researcher_detail', pk=pk)
    else:
        form = ResearcherForm(instance=researcher)
    return render(request, 'researcher_form.html', {'form': form})


@login_required
def researcher_delete(request, pk):
    researcher = get_object_or_404(Researcher, pk=pk)
    if request.method == "POST":
        researcher.delete()
        return redirect('researcher_list')
    return render(request, 'researcher_confirm_delete.html', {'researcher': researcher})


# Publication Views


def publication_list(request):
    publications = Publication.objects.all()
    return render(request, 'publication_list.html', {'publications': publications})


def publication_detail(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    return render(request, 'publication_detail.html', {'publication': publication})


@login_required
def publication_create(request):
    if request.method == "POST":
        form = PublicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publication_list')
    else:
        form = PublicationForm()
    return render(request, 'publication_form.html', {'form': form})


@login_required
def publication_update(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    if request.method == "POST":
        form = PublicationForm(request.POST, instance=publication)
        if form.is_valid():
            form.save()
            return redirect('publication_detail', pk=pk)
    else:
        form = PublicationForm(instance=publication)
    return render(request, 'publication_form.html', {'form': form})


@login_required
def publication_delete(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    if request.method == "POST":
        publication.delete()
        return redirect('publication_list')
    return render(request, 'publication_confirm_delete.html', {'publication': publication})

# Project Views


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})


@login_required
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {'form': form})


@login_required
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project_form.html', {'form': form})


@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        project.delete()
        return redirect('project_list')
    return render(request, 'project_confirm_delete.html', {'project': project})

# Search View


def search(request):
    researchers = Researcher.objects.all()
    projects = Project.objects.all()
    publications = Publication.objects.all()

    query = request.GET.get('q')
    if query:
        researchers = researchers.filter(
            Q(nom__icontains=query) | Q(specialite__icontains=query))
        projects = projects.filter(
            Q(titre__icontains=query) | Q(description__icontains=query))
        publications = publications.filter(
            Q(titre__icontains=query) | Q(resume__icontains=query))

    return render(request, 'search.html', {
        'researchers': researchers,
        'projects': projects,
        'publications': publications,
    })
