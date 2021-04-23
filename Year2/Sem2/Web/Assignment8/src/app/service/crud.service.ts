import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {environment} from '../../environments/environment';
import {GroupDTO} from '../dto/group-dto';
import {Observable} from 'rxjs';
import {GradeDTO} from '../dto/grade-dto';
import {CourseGradeDTO} from '../dto/course-grade-dto';
import {CourseDTO} from '../dto/course-dto';
import {StudentGradeDTO} from '../dto/student-grade-dto';

@Injectable({
  providedIn: 'root'
})
export class CrudService {

  constructor(private http: HttpClient) { }

  addGrade(studentId: number, courseId: number, value: number): Observable<void> {
    const formData = new FormData();
    formData.append('studentId', studentId.toString());
    formData.append('courseId', courseId.toString());
    formData.append('value', value.toString());

    return this.http.post<void>(environment.apiUrl + 'addGrade.php', formData);
  }

  deleteGrade(gradeId: number): Observable<void> {
    const formData = new FormData();
    formData.append('gradeId', gradeId.toString());

    return this.http.post<void>(environment.apiUrl + 'deleteGrade.php', formData);
  }

  getCourseGroupGrades(courseId: number, groupId: number): Observable<StudentGradeDTO[]> {
    const formData = new FormData();
    formData.append('courseId', courseId.toString());
    formData.append('groupId', groupId.toString());

    return this.http.post<StudentGradeDTO[]>(environment.apiUrl + 'getCourseGroupGrades.php', formData);
  }

  getCourses(teacherId: number): Observable<CourseDTO[]> {
    const formData = new FormData();
    formData.append('teacherId', teacherId.toString());

    return this.http.post<CourseDTO[]>(environment.apiUrl + 'getCourses.php', formData);
  }

  getGrades(studentId: number): Observable<CourseGradeDTO[]> {
    const formData = new FormData();
    formData.append('studentId', studentId.toString());

    return this.http.post<CourseGradeDTO[]>(environment.apiUrl + 'getGrades.php', formData);
  }

  getGroups(): Observable<GroupDTO[]> {
    return this.http.post<GroupDTO[]>(environment.apiUrl + 'getGroups.php', {});
  }
}
