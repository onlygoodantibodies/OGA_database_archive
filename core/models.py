from django.db import models

from django.db import models

class Gene(models.Model):
    name = models.CharField(max_length=100, unique=True)
    citation = models.TextField(blank=True, null=True)
    wb_image = models.ImageField(upload_to="gene_experiments/", null=True, blank=True)  # Western Blot
    ip_image = models.ImageField(upload_to="gene_experiments/", null=True, blank=True)  # IP
    icc_if_image = models.ImageField(upload_to="gene_experiments/", null=True, blank=True)  # ICC-IF
    fc_image = models.ImageField(upload_to="gene_experiments/", null=True, blank=True)  # FC
    f1000_report_link = models.URLField(blank=True, null=True)  # Add field for F1000 report link
    

    def __str__(self):
        return self.name

class Antibody(models.Model):
    name = models.CharField(max_length=255)
    gene = models.ForeignKey(Gene, on_delete=models.CASCADE, related_name="antibodies")

    def __str__(self):
        return f"{self.name} ({self.gene.name})"

class Experiment(models.Model):
    antibody = models.ForeignKey(Antibody, on_delete=models.CASCADE, related_name="experiments")
    experiment_type = models.CharField(
        max_length=50,
        choices=[
            ("WB", "Western Blot"),
            ("IP", "Immunoprecipitation"),
            ("ICC-IF", "Immunocytochemistry/IF"),
            ("FC", "Flow Cytometry"),
        ],
    )
    file_path = models.FileField(upload_to="experiments/", null=True, blank=True)  # Use FileField for SVG support

    def __str__(self):
        return f"{self.antibody.name} - {self.experiment_type}"

class Description(models.Model):
    antibody = models.OneToOneField(Antibody, on_delete=models.CASCADE, related_name="description")
    rrid = models.CharField(max_length=100, blank=True, null=True)
    supplier = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=100, blank=True, null=True)
    clonality = models.CharField(max_length=100, blank=True, null=True)
    clone_ID = models.CharField(max_length=100, blank=True, null=True)
    recombinant = models.CharField(max_length=100, blank=True, null=True)
    recomended_applications = models.CharField(max_length=100, blank=True, null=True)
    product_link= models.CharField(max_length=255, blank=True, null=True )
    discontinued = models.BooleanField(default=False)


    def __str__(self):
        return f"Description for {self.antibody.name}"

