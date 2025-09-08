Post.objects.create(title='One more post',
                    slug='one-more-post',
                    body='Post body.',
                    author=user)


from blog.models import Post
user = User.objects.get(username='admin')
post = Post(title='Another post',
            slug='another-post',
            body='Post body.',
            author=user)

post.title = 'New title'
post.save()

Post.objects.get()
all_posts = Post.objects.all()

Post.objects.filter(publish__year=2022)
Post.objects.filter(publish__year=2022, author__username='admin')


Post.objects.filter(publish__year=2022) \
            .exclude(title__startswith='Why')

from blog.models import Post
Post.published.filter(title__startswith='Who')
