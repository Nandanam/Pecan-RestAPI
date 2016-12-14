# RestAPI
This is Rest client and server application using pecan framework.The google postman acts as a client.

Steps to run the program:
1)  Go to pecan-env directory
2)  source bin/activate (To start the pecan environment)
3)  go to test_project directory
4)  pecan serve config.py (To start the server)
5)  At client side (postman) choose operations like Get,Put,Post and delete
6)  In the address bar for PUT in student table http://127.0.0.1:8080/univ/register?sid= &sname= &email= &age= &sex= &semister= to request the server.
7)  For GET from student http://127.0.0.1:8080/univ/give_details?sid=
8)  For DELETE in student http://127.0.0.1:8080/univ/update_details?sid=
