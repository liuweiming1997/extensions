import messageBox from '../messagebox/messagebox';
import log from '../lib/log';

const API_HOST = 'http://127.0.0.1:8888';

const OPT = Object.freeze({
  method: 'GET',
  mode: 'cors',
  redirect: 'follow',
  credentials: 'include',
  headers: new Headers({
    'content-type': 'application/json',
  })
});

const processResponse = async (response) => {
  const contentType = response.headers.get('Content-Type');
  if (!contentType) {
    throw "no content type";
  } else {
    if(contentType.indexOf('text') !== -1) {
      return await response.text()
    } else if(contentType.indexOf('form') !== -1) {
      return await response.formData();
    } else if(contentType.indexOf('video') !== -1) {
      return await response.blob();
    } else if(contentType.indexOf('json') !== -1) {
      return await response.json();
    }
  }
}

const processOptions = (options) => {
  return Object.assign(options, OPT);
}

export default class RequestBase {
  constructor() {
  }

  doRequest = async (url, options) => {
    try {
      const fetchUrl = `${API_HOST}${url}`;
      const response = await fetch(fetchUrl, options);
      if (response.status !== 200) {
        throw await processResponse(response);
      } else {
        return await processResponse(response);
      }
    } catch(fetchError) {
      const error = new Error(fetchError.message);
      error.data = fetchError;
      messageBox(`request  '${url}'  error`, JSON.stringify(error, null, 2));
      throw 'error';
    }
  }

  get = async (url, options = {}) => {
    const fetchOptions = processOptions(options);
    fetchOptions.method = 'GET';
    return await this.doRequest(url, fetchOptions);
  }
  post = async (url, options = {}, body = {}) => {
    const fetchOptions = processOptions(options);
    fetchOptions.method = 'POST';
    fetchOptions.body = JSON.stringify(body);
    return await this.doRequest(url, fetchOptions);
  }
  put = () => {}
  del = () => {}
  options = () => {}
};
