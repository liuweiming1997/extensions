import React from 'react';
import ReactDOM from 'react-dom';
import { Router, Route, Link, Switch} from 'react-router-dom';

import Login from './components/login.js';
import log from './common/lib/log';
import account from './common/account';
import history from './common/history';
import IndexPage from './components/indexpage';

class AppRouter extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <Router history={history}>
        <Switch>
          <Route exact path="/" component={Login}/>
          <Route exact path="/indexpage" component={IndexPage}/>
          <Route path="*" component={Login}/>
        </Switch>
      </Router>
    );
  }
};

const setupRouter = () => {
  ReactDOM.render(
    <AppRouter />,
    document.getElementById('root'),
  );
}

const begin = async () => {
  try {
    const result = await account.tryLogin();
    setupRouter();
    alert('user in');
  } catch(sessionTimeoutOrNotSessionError) {
    setupRouter();
  }
}

begin();
