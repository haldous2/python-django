
from django.conf.urls import patterns, url

urlpatterns = patterns('myblog.views',

    ## General pattern if nothing defined
    url(r'^$', 'stub_view', name="blog_index"),

    ## Capture post ID - pass as url to *args
    url(r'^posts/(\d+)/$', 'stub_view', name="blog_detail"),

    ## Capture post ID - pass as querystring to *kwargs
    #url(r'^posts/(?P<post_id>\d+)/$', 'stub_view', name="blog_detail"),

)
