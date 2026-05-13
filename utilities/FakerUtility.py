from faker import Faker


class FakerUtility(Faker):

    @staticmethod
    def generate_random_jobtitle():
        # Generates a realistic job title
        fake = Faker()
        # Takes only the first 10 characters of the job name + time
        return f"{fake.job()[:10]}_{fake.time()}"

    @staticmethod
    def generate_random_sentence():
        # Generates a realistic job title
        fake = Faker()
        # Option A: A single random sentence (Best for one-line descriptions)
        desc = fake.sentence()
        # Output: "Manage the development and implementation of all technical strategies."
        return desc
