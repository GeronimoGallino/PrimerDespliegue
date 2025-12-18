import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class RepAlqCliService {

  private baseUrl = environment.apiUrl + '/reportes/alquileres-por-cliente';

  constructor(private http: HttpClient) {}

  getByCliente(idCliente: number): Observable<any[]> {
    const res$ = this.http.get<any[]>(`${this.baseUrl}/${idCliente}`);
    res$.subscribe(data => console.log('Datos recibidos:', data));
    return res$;
  }
}
