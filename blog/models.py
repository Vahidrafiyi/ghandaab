from django.db import models
from django.core.exceptions import ValidationError
from django_jalali.db import models as jmodels
from datetime import datetime
def image_upload_to(instance, filename):
    model_name = instance._meta.model_name
    return 'images/{}/{}/{}'.format(instance._meta.model_name, datetime.now().strftime("%Y/%m/%d"), filename)

class Image(models.Model):
    image = models.ImageField(upload_to=image_upload_to)
    uploded_at = jmodels.jDateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model_name

class Category(models.Model):
    title = models.CharField(max_length=64)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return self.title

    def save(self):
        if self.pk is None:
            image = Image.objects.create(image=self.image, model_name='blog_category/')
            self.image = image
        super().save(*args, **kwargs)


class Tag(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title



class Post(models.Model):
    Draft = 1
    Published = 2
    STATUS = [
        (Draft, 'Draft'),
        (Published, 'Published')
    ]
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    body = models.TextField()
    main_image = models.ForeignKey(Image, on_delete=models.PROTECT, related_name='post_main_image', null=True, blank=True)
    body_images = models.ManyToManyField(Image, related_name='post_body_images', null=True, blank=True)
    author = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='related_group')
    tags = models.ManyToManyField(Tag, related_name='tags')
    related_posts = models.ManyToManyField('self', null=True, blank=True)
    status = models.PositiveIntegerField(choices=STATUS, default=Draft)
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    updated_at = jmodels.jDateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def clean(self):
        if self.status > 2:
            raise ValidationError('please enter 1 or 2. (1 for draft and 2 for published)')
        if self.tags.count() > 5:
            raise ValidationError('you can not add more than 5 tags \n please add the most relevant tags :)')
        if self.related_posts.count() > 5 :
            raise ValidationError('you can not add more than 5 related posts \n please add the most intresting posts :)')

    def save(self):
        if self.pk is None:
            main_image = Image.objects.create(image=self.main_image, model_name='posts/main/')
            body_images = Image.objects.create(image=self.body_images, model_name='posts/body/')
            self.main_image = main_image
            self.body_images = body_images
        super().save(*args, **kwargs)