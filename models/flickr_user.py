__author__ = 'michael.degain'

from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from django_flickr_gallery.models.managers import AlbumFeaturedManager
from django_flickr_gallery.models.managers import AlbumPublishedManager

from django_flickr_gallery.utils import get_photoset, AttributeDict

class BaseFlickrUser(models.Model):
    """
    Abstract core flickr user model class providing
    the fields and methods required for sync and token generation
    """

    #table columns
    username = models.CharField(max_length=50, null=False, blank=False)
    full_name = models.CharField(max_length=50, null=True, blank=True)
    nsid = models.CharField(max_length=50, null=True, blank=True)
    token = models.CharField(max_length=50, null=True, blank=True)
    ispro = models.BooleanField(default=False, null=True, blank=True)
    isadmin = models.BooleanField(default=False, null=False, blank=False)
    photos_url = models.URLField(max_length=255, null=True, blank=True)
    profile_url = models.URLField(max_length=255, null=True, blank=True)
    perms = models.CharField(max_length=20, default='read', null=True, blank=True)
    last_sync = models.DateTimeField()

    #model functions
    @property
    def get_user_albums(self):
        """
        Returns album objects from other side of one to many relationship.
        """
        return self.albums_set.all()

    @property
    def user_json(self):
        """
        This will return a list of jsons representing a users info
        """
        if not hasattr(self, 'user_data'):
            user_data = False#### make the call to get the users info
        return user_albums_data ####

    #may change this to full name at some point in the future
    def __str__(self):
        return self.username

    #stole functions from parent branch in order to be consistent
    def save(self, *args, **kwargs):
        if not self.pk:
            # the first sync
            self.sync(commit=False)
        super(BaseFlickrUser, self).save(*args, **kwargs)

    ######## NEED TO COME UP WITH A PLAN FOR SYNCING USER> WHAT TO DO WITH USER FUNCTION
    ######## Do I involve token getting in the process?
    ######## Do I attempt to populate every single field or just critical ones?
    def sync(self, commit=True):
        self.full_name = self.user.full_name
        self.slug = slugify(self.username)
        self.last_sync = timezone.now()

        # force commit changes
        if commit:
            self.save()

    ######### Do I need this? I mean I could always just return the users profile path.
    #def get_absolute_url(self):
    #    return reverse('gallery-photos', kwargs={"slug": self.slug})


    #ensure this is an abstract class
    class Meta():
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ['username']
        abstract = True

class FlickrUser(BaseFlickrUser):
    #handling this in this manner for consistency sake at the moment
    """
    Final abstract flickr user class assembling
    all the abstract album model classes into a single one.
    """
