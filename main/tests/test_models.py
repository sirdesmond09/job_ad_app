from django.forms import model_to_dict
from django.test import TestCase
from ..models import JobAdvert, JobApplication
from django.utils import timezone
from django.urls import reverse
from rest_framework.test import APITestCase
from faker import Faker
# Create your tests here.

class JobAdvertTests(TestCase):
    def test_create_job_ad(self):
        job_ad = JobAdvert.objects.create(
        title='Backend Developer', company_name="Torilo", employment_type="remote",employment_level="mid-level",description="This is a backend developer mid level role.", location="Jos",job_description="You need to do XYZ")
        
        
        self.assertEqual(job_ad.title, 'Backend Developer')
        self.assertEqual(job_ad.company_name, 'Torilo')
        self.assertEqual(job_ad.employment_level, 'mid-level')
        self.assertEqual(job_ad.description, 'This is a backend developer mid level role.')
        self.assertEqual(job_ad.job_description, 'You need to do XYZ')
        
        
class JobAppliciation(TestCase):
    
    def setUp(self):
        fake = Faker()
        
        job1 = JobAdvert.objects.create(title='Backend Developer', 
                                 company_name="Torilo", 
                                 employment_type="remote",
                                 employment_level="mid-level",
                                 location = f"{fake.city()}, {fake.country()}",
                                 description=fake.sentence(), 
                                 job_description=fake.sentence())
        
        job2 = JobAdvert.objects.create(title='Account Officer', 
                                 company_name="Johnson and Man", 
                                 employment_type="full-time",
                                 employment_level="mid-level",
                                 location = f"{fake.city()}, {fake.country()}",
                                 description=fake.sentence(), 
                                 job_description=fake.sentence())
    

        JobApplication.objects.create(first_name = fake.name().split()[0],
                                                     last_name= fake.name().split()[1],
                                                     email= fake.email(),
                                                     phone = fake.phone_number(),
                                                     linkedin_url= fake.url(),
                                                     github_url=fake.url(),
                                                     website=fake.url(),
                                                     years_of_experience="3 - 4",
                                                     cover_letter= fake.sentence(),
                                                     job_advert=job1)
        
        JobApplication.objects.create(first_name = fake.name().split()[0],
                                                     last_name= fake.name().split()[1],
                                                     email= fake.email(),
                                                     phone = fake.phone_number(),
                                                     linkedin_url= fake.url(),
                                                     github_url=fake.url(),
                                                     years_of_experience="1 - 2",
                                                     cover_letter= fake.sentence(),
                                                     job_advert=job1)
        
        JobApplication.objects.create(first_name = fake.name().split()[0],
                                                     last_name= fake.name().split()[1],
                                                     email= fake.email(),
                                                     phone = fake.phone_number(),
                                                     linkedin_url= fake.url(),
                                                     github_url=fake.url(),
                                                     website=fake.url(),
                                                     years_of_experience="5 - 6",
                                                     cover_letter= fake.sentence(),
                                                     job_advert=job2)
        
        JobApplication.objects.create(first_name = fake.name().split()[0],
                                                     last_name= fake.name().split()[1],
                                                     email= fake.email(),
                                                     phone = fake.phone_number(),
                                                     linkedin_url= fake.url(),
                                                     github_url=fake.url(),
                                                     years_of_experience="3 - 4",
                                                     cover_letter= fake.sentence(),
                                                     job_advert=job2)
        
        
    def test_job_advert_applications(self):
        ad1 = JobAdvert.objects.prefetch_related("applications").first()
        ad2 = JobAdvert.objects.prefetch_related("applications").last()
        self.assertEquals(ad1.applications.count(), 2)
        self.assertEquals(ad2.applications.count(), 2)
        
    
    def test_delete_related_applications(self):
        ad1 = JobAdvert.objects.first()
        ad1.delete()
        
        self.assertEquals(ad1.applications.count(), 0)
        
                                                     

        

