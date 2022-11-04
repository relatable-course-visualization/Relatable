## Database Purpose

Store University of Saskatchewan courses, defining prerequisite and dependency relationships to corresponding sets of courses.

## Datapoints

### Relevant Links:

- University of Saskatchewan Course Catalogue (all courses): [https://catalogue.usask.ca/](https://catalogue.usask.ca/)

### Course

- Course code
  - e.g., CMPT 370
  - The structure consists of a of a two-four letter String, a space, and an integer code
    - Because of the initial String, this datapoint can be represented as a String
  - The decimal point and following numbers may be ignored (e.g., the ".3" in CMPT 370.3 can be ignored)
- Name
  - e.g., Intermediate Software Engineering
  - Can be represented as a String
- Description
  - e.g., Principles and techniques for developing software combined with the practical experience of creating a mid-size software system as a member of a software development team. Includes: teamwork; projects, planning and process; users and requirements; use cases; modeling; quality; software architecture; testing; GUI design, design principles, patterns and implementation; ethics; professionalism.
  - Can be represented as a String
- Prerequisite(s)
  - e.g., CMPT 280
  - Must be consistent with the Course Code datapoint
- Restriction(s)
  - e.g., Restricted to students in Applied Computing.
  - Can be represented as a String
- Hyperlink
  - e.g., [https://catalogue.usask.ca/CMPT-370](https://catalogue.usask.ca/CMPT-370)
  - Can be represented as a String
- Number of credits
  - e.g., 3
  - This can be derived from the original course code (e.g., the ".3" in CMPT 370.3 represents three credits)

## Prerequisite Theory

Let C = the set of all courses. Let P be the set of all prerequisites. Given a course c ∈ C, define p ∈ P recursively as a set representing the prerequisites of c st it holds one of the following forms ∀p<sub>1</sub>, ..., p<sub>n</sub> ∈ P, ∀c<sub>i</sub> ∈ C:

- p = Ø
- p = c<sub>i</sub>
- p = {p<sub>1</sub>, ..., p<sub>n</sub>}
- p = p<sub>1</sub> v ... v p<sub>n</sub>

Note, form four follows the conventional definition of v (that is, an inclusive disjunction).

## MySQL Tables

For each table, the first row is the fields and the second is an example record. Datatypes and incrementation are included for specificity.

### Course Table

Perhaps unintuitively, there is no column for a foreign key to a prerequisite record. While I tried this method--storing an entry for a prerequisite in the prerequite table corresponding to each course--initially, it could not handle the relational complexity of the prerequisite definition above. Thus, I have configured a more abtrast solution; you can see it defined in writing and in the tables for the prerequisite table below.

Primary key: id

| id : INT , AUTO_INCREMENT | course_code : VARCHAR(10) | name : VARCHAR(255)                 | description : TEXT                                                                                                                                                                                                                                                                                                                                                                                           | restrictions : TEXT                            | hyperlink : VARCHAR(255)            | num_credits : INT |
| ------------------------- | ------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------- | ----------------------------------- | ----------------- |
| 5                         | "CMPT 370"                | "Intermediate Software Engineering" | "Principles and techniques for developing software combined with the practical experience of creating a mid-size software system as a member of a software development team. Includes: teamwork; projects, planning and process; users and requirements; use cases; modeling; quality; software architecture; testing; GUI design, design principles, patterns and implementation; ethics; professionalism." | "Restricted to students in Applied Computing." | https://catalogue.usask.ca/CMPT-370 | 3                 |

![ERR for course table](course_table.png)

### Prerequisite Table

Primary key: id

Foreign keys

- course_id
- course_id_prereq

| id : INT , AUTO_INCREMENT | course_id : INT | disjunction_variable : CHAR(1) | course_id_prereq : INT |
| ------------------------- | --------------- | ------------------------------ | ---------------------- |
|                           |                 |                                |                        |
