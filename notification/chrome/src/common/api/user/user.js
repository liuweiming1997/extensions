import RequestBase from '../base';
import account from '../../account';

class User extends RequestBase {
  constructor() {
    super();
  }
  loadOrCreate = async (username, password) => {
    const response = await this.post('/user/load_or_create/', {}, {
      username: username,
      password: password,
    });
    return account.updateUserInfo(response);
  }
  checkSession = async () => {
    const response = await this.get('/user/check_session/');
    return response;
  }
  logout = async () => {
    const response = await this.get('/user/logout/');
    return account.logout(response);
  }
};

const user = new User();
export default user;
