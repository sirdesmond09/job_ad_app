from faker import Faker
from main.models import JobAdvert, JobApplication
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Populates the DB with agencies, issues and questions'

    def handle(self, *args, **options):
        fake = Faker()


        JobAdvert.objects.all().delete()
        
        job1 = JobAdvert.objects.create(title='Backend Developer', 
                                    company_name="Torilo", 
                                    employment_type="remote",
                                    employment_level="mid-level",
                                    status = "unpublished",
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

        job3 = JobAdvert.objects.create(title='Accountant', 
                                    company_name="Johnson and Man", 
                                    employment_type="full-time",
                                    employment_level="mid-level",
                                    status = "unpublished",
                                    location = f"{fake.city()}, {fake.country()}",
                                    description=fake.sentence(), 
                                    job_description=fake.sentence())
        
        job4 = JobAdvert.objects.create(title='Front End Developer', 
                                    company_name="Johnson and Man", 
                                    employment_type="full-time",
                                    employment_level="mid-level",
                                    status = "published",
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


        JobApplication.objects.create(first_name = fake.name().split()[0],
                                                        last_name= fake.name().split()[1],
                                                        email= fake.email(),
                                                        phone = fake.phone_number(),
                                                        linkedin_url= fake.url(),
                                                        github_url=fake.url(),
                                                        years_of_experience="3 - 4",
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


        JobApplication.objects.create(first_name = fake.name().split()[0],
                                                        last_name= fake.name().split()[1],
                                                        email= fake.email(),
                                                        phone = fake.phone_number(),
                                                        linkedin_url= fake.url(),
                                                        github_url=fake.url(),
                                                        years_of_experience="3 - 4",
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
                                                        job_advert=job4)

        JobApplication.objects.create(first_name = fake.name().split()[0],
                                                        last_name= fake.name().split()[1],
                                                        email= fake.email(),
                                                        phone = fake.phone_number(),
                                                        linkedin_url= fake.url(),
                                                        github_url=fake.url(),
                                                        years_of_experience="3 - 4",
                                                        cover_letter= fake.sentence(),
                                                        job_advert=job3)


        JobApplication.objects.create(first_name = fake.name().split()[0],
                                                        last_name= fake.name().split()[1],
                                                        email= fake.email(),
                                                        phone = fake.phone_number(),
                                                        linkedin_url= fake.url(),
                                                        github_url=fake.url(),
                                                        years_of_experience="3 - 4",
                                                        cover_letter= fake.sentence(),
                                                        job_advert=job4)
        
        self.stdout.write(self.style.SUCCESS('Populate data complete'))