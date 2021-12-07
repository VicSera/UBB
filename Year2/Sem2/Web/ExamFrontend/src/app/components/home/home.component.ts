import { Component, OnInit } from '@angular/core';
import {Service} from '../../service/service';
import {AuthorDTO} from '../../dto/authorDTO';
import {MovieDTO} from '../../dto/movieDTO';
import {DocumentDTO} from '../../dto/documentDTO';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  public author: AuthorDTO | undefined;
  public listElems: any[] = [];

  constructor(private service: Service) {
  }

  ngOnInit(): void {
    this.author = this.service.cachedAuthor;

    let movies: MovieDTO[] = [];
    this.service.getMovies(this.author!!.id).subscribe(
      result => movies = result
    )
    let documents: DocumentDTO[] = [];
    this.service.getDocuments(this.author!!.id).subscribe(
      result => documents = result
    )

    this.listElems = HomeComponent.interleave(movies, documents);
  }

  private static interleave(a: any[], b: any[]) {
    const length = Math.max(a.length, b.length);
    const result = []
    for (var i = 0; i < length; ++i) {
      if (i < a.length)
        result.push(a[i]);
      if (i < b.length)
        result.push(b[i]);
    }
    return result;
  }

  isDocument(elem: any) {
    return elem.hasOwnProperty('contents');
  }
}
