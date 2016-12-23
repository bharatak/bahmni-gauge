Registration
=============

Create a new patient with Auto generated id, search by name & validate patient details
--------------------------------------------------------------------------------------

Tags: regression, sanity

* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_ANOTHER_LOCATION"
* Click on registration app
* Click on create new patient link
* Create the following patient
    |prefix|firstName|lastName|gender|dateOfBirth|age|district|village|
    |GAN|Maria|Jones|Female|20/01/2011|50|Bilaspur|Kahnapur|

* Click on search patient link
* Search previously created patient with name
* Verify previous patient is listed in search result
* Click on previous patient link from search results
* Verify patient details
* Logout the user



Login with the user which have only Registration role assigned and register a new user
--------------------------------------------------------------------------------------------

Tags: regression, sanity

* On the login page
* Login with user "regone" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "Registration Desk"
* Verify only the following app is available
    |Application-ID(tagName)|
    |Registration|
* Click on registration app
* Click on create new patient link
* Create the following patient
    |prefix|firstName|lastName|gender|dateOfBirth|age|district|village|
    |GAN|Maria|Jones|Female|20/01/2011|50|Bilaspur|Kahnapur|
* Start a visit "OPD"
* Enter visit details from table
    |height|weight|fees|comments|
    |50|5|100|bmi observations seems normal|
* Verify the details on "bmi" display control
    |details|
    |HEIGHT50|
    |WEIGHT5|
    |BMI20|
    |BMI STATUSNormal|




Verify the patient creation fails for duplicated id
----------------------------------------------------

Tags: regression, sanity

* Create a new patient through API
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_ANOTHER_LOCATION"
* Click on registration app
* Click on create new patient link
* Try creating patient with same identifier
    |prefix|firstName|lastName|gender|dateOfBirth|age|district|
    |GAN|DevKumar|Karia|Male|20/01/2011|50|Bilaspur|

* Verify Identifier Error popup with message "'Patient#null' failed to validate with reason: Identifier %s already in use by another patient" is displayed
* Logout the user

Update patient, Search by gram panchayat, fetch & validate patient details
--------------------------------------------------------------------------

Tags: regression, sanity

* Create the following patient using api
    |prefix|firstName|lastName|gender|dateOfBirth|district|gramPanchayat|
    |GAN|Hanah|Jones|F|20/01/2011|Bilaspur|Narnia|

* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_ANOTHER_LOCATION"
* Click on registration app
* Search previously created patient with exact identifier
* Edit previous patient details as follow
    |prefix|firstName|lastName|gender|dateOfBirth|age|district|gramPanchayat|
    |GAN|Maria|Karia|Female|20/01/2011|50|Dispur|Brindavan|
* Click on search patient link
* Search previously created patient with gram panchayat
* Verify previous patient is listed in search result
* Click on previous patient link from search results
* Verify patient details
* Logout the user

Verify BMI display control verification
---------------------------------------
Tags: regression, sanity
* Create a new patient through API
* On the login page 
* Login to the application
* Click on registration app
* Search previously created patient with exact identifier
* Start a visit "OPD"
* Enter visit details from table
    |height|weight|fees|comments|
    |50|5|100|bmi observations seems normal|
* Verify the details on "bmi" display control
    |details|
    |HEIGHT50|
    |WEIGHT5|
    |BMI20|
    |BMI STATUSNormal|
* Enter visit details from table
    |height|weight|fees|
    |50|1|100|
* Verify the details on "bmi" display control
    |details|
    |HEIGHT50|
    |WEIGHT1|
    |BMI4|
    |BMI STATUSVery Severely Underweight|

Closing visit for an admitted patient displays error message
-------------------------------------------------------------
Tags: regression, sanity

* Create and admit a patient through API 
* On the login page 
* Login to the application
* Click on registration app
 * Search previously created patient with exact identifier 
* Enter Visit Details for Admitted Patient
 * Try close visit
 * Verify Error popup with message "Admitted patient's visit cannot be closed. Discharge the patient and try again" is displayed
 * Discharge the patient through api 
* Close visit  
* Search previously created patient with exact identifier
   * Verify "Start OPD visit" button is "displayed" 
* Navigate to dashboard 
* Click on inpatient app 
* Select existing patient from patient listing page under tab "All" 
* Verify only "Admit Patient" option is displayed in Patient Movement  
* Navigate to dashboard  
* Logout the user
