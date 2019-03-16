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

  updateUserInfo = (user) => {
    if (user) {
      this.isLogin = true;
      this.user = user;
      return true;
    } else {
      return false;
    }
  }

};

const account = new Account();
export default account;
