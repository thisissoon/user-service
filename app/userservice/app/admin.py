# Third Party Libs
from django.contrib import admin
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.http import Http404


def sites(obj):
    return ', '.join(map(lambda site: site.name, obj.sites))
sites.short_description = 'Translated'


class SiteTabAdminView(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            kwargs['exclude'] = kwargs.get('exclude', []) + ['site']
        return super(SiteTabAdminView, self).get_form(request, obj, **kwargs)

    def clone_obj(self, obj, site):
        obj.pk = None
        obj.site = site
        obj.save()
        return obj

    def delete_model(self, request, obj):
        if not request.GET.get('site'):
            obj = obj.__class__.objects.filter(model_id=obj.model_id)
        obj.delete()

    def get_actions(self, request):
        actions = super(SiteTabAdminView, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def get_object(self, request, object_id, from_field=None):
        obj = super(SiteTabAdminView, self).get_object(request, object_id, from_field)
        if obj is None:
            return None

        site = request.GET.get('site')
        if site:
            site = Site.objects.get(id=site)
        else:
            return obj

        queryset = self.get_queryset(request)
        try:
            return queryset.get(**{'model_id': obj.model_id, 'site': site})
        except queryset.model.DoesNotExist:
            return self.clone_obj(obj, site)
        except (ValidationError, ValueError):
            return None

    def get_queryset(self, request):
        qs = super(SiteTabAdminView, self).get_queryset(request)
        return qs.distinct('model_id').order_by('model_id')

    def change_view(self, request, object_id, form_url='', extra_context=None):
        try:
            if request.GET.get('site'):
                site = Site.objects.get(id=request.GET.get('site'))
            else:
                site = self.get_object(request, object_id).site
        except (Site.DoesNotExist, self.model.DoesNotExist):
            raise Http404()

        extra_context = extra_context or {}
        extra_context.update({
            'sites': Site.objects.all(),
            'current_site': site,
        })
        return super(SiteTabAdminView, self).change_view(
            request, object_id, form_url, extra_context=extra_context
        )
