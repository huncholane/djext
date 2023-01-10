/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

export type user = {
  readonly url?: string;
  readonly id?: number;
  /**
   * Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
   */
  username: string;
  first_name?: string;
  last_name?: string;
  email?: string;
  password: string;
};
