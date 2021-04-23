import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';
import {UserDTO} from '../dto/user-dto';
import {HttpClient} from '@angular/common/http';
import {environment} from '../../environments/environment';
import {Router} from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  constructor(
    private http: HttpClient,
    private router: Router) { }

  requestLogin(username: string, password: string): Observable<UserDTO> {
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    return this.http.post<UserDTO>(environment.apiUrl + 'login.php', formData);
  }

  storeUser(userDTO: UserDTO): void {
    sessionStorage.setItem('userJson', JSON.stringify(userDTO));
  }

  loadUser(): UserDTO {
    return JSON.parse(sessionStorage.getItem('userJson'));
  }

  logout(): void {
    this.router.navigate(['login']);
  }
}
