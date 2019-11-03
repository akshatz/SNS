from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from users.models import Profile, FriendRequest
User = get_user_model()


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            form.cleaned_data.get('username')
            msg = 'Your account is created ! You are now able to login'
            messages.success(request, msg)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def users_list(request):
    users = Profile.objects.exclude(user=request.user)
    context = {
        'users': users
    }
    return render(request, "home.html", context)


def send_friend_request(request, id):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=id)
        frequest, created = FriendRequest.objects.get_or_create(
            from_user=request.user,
            to_user=user)
        return HttpResponseRedirect('/users')


def cancel_friend_request(request, id):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=id)
        frequest = FriendRequest.objects.filter(
            from_user=request.user,
            to_user=user).first()
        frequest.delete()
        return HttpResponseRedirect('/users')


def accept_friend_request(request, id):
    from_user = get_object_or_404(User, id=id)
    frequest = FriendRequest.objects.filter(from_user=from_user, to_user=request.user).first()
    print(frequest)
    user1 = frequest.to_user
    user2 = from_user
    user1.profile.friends.add(user2.profile)
    user2.profile.friends.add(user1.profile)
    frequest.delete()
    return HttpResponseRedirect('/users/{}'.format(request.user.profile.slug))


def delete_friend_request(request, id):
    from_user = get_object_or_404(User, id=id)
    frequest = FriendRequest.objects.filter(from_user=from_user, to_user=request.user).first()
    frequest.delete()
    return HttpResponseRedirect('/users/{}'.format(request.user.profile.slug))


def profile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            msg = 'Your account has been successfully updated!'
            messages.success(request, msg)
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user)
    p = Profile.objects.all().first()
    u = p.user
    print(u)
    sent_friend_requests = FriendRequest.objects.filter(from_user=p.user)
    rec_friend_requests = FriendRequest.objects.filter(to_user=p.user)
    friends = p.friends.all()
    button_status = 'none'
    if p not in request.user.profile.friends.all():
        button_status = 'not_friend'
        if len(FriendRequest.objects.filter(
                from_user=request.user).filter(to_user=p.user)) == 1:
            button_status = 'friend_request_sent'

    return render(request, 'users/profile.html', {'u': u,
                                                  'button_status': button_status,
                                                  'friends_list': friends,
                                                  'sent_friend_requests': sent_friend_requests,
                                                  'rec_friend_requests': rec_friend_requests,
                                                  'u_form': u_form,
                                                  'p_form': p_form
                                                  }
                  )


def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query is not None:
            lookups = Q(first_name=query)
            results = User.objects.filter(lookups)
            return render(request, query.profile, {'results': results})
        else:
            return render(request, 'base.html')
    else:
        return render(request, 'search.html')
