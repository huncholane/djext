/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { logged_in } from '../models/logged_in';
import type { login } from '../models/login';
import type { logout } from '../models/logout';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class AuthService {

  /**
   * @returns logout 
   * @throws ApiError
   */
  public static retrieveLogout(): CancelablePromise<logout> {
    return __request(OpenAPI, {
      method: 'GET',
      url: '/api/auth/logout',
    });
  }

  /**
   * @returns logged_in 
   * @throws ApiError
   */
  public static retrieveLoggedIn(): CancelablePromise<logged_in> {
    return __request(OpenAPI, {
      method: 'GET',
      url: '/api/auth/logged-in',
    });
  }

  /**
   * @param requestBody 
   * @returns login 
   * @throws ApiError
   */
  public static createLogin(
requestBody?: login,
): CancelablePromise<login> {
    return __request(OpenAPI, {
      method: 'POST',
      url: '/api/auth/login',
      body: requestBody,
      mediaType: 'application/json',
    });
  }

}
