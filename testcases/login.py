from pageobjects.loginpage import login
from utilities import customlogger
class Test_1:
    baseurl = "https:/opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"
    firstname = "pradeep"
    lastname = "G"
    emp_name = "pradeep"
    user_name = "pradeep"
    pass_word = "17Bco836bala@"
    conf_pass = "17Bco836bala@"
    user_name_txt_xpath = "pradeep"
    newusername = "pradeep"
    newpassword = "17Bco836bala@"
    otherid = 1253235
    driverlicnum = 63763352
    licexpdate = "2030-10-23"
    ssn = 34354
    sin = 56355
    dob = "1999-10-15"
    military_Service = "no"
    street1 = "Ts"
    street2 = "colony"
    city = "palladam"
    state = "tiruppur"
    pin = 641658
    home = 264241
    mobile = 9756786383
    work = 8072750266
    work_email = "hkl7p@gmail.com"
    other_email = "hk8kogj@gmail.com"
    name = "ram"
    relationship = "friend"
    emc_mobile = 9875859933
    dep_name = "surya"
    dep_dob = "2010-05-4"
    number = 9784442
    issued_date = "2022-09-13"
    expiry_date = "2025-09-18"
    eligible_status = "yes"
    eligible_review_date = "2022-09-29"
    commands = "immigration"
    join_date = "2022-09-21"
    salcomponent = "hike"
    amount1 = 40000
    comments = "this is my ssl"
    acountno = 123456789743
    routingno = 564
    amount2 = 40000
    federal_income_tax = 10
    state_income_tax = 14
    supervisors_name = "Peter"
    subordinate_name = "Paul"
    company = "tcs"
    jobtitle = "PA"
    fromdate = "2015-10-3"
    todate = "2022-08-23"
    qulcomments = "job"
    institute = "krishna clg"
    major = "bcom"
    year = 3
    gpa = 80
    startdate = "2017-09-14"
    enddate = "2020-09-23"
    yearofexp = 5
    sklcomments = "python selenium"
    langu_save_xpath = "english"
    licenseno = 3749849
    issueddate = "2010-09-16"
    expirydate = "2030-09-16"
    subscription_amount = 250
    commence_date = "2022-09-13"
    renewal_date = "2022-10-13"
    logger = customlogger.test_logDemo()

    def test_user_login(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(20)
        loginPageObj = login(self.driver)
        loginPageObj.setlogin(self.username,self.password)
        self.logger.info("***************** Login successful *****************")
        loginPageObj.pim(self.firstname,self.lastname)
        self.logger.info("***************** Add New Customer *****************")
        loginPageObj.personal(self.otherid,self.driverlicnum,self.licexpdate,self.ssn,self.sin,self.dob,self.military_Service)
        self.logger.info("***************** Adding personal details *****************")
        self.driver.execute_script("window.scrollBy(0,-2000)", "")
        loginPageObj.contect_detail(self.street1,self.street2,self.city,self.state,self.pin,self.home,self.mobile,self.work,self.work_email,self.other_email)
        self.logger.info("***************** Adding contect details *****************")
        loginPageObj.emergency_contact(self.name,self.relationship,self.emc_mobile)
        self.logger.info("***************** Adding emergency contect details *****************")
        loginPageObj.dependent(self.dep_name,self.dep_dob)
        self.logger.info("***************** Adding dependent details *****************")
        loginPageObj.immigration(self.number,self.issued_date,self.expiry_date,self.eligible_status,self.eligible_review_date,self.commands)
        self.logger.info("***************** Adding immigration details *****************")
        loginPageObj.job(self.join_date)
        self.logger.info("***************** Adding job details *****************")
        loginPageObj.salary_details(self.salcomponent, self.amount1, self.comments, self.acountno, self.routingno,self.amount2)
        self.logger.info("***************** Adding salary details *****************")
        loginPageObj.tax(self.federal_income_tax,self.state_income_tax)
        self.logger.info("***************** Adding tax details *****************")
        loginPageObj.report(self.supervisors_name,self.subordinate_name)
        self.logger.info("***************** Adding report details *****************")
        loginPageObj.qualification_wrk_experience(self.company,self.jobtitle,self.fromdate,self.todate,self.qulcomments)
        self.logger.info("***************** Adding qualification work experience details *****************")
        loginPageObj.qualification_education(self.institute,self.major,self.year,self.gpa,self.startdate,self.enddate)
        self.logger.info("***************** Adding education details *****************")
        loginPageObj.qualification_skills(self.yearofexp,self.sklcomments)
        self.logger.info("***************** Adding skills details *****************")
        loginPageObj.qualification_language(self.langu_save_xpath)
        self.logger.info("***************** Adding language details *****************")
        loginPageObj.qualification_license(self.licenseno,self.issueddate,self.expirydate)
        self.logger.info("***************** Adding license details *****************")
        self.driver.execute_script("window.scrollBy(0,-1000)", "")
        loginPageObj.memberships(self.subscription_amount,self.commence_date,self.renewal_date)
        self.logger.info("***************** Adding Memberships details *****************")
        loginPageObj.add_user(self.emp_name,self.user_name,self.pass_word,self.conf_pass,self.user_name_txt_xpath)
        self.logger.info("***************** Adding add new user details *****************")
        username = loginPageObj.check_customer_added()
        print(username)
        if username == "pradeep":
            self.logger.info("***************** customer successfully added *****************")
            assert True
        else:
            self.logger.info("***************** customer not added *****************")
            assert False
        self.logger.info("***************** logout from old customer *****************")
        loginPageObj.logout()

        self.logger.info("***************** Login new customer *****************")

        newloginPageObj = login(self.driver)
        newloginPageObj.setlogin(self.newusername, self.newpassword)
        self.logger.info("***************** successfully login new customer *****************")
