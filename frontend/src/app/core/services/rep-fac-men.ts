import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class RepFacMen {
  private baseUrl = environment.apiUrl + '/reportes/facturacion-mensual';

  constructor(private http: HttpClient) {}

  getFacMensual(): Observable<any[]> {
    const res$ = this.http.get<any[]>(this.baseUrl);
    res$.subscribe(data => console.log('Datos recibidos:', data));
    return res$;
  }
}
