from django.contrib import admin
from django import forms
from django.urls import path  # Import path for custom URLs
from django.http import JsonResponse  # Import JsonResponse for AJAX responses
from .models import Gene, Antibody, Experiment, Description

# Gene Admin
class GeneAdmin(admin.ModelAdmin):
    fields = ('name', 'wb_image', 'ip_image', 'icc_if_image', 'fc_image', 'f1000_report_link')


# Inline class for Description
class DescriptionInline(admin.StackedInline):
    model = Description
    extra = 1
    fields = ('rrid', 'supplier', 'host', 'clonality', 'recombinant', 'product_link')


# Antibody Admin
class AntibodyAdmin(admin.ModelAdmin):
    inlines = [DescriptionInline]
    list_display = ('name', 'gene')
    search_fields = ('name', 'gene__name')

class ExperimentAdminForm(forms.ModelForm):
    gene = forms.ModelChoiceField(
        queryset=Gene.objects.all(),
        required=False,
        label="Gene",
        help_text="Select a gene to filter antibodies."
    )

    class Meta:
        model = Experiment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Default: empty queryset for antibodies
        self.fields['antibody'].queryset = Antibody.objects.none()

        if self.instance and self.instance.pk:
            # Editing an existing experiment
            gene = self.instance.antibody.gene
            self.fields['gene'].initial = gene
            self.fields['antibody'].queryset = Antibody.objects.filter(gene=gene)
        elif 'gene' in self.data:
            # Adding a new experiment and filtering antibodies based on selected gene
            try:
                gene_id = int(self.data.get('gene'))
                self.fields['antibody'].queryset = Antibody.objects.filter(gene_id=gene_id)
            except (ValueError, TypeError):
                self.fields['antibody'].queryset = Antibody.objects.none()


from django.urls import path
from django.http import JsonResponse

class ExperimentAdmin(admin.ModelAdmin):
    form = ExperimentAdminForm

    def get_urls(self):
        urls = super().get_urls()  # Get the default admin URLs
        custom_urls = [
            path(
                'antibodies_by_gene/',  # Custom URL
                self.admin_site.admin_view(self.antibodies_by_gene),  # View for the custom URL
                name='antibodies_by_gene',  # Name for the URL
            ),
        ]
        return custom_urls + urls  # Append custom URLs to the default ones

    def antibodies_by_gene(self, request):
        """
        View to handle AJAX requests for antibodies filtered by gene.
        """
        gene_id = request.GET.get('gene_id')
        if gene_id:
            antibodies = Antibody.objects.filter(gene_id=gene_id).values('id', 'name')
            return JsonResponse({'antibodies': list(antibodies)})
        return JsonResponse({'antibodies': []})



    class Media:
        js = ('core/experiment_admin.js',)

# Register models in admin
admin.site.register(Gene, GeneAdmin)
admin.site.register(Antibody, AntibodyAdmin)
admin.site.register(Experiment, ExperimentAdmin)
