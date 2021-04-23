import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';

import {AppComponent} from './app.component';
import {HttpClientModule} from '@angular/common/http';
import {AppRoutingModule} from './app-routing.module';
import {RouterModule} from '@angular/router';
import { LoginComponent } from './login/login.component';
import {AuthenticationService} from './service/authentication.service';
import {CrudService} from './service/crud.service';
import {FormsModule} from '@angular/forms';
import { StudentComponent } from './student/student.component';
import { TeacherComponent } from './teacher/teacher.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    StudentComponent,
    TeacherComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    RouterModule,
    FormsModule
  ],
  providers: [AuthenticationService, CrudService],
  bootstrap: [AppComponent]
})
export class AppModule {
}
