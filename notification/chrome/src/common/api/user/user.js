import RequestBase from '../base';

class User extends RequestBase {
  constructor() {
    super();
  }
  loadOrCreate = async (username, password) => {
    const response = await this.post('/user/load_or_create/', {}, {
      username: username,
      password: password,
    });
    alert("????");
  }
};

const user = new User();
export default user;
