from encodings.punycode import selective_find

import pytest

from tests.base_test import Base_Test
from utilities.FakerUtility import FakerUtility


class Test_Job_Page(Base_Test):

    def test_add_new_job(self):
        # 1. Trigger Login first
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickOnLogin()

        status = self.dp.is_header_Dashboard_present()
        assert status == True, "❌ Login Failed: Dashboard header not displayed!"

        self.dp.click_anchor_Admin()
        self.jp.click_on_jobtitle()
        self.jp.click_on_add_job()

        job_title = FakerUtility.generate_random_jobtitle()
        job_description = FakerUtility.generate_random_sentence()
        file_name = "test-data/job_spec.pdf"
        job_note = FakerUtility.generate_random_sentence()

        self.jp.enter_job_details(job_title, job_description, file_name, job_note)
        assert self.jp.is_job_success_message_is_displayed() is True
