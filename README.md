-->Language and Framework: Python and Django

-->Database: pgAdmin 4

-->SQL: postgresql

-->Frontend Languages: HTML, CSS, Javascript

-->Deployment : Railway

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

FormSerializer is created with the required fields to fetch the complex data and convert to json format and finally rendered into the database in the original format. Views 
are used for processing the data. It defines the POST request.

Example of the Serializer and API:

![Screenshot from 2022-12-14 03-38-22](https://user-images.githubusercontent.com/71372587/207455071-2e17be2a-be75-452a-af06-d4f4b8c5d3b0.png)

![Screenshot from 2022-12-14 03-38-30](https://user-images.githubusercontent.com/71372587/207455101-23751842-2550-47de-971a-7d5c671d8ef5.png)

4. API Testing with Postman

![Screenshot from 2022-12-14 03-44-18](https://user-images.githubusercontent.com/71372587/207456124-395f849e-fb05-402e-a8b2-e741c83f9d7e.png)

5. Creating forms for frontend:

![Screenshot from 2022-12-14 03-50-48](https://user-images.githubusercontent.com/71372587/207457909-4cdde75b-ebd0-4708-a079-a059f7984b7b.png)

![Screenshot from 2022-12-14 03-50-51](https://user-images.githubusercontent.com/71372587/207457939-20d26b06-473c-4bc2-888d-ca71946a3fe5.png)

Form Validation

![Screenshot from 2022-12-14 03-51-03](https://user-images.githubusercontent.com/71372587/207457998-f95c7a38-7ed8-4301-a1a5-9418494b6a26.png)

![Screenshot from 2022-12-14 03-51-21](https://user-images.githubusercontent.com/71372587/207458018-ed338bd5-8c36-4a9b-9d0e-aa032995331f.png)

![Screenshot from 2022-12-14 03-52-19](https://user-images.githubusercontent.com/71372587/207458090-b980997b-5340-4274-87f5-95076ced25fe.png)

![Screenshot from 2022-12-14 03-52-30](https://user-images.githubusercontent.com/71372587/207458109-e7af791d-d03b-49e4-b1b7-05da1bcff383.png)

![Screenshot from 2022-12-14 03-52-43](https://user-images.githubusercontent.com/71372587/207458176-b8be0a84-c586-44f4-8cfd-ea4ea94293d7.png)

6. The idea here is to register the user and send the payment link in mail so that user can pay the amount within 30 days and also the admission is
confirmed after the completion of payment. 

Assumption: Here the complete payment is stubbed function and it is always set to true. Hence all the registered users are admitted. The user registering 
for next month is registered again for that month. 

Email is sent to the user using Django send_mail and Sendgrid API:

![Screenshot from 2022-12-14 04-02-42](https://user-images.githubusercontent.com/71372587/207459643-76f2bcaf-13d4-404c-985c-156356b0a3d6.png)

![Screenshot from 2022-12-14 04-01-44](https://user-images.githubusercontent.com/71372587/207459534-72534894-f17f-43bf-8eb6-9114e7658eaa.png)

7. On clicking the link sent in mail:

HTTP Response 'Payment Successful' is generated.

![Screenshot from 2022-12-14 04-12-35](https://user-images.githubusercontent.com/71372587/207460805-89ed2bf8-7a65-49c2-8a50-40011c94853f.png)

8. User Data is successfully stored in database:

![userTableData](https://user-images.githubusercontent.com/71372587/207460365-ee2b10dc-3b8e-423e-ae38-a98f11351ea5.png)

![paymentTableData](https://user-images.githubusercontent.com/71372587/207460391-f525a021-39bf-4a4b-acc1-bd21282247cd.png)

![batchTableData](https://user-images.githubusercontent.com/71372587/207462217-e5624d5b-b68f-4e4b-9560-93027c520e13.png)

![admissionTableData](https://user-images.githubusercontent.com/71372587/207462233-5bcadde7-482b-4a02-90a2-6b0ba5cf7aac.png)

Assumption:

The complete payment function is a stubbed function. Right now the complete payment is always true and all the users are admitted. Complete payment should keep the track of link sent in mail and only if the user pays the amount, the user's admission is confirmed else the user details should not be added to admission.

Have a look at the demonstration of the Project: https://drive.google.com/drive/folders/1Cj-d0DuSZa7FcayrDO30TYk5yg6oT-cL?usp=share_link
