from django.shortcuts import render, redirect, get_object_or_404
from .models import SearchRecord, SafetyFilter, Accommodation, Post, Comment, Like
from .forms import SearchRecordForm, PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def main(request):
    form = SearchRecordForm()
    safety_filters = SafetyFilter.objects.all()
    return render(request, 'homst/main.html', {'form': form, 'safety_filters': safety_filters})

@login_required
def search_results(request):
    if request.method == 'GET':
        form = SearchRecordForm(request.GET)
        if form.is_valid():
            destination = form.cleaned_data['destination']
            travel_date = form.cleaned_data['travel_date']
            travel_date2 = form.cleaned_data['travel_date2']
            people = form.cleaned_data['people']
            safety_filters_ids = request.GET.getlist('safety_filter')
            safety_filters = SafetyFilter.objects.filter(id__in=safety_filters_ids)
            sort_by = request.GET.get('sort_by', '')

            accommodations = Accommodation.objects.filter(
                location__icontains=destination,
                safety_filters__in=safety_filters
            ).distinct()

            if sort_by == 'price_asc':
                accommodations = accommodations.order_by('price')
            elif sort_by == 'price_desc':
                accommodations = accommodations.order_by('-price')
            elif sort_by == 'rating_asc':
                accommodations = accommodations.order_by('review_score')
            elif sort_by == 'rating_desc':
                accommodations = accommodations.order_by('-review_score')

            search_results_count = accommodations.count()

            # 검색 기록 저장
            search_record = SearchRecord.objects.create(
                user=request.user,
                destination=destination,
                travel_date=travel_date,
                travel_date2=travel_date2,
                people=people,
            )

            return render(request, 'homst/search_results.html', {
                'accommodations': accommodations,
                'search_results_count': search_results_count,
                'destination': destination,
                'travel_date': travel_date,
                'travel_date2': travel_date2,
                'people': people,
                'safety_filters': safety_filters,
                'form': form,
                'sort_by': sort_by
            })
    
    else:
        form = SearchRecordForm()

    safety_filters = SafetyFilter.objects.all()
    return render(request, 'homst/main.html', {'form': form, 'safety_filters': safety_filters})

@login_required
def record_detail(request, record_id):
    accommodation = get_object_or_404(Accommodation, id=record_id)
    context = {
        'accommodation': accommodation,
    }
    return render(request, 'homst/record_detail.html', context)

@login_required
def community(request):
    category = request.GET.get('category', '')
    if category:
        posts = Post.objects.filter(category=category)
    else:
        posts = Post.objects.all()

    words = set()  # 중복을 피하기 위해 집합(set)을 사용
    for post in posts:
        words.update(post.words.split())

    return render(request, 'homst/community.html', {'posts': posts, 'words': words})

@login_required
def community_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            
            # 단어 추출 및 저장
            selected_word = request.POST.get('search_input', '')  # 선택된 단어
            post.words = selected_word
            
            post.save()
            return redirect('community')
    else:
        form = PostForm(initial={'search_input': request.GET.get('search_input', '')})
    words = ['스카이하우스', '더퍼스트펜션', '강릉 테레인바이 더블류스파펜션','강릉시티호텔','세인트존스호텔','스카이베이호텔']  # 예시: 실제 데이터베이스 쿼리나 다른 데이터로 대체되어야 합니다.
    return render(request, 'homst/community_create.html', {'words': words, 'form': form})


@login_required
def community_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    words = post.words.split(', ') if post.words else []  # 저장된 단어를 쉼표로 구분하여 리스트로 변환
    return render(request, 'homst/community_detail.html', {'post': post, 'words': words})

@login_required
def community_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('community_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'homst/community_update.html', {'form': form, 'post': post})

@login_required
def community_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")

    if request.method == 'POST':
        post.delete()
        return redirect('community')
    return render(request, 'homst/community_delete.html', {'post': post})


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
        return redirect('community_detail', pk=post.id)
    else:
        form = CommentForm()

    return render(request, 'community_detail.html', {'post': post, 'comment_form': form})

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('community_detail', pk=pk)

@login_required
def mypage(request):
    user = request.user
    liked_posts = user.liked_posts.all()
    authored_posts = user.posts.all()

    context = {
        'user': user,
        'liked_posts': liked_posts,
        'authored_posts': authored_posts,
    }
    return render(request, 'homst/mypage.html', context)

