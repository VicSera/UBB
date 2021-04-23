import {Component, OnDestroy, OnInit} from '@angular/core';
import {AuthenticationService} from '../service/authentication.service';
import {CourseGradeDTO} from '../dto/course-grade-dto';
import {CrudService} from '../service/crud.service';
import {Subscription} from 'rxjs';

@Component({
  selector: 'app-student',
  templateUrl: './student.component.html',
  styleUrls: ['./student.component.css']
})
export class StudentComponent implements OnInit, OnDestroy {
  courseGradeDTOs: CourseGradeDTO[] = [];

  private sub: Subscription;

  constructor(
    public authenticationService: AuthenticationService,
    private crudService: CrudService) { }

  ngOnInit(): void {
    this.sub = this.crudService.getGrades(this.authenticationService.loadUser().id).subscribe(
      courseGradeDTOs => {
        this.courseGradeDTOs = courseGradeDTOs;
      }
    );
  }

  ngOnDestroy(): void {
    this.sub.unsubscribe();
  }

}
