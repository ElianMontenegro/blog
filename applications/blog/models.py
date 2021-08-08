from datetime import datetime, timedelta
#
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
# apps terceros
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField
#managers
from .managers import BlogManager

class Category(TimeStampedModel):
    """Model definition for Category."""

    name = models.CharField(
        'nombre', 
        max_length=30,
        unique = True
    )
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    def __str__(self):
        return self.name

class Tag(TimeStampedModel):
    """Model definition for Tag."""
    name = models.CharField(
        'nombre', 
        max_length=30
    )
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name

class Blog(TimeStampedModel):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    tag = models.ManyToManyField(Tag)

    tittle = models.CharField(
        'titulo', 
        max_length=200
    )

    resume = models.TextField('resumen')

    content = RichTextUploadingField('contenido', max_length=100000)#ediitor de texto

    public = models.BooleanField(default=False)

    image = models.URLField('Url image',blank=True)

    portada = models.BooleanField(default=False)

    in_home = models.BooleanField(default=False)

    slug = models.SlugField(editable=False, max_length=300)
    
    objects = BlogManager()

    class Meta:

        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.tittle

    def get_absolute_url(self):
        return reverse_lazy(
            'blog_app:detail-blog', 
            kwargs={
                'slug': self.slug
            }
        )


    def save(self, *args ,**kwargs):
        # calculamos el total de segundos de la hora actual
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds = int(total_time.total_seconds())
        slug_unique = '%s %s' % (self.tittle, str(seconds))

        self.slug = slugify(slug_unique)

        super(Blog, self).save(*args , **kwargs)



