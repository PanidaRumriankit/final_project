# Final project for 2023's 219114/115 Programming I
* Files
  - database.py
      database class and table class
  - project_manage.py
      
  - persons.csv
      Collect persons information
  - project.csv
      Collect project information
  - login.csv
      each persons login information
  - advisor_pending_table.csv
      an inviting to be an advisor table
  - member_pending_request.csv
      an inviting to be a member table
* How to run the program ?
  - click run, input your username and password
      * if you are an admin
          you can update the tables by editing a dictionary in a list using key that generate in initializing step
      * if you are a student
          you can choose to see a pending project or create a project
          - see a pending project
              you can see apending project one by one and answer to them, 'yes' or 'no'
          - create a project
              you can create a project and give it a name, then send the member request to other student
      * if you are a member
          you can see all your project information and modify(change its name)
      * if you are a lead
          you can see all your project information, modify(change its name or submit), and send the member requests
      * if you are a faculty
          you can see all projects information, see a pending project, evaluate project after the advisor evaluated it (give a comment or send to advisor to approve it)
      * if you are an advisor
          you can evaluate (give a comment or send to faculty to evaluate it after you think it's good enough), approve it so the project finish after this step
        
| Role   |  Action                    | Method  | Class  | Completion percentage  |
|--------|----------------------------|---------|--------|------------------------|
|Admin   |editing a dictionary by keys|    -    |   -    |         100%           |
|Student |see pending project         |    -    |   -    |         100%           |
|Student |response a pending project  |    -    |   -    |         100%           |
|Student |create a project            |    -    |   -    |         100%           |
|Member  |see the project information |    -    |   -    |         100%           |
|Member  |change project's name       |    -    |   -    |         100%           |
|Lead    |see the project information |    -    |   -    |         100%           |
|Lead    |change project's name       |    -    |   -    |         100%           |
|Lead    |send the request to students|    -    |   -    |         100%           |
|Faculty |see the project information |    -    |   -    |         100%           |
|Faculty |response a pending project  |    -    |   -    |          50%           |
|Faculty |evaluate a project          |    -    |   -    |         100%           |
|Advisor |evaluate a project          |    -    |   -    |         100%           |
|Advisor |approve a project           |    -    |   -    |         100%           |

* Bugs: 
  a faculty does not updates after response 'no'
