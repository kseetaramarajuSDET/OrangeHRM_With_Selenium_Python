from faker import Faker


class FakerUtility(Faker):

    @staticmethod
    def generate_random_jobtitle():
        # Generates a realistic job title
        fake = Faker()
        # Takes only the first 10 characters of the job name + time
        return f"{fake.job()[:10]}_{fake.time()}"
