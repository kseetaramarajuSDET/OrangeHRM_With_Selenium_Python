import pytest
from tests.base_test import Base_Test
from utilities.FakerUtility import FakerUtility


class Test_Job_Page(Base_Test):

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_add_new_job(self):
        self.logger.info("**** Starting: test_add_new_job ****")

        # 1. Trigger Login first
        self.logger.info(f"Logging in with user: {self.username}")
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickOnLogin()

        status = self.dp.is_header_Dashboard_present()
        if status:
            self.logger.info("✅ Login successful, proceeding to Admin section")
        else:
            self.logger.error("❌ Login Failed inside Job Test")
            assert False, "❌ Login Failed: Dashboard header not displayed!"

        # 2. Navigation
        self.logger.info("Navigating to Admin -> Job -> Job Titles")
        self.dp.click_anchor_Admin()
        self.jp.click_on_jobtitle()
        self.jp.click_on_add_job()

        # 3. Data Generation
        self.logger.info("Generating random test data using FakerUtility")
        job_title = FakerUtility.generate_random_jobtitle()
        job_description = FakerUtility.generate_random_sentence()
        file_name = "test-data/job_spec.pdf"
        job_note = FakerUtility.generate_random_sentence()

        self.logger.info(f"Generated Job Title: {job_title}")

        # 4. Action
        self.logger.info("Entering job details and uploading specification file")
        self.jp.enter_job_details(job_title, job_description, file_name, job_note)

        # 5. Assertion
        self.logger.info("Verifying success message")
        success = self.jp.is_job_success_message_is_displayed()

        if success:
            self.logger.info(f"✅ Successfully added new job title: {job_title}")
            assert True
        else:
            self.logger.error(f"❌ Failed to add job title: {job_title}")
            self.take_screenshot("Failed_Add_Job")
            assert False

        self.logger.info("**** Finished: test_add_new_job ****")
