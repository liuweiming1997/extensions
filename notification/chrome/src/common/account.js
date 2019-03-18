import user from './api/user/user';

class Account {
  constructor() {
    this.isLogin = false;
    this.user = {};
  }

  tryLogin = async () => {
    const response = await user.checkSession();
    return this.updateUserInfo(response);
  }

  logout = (response) => {
    if (response.logout) {
      return !this.updateUserInfo(null);
    } else return false;
  }

  updateUserInfo = (user) => {
    if (user) {
      this.isLogin = true;
      this.user = user;
      return true;
    } else {
      this.isLogin = false;
      this.user = {};
      return false;
    }
  }

};

const account = new Account();
export default account;
