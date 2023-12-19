**Tech Stack**

-->Language and Framework: Python and Django

-->Database: pgAdmin 4

-->SQL: postgresql

-->Frontend Languages: HTML, CSS, Javascript

**Project Architecture**

![Screenshot 2023-12-19 192244](https://github.com/VartikaB/Flexmoney_YogaForm/assets/81951781/a0be37a0-9de8-4646-a00c-a9647e56bbc4)

**Designing Database and ER Diagram:**


There are 4 tables: User, Batch, Payment, Admission. The basic information is saved in user table along with batch ids. 4 batches are given. Payment details for each user are stored in Payment Table. If the payment is successful the admission of the user is confirmed and stored in the admission tables.

Tables are as follows in postgres:

![user_table2](https://github.com/VartikaB/Flexmoney_YogaForm/assets/81951781/a41e95c4-67e1-49a5-9233-72efd5de50db)

![batch_table2](https://github.com/VartikaB/Flexmoney_YogaForm/assets/81951781/b5da6a20-3025-4153-8c4d-61e02e0655e0)

![payment_table2](https://github.com/VartikaB/Flexmoney_YogaForm/assets/81951781/937ccada-d93a-42e2-93cf-9ea9e478ad82)

![admission_table2](https://github.com/VartikaB/Flexmoney_YogaForm/assets/81951781/d610916d-9301-4f5d-81a5-42432ef8240e)

ER Diagram:

![er_dig](https://github.com/VartikaB/Flexmoney_YogaForm/assets/81951781/9da82d7c-9556-459c-8e32-3bec95bccd99)

2. Creating models:

Django models are created for the above mentioned tables and validation errors are raised.

3. Creating API:

FormSerializer facilitates data retrieval from complex fields, transforming it into JSON format, then storing it in the original database structure. Views manage data processing, primarily defining the POST request for seamless functionality.


4. API Testing with Postman

![postman](https://github.com/VartikaB/Flexmoney_YogaForm/assets/81951781/24e0861b-58dc-4fe0-81a8-90ef3eb70b72)

5. Frontend form

![frontend](https://github.com/VartikaB/Flexmoney_YogaForm/assets/81951781/3ec6c341-41cf-497c-ad50-436cf1bc58aa)

![frontend1](https://github.com/VartikaB/Flexmoney_YogaForm/assets/81951781/b3b2bfa5-9a1d-4ed3-a864-6439e02d0c18)

![Form2](https://github.com/VartikaB/Flexmoney_YogaForm/assets/81951781/6d722213-a37a-4e33-aaa7-6e4be0931313)


6. Response on Frontend 




**On adding valid credentials maintaing all criteria**

![Successful_form](https://github.com/VartikaB/Flexmoney_YogaForm/assets/81951781/31694b51-8348-4cf7-a317-d9499a939f51)

**If age is not in the critera**

![Screenshot (118)](https://github.com/VartikaB/Flexmoney_YogaForm/assets/81951781/a4fabc81-2b1f-4f46-ac89-ee6d228a234d)

**If conatct is not in the criteria**

![Screenshot (119)](https://github.com/VartikaB/Flexmoney_YogaForm/assets/81951781/d9937411-d30c-452e-a32c-c3936f8185e1)

**If the entry already exist**

![Screenshot (120)](https://github.com/VartikaB/Flexmoney_YogaForm/assets/81951781/88647516-d983-49d9-9f13-1d73a8ee74e2)

**If updation of batch is successful for registered user**

![Succ_Updation](https://github.com/VartikaB/Flexmoney_YogaForm/assets/81951781/0210aa99-f86a-43d3-a109-c84de9f7bb6f)




6. User Data is successfully stored in database:

![adm_table1](https://github.com/VartikaB/Flexmoney_YogaForm/assets/81951781/a0d55d93-f83e-424a-ab88-a53fdb1f3374)

![batch_table1](https://github.com/VartikaB/Flexmoney_YogaForm/assets/81951781/c4ff440a-3a0c-42cd-83f4-7ff75a6d1aad)

![payment_table1](https://github.com/VartikaB/Flexmoney_YogaForm/assets/81951781/b63adafd-2846-40f2-84b0-33cd8a505e6c)

![user_table1](https://github.com/VartikaB/Flexmoney_YogaForm/assets/81951781/eb3cf0e8-2ced-4657-b996-648dee71ebe0)

Assumption:

Data is currently added upon registration without payment validation. Enhancing this, user addition to the database will occur solely upon successful payment, ensuring a more robust process.


