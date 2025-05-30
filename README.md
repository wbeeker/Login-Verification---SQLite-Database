# Login-Verification---SQLite-Database
This username/password login verification checks credentials against an SQLite database and uses scrypt to secure passwords and salts.

Starting the program should prompt this login window:

<img width="386" alt="Image" src="https://github.com/user-attachments/assets/a8869883-411f-4843-91e9-cbea936f6621" />


If the user attempts to login without first creating an account:

<img width="385" alt="Image" src="https://github.com/user-attachments/assets/6bfe289b-e901-4e14-bc4e-81018c5216b3" />


The user will see a failed login window:

<img width="253" alt="Image" src="https://github.com/user-attachments/assets/5e4fe8a6-227f-4055-aedf-b56b7d79e234" />


The user can select Creat Account and fill in the boxes below:

<img width="396" alt="Image" src="https://github.com/user-attachments/assets/ff9afb8d-9c15-4d3a-a441-6379db3b1445" />

<img width="398" alt="Image" src="https://github.com/user-attachments/assets/f898bfcd-0120-4e79-b0f7-902d61196ab5" />


If the account is created successfully, the user will see this window:

<img width="254" alt="Image" src="https://github.com/user-attachments/assets/2861fea0-c47e-4d9c-b4ec-3bf781c19e3b" />


The user can now use their credentials to log in:

<img width="385" alt="Image" src="https://github.com/user-attachments/assets/6bfe289b-e901-4e14-bc4e-81018c5216b3" />


If they enter their credentials correctly, they will see a successful login window:

<img width="251" alt="Image" src="https://github.com/user-attachments/assets/af12cfb3-d93f-401b-b0dc-e39a3db16168" />


Their credentials will be stored in an SQLite3 database, with passwords and salt hashed with scrypt:

![Image](https://github.com/user-attachments/assets/c5b814c5-b70e-4f8b-838e-84e24f2d03af)
![Image](https://github.com/user-attachments/assets/49c59234-f60c-47ff-8e18-5b2635c72a92)


Here is the full 128-digit hashed password:

![Image](https://github.com/user-attachments/assets/c212c421-dfff-44bd-b397-497ca166eb47)


And here is the full 32-digit hashed salt:

![Image](https://github.com/user-attachments/assets/52aa2256-781a-4817-8d77-efebd0526d29)

