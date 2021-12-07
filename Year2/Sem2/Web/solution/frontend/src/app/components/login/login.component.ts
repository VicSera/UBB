import { Component, OnInit } from '@angular/core';
import {Service} from '../../service/service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  public username = '';

  constructor(
    private service: Service,
    private router: Router
  ) { }

  ngOnInit(): void {
  }

  logIn() {
    this.service.logIn(this.username).subscribe(
      author => {
        alert('Welcome ' + author.name);
        this.router.navigate(['home'])
      },
      () => alert('Login failed')
    );
  }
}
