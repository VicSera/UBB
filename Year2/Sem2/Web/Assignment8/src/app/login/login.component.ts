import {Component, OnDestroy, OnInit} from '@angular/core';
import {AuthenticationService} from '../service/authentication.service';
import {Subscription} from 'rxjs';
import {Router} from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit, OnDestroy {
  username: string;
  password: string;

  private sub: Subscription;

  constructor(
    private authenticationService: AuthenticationService,
    private router: Router
  ) { }

  ngOnInit(): void {
  }

  login(): void {
    this.sub = this.authenticationService.requestLogin(this.username, this.password)
      .subscribe(userDTO => {
        this.authenticationService.storeUser(userDTO);
        this.router.navigate([userDTO.isTeacher === '1' ? 'teacher' : 'student']);
      }, _ => {
        alert('Bad credentials');
      });
  }

  ngOnDestroy(): void {
    this.sub.unsubscribe();
  }
}
