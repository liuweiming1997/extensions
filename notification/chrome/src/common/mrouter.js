import {account} from './account.js';
import history from './history.js';

function issame(changePath) {
  if (history.location.pathname === changePath) {
    return true;
  } else return false;
}

function goToIndexPage() {
  const path = `/indexpage`;
  if (issame(path)) {
    return;
  }
  history.push(path);
}

function backOnePage() {
  history.goBack();
}

export default {
  goToIndexPage,
  backOnePage,
}
