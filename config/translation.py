from modeltranslation.translator import register, TranslationOptions

from opendata.models import Opendata, OpendataImages
from menu.models import Menu
from news.models import News
from useful_link.models import UsefulLink
from organizations.models import Organization, AccountOrganization
from contact.models import Contact, LandmarkPhotos

@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('address', 'transport', 'position', 'reseption_days',)


@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    fields = ('title', 'note')
    required_languages = {'uz': ('title',)}


@register(UsefulLink)
class UsefulLinkTranslationOptions(TranslationOptions):
    fields = ['title']


@register(Opendata)
class OpendataTranslationOptions(TranslationOptions):
    fields = ['title', 'ilova']


@register(OpendataImages)
class OpendataImagesTranslationOptions(TranslationOptions):
    fields = ('name', 'file')
    required_languages = ('uz',)


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
    required_languages = {'uz': ('title', 'content')}


@register(Organization)
class OrganizationTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)
    required_languages = ('uz',)


@register(AccountOrganization)
class AccountOrganizationTranslationOptions(TranslationOptions):
    fields = ('title')
    required_languages = ('uz',)
