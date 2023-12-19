# Final project for 2023's 219114/115 Programming I
* Files
  - database.py
      database class and table class
  - project_manage.py
      main program
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
* How to run the program ? each question the program ask will have choices that we can choose
	- A student create a project, send invite request to be a member to other students. If other students accept, project information will be update. If the student in a group are 3 already, the project is ready to be submitted. if the project is submitted, the advisor will evaluate it then approve to the faculty. The faculty will evaluate the project as the last step, if there are no comment for improveing, the project satus will be 'finished'
  - click run, input your username and passwordelde
      * if you are an admin
          you can update the tables by editing a dictionary in a list using key that generate in initialization step
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
          you can see all projects information, see a pending project, evaluate project after the advisor approved it (give a comment or mark as finished)
      * if you are an advisor
          you can evaluate (give a comment or marked as 'evaluated'), approve it and give it to faculty to evaluate it
        
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
|Faculty |response a pending project  |    -    |   -    |         100%           |
|Faculty |evaluate a project          |    -    |   -    |         100%           |
|Advisor |evaluate a project          |    -    |   -    |         100%           |
|Advisor |approve a project           |    -    |   -    |         100%           |

* Bugs: 
  not have a big bug but some functions are hard to use
