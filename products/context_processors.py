from products.models import MainCategory, SiteContent


def categories_processor(request):
    categories = MainCategory.objects.all()
    return {'categories': categories}


def content_processor(request):
    content = SiteContent.objects.all()
    return {'content': content}
