from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Experiences, ExperienceCategory, ExperienceReview
from .forms import ReviewAdd


def all_experiences(request):
    """
    A view to show all experiences,
    including sorting and search queries.
    """
    experiences = Experiences.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                experiences = experiences.annotate(lower_name=Lower('name'))
            if sortkey == 'experience_category':
                sortkey = 'experience_category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            experiences = experiences.order_by(sortkey)

        if 'experience_category' in request.GET:
            categories = request.GET['experience_category'].split(',')
            experiences = experiences.filter(experience_category__name__in=categories)
            categories = ExperienceCategory.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!n\
                               ")
                return redirect(reverse('experiences'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            experiences = experiences.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'experiences': experiences,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'experiences/experiences.html', context)


def experiences_detail(request, experience_id):
    """ A view to show individual experience details """
    experience = get_object_or_404(Experiences, pk=experience_id)
    form = ReviewAdd
    reviews = experience.reviews.filter()
    print(reviews)

    context = {
        'experience': experience,
        'form': form,
        'reviews': reviews,
    }

    return render(request, 'experiences/experiences_detail.html', context)


def all_reviews(request):
    """ A view to render all reviews """
    reviews = ExperienceReview.objects.all()
    print(f'any reviews: {reviews}')
    form = ReviewAdd()

    context = {'reviews': reviews, 'review_form': form}
    return render(request, 'experiences/experiences_detail.html', context)


def add_review(request, experience_id):
    """
    users can add a review to an experience
    """
    experience = get_object_or_404(Experiences, pk=experience_id)
    if request.method == 'POST':
        review_form = ReviewAdd(request.POST or None)
        if review_form.is_valid():
            data = review_form.save(commit=False)
            data.user = request.user
            data.experience = experience
            data.save()
            messages.success(request, 'Your review was successfully posted')
            return redirect(reverse('experiences_detail',
                                    args=[experience.id]))
        else:
            form = ReviewAdd()
            messages.error(request,
                           'Failed to add your review,n\
                            please ensure form is valid')

    context = {'form': form}

    return render(request, context)


def edit_review(request, review_id):
    """
    users/admin can edit their own experience reviews
    """
    review = get_object_or_404(ExperienceReview, pk=review_id)
    print("Review", review)
    experience = review.experience
    if request.method == 'POST':
        form = ReviewAdd(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.info(request, 'Review has been Updated')
            return redirect(reverse('experiences_detail',
                            args=[experience.id]))
        else:
            messages.error(request, 'Review Update failed, Please try again!')

    else:
        form = ReviewAdd(instance=review)

    messages.info(request, 'You are updating your review')
    template = 'experiences/experiences_detail.html'
    context = {
        'form': form,
        'review': review,
        'experience': experience,
        'edit': True,
    }
    return render(request, template, context)


def delete_review(request, review_id):
    '''function to delete a users review'''
    review = get_object_or_404(ExperienceReview, pk=review_id)
    review.delete()
    messages.success(request, 'Removed review')
    return redirect(reverse('experiences'))