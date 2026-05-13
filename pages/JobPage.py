from pages.BasePage import BasePage
from utilities.ReadConfig import ReadConfig
from selenium.webdriver.common.by import By


class JobPage(BasePage):
    span_job_xpath = (By.XPATH, "//span[text()='Job ']")
    li_jobtitle_xpath = (By.XPATH, "//a[text()='Job Titles']")
    button_add_xpath = (By.XPATH, "//button[text()=' Add ']")
    input_jobtitle_xpath = (By.XPATH, "//label[text()='Job Title']/parent::div/following-sibling::div/input")
    textarea_jobdescription_xpath = (By.XPATH,
                                     "//label[text()='Job Description']/parent::div/following-sibling::div/textarea")
    input_job_specification_xpath = (By.XPATH, "//input[@type='file']")
    textarea_add_note_xpath = (By.XPATH,
                               "//label[text()='Note']/parent::div/following-sibling::div/textarea")
    btn_save_xpath = (By.XPATH, "//button[text()=' Save ']")
    job_sucess_msg = (By.XPATH, "//p[text()='Successfully Saved']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_jobtitle(self):
        self.click(self.span_job_xpath)
        self.click(self.li_jobtitle_xpath)

    def click_on_add_job(self):
        self.click(self.button_add_xpath)

    def enter_job_details(self, job_title, job_description, file_name, job_note):
        self.type(self.input_jobtitle_xpath, job_title)
        self.type(self.textarea_jobdescription_xpath, job_description)
        self.upload_file(self.input_job_specification_xpath, file_name)
        self.type(self.textarea_add_note_xpath, job_note)
        self.click(self.btn_save_xpath)

    def is_job_success_message_is_displayed(self):
        return self.is_displayed(self.job_sucess_msg)
