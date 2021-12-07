create database PracticalExam
go;

use PracticalExam;


create table Program (
    id int primary key,
    name varchar(255)
);

create table [Group] (
    id int primary key,
    name varchar(255),
    program_id int foreign key references Program(id)
);

create table Student (
    registration_number int primary key,
    name varchar(255),
    email varchar(255),
    group_id int foreign key references [Group] (id)
);

create table Assignment (
    id int primary key,
    description varchar(255),
    student_id int foreign key references Student(registration_number) on delete cascade,
    grade int
);

create table Comment (
    id int primary key,
    content varchar(255),
    assignment_id int foreign key references Assignment(id) on delete cascade
);
