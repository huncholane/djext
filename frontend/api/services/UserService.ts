/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { user } from '../models/user';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class UserService {

  /**
   * API endpoint that allows users to be viewed or edited.
   * @returns user 
   * @throws ApiError
   */
  public static listUsers(): CancelablePromise<Array<user>> {
    return __request(OpenAPI, {
      method: 'GET',
      url: '/api/user/',
    });
  }

  /**
   * API endpoint that allows users to be viewed or edited.
   * @param requestBody 
   * @returns user 
   * @throws ApiError
   */
  public static createUser(
requestBody?: user,
): CancelablePromise<user> {
    return __request(OpenAPI, {
      method: 'POST',
      url: '/api/user/',
      body: requestBody,
      mediaType: 'application/json',
    });
  }

  /**
   * API endpoint that allows users to be viewed or edited.
   * @param id A unique integer value identifying this user.
   * @returns user 
   * @throws ApiError
   */
  public static retrieveUser(
id: string,
): CancelablePromise<user> {
    return __request(OpenAPI, {
      method: 'GET',
      url: '/api/user/{id}/',
      path: {
        'id': id,
      },
    });
  }

  /**
   * API endpoint that allows users to be viewed or edited.
   * @param id A unique integer value identifying this user.
   * @param requestBody 
   * @returns user 
   * @throws ApiError
   */
  public static updateUser(
id: string,
requestBody?: user,
): CancelablePromise<user> {
    return __request(OpenAPI, {
      method: 'PUT',
      url: '/api/user/{id}/',
      path: {
        'id': id,
      },
      body: requestBody,
      mediaType: 'application/json',
    });
  }

  /**
   * API endpoint that allows users to be viewed or edited.
   * @param id A unique integer value identifying this user.
   * @param requestBody 
   * @returns user 
   * @throws ApiError
   */
  public static partialUpdateUser(
id: string,
requestBody?: user,
): CancelablePromise<user> {
    return __request(OpenAPI, {
      method: 'PATCH',
      url: '/api/user/{id}/',
      path: {
        'id': id,
      },
      body: requestBody,
      mediaType: 'application/json',
    });
  }

  /**
   * API endpoint that allows users to be viewed or edited.
   * @param id A unique integer value identifying this user.
   * @returns void 
   * @throws ApiError
   */
  public static destroyUser(
id: string,
): CancelablePromise<void> {
    return __request(OpenAPI, {
      method: 'DELETE',
      url: '/api/user/{id}/',
      path: {
        'id': id,
      },
    });
  }

}
