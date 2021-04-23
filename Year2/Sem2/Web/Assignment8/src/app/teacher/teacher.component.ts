import { Component, OnInit } from '@angular/core';
import {GroupDTO} from '../dto/group-dto';
import {CourseDTO} from '../dto/course-dto';
import {StudentGradeDTO} from '../dto/student-grade-dto';
import {Subscription} from 'rxjs';
import {CrudService} from '../service/crud.service';
import {AuthenticationService} from '../service/authentication.service';

@Component({
  selector: 'app-teacher',
  templateUrl: './teacher.component.html',
  styleUrls: ['./teacher.component.css']
})
export class TeacherComponent implements OnInit {

  startingIndex = 0;
  endingIndex = 3;
  studentsPerPage = 4;

  selectedGroup = 0;
  selectedCourse = 0;
  selectedCourseName = '';

  groups: GroupDTO[] = [];
  courses: CourseDTO[] = [];
  studentGrades: StudentGradeDTO[] = [];
  visibleStudentGrades: StudentGradeDTO[] = [];

  private subs: Subscription[] = [];

  constructor(
    private crudService: CrudService,
    private authenticationService: AuthenticationService) { }

  ngOnInit(): void {
    this.loadGroups();
    this.loadCourses();
  }

  loadGroups(): void {
    this.subs.push(this.crudService.getGroups().subscribe(groups => {
      this.groups = groups;
      this.selectGroup(groups[0].id);
    }));
  }

  loadCourses(): void {
    this.subs.push(this.crudService.getCourses(this.authenticationService.loadUser().id).subscribe(courses => {
      this.courses = courses;
      this.selectCourse(courses[0].id, courses[0].name);
    }));
  }

  selectGroup(groupId: number): void {
    this.selectedGroup = groupId;
    this.loadGrades();
  }

  selectCourse(courseId: number, courseName: string): void {
    this.selectedCourse = courseId;
    this.selectedCourseName = courseName;
    this.loadGrades();
  }

  loadGrades(): void {
    if (this.selectedCourse === null || this.selectedGroup === null) {
      return;
    }

    this.crudService.getCourseGroupGrades(this.selectedCourse, this.selectedGroup).subscribe(
      grades => {
        this.studentGrades = grades;

        this.startingIndex = 0;
        this.endingIndex = Math.min(this.startingIndex + 4, this.studentGrades.length) - 1;
        this.refreshVisibleStudentGrades();
      }
    );
  }

  prevStudentPage(): void {
    this.startingIndex -= this.studentsPerPage;
    this.endingIndex = Math.min(this.startingIndex + 4, this.studentGrades.length) - 1;

    this.refreshVisibleStudentGrades();
  }

  nextStudentPage(): void {
    this.startingIndex += this.studentsPerPage;
    this.endingIndex = Math.min(this.startingIndex + 4, this.studentGrades.length) - 1;

    this.refreshVisibleStudentGrades();
  }

  refreshVisibleStudentGrades(): void {
    this.visibleStudentGrades = [];
    for (let i = this.startingIndex; i <= this.endingIndex; ++i) {
      this.visibleStudentGrades.push(this.studentGrades[i]);
    }
  }

  getInputId(studentId: number): string {
    return 'addGrade' + studentId;
  }

  removeGrade(gradeId: number): void {
    this.subs.push(this.crudService.deleteGrade(gradeId).subscribe(() =>
      this.loadGrades()));
  }

  addGradeFieldSubmitted(studentId, courseId, inputFieldId): void {
    // @ts-ignore
    const grade = parseInt(document.getElementById(`${inputFieldId}`).value, 10);
    this.subs.push(this.crudService.addGrade(studentId, courseId, grade).subscribe(() =>
      this.loadGrades()));
  }
}
