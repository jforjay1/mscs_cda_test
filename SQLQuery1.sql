CREATE DATABASE STUDENT;

USE STUDENT;

CREATE TABLE STUDENT_1NF (Student_ID INT, Student_Name VARCHAR(20),Phone VARCHAR(15),Course VARCHAR(20),Points FLOAT);

INSERT INTO STUDENT_1NF(Student_ID,Student_Name,Phone,Course,Points)
		VALUES
		(00012,'Jhon Smith','902-5556','Mathematics',86),
		(00014,'Raj Sharma','902-8589','Mathematics',75),
		(00016,'Anan Obi','902-8974','Mathematics',96),
		(00016,'Anan Obi','902-8974','Mathematics',97),
		(00015,'Lee Wang','902-7845','Physics',92),
		(00015,'Lee Wang','902-7845','Physics',65),
		(00012,'Jhon Smith','902-5556','Physics',63),
		(00016,'Anan Obi','902-8974','Physics',58),
		(00014,'Raj Sharma','902-8589','Physics',78),
		(00014,'Raj Sharma','902-8589','Chemistry',83),
		(00015,'Lee Wang','902-7845','Chemistry',65),
		(00012,'Jhon Smith','902-5556','Chemistry',95),
		(00012,'Jhon Smith','902-5556','Chemistry',90);


SELECT * FROM STUDENT_1NF;

CREATE TABLE STUDENT_DATA(
					Student_ID INT PRIMARY KEY NOT NULL,
					Student_Name VARCHAR(20),
					Phone VARCHAR(15));

INSERT INTO STUDENT_DATA(Student_ID,Student_Name,Phone) SELECT DISTINCT Student_ID,Student_Name,Phone FROM STUDENT_1NF;

SELECT * FROM STUDENT_DATA;

CREATE TABLE STUDENT_SCORE(
				Student_ID INT,
				Course VARCHAR(20),
				Attempt_ID INT,
				Points FLOAT,
				FOREIGN KEY (Student_ID) REFERENCES STUDENT_DATA(Student_ID));

INSERT INTO STUDENT_SCORE(Student_ID,Course,Attempt_ID,Points) SELECT DISTINCT Student_ID,Course,row_number() over (partition by Student_ID,Course order by Student_ID),Points FROM STUDENT_1NF;

SELECT * FROM STUDENT_SCORE;

SELECT STUDENT_DATA.Student_Name AS 'name',SUBSTRING(STUDENT_SCORE.Course,1,4) as 'course', CAST(AVG(STUDENT_SCORE.Points) AS DECIMAL(10,5)) AS 'avg (points)' 
		FROM STUDENT_SCORE INNER JOIN STUDENT_DATA ON STUDENT_SCORE.Student_ID=STUDENT_DATA.Student_ID 
		GROUP BY STUDENT_DATA.Student_Name,STUDENT_SCORE.Course
		ORDER BY STUDENT_DATA.Student_Name,CASE course
											WHEN 'Mathematics' THEN 1
											WHEN 'Physics' THEN 2
											WHEN 'Chemistry' THEN 3
											ELSE 0
											END;