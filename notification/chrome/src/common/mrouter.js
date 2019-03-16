import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route, Link, Redirect} from 'react-router-dom';
import {account} from './account.js';
import history from './history.js';

function issame(changePath) {
  if (history.location.pathname === changePath) {
    return true;
  } else return false;
}

function goToBlogPage(username, user_blog_id) {
  const path = `/blog/${username}/${user_blog_id}`;
  if (issame(path)) {
    return;
  }
  history.push(path);
}

function goToProfilePage(username) {
  const path = `/profile/${username}`;
  if (issame(path)) {
    return;
  }
  history.push(path);
}

function goToWriteBlogPage() {
  if (account.hasLogin()) {
    const path = "/blog/write_blog/";
    if (issame(path)) {
      return;
    }
    history.push(path);
  } else {
    goToLoginPage();
  }
}

function goToLoginPage() {
  account.logout(() => {
    const path = "/";
    if (issame(path)) {
      return;
    }
    history.push(path);
  });
}

function goToFirstPage() {
  const path = '/first';
  if (issame(path)) {
    return;
  }
  history.push(path);
}

function backOnePage() {
  history.goBack();
}

export default {
  goToProfilePage,
  goToLoginPage,
  goToBlogPage,
  goToWriteBlogPage,
  backOnePage,
  goToFirstPage,
}
