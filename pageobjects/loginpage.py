import time
from selenium.webdriver.common.by import By

class login:
    def __init__(self, driver):
        self.driver = driver
    txtbx_email_xpath = "//input[@placeholder='Username']"
    txtbx_password_xpath = "//input[@placeholder='Password']"
    btn_login_button ="//button[normalize-space()='Login']"
    def setlogin(self,username,password):
        self.driver.find_element(By.XPATH, self.txtbx_email_xpath).send_keys(username)
        self.driver.find_element(By.XPATH, self.txtbx_password_xpath).send_keys(password)
        self.driver.find_element(By.XPATH, self.btn_login_button).click()
    pim_add_xpath = "//button[normalize-space()='Add']"
    fst_name_xpath = "//input[@placeholder='First Name']"
    lst_name_xpath = "//input[@placeholder='Last Name']"
    save_btn_xpath = "//button[normalize-space()='Save']"
    def pim(self,firstname,lastname):
        self.driver.find_element(By.XPATH,self.pim_add_xpath).click()
        self.driver.find_element(By.XPATH,self.fst_name_xpath).send_keys(firstname)
        self.driver.find_element(By.XPATH,self.lst_name_xpath).send_keys(lastname)
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.save_btn_xpath).click()
    other_id_Xpath = "//div[2]/div[1]/div[2]//div[2]/input[@class='oxd-input oxd-input--active']"
    driver_lic_num_xpath = "//div[2]/div[2]/div[1]/div/div[2]/input[@class='oxd-input oxd-input--active']"
    lic_exp_date_xpath = "//form/div[2]//div[2]//div/input[@placeholder='yyyy-mm-dd']"
    ssn_num_xpath = "//div[3]/div[1]//div[2]/input[@class='oxd-input oxd-input--active']"
    sin_num_xpath = "//div[3]/div[2]//div[2]/input[@class='oxd-input oxd-input--active']"
    drp_nationality_xpath = "//div[@class='oxd-form-row']/div[1]/div[1]//div[@clear]"
    select_country_xpath = "//*[contains(text(),'Indian')]"
    drp_marital_xpath = "//div[2]/div/div[2]//div[@class='oxd-select-text-input']"
    select_status_xpath = "//*[contains(text(),'Single')]"
    dob_xpath = "//form/div[3]//div[2]//div/input[@placeholder='yyyy-mm-dd']"
    radio_btn_xpath = "//label[normalize-space()='Male']"
    mil_serv_xpath = "//div[4]//div[2]/input[@class='oxd-input oxd-input--active']"
    drp_blood_xpath = "//form/div[1]//div[2]//div[@class='oxd-select-text-input']"
    select_type_xpath = "//*[contains(text(),'A+')]"
    pd_save_btn_xpath = "//div[5]/button[@type='submit']"
    pd1_save_btn_xpath = "//div[2]/button"
    def personal(self,otherid,driverlicnum,licexpdate,ssn,sin,dob,military_Service):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.other_id_Xpath).send_keys(otherid)
        self.driver.find_element(By.XPATH, self.driver_lic_num_xpath).send_keys(driverlicnum)
        self.driver.find_element(By.XPATH, self.lic_exp_date_xpath).send_keys(licexpdate)
        self.driver.find_element(By.XPATH,self.ssn_num_xpath).send_keys(ssn)
        self.driver.find_element(By.XPATH,self.sin_num_xpath).send_keys(sin)
        self.driver.find_element(By.XPATH, self.drp_nationality_xpath).click()
        self.driver.find_element(By.XPATH, self.select_country_xpath).click()
        self.driver.find_element(By.XPATH, self.drp_marital_xpath).click()
        self.driver.find_element(By.XPATH, self.select_status_xpath).click()
        self.driver.find_element(By.XPATH, self.dob_xpath).send_keys(dob)
        self.driver.find_element(By.XPATH, self.radio_btn_xpath).click()
        self.driver.find_element(By.XPATH, self.mil_serv_xpath).send_keys(military_Service)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.pd_save_btn_xpath).click()
        self.driver.find_element(By.XPATH, self.drp_blood_xpath).click()
        self.driver.find_element(By.XPATH, self.select_type_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.pd1_save_btn_xpath).click()
    link_contactdetails_xpath = "//a[contains(text(),'Contact Details')]"
    txt_street1_xpath = "//form[@class='oxd-form']/div[1]/div/div[1]//input"
    txt_street2_xpath = "//form[@class='oxd-form']/div[1]/div/div[2]//input"
    txt_city_xpath = "//form[@class='oxd-form']/div[1]/div/div[3]//input"
    txt_state_xpath = "//form[@class='oxd-form']/div[1]/div/div[4]//input"
    txt_pin_xpath = "//form[@class='oxd-form']/div[1]/div/div[5]//input"
    drp_country_xpath = "//*[contains(text(),'-- Select --')]"
    drp_select_xpath = "//*[text()='India']"
    txt_homenumber_xpath = "//form[@class='oxd-form']/div[2]//div[1]/div/div[2]/input"
    txt_mobile_xpath = "//form[@class='oxd-form']/div[2]/div/div[2]//input"
    txt_work_xpath = "//form[@class='oxd-form']/div[2]/div/div[3]//input"
    txt_workemail_xpath = "//form[@class='oxd-form']/div[3]/div/div[1]//input"
    txt_othermail_xpath = "//form[@class='oxd-form']/div[3]/div/div[2]//input"
    txt_contactsave_xpath = "//form[@class='oxd-form']/div[4]//button"
    def contect_detail(self,street1,street2,city,state,pin,home,mobile,work,work_email,other_email):
        self.driver.find_element(By.XPATH,self.link_contactdetails_xpath).click()
        self.driver.find_element(By.XPATH,self.txt_street1_xpath).send_keys(street1)
        self.driver.find_element(By.XPATH,self.txt_street2_xpath).send_keys(street2)
        self.driver.find_element(By.XPATH,self.txt_city_xpath).send_keys(city)
        self.driver.find_element(By.XPATH,self.txt_state_xpath).send_keys(state)
        self.driver.find_element(By.XPATH,self.txt_pin_xpath).send_keys(pin)
        self.driver.find_element(By.XPATH,self.drp_country_xpath).click()
        self.driver.find_element(By.XPATH,self.drp_select_xpath).click()
        self.driver.find_element(By.XPATH,self.txt_homenumber_xpath).send_keys(home)
        self.driver.find_element(By.XPATH,self.txt_mobile_xpath).send_keys(mobile)
        self.driver.find_element(By.XPATH,self.txt_work_xpath).send_keys(work)
        self.driver.find_element(By.XPATH,self.txt_workemail_xpath).send_keys(work_email)
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.txt_othermail_xpath).send_keys(other_email)
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.txt_contactsave_xpath).click()
        time.sleep(2)
    link_emergencycontact_xpath ="//a[normalize-space()='Emergency Contacts']"
    add_btn_xpath = "//div/div[2]/div[1]/div/button"
    txt_name_xpath = "//form[@class='oxd-form']/div[1]/div/div[1]//input"
    txt_relationship_xpath = "//form[@class='oxd-form']/div[1]/div/div[2]//input"
    txt_mobilenumber_xpath = "//form[@class='oxd-form']/div[2]/div/div[2]//input"
    btn_emergencycontactsave_xpath = "//form[@class='oxd-form']/div//button[2]"
    def emergency_contact(self,name,relationship,emcmobile):
        self.driver.find_element(By.XPATH,self.link_emergencycontact_xpath).click()
        self.driver.find_element(By.XPATH,self.add_btn_xpath).click()
        self.driver.find_element(By.XPATH,self.txt_name_xpath).send_keys(name)
        self.driver.find_element(By.XPATH,self.txt_relationship_xpath).send_keys(relationship)
        self.driver.find_element(By.XPATH,self.txt_mobilenumber_xpath).send_keys(emcmobile)
        self.driver.find_element(By.XPATH,self.btn_emergencycontactsave_xpath).click()
    link_dependents_xpath = "//a[normalize-space()='Dependents']"
    dep_add_btn_xpath = "//div[1]/div[2]/div[2]//div[2]/div[1]//button"
    txt_dependentname_xpath = "//form[@class='oxd-form']/div[1]/div/div[1]//input"
    drp_relationship_xpath = "//*[contains(text(),'-- Select --')]"
    drp_other_xpath = "//*[contains(text(),'Child')]"
    list_dob_xpath = "//form[@class='oxd-form']/div[2]//input"
    list_dependentsave_xpath = "//form/div//button[@type='submit']"
    def dependent(self,dep_name,dep_dob):
        self.driver.find_element(By.XPATH,self.link_dependents_xpath).click()
        self.driver.find_element(By.XPATH,self.dep_add_btn_xpath).click()
        self.driver.find_element(By.XPATH,self.txt_dependentname_xpath).send_keys(dep_name)
        self.driver.find_element(By.XPATH,self.drp_relationship_xpath).click()
        self.driver.find_element(By.XPATH,self.drp_other_xpath).click()
        self.driver.find_element(By.XPATH,self.list_dob_xpath).send_keys(dep_dob)
        self.driver.find_element(By.XPATH,self.list_dependentsave_xpath).click()
    link_immigration_xpath = "//a[normalize-space()='Immigration']"
    immi_add_xpath = "//div[1]/div/div[2]/div[1]/div/button"
    txt_number_xpath = "//form[@class='oxd-form']/div[2]/div/div[1]//input"
    txt_issueddate_xpath = "//form[@class='oxd-form']/div[2]/div/div[2]//input"
    immi_drp_xpath = "//*[contains(text(),'-- Select --')]"
    immi_select_xpath = "//*[contains(text(),'India')]"
    txt_expiryddate_xpath = "//form[@class='oxd-form']/div[2]/div/div[3]//input"
    txt_eligiblestatus_xpath = "//form[@class='oxd-form']/div[2]/div/div[4]//input"
    txt_eligiblereview_xpath = "//form[@class='oxd-form']/div[2]/div/div[6]//input"
    txt_cmd_xpath = "//textarea"
    immi_save_xpath = "//button[normalize-space()='Save']"
    def immigration(self,number,issued_date,expiry_date,eligible_status,eligible_review_date,commands):
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.link_immigration_xpath).click()
        self.driver.find_element(By.XPATH,self.immi_add_xpath).click()
        self.driver.find_element(By.XPATH,self.txt_number_xpath).send_keys(number)
        self.driver.find_element(By.XPATH,self.txt_issueddate_xpath).send_keys(issued_date)
        self.driver.find_element(By.XPATH,self.immi_drp_xpath).click()
        self.driver.find_element(By.XPATH,self.immi_select_xpath).click()
        self.driver.find_element(By.XPATH,self.txt_expiryddate_xpath).send_keys(expiry_date)
        self.driver.find_element(By.XPATH,self.txt_eligiblestatus_xpath).send_keys(eligible_status)
        self.driver.find_element(By.XPATH,self.txt_eligiblereview_xpath).send_keys(eligible_review_date)
        self.driver.find_element(By.XPATH,self.txt_cmd_xpath).send_keys(commands)
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.immi_save_xpath).click()
    link_job_xpath = "//a[normalize-space()='Job']"
    txt_joineddate_xpath = "//input[@placeholder='yyyy-mm-dd']"
    drp_job_title_path = "//div[2]/div/div[2]//div[@tabindex='0']"
    select_job_title = "//*[contains(text(),'Chief Executive Officer')]"
    drp_job_categery = "//div[4]/div/div[2]//div[@tabindex='0']"
    select_job_categery ="//*[contains(text(),'Professionals')]"
    sub_unit_xpath = "//div[5]/div/div[2]//div[@tabindex='0']"
    select_sub_unit = "//*[contains(text(),'Administration')]"
    location_path = "//div[6]/div/div[2]//div[@tabindex='0']"
    select_location_path = "//*[contains(text(),'HQ - CA, USA')]"
    employement_status = "//div[7]/div/div[2]//div[@tabindex='0']"
    click_employee_status = "//*[contains(text(),'Full-Time Permanent')]"
    btn_jobsave_xpath = "//button[@type='submit']"
    def job(self,join_date):
        self.driver.find_element(By.XPATH,self.link_job_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.txt_joineddate_xpath).send_keys(join_date)
        self.driver.find_element(By.XPATH,self.drp_job_title_path).click()
        self.driver.find_element(By.XPATH,self.select_job_title).click()
        self.driver.find_element(By.XPATH,self.drp_job_categery).click()
        self.driver.find_element(By.XPATH,self.select_job_categery).click()
        self.driver.find_element(By.XPATH,self.sub_unit_xpath).click()
        self.driver.find_element(By.XPATH,self.select_sub_unit).click()
        self.driver.find_element(By.XPATH,self.location_path).click()
        self.driver.find_element(By.XPATH,self.select_location_path).click()
        self.driver.find_element(By.XPATH,self.employement_status).click()
        self.driver.find_element(By.XPATH,self.click_employee_status).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.btn_jobsave_xpath).click()
    salary_click = "//a[normalize-space()='Salary']"
    ad_salary = "//div[2]//div[1]//div[2]/div[1]//button[@type='button']"
    salary_component = "//div[1]/div/div[2]/input"
    pay_grade = "//div[2]/div/div[2]//div[@class='oxd-select-text-input']"
    select_pay_grade = "//*[contains(text(),'Grade 2')]"
    pay_frequency = "//div[3]/div/div[2]//div[@class='oxd-select-text-input']"
    select_pay_frequency = "//*[contains(text(),'Monthly')]"
    currency_path = "//div[4]/div/div[2]//div[@class='oxd-select-text-input']"
    select_currency = "//*[contains(text(),'United States Dollar')]"
    amount_path = "//div[5]/div/div[2]/input"
    salary_command = "//textarea"
    include_account = "//label/span"
    account_no_path = "//form/div[4]/div[1]/div[1]/div/div[2]/input"
    acount_type = "//form/div[4]//div[2]//div[@class='oxd-select-text-input']"
    select_account_type = "//*[contains(text(),'Savings')]"
    routing_no = "//form/div[4]/div[2]/div[1]/div/div[2]/input"
    amount_xpath = "//div[2]/div/div[2]/input"
    save_salary = "//button[normalize-space()='Save']"
    def salary_details(self, salcomponent, amount1, comments, acountno, routingno, amount2):
        self.driver.find_element(By.XPATH, self.salary_click).click()
        self.driver.find_element(By.XPATH, self.ad_salary).click()
        self.driver.find_element(By.XPATH, self.salary_component).send_keys(salcomponent)
        self.driver.find_element(By.XPATH, self.pay_grade).click()
        self.driver.find_element(By.XPATH, self.select_pay_grade).click()
        self.driver.find_element(By.XPATH, self.pay_frequency).click()
        self.driver.find_element(By.XPATH, self.select_pay_frequency).click()
        self.driver.find_element(By.XPATH, self.currency_path).click()
        self.driver.find_element(By.XPATH, self.select_currency).click()
        self.driver.find_element(By.XPATH, self.amount_path).send_keys(amount1)
        self.driver.find_element(By.XPATH, self.salary_command).send_keys(comments)
        self.driver.find_element(By.XPATH, self.include_account).click()
        self.driver.find_element(By.XPATH, self.account_no_path).send_keys(acountno)
        self.driver.find_element(By.XPATH, self.acount_type).click()
        self.driver.find_element(By.XPATH, self.select_account_type).click()
        self.driver.find_element(By.XPATH, self.routing_no).send_keys(routingno)
        self.driver.find_element(By.XPATH, self.amount_xpath).send_keys(amount2)
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.save_salary).click()
    tax_btn_xpath = "//a[normalize-space()='Tax Exemptions']"
    fede_drp_status_xpath = "//form/div[1]//div[2]//div[@tabindex='0']"
    fede_drp_sta_sel_xpath = "//*[contains(text(),'Single')]"
    fede_txt_xpath = "//div[2]/div/div[2]//input"
    state_drp_xpath = "//div[2]/div/div[1]/div/div[2]/div/div/div[@tabindex='0']"
    state_drp_select_xpath = "//*[contains(text(),'Alaska')]"
    status_drp_xpath = "//div[2]/div/div[2]//div[@class='oxd-select-text-input']"
    status_drp_select_xpath = "//div[2]/div/div[2]//*[contains(text(),'Single')]"
    state_txt_input = "//div[3]//div[2]/input"
    unemp_drp_xpath = "//form//div[4]//div[2]//div[@tabindex='0']"
    unemp_select_xpath = "//*[contains(text(),'New York')]"
    work_state_drp_xpath = "//form//div[5]//div[2]//div[@tabindex='0']"
    work_select_drp_xpath = "//*[contains(text(),'Montana')]"
    tax_save_xpath = "//button[normalize-space()='Save']"
    def tax(self,federal_income_tax,state_income_tax):
        self.driver.find_element(By.XPATH,self.tax_btn_xpath).click()
        self.driver.find_element(By.XPATH,self.fede_drp_status_xpath).click()
        self.driver.find_element(By.XPATH,self.fede_drp_sta_sel_xpath).click()
        self.driver.find_element(By.XPATH,self.fede_txt_xpath).send_keys(federal_income_tax)
        self.driver.find_element(By.XPATH,self.state_drp_xpath).click()
        self.driver.find_element(By.XPATH,self.state_drp_select_xpath).click()
        self.driver.find_element(By.XPATH,self.status_drp_xpath).click()
        self.driver.find_element(By.XPATH,self.status_drp_select_xpath).click()
        self.driver.find_element(By.XPATH,self.state_txt_input).send_keys(state_income_tax)
        self.driver.find_element(By.XPATH,self.unemp_drp_xpath).click()
        self.driver.find_element(By.XPATH,self.unemp_select_xpath).click()
        self.driver.find_element(By.XPATH,self.work_state_drp_xpath).click()
        self.driver.find_element(By.XPATH,self.work_select_drp_xpath).click()
        self.driver.find_element(By.XPATH,self.tax_save_xpath).click()
    report_btn_xpath = "//a[normalize-space()='Report-to']"
    report_add_xpath = "//div[2]/div[2]/div[1]/div/button"
    sup_name_xpath = "//input[@placeholder='Type for hints...']"
    sup_name_select_xpath = "//*[contains(text(),'Peter')]"
    drp_reporting_method_xpath = "//*[contains(text(),'-- Select --')]"
    drp_select_method_xpath = "//*[contains(text(),'Direct')]"
    sup_save_btn_xpath = "//button[normalize-space()='Save']"
    assinged_sub_xpath = "//div[2]/div[3]/div[1]/div/button"
    sub_name_xpath = "//div[1]/div[2]//div[2]/div[3]//input"
    sub_name_select_xpath = "//*[contains(text(),'Cecil')]"
    drp_sub_xpath = "//*[contains(text(),'-- Select --')]"
    drp_sub_select_xpath = "//*[contains(text(),'Indirect')]"
    sub_save_xpath = "//button[normalize-space()='Save']"
    def report(self,supervisors_name,subordinate_name):
        self.driver.find_element(By.XPATH,self.report_btn_xpath).click()
        self.driver.find_element(By.XPATH,self.report_add_xpath).click()
        self.driver.find_element(By.XPATH,self.sup_name_xpath).send_keys(supervisors_name)
        self.driver.find_element(By.XPATH,self.sup_name_select_xpath).click()
        self.driver.find_element(By.XPATH,self.drp_reporting_method_xpath).click()
        self.driver.find_element(By.XPATH,self.drp_select_method_xpath).click()
        self.driver.find_element(By.XPATH,self.sup_save_btn_xpath).click()
        self.driver.find_element(By.XPATH,self.assinged_sub_xpath).click()
        self.driver.find_element(By.XPATH,self.sub_name_xpath).send_keys(subordinate_name)
        self.driver.find_element(By.XPATH,self.sub_name_select_xpath).click()
        self.driver.find_element(By.XPATH,self.drp_sub_xpath).click()
        self.driver.find_element(By.XPATH,self.drp_sub_select_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.sub_save_xpath).click()
    qualification_select_xpath = "//a[normalize-space()='Qualifications']"
    work_experience_add_xpath = "//div[2]/div[2]/div[1]/div/button"
    company_name_xpath = "//div[1]/div/div[2]/input"
    job_title_xpath = "//div[2]/div/div[2]/input"
    from_date_xpath = "//div[1]/div/div[2]/div/div/input[@placeholder='yyyy-mm-dd']"
    to_date_xpath = "//div[2]/div/div[2]/div/div/input[@placeholder='yyyy-mm-dd']"
    work_cmd_xpath  = "//textarea"
    work_save_xpath = "//button[normalize-space()='Save']"
    def qualification_wrk_experience(self, company, jobtitle, fromdate, todate, qulcomments):
        self.driver.find_element(By.XPATH, self.qualification_select_xpath).click()
        self.driver.find_element(By.XPATH, self.work_experience_add_xpath).click()
        self.driver.find_element(By.XPATH, self.company_name_xpath).send_keys(company)
        self.driver.find_element(By.XPATH, self.job_title_xpath).send_keys(jobtitle)
        self.driver.find_element(By.XPATH, self.from_date_xpath).send_keys(fromdate)
        self.driver.find_element(By.XPATH, self.to_date_xpath).send_keys(todate)
        self.driver.find_element(By.XPATH, self.work_cmd_xpath).send_keys(qulcomments)
        self.driver.find_element(By.XPATH, self.work_save_xpath).click()
        time.sleep(5)
    education_add_xpath = "//div[2]//div[3]/div[1]/div/button"
    drp_edu_level_xpath = "//*[@class='oxd-select-text-input']"
    drp_edu_select_xpath = "//*[contains(text(),'Bachelor')]"
    lnstitude_name_xpath = "//div[2]/div/div[2]/input"
    major_name_xpath = "//div[3]/div/div[2]/input"
    year_txt_xpath = "//div[4]/div/div[2]/input"
    score_xpath = "//div[5]/div/div[2]/input"
    edu_start_date_xpath = "//div[1]/div/div[2]/div/div/input[@placeholder='yyyy-mm-dd']"
    edu_end_date_xpath = "//div[2]/div/div[2]/div/div/input[@placeholder='yyyy-mm-dd']"
    edu_save_btn_xpath = "//button[normalize-space()='Save']"
    def qualification_education(self, institute, major, year, gpa, startdate, enddate):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.education_add_xpath).click()
        self.driver.find_element(By.XPATH, self.drp_edu_level_xpath).click()
        self.driver.find_element(By.XPATH, self.drp_edu_select_xpath).click()
        self.driver.find_element(By.XPATH, self.lnstitude_name_xpath).send_keys(institute)
        self.driver.find_element(By.XPATH, self.major_name_xpath).send_keys(major)
        self.driver.find_element(By.XPATH, self.year_txt_xpath).send_keys(year)
        self.driver.find_element(By.XPATH, self.score_xpath).send_keys(gpa)
        self.driver.find_element(By.XPATH, self.edu_start_date_xpath).send_keys(startdate)
        self.driver.find_element(By.XPATH, self.edu_end_date_xpath).send_keys(enddate)
        self.driver.find_element(By.XPATH, self.edu_save_btn_xpath).click()
        time.sleep(5)
    skill_add_xpath = "//div[4]//div[1]/div/button"
    skill_drp_xpath = "//*[contains(text(),'-- Select --')]"
    drp_skill_xpath = "//*[contains(text(),'Python')]"
    year_of_exp_xpath = "//div[2]/div[2]//input"
    skill_cmd_xpath = "//textarea"
    skill_save_xpath = "//button[normalize-space()='Save']"
    def qualification_skills(self, yearofexp,sklcomments):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.skill_add_xpath).click()
        self.driver.find_element(By.XPATH, self.skill_drp_xpath).click()
        self.driver.find_element(By.XPATH, self.drp_skill_xpath).click()
        self.driver.find_element(By.XPATH, self.year_of_exp_xpath).send_keys(yearofexp)
        self.driver.find_element(By.XPATH, self.skill_cmd_xpath).send_keys(sklcomments)
        self.driver.find_element(By.XPATH, self.skill_save_xpath).click()
        time.sleep(5)
    langu_add_xpath = "//div[5]//div[1]/div/button"
    drp_langu_xpath = "//div[1]/div/div[1]/div/div[2]//div[@tabindex='0']"
    drp_langu_select_xpath = "//*[contains(text(),'English')]"
    drp_fluency_xpath = "//div[1]/div/div[2]/div/div[2]//div[@tabindex='0']"
    drp_fluency_select_xpath = "//*[contains(text(),'Writing')]"
    drp_competency_xpath = "//div[1]/div/div[3]/div/div[2]//div[@tabindex='0']"
    drp_competency_select_xpath = "//*[contains(text(),'Good')]"
    langu_cmd_xpath = "//textarea"
    langu_save_xpath = "//button[normalize-space()='Save']"
    def qualification_language(self,langucomments):
        self.driver.find_element(By.XPATH,self.langu_add_xpath).click()
        self.driver.find_element(By.XPATH, self.drp_langu_xpath).click()
        self.driver.find_element(By.XPATH, self.drp_langu_select_xpath).click()
        self.driver.find_element(By.XPATH, self.drp_fluency_xpath).click()
        self.driver.find_element(By.XPATH, self.drp_fluency_select_xpath).click()
        self.driver.find_element(By.XPATH, self.drp_competency_xpath).click()
        self.driver.find_element(By.XPATH, self.drp_competency_select_xpath).click()
        self.driver.find_element(By.XPATH, self.langu_cmd_xpath).send_keys(langucomments)
        self.driver.find_element(By.XPATH, self.langu_save_xpath).click()
        time.sleep(5)
    add_license = "//div[6]/div[1]/div/button"
    license_type = "//form/div[1]/div/div[1]//div[@tabindex='0']"
    select_license_type = "//*[contains(text(),'Certified Information Security Manager')]"
    license_no_xpath = "//div[2]//div[2]/input"
    license_issued_date = "//form/div[2]/div/div[1]//input"
    license_expiry_date = "//form/div[2]/div/div[2]//input"
    save_license = "//button[normalize-space()='Save']"
    def qualification_license(self, licenseno, issueddate, expirydate):
        self.driver.find_element(By.XPATH, self.add_license).click()
        self.driver.find_element(By.XPATH, self.license_type).click()
        self.driver.find_element(By.XPATH, self.select_license_type).click()
        self.driver.find_element(By.XPATH, self.license_no_xpath).send_keys(licenseno)
        self.driver.find_element(By.XPATH, self.license_issued_date).send_keys(issueddate)
        self.driver.find_element(By.XPATH, self.license_expiry_date).send_keys(expirydate)
        self.driver.find_element(By.XPATH, self.save_license).click()
        time.sleep(5)
    add_membership = "//a[normalize-space()='Memberships']"
    mem_add_xpath = "//div[1]/div/div[2]/div[1]/div/button"
    drp_memership_xpath = "//form/div/div/div[1]//div[@tabindex='0']"
    mem_drp_xpath = "//*[contains(text(),'ACCA')]"
    drp_subscription_xpath = "//form/div/div/div[2]//div[@tabindex='0']"
    mem_subscription_xpath = "//*[contains(text(),'Company')]"
    subscription_amt_xpath = "//div[3]//div[2]//input"
    drp_currency_xpath = "//form/div/div/div[4]//div[@tabindex='0']"
    mem_currency_xpath = "//*[contains(text(),'Indian Rupee')]"
    sub_commence_date_xpath = "//div[5]//input[@placeholder='yyyy-mm-dd']"
    sub_renewal_date_xpath = "//div[6]//input[@placeholder='yyyy-mm-dd']"
    membership_save_xpath = "//button[normalize-space()='Save']"
    def memberships(self,subscription_amount,commence_date,renewal_date):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.add_membership).click()
        self.driver.find_element(By.XPATH,self.mem_add_xpath).click()
        self.driver.find_element(By.XPATH,self.drp_memership_xpath).click()
        self.driver.find_element(By.XPATH,self.mem_drp_xpath).click()
        self.driver.find_element(By.XPATH,self.drp_subscription_xpath).click()
        self.driver.find_element(By.XPATH,self.mem_subscription_xpath).click()
        self.driver.find_element(By.XPATH,self.subscription_amt_xpath).send_keys(subscription_amount)
        self.driver.find_element(By.XPATH,self.drp_currency_xpath).click()
        self.driver.find_element(By.XPATH,self.mem_currency_xpath).click()
        self.driver.find_element(By.XPATH,self.sub_commence_date_xpath).send_keys(commence_date)
        self.driver.find_element(By.XPATH,self.sub_renewal_date_xpath).send_keys(renewal_date)
        self.driver.find_element(By.XPATH,self.membership_save_xpath).click()
        time.sleep(3)
    admin_btn_xpath = "//span[normalize-space()='Admin']"
    user_add_btn_xpath = "//button[normalize-space()='Add']"
    drp_user_xpath = "//div[1]/div/div[2]/div/div/div[@class='oxd-select-text-input']"
    user_drp_select_xpath = "//*[contains(text(),'Admin')]"
    emp_name_xpath = "//input[@placeholder='Type for hints...']"
    emp_select_xpath = "//div[1]/div/div[2]/div/div[2]/div/div"
    obj = "//*[contains(text(),'pradeep')]"
    drp_status_xpath = "//div[1]/div/div[3]//div/div[@class='oxd-select-text-input']"
    drp_ena_xpath = "//*[contains(text(),'Enabled')]"
    user_name_xpath = "//div[4]//div[2]/input[@class='oxd-input oxd-input--active']"
    password_xpath = "//div[1]/div/div[2]/input[@class='oxd-input oxd-input--active']"
    conf_password_xpath = "//div[2]/div/div[2]/input[@class='oxd-input oxd-input--active']"
    save_xpath = "//*[normalize-space()='Save']"
    user_name_txt_xpath = "//div[1]/div/div[2]//input[@class='oxd-input oxd-input--active']"
    save_txt_xpath = "//button[normalize-space()='Search']"
    def add_user(self,emp_name,user_name,pass_word,conf_pass,add_username):
        time.sleep(4)
        self.driver.find_element(By.XPATH, self.admin_btn_xpath).click()
        self.driver.find_element(By.XPATH, self.user_add_btn_xpath).click()
        self.driver.find_element(By.XPATH,self.drp_user_xpath).click()
        self.driver.find_element(By.XPATH,self.user_drp_select_xpath).click()
        self.driver.find_element(By.XPATH,self.emp_name_xpath).send_keys(emp_name)
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.obj).click()
        self.driver.find_element(By.XPATH,self.drp_status_xpath).click()
        self.driver.find_element(By.XPATH,self.drp_ena_xpath).click()
        self.driver.find_element(By.XPATH,self.user_name_xpath).send_keys(user_name)
        self.driver.find_element(By.XPATH,self.password_xpath).send_keys(pass_word)
        self.driver.find_element(By.XPATH,self.conf_password_xpath).send_keys(conf_pass)
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.save_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.user_name_txt_xpath).send_keys(add_username)
        self.driver.find_element(By.XPATH,self.save_txt_xpath).click()
        time.sleep(5)

    k = "//div[@class='oxd-table-card']//div//div[2]"
    def check_customer_added(self):
        return self.driver.find_element(By.XPATH,self.k).text
    click_btn_xpath = "//i/preceding::p"
    logout_btn_xpath = "//a[text()='Logout']"
    def logout(self):
        self.driver.find_element(By.XPATH,self.click_btn_xpath).click()
        self.driver.find_element(By.XPATH,self.logout_btn_xpath).click()
