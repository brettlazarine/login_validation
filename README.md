# *login_validation*
### This CLI Python program does as it says, **validates logins**:
- Verifies email format by putting the *email-validator* library to work
- Verifies password complexity by checking for a number of different requirements
- Allows users to register their email and password, so long as their email isn't already in the database
- The database queries are parameterized to prevent SQL injection
- Circular control flow in the CLI, allowing the user to register and login in the same interaction
 
### The parts
- All code was written with VSCode in a Linux subsystem on a Windows machine
- The database was created and hosted by a local SQL Server instance on Windows
  - The connection was routed using the machine's IP to be accessible in the Linux subsystem

### How to run after cloning
- Ensure you have python
  - python3 --version
- Install if not
  - sudo apt update
  - sudo apt install python3
  - sudo apt install python3-pip (optional but will help with the other installs)
- Configure appsettings.json in the root of the directory for SQL Server
  - { "database": { "connectionString": "DRIVER={(your driver here)};SERVER=(your server here);DATABASE=(your db here);UID=(your db username);PWD=(your db password); } }
    - Because I used a Linux subsystem:
      - I had to use my machine's IP for Linux to reach the server
      - I created an inbound rule in Firewall
      - I enabled TCP/IP for SQL Server and configured for Port 1433
- Install email-validator
  - pip install email-validator
- Install pyodbc
  - sudo apt-get install python3-pyodbc
- If needed, install the ODBC driver for SQL Server:
  - sudo apt-get update
  - sudo apt-get install unixodbc-dev
  - curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
  - curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list
  - sudo apt-get update
  - sudo ACCEPT_EULA=Y apt-get install msodbcsql17
 

### Possible future extensions
- CRUD methods already written and function, can expand to allow for updating and deleting from the database
- Possibly add another table for data analytics
  - User count
  - Email domain info (how many different domains, most popular, least popular, etc.)
  - Input tracking
    - How often passwords fail complexity
    - How often users get their passwords wrong
