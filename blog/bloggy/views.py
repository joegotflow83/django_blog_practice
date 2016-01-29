from django.shortcuts import render, get_object_or_404, \
		render_to_response, redirect
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.template import loader
from bloggy.models import Users, Posts
from bloggy.forms import PostForm

# Home Page Once logged on
def index(request):

	my_posts = Posts.objects.all().order_by('-date')
	t = loader.get_template('blog.html')
	context_dict = {'my_posts': my_posts}
	c = Context(context_dict)

	return HttpResponse(t.render(c))

# Allow the user to create a post
def add_post(request):

	context = RequestContext(request)

	if request.method == 'POST':

		form = PostForm(request.POST, request.FILES)

		if form.is_valid():

			form.save(commit=True)

			return redirect(index)

		else:

			print(form.errors)

	else:

		form = PostForm()

	return render_to_response('add_post.html', {'form': form}, context)