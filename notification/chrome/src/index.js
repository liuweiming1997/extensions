import React from 'react';
import ReactDOM from 'react-dom';

import Login from './components/login.js';
import log from './common/lib/log';
import meishi from './common/api/meituan/meishi'

log.info('index page start');

ReactDOM.render(
  <Login />,
  document.getElementById('root'),
);
