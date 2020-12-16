from django.db import models



class BlogManager(models.Manager):

    def blog_portada(self):
        return self.filter(
            public=True,
            portada=True,  
        ).order_by('-created')[:1]
    
    def blog_in_home(self):
        return self.filter(
            public=True,
            in_home=True,  
        ).order_by('-created')[:3]
    
    def blog_medium(self):
        return self.filter(
            public=True,
            in_home=True,  
        )[:2]

    def search_blog(self,kword , category):
        if (len(category) > 0):
            return self.filter(
                category__name=category,
                tittle__icontains=kword,
                public=True,
            ).order_by('-created')
        else:
            return self.filter(
                tittle__icontains=kword,
                public=True,
            ).order_by('-created')
            


    