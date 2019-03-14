import React from 'react';
import ReactDOM from 'react-dom';
import MessageBox from './dialog.js';

function messageBox(title, message, callbackOK, callbackCancel) {
  ReactDOM.render(
    <MessageBox title={title} message={message} callbackOK={callbackOK} callbackCancel={callbackCancel}/>,
    document.getElementById('modal'),
  );
}

export default messageBox;
