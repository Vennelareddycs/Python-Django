from django.shortcuts import render, get_object_or_404
from .models import Post



def get_date(post):
    return post['date']

# Create your views here.
def starting_page(request):
    latest_posts=Post.objects.all().order_by("-date")[:3]
    # sorted_posts=sorted(all_posts,key= get_date)
    # latest_posts=sorted_posts[-3:]
    return render(request, "blog/index.html",{
        "posts": latest_posts,
        
    })

def posts(request):
    all_posts=Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html",
    {
        "all_posts":all_posts
    })

def post_detail(request, slug):
    identified_post=get_object_or_404(Post, slug=slug)
    #identified_post=Post.objects.get(slug=slug)
    #identified_post=next(post for post in all_posts if post['slug']== slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })

'''
#dummy data
all_posts=[
    {
        "slug":"hike-in-the-mountains",
        "image":"mountains.jpg",
        "author":"Vennela",
        "date":date(2023, 10, 10),
        "title":"Mountain Hiking",
        "excerpt":"Join us for a mountain hiking adventure tour amidst the world's most thrilling landscapes! Descriptions of hiking tours are available by clicking",
        "content":"""
        Filters are basically adjustments or little transformations we can apply to values which we're outputting with interpolation.
        Filters are basically adjustments or little transformations we can apply to values which we're outputting with interpolation.
        Filters are basically adjustments or little transformations we can apply to values which we're outputting with interpolation.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]

'''