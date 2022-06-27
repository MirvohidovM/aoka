from modeltranslation.translator import register, TranslationOptions

from opendata.models import Opendata, OpendataAttachments
from menu.models import Menu
from news.models import News
from useful_link.models import UsefulLink
from organizations.models import Organization, AccountOrganization
from contact.models import Contact

@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('address', 'transport', 'position', 'reception_days',)


@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    fields = ('title', 'note')
    required_languages = {'uz': ('title',)}


@register(UsefulLink)
class UsefulLinkTranslationOptions(TranslationOptions):
    fields = ['title']


@register(Opendata)
class OpendataTranslationOptions(TranslationOptions):
    fields = ['title',]


@register(OpendataAttachments)
class OpendataAttachmentsTranslationOptions(TranslationOptions):
    fields = ('name',)
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
    fields = ('title',)
    required_languages = ('uz',)
