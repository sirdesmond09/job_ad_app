from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class JobAdvert(models.Model):
    EMPLOYMENT_CHOICES = (("full-time", "Full Time"),
                        ("contract", "Contract"),
                        ("remote","Remote"),
                        ("part-time", "Part Time"),)
    
    EMPLOYMENT_LEVELS = ( ("entry-level","Entry level"), 
                         ("mid-level","Mid-level"), 
                         ("senior","Senior"))
    
    STATUS = (("unpublished","Unpublished"), 
              ("published","Published"))
    

    title = models.CharField(max_length=250)
    company_name = models.CharField(max_length=250)
    employment_type = models.CharField(max_length=250, choices=EMPLOYMENT_CHOICES)
    employment_level = models.CharField(max_length=250, choices=EMPLOYMENT_LEVELS)
    description= models.TextField()
    location = models.CharField(max_length=250)
    job_description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS, default="published")
    date_added = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.title} --- {self.company_name}"
    
    
class JobApplication(models.Model):
    
    EXPERIENCE_LEVELS = (("0 - 1", "0 - 1"), 
                         ("1 - 2", "1 - 2"), 
                         ("3 - 4", "3 - 4"),
                         ("5 - 6", "5 - 6"), 
                         ("7 and above", "7 and above")
                        )
    
    
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length = 50)
    linkedin_url = models.URLField()
    github_url = models.URLField()
    website = models.URLField(blank=True, null=True)
    years_of_experience = models.CharField(max_length=50, choices=EXPERIENCE_LEVELS)
    cover_letter = models.TextField(blank=True, null=True)
    job_advert = models.ForeignKey("main.JobAdvert", related_name="applications", on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)

    
    
    def __str__(self):
        return f"Application for --- {self.job_advert}"