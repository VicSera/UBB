import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {AuthorDTO} from '../dto/authorDTO';
import {tap} from 'rxjs/operators';
import {DocumentDTO} from '../dto/documentDTO';
import {MovieDTO} from '../dto/movieDTO';

@Injectable({
  providedIn: 'root'
})
export class Service {
  private apiUrl = 'http://localhost:8080/api';
  private _cachedAuthor: AuthorDTO | undefined = undefined;

  constructor(private http: HttpClient) { }

  logIn(username: string) {
    return this.http.post<AuthorDTO>(this.apiUrl + '/authors/login', username).pipe(
      tap(author => this._cachedAuthor = author)
    );
  }

  getDocuments(authorId: number) {
    return this.http.get<DocumentDTO[]>(this.apiUrl + '/authors/get-documents/' + authorId.toString());
  }

  getMovies(authorId: number) {
    return this.http.get<MovieDTO[]>(this.apiUrl + '/authors/get-movies/' + authorId.toString());
  }

  get cachedAuthor() {
    return this._cachedAuthor;
  }
}
