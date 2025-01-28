from django.utils.text import slugify
from django.utils import timezone

def generate_unique_slug(model_class, title):
    slug = slugify(title)
    unique_slug = slug
    counter = 1
    while model_class.objects.filter(slug=unique_slug).exists():
        if counter == 1:
            unique_slug - f"{slug}-{timezone.now().strftime('%Y%m%d')}"
        
        else:
            unique_slug = f"{slug}-{timezone.now().strftime('%Y%m%d')}-{counter}"
        counter +=1
    return unique_slug