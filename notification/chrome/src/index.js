import React from 'react';
import ReactDOM from 'react-dom';

import Login from './components/login.js';
import log from './common/lib/log';
import user from './common/api/user/user';

user.loadOrCreate('weimingliu', 'stupidone');

ReactDOM.render(
  <Login />,
  document.getElementById('root'),
);
